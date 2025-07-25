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

class allStreamlineOptions:
	
	def compute_spline_curvature(self, points, s=0):
		
		x, y, z = points.T
		tck, u = splprep([x, y, z], s=s)

		# First and second derivatives
		dx, dy, dz = splev(u, tck, der=1)
		ddx, ddy, ddz = splev(u, tck, der=2)

		# Cross product of first and second derivatives
		d1 = np.array([dx, dy, dz])
		d2 = np.array([ddx, ddy, ddz])
		cross = np.cross(d1.T, d2.T)
		num = np.linalg.norm(cross, axis=1)
		denom = np.linalg.norm(d1.T, axis=1) ** 3 + 1e-12  # Avoid division by zero

		kappa = num / denom
		return kappa, tck
	
	def count_streamlines(self, lines_array):
		count = 0
		i = 0
		n = len(lines_array)
		while i < n:
			npts = lines_array[i]
			i += 1 + npts
			count += 1
		return count
	
	def update_camera_at_current_timestep_with_camPath(self, \
	camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle):
		
		# If camera path is set, use that instead
		if not self.camPathType == 'None':
			_, camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll, _ = np.loadtxt('cameraPath.txt')[self.whichTime1]
		viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=figureHandle)
		viewControlRoll = mlab.roll(camRoll, figure=figureHandle)
	
	def streamlineRender1_actual(self, scNumber, figureHandle):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
			camRoll = mlab.roll(figure=figureHandle)
		
		# Setup vector data
			
		if self.whichVector == 'Velocity':
			
			if scNumber == 1:
				self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], \
				self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
			if scNumber == 2:
				self.sf1_sc2 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], \
				self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc2)
			if scNumber == 3:
				self.sf1_sc3 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], \
				self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc3)
			if scNumber == 4:
				self.sf1_sc4 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.u1[:, :, :, self.whichTime1], \
				self.v1[:, :, :, self.whichTime1], self.w1[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc4)
		
		else:
			
			if scNumber == 1:
				self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], \
				self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc1)
			if scNumber == 2:
				self.sf1_sc2 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], \
				self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc2)
			if scNumber == 3:
				self.sf1_sc3 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], \
				self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc3)
			if scNumber == 4:
				self.sf1_sc4 = mlab.pipeline.vector_field(self.x1, self.y1, self.z1, self.omega1[:, :, :, self.whichTime1], \
				self.omega2[:, :, :, self.whichTime1], self.omega3[:, :, :, self.whichTime1], figure=figureHandle)
				magnitude = mlab.pipeline.extract_vector_norm(self.sf1_sc4)
		
		# Apply streamlines on vector data
		if scNumber == 1:
			self.volStream1_sc1 = mlab.pipeline.streamline(magnitude, \
			seedtype = self.seedType, seed_visible = self.seedRegionVisible, seed_scale = self.seedScale, \
			seed_resolution = self.seedResolution, linetype = self.lineType, line_width = self.lineWidth, opacity = self.contourOpacity1, \
			integration_direction = self.integrationDirection, colormap = self.contourColormap1, vmin = self.colormapMin1, \
			vmax = self.colormapMax1, figure = figureHandle)
			if self.seedType == 'sphere':
				self.volStream1_sc1.seed.widget.center = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc1.update_streamlines = 1
			if self.seedType == 'point':
				# self.volStream1_sc1.seed.widget.position = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				# find max in one half of self.omega2[:, :, :, self.whichTime1]
				# Draw box around the data so that it is easier to follow
				zmin = self.zlength_data1//2
				zmax = self.zlength_data1//2 + 5
				zmin1 = self.zlength_data1//2 - 10
				zmax1 = self.zlength_data1//2 
				# print(self.omega2[:, :, zmin:zmax, :80].max())
				# print(np.where(self.omega2[:, :, zmin:zmax, :80] == self.omega2[:, :, zmin:zmax, :80].max()))
				# self.tmp_scalar = mlab.pipeline.scalar_field(self.x1[:, :, zmin:zmax], self.y1[:, :, zmin:zmax], self.z1[:, :, zmin:zmax], self.omega2[:, :, zmin:zmax, self.whichTime1], figure=self.scene1.mayavi_scene)
				# self.tmp_iso = mlab.pipeline.iso_surface(self.tmp_scalar, contours=[self.omega2[:, :, zmin:zmax, self.whichTime1].min()])
				# self.tmp_out = mayavi.tools.pipeline.outline(self.tmp_iso)
				# self.tmp_scalar = mlab.pipeline.scalar_field(self.x1[:, :, zmin1:zmax1], self.y1[:, :, zmin1:zmax1], self.z1[:, :, zmin1:zmax1], self.omega2[:, :, zmin1:zmax1, self.whichTime1], figure=self.scene1.mayavi_scene)
				# self.tmp_iso = mlab.pipeline.iso_surface(self.tmp_scalar, contours=[self.omega2[:, :, zmin1:zmax1, self.whichTime1].min()])
				# self.tmp_out = mayavi.tools.pipeline.outline(self.tmp_iso)
				# ind_pos = np.where(self.omega2[32:, self.ylength_data1//2, 32:, self.whichTime1] == self.omega2[32:, self.ylength_data1//2, 32:, self.whichTime1].max())
				# ind_pos_max = np.where(self.omega2[:, :, zmin:zmax, self.whichTime1] == self.omega2[:, :, zmin:zmax, self.whichTime1].max())
				ind_pos_max = np.where(self.omega2[:, :, zmin:zmax, :80] == self.omega2[:, :, zmin:zmax, :80].max())
				# ind_pos_min = np.where(self.omega2[:, :, zmin1:zmax1, self.whichTime1] == self.omega2[:, :, zmin1:zmax1, self.whichTime1].min())
				# print(ind_pos)
				# print(ind_pos[0])
				# print(np.unique(self.x1)[ind_pos[0][0]])
				# print(np.unique(self.z1)[ind_pos[1][0]])
				# self.volStream1_sc1.seed.widget.position = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				# print(self.volStream1_sc1.outputs[0].output.lines)
				# print(dir(self.volStream1_sc1.stream_tracer.output))
				# print(self.volStream1_sc1.stream_tracer.output.polys)
				self.volStream1_sc1.seed.widget.position = [np.unique(self.x1)[ind_pos_max[0][0]], np.unique(self.y1)[ind_pos_max[1][0]], np.unique(self.z1)[zmin + ind_pos_max[2][0]]]
				# self.volStream1_sc1.seed.widget.position = [np.unique(self.x1)[ind_pos_min[0][0]], np.unique(self.y1)[ind_pos_min[1][0]], np.unique(self.z1)[zmin1 + ind_pos_min[2][0]]]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc1.update_streamlines = 1
				streamline_points = np.array(self.volStream1_sc1.get_output_dataset().points.data)
				streamline_lineData = np.array(self.volStream1_sc1.get_output_dataset().lines.to_array())
				# print(streamline_lineData)
				numStreamlines = self.count_streamlines(streamline_lineData)
				print('Number of streamlines found:', numStreamlines)
				# Get first streamline
				n_pts = streamline_lineData[0]
				indices = streamline_lineData[1 : 1 + n_pts]
				act_streamline = streamline_points[indices]
				kappa, tck = self.compute_spline_curvature(act_streamline)
				print("Max curvature:", np.max(kappa))
				# print(np.shape(act_streamline))
				# print(act_streamline)
				# print(np.shape(self.volStream1_sc1.get_output_dataset().lines.to_array()))
		if scNumber == 2:
			self.volStream1_sc2 = mlab.pipeline.streamline(magnitude, \
			seedtype = self.seedType, seed_visible = self.seedRegionVisible, seed_scale = self.seedScale, \
			seed_resolution = self.seedResolution, linetype = self.lineType, line_width = self.lineWidth, opacity = self.contourOpacity1, \
			integration_direction = self.integrationDirection, colormap = self.contourColormap1, vmin = self.colormapMin1, \
			vmax = self.colormapMax1, figure = figureHandle)
			if self.seedType == 'sphere':
				self.volStream1_sc2.seed.widget.center = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc2.update_streamlines = 1
			if self.seedType == 'point':
				self.volStream1_sc2.seed.widget.position = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc2.update_streamlines = 1
		if scNumber == 3:
			self.volStream1_sc3 = mlab.pipeline.streamline(magnitude, \
			seedtype = self.seedType, seed_visible = self.seedRegionVisible, seed_scale = self.seedScale, \
			seed_resolution = self.seedResolution, linetype = self.lineType, line_width = self.lineWidth, opacity = self.contourOpacity1, \
			integration_direction = self.integrationDirection, colormap = self.contourColormap1, vmin = self.colormapMin1, \
			vmax = self.colormapMax1, figure = figureHandle)
			if self.seedType == 'sphere':
				self.volStream1_sc3.seed.widget.center = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc3.update_streamlines = 1
			if self.seedType == 'point':
				self.volStream1_sc3.seed.widget.position = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc3.update_streamlines = 1
		if scNumber == 4:
			self.volStream1_sc4 = mlab.pipeline.streamline(magnitude, \
			seedtype = self.seedType, seed_visible = self.seedRegionVisible, seed_scale = self.seedScale, \
			seed_resolution = self.seedResolution, linetype = self.lineType, line_width = self.lineWidth, opacity = self.contourOpacity1, \
			integration_direction = self.integrationDirection, colormap = self.contourColormap1, vmin = self.colormapMin1, \
			vmax = self.colormapMax1, figure = figureHandle)
			if self.seedType == 'sphere':
				self.volStream1_sc4.seed.widget.center = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc4.update_streamlines = 1
			if self.seedType == 'point':
				self.volStream1_sc4.seed.widget.position = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, figureHandle) # For some reason, the camera update forces the streamline to update as well
				self.volStream1_sc4.update_streamlines = 1
			
		self.firstRun = True
	
	@on_trait_change('enableStreamlines')
	def enableStreamlinesChanged(self):
		
		if self.screen1_ts1:
			
			if not self.justRemovedStreamlines:
				if self.firstRun and self.seedType == 'sphere':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
				if self.firstRun and self.seedType == 'point':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.position
				try:
					self.volStream1_sc1.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			self.streamlineRender1_actual(1, self.scene1.mayavi_scene)
		
		if self.screen2_ts1:
			
			if not self.justRemovedStreamlines:
				if self.firstRun and self.seedType == 'sphere':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc2.seed.widget.center
				if self.firstRun and self.seedType == 'point':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc2.seed.widget.position
				try:
					self.volStream1_sc2.remove()
				except AttributeError:
					pass # Set volume rendering first
		
			self.streamlineRender1_actual(2, self.scene2.mayavi_scene)
		
		if self.screen3_ts1:
			
			if not self.justRemovedStreamlines:
				if self.firstRun and self.seedType == 'sphere':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc3.seed.widget.center
				if self.firstRun and self.seedType == 'point':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc3.seed.widget.position
				try:
					self.volStream1_sc3.remove()
				except AttributeError:
					pass # Set volume rendering first
		
			self.streamlineRender1_actual(3, self.scene3.mayavi_scene)
		
		if self.screen4_ts1:
			
			if not self.justRemovedStreamlines:
				if self.firstRun and self.seedType == 'sphere':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc4.seed.widget.center
				if self.firstRun and self.seedType == 'point':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc3.seed.widget.position
				try:
					self.volStream1_sc4.remove()
				except AttributeError:
					pass # Set volume rendering first
		
			self.streamlineRender1_actual(4, self.scene4.mayavi_scene)
		
		self.justRemovedStreamlines = False

	@on_trait_change('removeStreamlines')
	def removeStreamlinesChanged(self):
		
		if self.screen1_ts1:
			if self.seedType == 'sphere':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
			if self.seedType == 'point':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.position
			try:
				self.volStream1_sc1.remove()
			except AttributeError:
				pass # Set slice first
		
		if self.screen2_ts1:
			if self.seedType == 'sphere':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc2.seed.widget.center
			if self.seedType == 'point':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc2.seed.widget.position
			try:
				self.volStream1_sc2.remove()
			except AttributeError:
				pass # Set slice first
		
		if self.screen3_ts1:
			if self.seedType == 'sphere':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc3.seed.widget.center
			if self.seedType == 'point':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc3.seed.widget.position
			try:
				self.volStream1_sc3.remove()
			except AttributeError:
				pass # Set slice first
		
		if self.screen4_ts1:
			if self.seedType == 'sphere':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc4.seed.widget.center
			if self.seedType == 'point':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc4.seed.widget.position
			try:
				self.volStream1_sc4.remove()
			except AttributeError:
				pass # Set slice first
			
		self.justRemovedStreamlines = True
