# Supplement to Mayavi Visualization
# Time update (for time series) is defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import mayavi

class timeUpdateBehavior:
	
	def update_camera_at_current_timestep_with_camPath(self, \
	camAzimuth, camElevation, camDistance, focalPoint, camRoll, fig_handle):
		
		# If camera path is set, use that instead
		if not self.camPathType == 'None':
			_, camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll, _ = np.loadtxt('cameraPath.txt')[self.whichTime1]
		viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=fig_handle)
		viewControlRoll = mlab.roll(camRoll, figure=fig_handle)

	@on_trait_change('whichTime1')
	def time_changed1(self):
		
		# if self.chkBox1: # Update only of checkbox is active
		if self.screen1_ts1: # Update only if screen 1 of ts1 is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene1.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
			
			# Choose data at other timestep
			_data1 = self._dataTs1[:, :, :, self.whichTime1]
			
			# Update min, max data
			self.thresholdMinimum1 = np.floor(float(_data1.min()))
			self.thresholdMaximum1 = np.ceil(float(_data1.max()))
			
			try:
				
				if not self.threshold1 == '' or not self.thresholdPercent1 == '':
					mlab.clf(figure=self.scene1.mayavi_scene)	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso1_sc1 = mlab.pipeline.iso_surface(self.sf1_sc1, contours=[_data1.min()])
			
			if self.outlineToggle1:
			
				# Plot the outline
				self.out1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1)
				
				# Change outline width
				self.out1_sc1.actor.property.line_width = self.outlineWidth1
				
				# Set outline color
				self.out1_sc1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
			
			# Change contour opacity
			self.iso1_sc1.actor.property.opacity = self.contourOpacity1
			
			# Change contour representation
			self.iso1_sc1.actor.property.representation = self.contourRepresentation1
			
			# Change contour colormap
			self.iso1_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
			
			# Change colormap range
			self.iso1_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
			
			# If volume rendering is enabled, update that
			if self.allLocalOptions == "Volume Rendering":
				
				self.enableVolRenderingChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene1.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Slice":
				
				self.enableSliceChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene1.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Streamlines (3D)":
				
				self.enableStreamlinesChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene1.mayavi_scene)
			
			try:
			
				if not self.threshold1 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold1.split(',')
					self.iso1_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene1.mayavi_scene)
				
				if not self.thresholdPercent1 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent1.split(',')
					self.iso1_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene1.mayavi_scene)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
		if self.screen2_ts1: # Update only if screen 2 of ts1 is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene2.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene2.mayavi_scene)
			
			# Choose data at other timestep
			_data1 = self._dataTs1[:, :, :, self.whichTime1]
			
			# Update min, max data
			self.thresholdMinimum1 = np.floor(float(_data1.min()))
			self.thresholdMaximum1 = np.ceil(float(_data1.max()))
			
			try:
				
				if not self.threshold1 == '' or not self.thresholdPercent1 == '':
					mlab.clf(figure=self.scene2.mayavi_scene)	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf1_sc2 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene2.mayavi_scene)
			
			# Set the threshold
			self.iso1_sc2 = mlab.pipeline.iso_surface(self.sf1_sc2, contours=[_data1.min()])
			
			if self.outlineToggle1:
			
				# Plot the outline
				self.out1_sc2 = mayavi.tools.pipeline.outline(self.iso1_sc2)
				
				# Change outline width
				self.out1_sc2.actor.property.line_width = self.outlineWidth1
				
				# Set outline color
				self.out1_sc2.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
			
			# Change contour opacity
			self.iso1_sc2.actor.property.opacity = self.contourOpacity1
			
			# Change contour representation
			self.iso1_sc2.actor.property.representation = self.contourRepresentation1
			
			# Change contour colormap
			self.iso1_sc2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
			
			# Change colormap range
			self.iso1_sc2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
			
			# If volume rendering is enabled, update that
			if self.allLocalOptions == "Volume Rendering":
				
				self.enableVolRenderingChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene2.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Slice":
				
				self.enableSliceChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene2.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Streamlines (3D)":
				
				self.enableStreamlinesChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene2.mayavi_scene)
			
			try:
			
				if not self.threshold1 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold1.split(',')
					self.iso1_sc2.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene2.mayavi_scene)
				
				if not self.thresholdPercent1 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent1.split(',')
					self.iso1_sc2.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene2.mayavi_scene)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
		if self.screen3_ts1: # Update only if screen 3 of ts1 is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene3.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene3.mayavi_scene)
			
			# Choose data at other timestep
			_data1 = self._dataTs1[:, :, :, self.whichTime1]
			
			# Update min, max data
			self.thresholdMinimum1 = np.floor(float(_data1.min()))
			self.thresholdMaximum1 = np.ceil(float(_data1.max()))
			
			try:
				
				if not self.threshold1 == '' or not self.thresholdPercent1 == '':
					mlab.clf(figure=self.scene3.mayavi_scene)	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf1_sc3 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene3.mayavi_scene)
			
			# Set the threshold
			self.iso1_sc3 = mlab.pipeline.iso_surface(self.sf1_sc3, contours=[_data1.min()])
			
			if self.outlineToggle1:
			
				# Plot the outline
				self.out1_sc3 = mayavi.tools.pipeline.outline(self.iso1_sc3)
				
				# Change outline width
				self.out1_sc3.actor.property.line_width = self.outlineWidth1
				
				# Set outline color
				self.out1_sc3.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
			
			# Change contour opacity
			self.iso1_sc3.actor.property.opacity = self.contourOpacity1
			
			# Change contour representation
			self.iso1_sc3.actor.property.representation = self.contourRepresentation1
			
			# Change contour colormap
			self.iso1_sc3.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
			
			# Change colormap range
			self.iso1_sc3.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
			
			# If volume rendering is enabled, update that
			if self.allLocalOptions == "Volume Rendering":
				
				self.enableVolRenderingChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene3.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Slice":
				
				self.enableSliceChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene3.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Streamlines (3D)":
				
				self.enableStreamlinesChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene3.mayavi_scene)
			
			try:
			
				if not self.threshold1 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold1.split(',')
					self.iso1_sc3.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene3.mayavi_scene)
				
				if not self.thresholdPercent1 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent1.split(',')
					self.iso1_sc3.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene3.mayavi_scene)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
		if self.screen4_ts1: # Update only if screen 4 of ts1 is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene4.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene4.mayavi_scene)
			
			# Choose data at other timestep
			_data1 = self._dataTs1[:, :, :, self.whichTime1]
			
			# Update min, max data
			self.thresholdMinimum1 = np.floor(float(_data1.min()))
			self.thresholdMaximum1 = np.ceil(float(_data1.max()))
			
			try:
				
				if not self.threshold1 == '' or not self.thresholdPercent1 == '':
					mlab.clf(figure=self.scene4.mayavi_scene)	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf1_sc4 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene4.mayavi_scene)
			
			# Set the threshold
			self.iso1_sc4 = mlab.pipeline.iso_surface(self.sf1_sc4, contours=[_data1.min()])
			
			if self.outlineToggle1:
			
				# Plot the outline
				self.out1_sc4 = mayavi.tools.pipeline.outline(self.iso1_sc4)
				
				# Change outline width
				self.out1_sc4.actor.property.line_width = self.outlineWidth1
				
				# Set outline color
				self.out1_sc4.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
			
			# Change contour opacity
			self.iso1_sc4.actor.property.opacity = self.contourOpacity1
			
			# Change contour representation
			self.iso1_sc4.actor.property.representation = self.contourRepresentation1
			
			# Change contour colormap
			self.iso1_sc4.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
			
			# Change colormap range
			self.iso1_sc4.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
			
			# If volume rendering is enabled, update that
			if self.allLocalOptions == "Volume Rendering":
				
				self.enableVolRenderingChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene4.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Slice":
				
				self.enableSliceChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene4.mayavi_scene)
			
			# If slice is enabled, update that
			if self.allLocalOptions == "Streamlines (3D)":
				
				self.enableStreamlinesChanged()
				# Keep the previous view
				self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
				camElevation, camDistance, focalPoint, camRoll, self.scene4.mayavi_scene)
			
			try:
			
				if not self.threshold1 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold1.split(',')
					self.iso1_sc4.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene4.mayavi_scene)
				
				if not self.thresholdPercent1 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent1.split(',')
					self.iso1_sc4.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
					
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, self.scene4.mayavi_scene)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('whichTime2')
	def time_changed2(self):
		
		if self.chkBox2: # Update only of checkbox is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
				camRoll = mlab.roll()
			
			# Choose data at other timestep
			_data2 = self._dataTs2[:, :, :, self.whichTime2]
			
			# Update min, max data
			self.thresholdMinimum2 = np.floor(float(_data2.min()))
			self.thresholdMaximum2 = np.ceil(float(_data2.max()))
			
			try:
				
				if not self.threshold2 == '' or not self.thresholdPercent2 == '':
					mlab.clf()	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf2 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, _data2, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso2 = mlab.pipeline.iso_surface(self.sf2, contours=[_data2.min()])
			
			if self.outlineToggle2:
			
				# Plot the outline
				self.out2 = mayavi.tools.pipeline.outline(self.iso2)
				
				# Change outline width
				self.out2.actor.property.line_width = self.outlineWidth2
				
				# Set outline color
				self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
			
			# Change contour opacity
			self.iso2.actor.property.opacity = self.contourOpacity2
			
			# Change contour representation
			self.iso2.actor.property.representation = self.contourRepresentation2
			
			# Change contour colormap
			self.iso2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
			
			# Change colormap range
			self.iso2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
			
			try:
			
				if not self.threshold2 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold2.split(',')
					self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent2 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent2.split(',')
					self.iso2.contour.contours = [np.float32(i)*self.thresholdMaximum2 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('whichTime3')
	def time_changed3(self):
		
		if self.chkBox3: # Update only of checkbox is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
				camRoll = mlab.roll()
			
			# Choose data at other timestep
			_data3 = self._dataTs3[:, :, :, self.whichTime3]
			
			# Update min, max data
			self.thresholdMinimum3 = np.floor(float(_data3.min()))
			self.thresholdMaximum3 = np.ceil(float(_data3.max()))
			
			try:
				
				if not self.threshold3 == '' or not self.thresholdPercent3 == '':
					mlab.clf()	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf3 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, _data3, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso3 = mlab.pipeline.iso_surface(self.sf3, contours=[_data3.min()])
			
			if self.outlineToggle3:
			
				# Plot the outline
				self.out3 = mayavi.tools.pipeline.outline(self.iso3)
				
				# Change outline width
				self.out3.actor.property.line_width = self.outlineWidth3
				
				# Set outline color
				self.out3.actor.property.color = (self.outlineColorRed3, self.outlineColorGreen3, self.outlineColorBlue3)
			
			# Change contour opacity
			self.iso3.actor.property.opacity = self.contourOpacity3
			
			# Change contour representation
			self.iso3.actor.property.representation = self.contourRepresentation3
			
			# Change contour colormap
			self.iso3.module_manager.scalar_lut_manager.lut_mode = self.contourColormap3
			
			# Change colormap range
			self.iso3.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin3, self.colormapMax3])
			
			try:
			
				if not self.threshold3 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold3.split(',')
					self.iso3.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent3 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent3.split(',')
					self.iso3.contour.contours = [np.float32(i)*self.thresholdMaximum3 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('whichTime4')
	def time_changed4(self):
		
		if self.chkBox4: # Update only of checkbox is active
		
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
				camRoll = mlab.roll()
			
			# Choose data at other timestep
			_data4 = self._dataTs4[:, :, :, self.whichTime4]
			
			# Update min, max data
			self.thresholdMinimum4 = np.floor(float(_data4.min()))
			self.thresholdMaximum4 = np.ceil(float(_data4.max()))
			
			try:
				
				if not self.threshold4 == '' or not self.thresholdPercent4 == '':
					mlab.clf()	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf4 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, _data4, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso4 = mlab.pipeline.iso_surface(self.sf4, contours=[_data4.min()])
			
			if self.outlineToggle4:
			
				# Plot the outline
				self.out4 = mayavi.tools.pipeline.outline(self.iso4)
				
				# Change outline width
				self.out4.actor.property.line_width = self.outlineWidth4
				
				# Set outline color
				self.out4.actor.property.color = (self.outlineColorRed4, self.outlineColorGreen4, self.outlineColorBlue4)
			
			# Change contour opacity
			self.iso4.actor.property.opacity = self.contourOpacity4
			
			# Change contour representation
			self.iso4.actor.property.representation = self.contourRepresentation4
			
			# Change contour colormap
			self.iso4.module_manager.scalar_lut_manager.lut_mode = self.contourColormap4
			
			# Change colormap range
			self.iso4.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin4, self.colormapMax4])
			
			try:
			
				if not self.threshold4 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold4.split(',')
					self.iso4.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent4 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent4.split(',')
					self.iso4.contour.contours = [np.float32(i)*self.thresholdMaximum4 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('whichTimeGlobal')
	def time_changedGlobal(self):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
			camRoll = mlab.roll()
		
		# if self.chkBox1: # Update only of checkbox is active
		if self.screen1_ts1: # Update only of checkbox is active
		
			# Choose data at other timestep
			_data1 = self._dataTs1[:, :, :, self.whichTimeGlobal]
			
			# Update min, max data
			self.thresholdMinimum1 = np.floor(float(_data1.min()))
			self.thresholdMaximum1 = np.ceil(float(_data1.max()))
			
			try:
				
				if not self.threshold1 == '' or not self.thresholdPercent1 == '':
					mlab.clf()	
					
			except AttributeError:
				
				# Wait until user enters the values
				pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso1_sc1 = mlab.pipeline.iso_surface(self.sf1, contours=[_data1.min()])
			
			if self.outlineToggle1:
			
				# Plot the outline
				self.iso1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1)
				
				# Change outline width
				self.iso1_sc1.actor.property.line_width = self.outlineWidth1
				
				# Set outline color
				self.iso1_sc1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
			
			# Change contour opacity
			self.iso1_sc1.actor.property.opacity = self.contourOpacity1
			
			# Change contour representation
			self.iso1_sc1.actor.property.representation = self.contourRepresentation1
			
			# Change contour colormap
			self.iso1_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
			
			# Change colormap range
			self.iso1_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
			
			try:
			
				if not self.threshold1 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold1.split(',')
					self.iso1_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent1 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent1.split(',')
					self.iso1_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
				
	
		if self.chkBox2: # Update only of checkbox is active
			
			# Choose data at other timestep
			_data2 = self._dataTs2[:, :, :, self.whichTimeGlobal]
			
			# Update min, max data
			self.thresholdMinimum2 = np.floor(float(_data2.min()))
			self.thresholdMaximum2 = np.ceil(float(_data2.max()))
			
			# try:
				
				# if not self.threshold2 == '' or not self.thresholdPercent2 == '':
					# mlab.clf()	
					
			# except AttributeError:
				
				# # Wait until user enters the values
				# pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf2 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, _data2, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso2 = mlab.pipeline.iso_surface(self.sf2, contours=[_data2.min()])
			
			if self.outlineToggle2:
			
				# Plot the outline
				self.out2 = mayavi.tools.pipeline.outline(self.iso2)
				
				# Change outline width
				self.out2.actor.property.line_width = self.outlineWidth2
				
				# Set outline color
				self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
			
			# Change contour opacity
			self.iso2.actor.property.opacity = self.contourOpacity2
			
			# Change contour representation
			self.iso2.actor.property.representation = self.contourRepresentation2
			
			# Change contour colormap
			self.iso2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
			
			# Change colormap range
			self.iso2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
			
			try:
			
				if not self.threshold2 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold2.split(',')
					self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent2 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent2.split(',')
					self.iso2.contour.contours = [np.float32(i)*self.thresholdMaximum2 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
				
	
		if self.chkBox3: # Update only of checkbox is active
			
			# Choose data at other timestep
			_data3 = self._dataTs3[:, :, :, self.whichTimeGlobal]
			
			# Update min, max data
			self.thresholdMinimum3 = np.floor(float(_data3.min()))
			self.thresholdMaximum3 = np.ceil(float(_data3.max()))
			
			# try:
				
				# if not self.threshold3 == '' or not self.thresholdPercent3 == '':
					# mlab.clf()	
					
			# except AttributeError:
				
				# # Wait until user enters the values
				# pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf3 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, _data3, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso3 = mlab.pipeline.iso_surface(self.sf3, contours=[_data3.min()])
			
			if self.outlineToggle3:
			
				# Plot the outline
				self.out3 = mayavi.tools.pipeline.outline(self.iso3)
				
				# Change outline width
				self.out3.actor.property.line_width = self.outlineWidth3
				
				# Set outline color
				self.out3.actor.property.color = (self.outlineColorRed3, self.outlineColorGreen3, self.outlineColorBlue3)
			
			# Change contour opacity
			self.iso3.actor.property.opacity = self.contourOpacity3
			
			# Change contour representation
			self.iso3.actor.property.representation = self.contourRepresentation3
			
			# Change contour colormap
			self.iso3.module_manager.scalar_lut_manager.lut_mode = self.contourColormap3
			
			# Change colormap range
			self.iso3.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin3, self.colormapMax3])
			
			try:
			
				if not self.threshold3 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold3.split(',')
					self.iso3.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent3 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent3.split(',')
					self.iso3.contour.contours = [np.float32(i)*self.thresholdMaximum3 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
				
	
		if self.chkBox4: # Update only of checkbox is active
			
			# Choose data at other timestep
			_data4 = self._dataTs4[:, :, :, self.whichTimeGlobal]
			
			# Update min, max data
			self.thresholdMinimum4 = np.floor(float(_data4.min()))
			self.thresholdMaximum4 = np.ceil(float(_data4.max()))
			
			# try:
				
				# if not self.threshold4 == '' or not self.thresholdPercent4 == '':
					# mlab.clf()	
					
			# except AttributeError:
				
				# # Wait until user enters the values
				# pass	
			
			# With same threshold update contour
			
			# Plot the isosurface with minimum value from data
			self.sf4 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, _data4, figure=self.scene1.mayavi_scene)
			
			# Set the threshold
			self.iso4 = mlab.pipeline.iso_surface(self.sf4, contours=[_data4.min()])
			
			if self.outlineToggle4:
			
				# Plot the outline
				self.out4 = mayavi.tools.pipeline.outline(self.iso4)
				
				# Change outline width
				self.out4.actor.property.line_width = self.outlineWidth4
				
				# Set outline color
				self.out4.actor.property.color = (self.outlineColorRed4, self.outlineColorGreen4, self.outlineColorBlue4)
			
			# Change contour opacity
			self.iso4.actor.property.opacity = self.contourOpacity4
			
			# Change contour representation
			self.iso4.actor.property.representation = self.contourRepresentation4
			
			# Change contour colormap
			self.iso4.module_manager.scalar_lut_manager.lut_mode = self.contourColormap4
			
			# Change colormap range
			self.iso4.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin4, self.colormapMax4])
			
			try:
			
				if not self.threshold4 == '':
					
					# Set threshold range
					tmpthreshvals = self.threshold4.split(',')
					self.iso4.contour.contours = [np.float32(i) for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
				
				if not self.thresholdPercent4 == '':
					
					# Set threshold range
					tmpthreshvals = self.thresholdPercent4.split(',')
					self.iso4.contour.contours = [np.float32(i)*self.thresholdMaximum4 for i in tmpthreshvals]
					
					# Keep the previous view
					viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
					viewControlRoll = mlab.roll(camRoll)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
			
			except AttributeError:
				
				# Wait until user enters the values
				pass
