# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from tvtk.util.ctf import PiecewiseFunction
from tvtk.util.ctf import ColorTransferFunction
from vtk.util import numpy_support
import mayavi
from scipy.interpolate import splprep, splev

class allFieldLineTrackingOptions:
	
	def update_camera_at_current_timestep_with_camPath(self, \
	camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle):
		
		# If camera path is set, use that instead
		if not self.camPathType == 'None':
			_, camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll, _ = np.loadtxt('cameraPath.txt')[self.whichTime1]
		viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=figureHandle)
		viewControlRoll = mlab.roll(camRoll, figure=figureHandle)
	
	def fieldlineRender2_actual(self, figureHandle):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
			camRoll = mlab.roll(figure=figureHandle)
		
		# Setup vector data
			
		if self.whichVector_flt == 'Velocity':
			
			self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], 
			self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
			magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
		
		else:
			
			self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], 
			self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
			magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
			
		self.volStream2_sc1 = mlab.pipeline.streamline(
		magnitude, 
		seedtype = 'sphere', 
		seed_visible = self.seedRegionVisible_fl2, 
		seed_scale = self.seedScale_fl2, 
		seed_resolution = self.seedResolution_fl2, 
		linetype = 'line', 
		line_width = self.lineWidth_fl2, 
		opacity = self.contourOpacity1, 
		integration_direction = 'both', 
		color = (self.red_fl2, self.green_fl2, self.blue_fl2),
		figure = figureHandle
		)
		
		self.volStream2_sc1_mirror = mlab.pipeline.streamline(
		magnitude, 
		seedtype = 'sphere', 
		seed_visible = self.seedRegionVisible_fl2, 
		seed_scale = self.seedScale_fl2, 
		seed_resolution = self.seedResolution_fl2, 
		linetype = 'line', 
		line_width = self.lineWidth_fl2, 
		opacity = self.contourOpacity1, 
		integration_direction = 'both', 
		color = (self.red_fl2, self.green_fl2, self.blue_fl2),
		figure = figureHandle
		)
		
		# Get the center of the sphere with the tracking scalar and 
		# set threshold
		
		if self.whichScalarSlice_fl2 == 'Computed scalar (default)':
			trackingScalar = self._dataTs1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Vorticity x':
			trackingScalar = self.omega1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Vorticity y':
			trackingScalar = self.omega2[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Vorticity z':
			trackingScalar = self.omega3[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Vorticity magnitude':
			trackingScalar = np.sqrt(self.omega1[:, :, :, self.whichTime1] + self.omega2[:, :, :, self.whichTime1] + self.omega3[:, :, :, self.whichTime1])
		elif self.whichScalarSlice_fl2 == 'Velocity x':
			trackingScalar = self.u1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Velocity y':
			trackingScalar = self.v1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Velocity z':
			trackingScalar = self.w1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl2 == 'Velocity magnitude':
			trackingScalar = np.sqrt(self.u1[:, :, :, self.whichTime1] + self.v1[:, :, :, self.whichTime1] + self.w1[:, :, :, self.whichTime1])
		
		if self.planeOrientation_fl2 == 'X':
			trackingScalar = trackingScalar[self.whichSliceX_fl2, :, :]
		elif self.planeOrientation_fl2 == 'Y':
			trackingScalar = trackingScalar[:, self.whichSliceY_fl2, :]
		elif self.planeOrientation_fl2 == 'Z':
			trackingScalar = trackingScalar[:, :, self.whichSliceZ_fl2]
		
		if '-' in self.thresholdPercent1_fl2:
			mask = trackingScalar < float(self.thresholdPercent1_fl2) * trackingScalar.max() 
		else:
			mask = trackingScalar > float(self.thresholdPercent1_fl2) * trackingScalar.max()
		
		if self.planeOrientation_fl2 == 'X':
			yy = self.y1[:, :, self.whichSliceX_fl2]
			zz = self.z1[:, :, self.whichSliceX_fl2]
			yval = np.mean(yy[mask == 1])
			zval = np.mean(zz[mask == 1])
			xval = np.unique(self.x1)[self.whichSliceX_fl2]
			self.volStream2_sc1.seed.widget.center = [xval, yval, zval]
		
		elif self.planeOrientation_fl2 == 'Y':
			xx = self.x1[:, :, self.whichSliceY_fl2]
			zz = self.z1[:, :, self.whichSliceY_fl2]
			xval = np.mean(xx[mask == 1])
			zval = np.mean(zz[mask == 1])
			yval = np.unique(self.y1)[self.whichSliceY_fl2]
			self.volStream2_sc1.seed.widget.center = [xval, yval, zval]
		
		elif self.planeOrientation_fl2 == 'Z':
			xx = self.x1[:, :, self.whichSliceZ_fl2]
			yy = self.y1[:, :, self.whichSliceZ_fl2]
			# xval = np.mean(xx[mask == 1]) + 0.075
			# yval = np.mean(yy[mask == 1])
			# zval = np.unique(self.z1)[self.whichSliceZ_fl2]
			xval = 0.075
			yval = -0.0875
			zval = -0.5
			self.volStream2_sc1.seed.widget.center = [xval, yval, zval]
			self.volStream2_sc1_mirror.seed.widget.center = [xval, yval, -zval]
		
		self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle) 
		self.volStream2_sc1.update_streamlines = 1
		self.volStream2_sc1_mirror.update_streamlines = 1
			
		self.firstRun = True
	
	def fieldlineRender1_actual(self, figureHandle):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
			camRoll = mlab.roll(figure=figureHandle)
		
		# Setup vector data
			
		if self.whichVector_flt == 'Velocity':
			
			self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], 
			self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
			magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
		
		else:
			
			self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], 
			self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
			magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
			
		self.volStream1_sc1 = mlab.pipeline.streamline(
		magnitude, 
		seedtype = 'sphere', 
		seed_visible = self.seedRegionVisible_fl1, 
		seed_scale = self.seedScale_fl1, 
		seed_resolution = self.seedResolution_fl1, 
		linetype = 'line', 
		line_width = self.lineWidth_fl1, 
		opacity = self.contourOpacity1, 
		integration_direction = 'both', 
		color = (self.red_fl1, self.green_fl1, self.blue_fl1),
		figure = figureHandle
		)
		
		self.volStream1_sc1_mirror = mlab.pipeline.streamline(
		magnitude, 
		seedtype = 'sphere', 
		seed_visible = self.seedRegionVisible_fl1, 
		seed_scale = self.seedScale_fl1, 
		seed_resolution = self.seedResolution_fl1, 
		linetype = 'line', 
		line_width = self.lineWidth_fl1, 
		opacity = self.contourOpacity1, 
		integration_direction = 'both', 
		color = (self.red_fl1, self.green_fl1, self.blue_fl1),
		figure = figureHandle
		)
		
		# Get the center of the sphere with the tracking scalar and 
		# set threshold
		
		if self.whichScalarSlice_fl1 == 'Computed scalar (default)':
			trackingScalar = self._dataTs1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Vorticity x':
			trackingScalar = self.omega1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Vorticity y':
			trackingScalar = self.omega2[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Vorticity z':
			trackingScalar = self.omega3[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Vorticity magnitude':
			trackingScalar = np.sqrt(self.omega1[:, :, :, self.whichTime1] + self.omega2[:, :, :, self.whichTime1] + self.omega3[:, :, :, self.whichTime1])
		elif self.whichScalarSlice_fl1 == 'Velocity x':
			trackingScalar = self.u1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Velocity y':
			trackingScalar = self.v1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Velocity z':
			trackingScalar = self.w1[:, :, :, self.whichTime1]
		elif self.whichScalarSlice_fl1 == 'Velocity magnitude':
			trackingScalar = np.sqrt(self.u1[:, :, :, self.whichTime1] + self.v1[:, :, :, self.whichTime1] + self.w1[:, :, :, self.whichTime1])
		
		if self.planeOrientation_fl1 == 'X':
			trackingScalar = trackingScalar[self.whichSliceX_fl1, :, :]
		elif self.planeOrientation_fl1 == 'Y':
			trackingScalar = trackingScalar[:, self.whichSliceY_fl1, :]
		elif self.planeOrientation_fl1 == 'Z':
			trackingScalar = trackingScalar[:, :, self.whichSliceZ_fl1]
		
		if '-' in self.thresholdPercent1_fl1:
			mask = trackingScalar < float(self.thresholdPercent1_fl1) * trackingScalar.max() 
		else:
			mask = trackingScalar > float(self.thresholdPercent1_fl1) * trackingScalar.max()
		
		if self.planeOrientation_fl1 == 'X':
			yy = self.y1[:, :, self.whichSliceX_fl1]
			zz = self.z1[:, :, self.whichSliceX_fl1]
			yval = np.mean(yy[mask == 1])
			zval = np.mean(zz[mask == 1])
			xval = np.unique(self.x1)[self.whichSliceX_fl1]
			self.volStream1_sc1.seed.widget.center = [xval, yval, zval]
		
		elif self.planeOrientation_fl1 == 'Y':
			xx = self.x1[:, :, self.whichSliceY_fl1]
			zz = self.z1[:, :, self.whichSliceY_fl1]
			xval = np.mean(xx[mask == 1])
			zval = np.mean(zz[mask == 1])
			yval = np.unique(self.y1)[self.whichSliceY_fl1]
			self.volStream1_sc1.seed.widget.center = [xval, yval, zval]
		
		elif self.planeOrientation_fl1 == 'Z':
			xx = self.x1[:, :, self.whichSliceZ_fl1] + 0.075
			yy = self.y1[:, :, self.whichSliceZ_fl1]
			# xval = np.mean(xx[mask == 1])
			# yval = np.mean(yy[mask == 1])
			# zval = np.unique(self.z1)[self.whichSliceZ_fl1]
			xval = 0.075
			yval = 0.0875
			zval = -0.5
			self.volStream1_sc1.seed.widget.center = [xval, yval, zval]
			self.volStream1_sc1_mirror.seed.widget.center = [xval, yval, -zval]
			
			# print(xval, yval, zval)
		
		self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle) 
		self.volStream1_sc1.update_streamlines = 1
		self.volStream1_sc1_mirror.update_streamlines = 1
			
		self.firstRun = True
	
	@on_trait_change('setThresholdPercent1_fl1')
	def enableFieldlinesChanged1(self):
		
		if self.thresholdPercent1_fl1 == '':
			try:
				self.volStream1_sc1.remove()
				self.volStream1_sc1_mirror.remove()
			except AttributeError:
				pass 
		else:
			
			try:
				self.volStream1_sc1.remove()
				self.volStream1_sc1_mirror.remove()
			except AttributeError:
				pass 
			
			self.fieldlineRender1_actual(self.scene1.mayavi_scene)
			
			if self.firstRun:
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
	
	@on_trait_change('setThresholdPercent1_fl2')
	def enableFieldlinesChanged2(self):
		
		if self.thresholdPercent1_fl2 == '':
			try:
				self.volStream2_sc1.remove()
				self.volStream2_sc1_mirror.remove()
			except AttributeError:
				pass 
		else:
			
			try:
				self.volStream2_sc1.remove()
				self.volStream2_sc1_mirror.remove()
			except AttributeError:
				pass 
			
			self.fieldlineRender2_actual(self.scene1.mayavi_scene)
			
			if self.firstRun:
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream2_sc1.seed.widget.center
