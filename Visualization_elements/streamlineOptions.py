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
				
				# custom scalar
				import os
				import netCDF4 as nc
				case = '0.004Hz_contra_water'
				run = 'run27'
				
				xmin = 12
				xmax = -12
				ymin = 12
				ymax = -12
				zmin = 12
				zmax = -12

				_dtype = 'f' # 'd' for double precision

				scale = 1

				which = 'DR'
				
				allFiles = os.listdir('/media/rosaline/experimental/GVK/NOVEMBRE_2023/ANGLES_22_FILTERS_ON/DR_Eul/' + case + '/BenProcd/ShortTracksMin10/' + run + '/')
				allFiles = [i for i in allFiles if '.nc' in i]
				allFiles = [i for i in allFiles if not 'Coordinates' in i]
				allFiles.sort(key = lambda x: int(x.split('_')[2].split('.')[0][1:]))
				
				cdata = nc.Dataset('/media/rosaline/experimental/GVK/NOVEMBRE_2023/ANGLES_22_FILTERS_ON/FlowFit/' + case + '/BenProcd/ShortTracksMin10/'+run+'/CoordinatesCube.nc')
				
				# Get grid data and trim
				x = np.unique(cdata['x_mesh'][:])
				y = np.unique(cdata['y_mesh'][:])
				z = np.unique(cdata['z_mesh'][:])
				z = np.array(z)
				# x = x[xmin:xmax]
				# y = y[ymin:ymax]
				# z = z[zmin:zmax]

				# dx = np.diff(x)[0]
				# dy = np.diff(y)[0]
				# dz = np.diff(z)[0]

				xlen = len(x)
				ylen = len(y)
				zlen = len(z)
				
				data = nc.Dataset('/media/rosaline/experimental/GVK/NOVEMBRE_2023/ANGLES_22_FILTERS_ON/DR_Eul/' + case + '/BenProcd/ShortTracksMin10/'+run+'/' + allFiles[50+self.whichTime1])
				print('Processing DR:', '/media/rosaline/experimental/GVK/NOVEMBRE_2023/ANGLES_22_FILTERS_ON/DR_Eul/' + case + '/BenProcd/ShortTracksMin10/'+run+'/' + allFiles[50+self.whichTime1])
				
				scalar = np.array(data[which][:])
				scalar = scalar[:, :, :, scale]
				scalar = np.transpose(scalar, (1, 0, 2)) # Permute is necessary for visualization
				
				# Adjust for altBox
				xmin_reconn = 1
				xmax_reconn = -1
				ymin_reconn = 1
				ymax_reconn = -1
				zmin_reconn = 1
				zmax_reconn = -1
				
				scalar2 = np.zeros_like(scalar)
				scalar2[xmin:xmax, ymin:ymax, zmin:zmax] = scalar[xmin:xmax, ymin:ymax, zmin:zmax]
				# scalar = scalar[xmin:xmax, ymin:ymax, zmin:zmax]
				
				# print(xmin_reconn, xmax_reconn)
				# print(ymin_reconn, ymax_reconn)
				# print(zmin_reconn, zmax_reconn)
				
				scalar2 = scalar2[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn]
				
				# print(np.shape(scalar))
				# print(np.shape(scalar2))
				# print(np.shape(self.x1))
				
				assert np.shape(scalar2) == np.shape(self.y1)
				
				print(scalar2.min(), scalar2.max())
				
				# custom scalar
				
				self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, 
				self.y1, 
				self.z1, 
				self.u1[:, :, :, self.whichTime1],
				self.v1[:, :, :, self.whichTime1], 
				self.w1[:, :, :, self.whichTime1], 
				# scalars = np.sqrt(self.u1[:, :, :, self.whichTime1]**2 + self.v1[:, :, :, self.whichTime1]**2 + self.w1[:, :, :, self.whichTime1]**2), 
				scalars = scalar2,
				figure=figureHandle)
				
				# cb = mlab.colorbar(orientation='vertical', title='DR')
				# cb.label_text_property.color = (0, 0, 0)  # Black labels
				# cb.title_text_property.color = (0, 0, 0)  # Black title
		
		else:
			
			if scNumber == 1:
				self.sf1_sc1 = mlab.pipeline.vector_field(self.x1, 
				self.y1, 
				self.z1, 
				self.omega1[:, :, :, self.whichTime1], 
				self.omega2[:, :, :, self.whichTime1], 
				self.omega3[:, :, :, self.whichTime1], 
				scalars = np.sqrt(self.omega1[:, :, :, self.whichTime1]**2 + self.omega2[:, :, :, self.whichTime1]**2 + self.omega3[:, :, :, self.whichTime1]**2), 
				figure=figureHandle)
		
		# Apply streamlines on vector data
		if scNumber == 1:
			
			self.volStream1_sc1 = mlab.pipeline.streamline(
			self.sf1_sc1, 
			seedtype = self.seedType, 
			seed_visible = self.seedRegionVisible, 
			seed_scale = self.seedScale, 
			seed_resolution = self.seedResolution, 
			linetype = self.lineType, 
			line_width = self.lineWidth, 
			opacity = self.contourOpacity1, 
			integration_direction = self.integrationDirection, 
			colormap = self.contourColormap1, 
			vmin = self.colormapMin1, 
			vmax = self.colormapMax1, 
			figure = figureHandle
			)
			
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
			if self.seedType == 'plane':
				self.volStream1_sc1.seed.widget.center = [self.seedCenterx, self.seedCentery, self.seedCenterz]
				if self.planeOrientation == "X":
					self.volStream1_sc1.seed.widget.normal = np.array([ 1., 0.,  0.])
					self.volStream1_sc1.seed.widget.center = np.array([ 0., 0.,  0.])
					self.volStream1_sc1.seed.widget.origin = np.array([np.unique(self.x1)[self.whichSliceX], np.unique(self.y1)[0], np.unique(self.z1)[-1]])
					self.volStream1_sc1.seed.widget.point1 = np.array([np.unique(self.x1)[self.whichSliceX], np.unique(self.y1)[0], np.unique(self.z1)[0]])
					self.volStream1_sc1.seed.widget.point2 = np.array([np.unique(self.x1)[self.whichSliceX], np.unique(self.y1)[-1], np.unique(self.z1)[-1]])
				elif self.planeOrientation == "Y":
					self.volStream1_sc1.seed.widget.normal = np.array([ 0., 1.,  0.])
					self.volStream1_sc1.seed.widget.center = np.array([ 0., 0.,  0.])
					self.volStream1_sc1.seed.widget.origin = np.array([np.unique(self.x1)[0], np.unique(self.y1)[self.whichSliceY], np.unique(self.z1)[-1]])
					self.volStream1_sc1.seed.widget.point1 = np.array([np.unique(self.x1)[0], np.unique(self.y1)[self.whichSliceY], np.unique(self.z1)[0]])
					self.volStream1_sc1.seed.widget.point2 = np.array([np.unique(self.x1)[-1], np.unique(self.y1)[self.whichSliceY], np.unique(self.z1)[-1]])
				elif self.planeOrientation == "Z":
					self.volStream1_sc1.seed.widget.normal = np.array([ 0., 0.,  1.])
					self.volStream1_sc1.seed.widget.center = np.array([ 0., 0.,  0.])
					self.volStream1_sc1.seed.widget.origin = np.array([np.unique(self.x1)[0], np.unique(self.y1)[-1], np.unique(self.z1)[self.whichSliceZ]])
					self.volStream1_sc1.seed.widget.point1 = np.array([np.unique(self.x1)[0], np.unique(self.y1)[0], np.unique(self.z1)[self.whichSliceZ]])
					self.volStream1_sc1.seed.widget.point2 = np.array([np.unique(self.x1)[-1], np.unique(self.y1)[-1], np.unique(self.z1)[self.whichSliceZ]])
				
				# Force an update
				self.volStream1_sc1.seed.widget.enabled = False
				self.volStream1_sc1.seed.widget.enabled = True
				self.volStream1_sc1.seed.widget.enabled = False
			
		self.firstRun = True
	
	@on_trait_change('enableStreamlines')
	def enableStreamlinesChanged(self):
		
		if self.screen1_ts1:
			
			if not self.justRemovedStreamlines:
				if self.firstRun and self.seedType == 'sphere':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
				if self.firstRun and self.seedType == 'point':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.position
				if self.firstRun and self.seedType == 'plane':
					self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
				try:
					self.volStream1_sc1.parent.parent.remove()
					self.sf1_sc1.remove()
				except (ValueError, AttributeError):
					pass # Set volume rendering first
			
			self.streamlineRender1_actual(1, self.scene1.mayavi_scene)
		
		self.justRemovedStreamlines = False

	@on_trait_change('removeStreamlines')
	def removeStreamlinesChanged(self):
		
		if self.screen1_ts1:
			if self.seedType == 'sphere':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
			if self.seedType == 'point':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.position
			if self.seedType == 'plane':
				self.seedCenterx, self.seedCentery, self.seedCenterz = self.volStream1_sc1.seed.widget.center
			try:
				self.volStream1_sc1.parent.parent.remove()
				self.sf1_sc1.remove()
			except (ValueError, AttributeError):
				pass # Set slice first
			
		self.justRemovedStreamlines = True
