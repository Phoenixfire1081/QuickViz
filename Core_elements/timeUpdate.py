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
	
	def active_screen_counter(self):
		
		# Count the number of active screens for each time series
		
		ts1 = [0, 0, 0, 0]
		ts2 = [0, 0, 0, 0]
		ts3 = [0, 0, 0, 0]
		ts4 = [0, 0, 0, 0]
		
		if self.screen1_ts1:
			ts1[0] += 1
		if self.screen2_ts1:
			ts1[1] += 1
		if self.screen3_ts1:
			ts1[2] += 1
		if self.screen4_ts1:
			ts1[3] += 1
		if self.screen1_ts2:
			ts2[0] += 1
		if self.screen2_ts2:
			ts2[1] += 1
		if self.screen3_ts2:
			ts2[2] += 1
		if self.screen4_ts2:
			ts2[3] += 1
		if self.screen1_ts3:
			ts3[0] += 1
		if self.screen2_ts3:
			ts3[1] += 1
		if self.screen3_ts3:
			ts3[2] += 1
		if self.screen4_ts3:
			ts3[3] += 1
		if self.screen1_ts4:
			ts4[0] += 1
		if self.screen2_ts4:
			ts4[1] += 1
		if self.screen3_ts4:
			ts4[2] += 1
		if self.screen4_ts4:
			ts4[3] += 1
		
		return ts1, ts2, ts3, ts4

	@on_trait_change('whichTime1')
	def time_changed1(self):
		
		# Check which screens are active and run accordingly
		
		ts1, _, _, _ = self.active_screen_counter()

		for sc in range(len(ts1)):
		
			if ts1[sc] and sc == 0: 
				
				_figure = self.scene1.mayavi_scene
			
			elif ts1[sc] and sc == 1:
				
				_figure = self.scene2.mayavi_scene
			
			elif ts1[sc] and sc == 2:
				
				_figure = self.scene3.mayavi_scene
			
			elif ts1[sc] and sc == 3:
				
				_figure = self.scene4.mayavi_scene
			
			else:
				
				_figure = None
			
			if _figure is not None:
			
				# Get camera view
				if not mlab.view() is None:
					camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure = _figure)
					camRoll = mlab.roll(figure = _figure)
				
				# Choose data at other timestep
				_data1 = self._dataTs1[:, :, :, self.whichTime1]
				
				# Update min, max data
				self.thresholdMinimum1 = float(_data1.min())
				self.thresholdMaximum1 = float(_data1.max())
				
				try:
					
					if not self.threshold1 == '' or not self.thresholdPercent1 == '' and not self.clamp:
						mlab.clf(figure = _figure)	
						
				except AttributeError:
					
					# Wait until user enters the values
					pass	
				
				# With same threshold update contour
				
				# Plot the isosurface with minimum value from data
				self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure = _figure)
				
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
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If slice is enabled, update that
				if self.allLocalOptions == "Slice":
					
					self.enableSliceChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldlines are enabled, update that
				if self.allLocalOptions == "Streamlines (3D)":
					
					self.enableStreamlinesChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldline tracking is enabled, update that
				if self.allAnalysisOptions == "Fieldline tracking":
					
					self.enableFieldlinesChanged1()
					self.enableFieldlinesChanged2()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If Qtensor is enabled, update that
				if self.allAnalysisOptions == "Q-tensor":
					
					self.calculateQtensorChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				try:
				
					if not self.threshold1 == '':
						
						self.setThreshold_fired1()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
					
					if not self.thresholdPercent1 == '':
						
						self.setThresholdPercent_fired1()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
				
				except ValueError:
					
					# Wait until user enters the values
					pass
				
				except AttributeError:
					
					# Wait until user enters the values
					pass
		
	@on_trait_change('whichTime2')
	def time_changed2(self):
		
		# Check which screens are active and run accordingly
		
		_, ts2, _, _ = self.active_screen_counter()

		for sc in range(len(ts2)):
		
			if ts2[sc] and sc == 0: 
				
				_figure = self.scene1.mayavi_scene
			
			elif ts2[sc] and sc == 1:
				
				_figure = self.scene2.mayavi_scene
			
			elif ts2[sc] and sc == 2:
				
				_figure = self.scene3.mayavi_scene
			
			elif ts2[sc] and sc == 3:
				
				_figure = self.scene4.mayavi_scene
			
			else:
				
				_figure = None
			
			if _figure is not None:
		
				# Get camera view
				if not mlab.view() is None:
					camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure = _figure)
					camRoll = mlab.roll(figure = _figure)
				
				# Choose data at other timestep
				_data2 = self._dataTs2[:, :, :, self.whichTime2]
				
				# Update min, max data
				self.thresholdMinimum2 = float(_data2.min())
				self.thresholdMaximum2 = float(_data2.max())
				
				try:
					
					if not self.threshold2 == '' or not self.thresholdPercent2 == '' and not self.clamp:
						mlab.clf(figure = _figure)	
						
				except AttributeError:
					
					# Wait until user enters the values
					pass	
				
				# With same threshold update contour
				
				# Plot the isosurface with minimum value from data
				self.sf2_sc1 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, _data2, figure = _figure)
				
				# Set the threshold
				self.iso2_sc1 = mlab.pipeline.iso_surface(self.sf2_sc1, contours=[_data2.min()])
				
				if self.outlineToggle2:
				
					# Plot the outline
					self.out2_sc1 = mayavi.tools.pipeline.outline(self.iso2_sc1)
					
					# Change outline width
					self.out2_sc1.actor.property.line_width = self.outlineWidth2
					
					# Set outline color
					self.out2_sc1.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
				
				# Change contour opacity
				self.iso2_sc1.actor.property.opacity = self.contourOpacity2
				
				# Change contour representation
				self.iso2_sc1.actor.property.representation = self.contourRepresentation2
				
				# Change contour colormap
				self.iso2_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
				
				# Change colormap range
				self.iso2_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
				
				# If volume rendering is enabled, update that
				if self.allLocalOptions == "Volume Rendering":
					
					self.enableVolRenderingChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If slice is enabled, update that
				if self.allLocalOptions == "Slice":
					
					self.enableSliceChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldlines are enabled, update that
				if self.allLocalOptions == "Streamlines (3D)":
					
					self.enableStreamlinesChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldline tracking is enabled, update that
				if self.allAnalysisOptions == "Fieldline tracking":
					
					self.enableFieldlinesChanged1()
					self.enableFieldlinesChanged2()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If Qtensor is enabled, update that
				if self.allAnalysisOptions == "Q-tensor":
					
					self.calculateQtensorChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				try:
				
					if not self.threshold2 == '':
						
						self.setThreshold_fired2()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
					
					if not self.thresholdPercent2 == '':
						
						self.setThresholdPercent_fired2()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
				
				except ValueError:
					
					# Wait until user enters the values
					pass
				
				except AttributeError:
					
					# Wait until user enters the values
					pass
	
	@on_trait_change('whichTime3')
	def time_changed3(self):
		
		# Check which screens are active and run accordingly
		
		_, _, ts3, _ = self.active_screen_counter()

		for sc in range(len(ts3)):
		
			if ts3[sc] and sc == 0: 
				
				_figure = self.scene1.mayavi_scene
			
			elif ts3[sc] and sc == 1:
				
				_figure = self.scene2.mayavi_scene
			
			elif ts3[sc] and sc == 2:
				
				_figure = self.scene3.mayavi_scene
			
			elif ts3[sc] and sc == 3:
				
				_figure = self.scene4.mayavi_scene
			
			else:
				
				_figure = None
			
			if _figure is not None:
		
				# Get camera view
				if not mlab.view() is None:
					camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure = _figure)
					camRoll = mlab.roll(figure = _figure)
				
				# Choose data at other timestep
				_data3 = self._dataTs3[:, :, :, self.whichTime3]
				
				# Update min, max data
				self.thresholdMinimum3 = float(_data3.min())
				self.thresholdMaximum3 = float(_data3.max())
				
				try:
					
					if not self.threshold3 == '' or not self.thresholdPercent3 == '' and not self.clamp:
						mlab.clf(figure = _figure)	
						
				except AttributeError:
					
					# Wait until user enters the values
					pass	
				
				# With same threshold update contour
				
				# Plot the isosurface with minimum value from data
				self.sf3_sc1 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, _data3, figure = _figure)
				
				# Set the threshold
				self.iso3_sc1 = mlab.pipeline.iso_surface(self.sf3_sc1, contours=[_data3.min()])
				
				if self.outlineToggle3:
				
					# Plot the outline
					self.out3_sc1 = mayavi.tools.pipeline.outline(self.iso3_sc1)
					
					# Change outline width
					self.out3_sc1.actor.property.line_width = self.outlineWidth3
					
					# Set outline color
					self.out3_sc1.actor.property.color = (self.outlineColorRed3, self.outlineColorGreen3, self.outlineColorBlue3)
				
				# Change contour opacity
				self.iso3_sc1.actor.property.opacity = self.contourOpacity3
				
				# Change contour representation
				self.iso3_sc1.actor.property.representation = self.contourRepresentation3
				
				# Change contour colormap
				self.iso3_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap3
				
				# Change colormap range
				self.iso3_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin3, self.colormapMax3])
				
				# If volume rendering is enabled, update that
				if self.allLocalOptions == "Volume Rendering":
					
					self.enableVolRenderingChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If slice is enabled, update that
				if self.allLocalOptions == "Slice":
					
					self.enableSliceChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldlines are enabled, update that
				if self.allLocalOptions == "Streamlines (3D)":
					
					self.enableStreamlinesChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldline tracking is enabled, update that
				if self.allAnalysisOptions == "Fieldline tracking":
					
					self.enableFieldlinesChanged1()
					self.enableFieldlinesChanged2()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If Qtensor is enabled, update that
				if self.allAnalysisOptions == "Q-tensor":
					
					self.calculateQtensorChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				try:
				
					if not self.threshold3 == '':
						
						self.setThreshold_fired3()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
					
					if not self.thresholdPercent3 == '':
						
						self.setThresholdPercent_fired3()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
				
				except ValueError:
					
					# Wait until user enters the values
					pass
				
				except AttributeError:
					
					# Wait until user enters the values
					pass
		
	@on_trait_change('whichTime4')
	def time_changed4(self):
		
		# Check which screens are active and run accordingly
		
		_, _, _, ts4 = self.active_screen_counter()

		for sc in range(len(ts4)):
		
			if ts4[sc] and sc == 0: 
				
				_figure = self.scene1.mayavi_scene
			
			elif ts4[sc] and sc == 1:
				
				_figure = self.scene2.mayavi_scene
			
			elif ts4[sc] and sc == 2:
				
				_figure = self.scene3.mayavi_scene
			
			elif ts4[sc] and sc == 3:
				
				_figure = self.scene4.mayavi_scene
			
			else:
				
				_figure = None
			
			if _figure is not None:
		
				# Get camera view
				if not mlab.view() is None:
					camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure = _figure)
					camRoll = mlab.roll(figure = _figure)
				
				# Choose data at other timestep
				_data4 = self._dataTs4[:, :, :, self.whichTime4]
				
				# Update min, max data
				self.thresholdMinimum4 = float(_data4.min())
				self.thresholdMaximum4 = float(_data4.max())
				
				try:
					
					if not self.threshold4 == '' or not self.thresholdPercent4 == '' and not self.clamp:
						mlab.clf(figure = _figure)	
						
				except AttributeError:
					
					# Wait until user enters the values
					pass	
				
				# With same threshold update contour
				
				# Plot the isosurface with minimum value from data
				self.sf4_sc1 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, _data4, figure = _figure)
				
				# Set the threshold
				self.iso4_sc1 = mlab.pipeline.iso_surface(self.sf4_sc1, contours=[_data4.min()])
				
				if self.outlineToggle4:
				
					# Plot the outline
					self.out4_sc1 = mayavi.tools.pipeline.outline(self.iso4_sc1)
					
					# Change outline width
					self.out4_sc1.actor.property.line_width = self.outlineWidth4
					
					# Set outline color
					self.out4_sc1.actor.property.color = (self.outlineColorRed4, self.outlineColorGreen4, self.outlineColorBlue4)
				
				# Change contour opacity
				self.iso4_sc1.actor.property.opacity = self.contourOpacity4
				
				# Change contour representation
				self.iso4_sc1.actor.property.representation = self.contourRepresentation4
				
				# Change contour colormap
				self.iso4_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap4
				
				# Change colormap range
				self.iso4_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin4, self.colormapMax4])
				
				# If volume rendering is enabled, update that
				if self.allLocalOptions == "Volume Rendering":
					
					self.enableVolRenderingChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If slice is enabled, update that
				if self.allLocalOptions == "Slice":
					
					self.enableSliceChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldlines are enabled, update that
				if self.allLocalOptions == "Streamlines (3D)":
					
					self.enableStreamlinesChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If fieldline tracking is enabled, update that
				if self.allAnalysisOptions == "Fieldline tracking":
					
					self.enableFieldlinesChanged1()
					self.enableFieldlinesChanged2()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				# If Qtensor is enabled, update that
				if self.allAnalysisOptions == "Q-tensor":
					
					self.calculateQtensorChanged()
					# Keep the previous view
					self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
					camElevation, camDistance, focalPoint, camRoll, _figure)
				
				try:
				
					if not self.threshold4 == '':
						
						self.setThreshold_fired4()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
					
					if not self.thresholdPercent4 == '':
						
						self.setThresholdPercent_fired4()
						
						# Keep the previous view
						self.update_camera_at_current_timestep_with_camPath(camAzimuth, \
						camElevation, camDistance, focalPoint, camRoll, _figure)
				
				except ValueError:
					
					# Wait until user enters the values
					pass
				
				except AttributeError:
					
					# Wait until user enters the values
					pass
		
	@on_trait_change('whichTimeGlobal')
	def time_changedGlobal(self):
		
		# If global time slider is used, clear figures manually
		if not self.threshold1 == '' or not self.thresholdPercent1 == ''\
		or not self.threshold2 == '' or not self.thresholdPercent2 == ''\
		or not self.threshold3 == '' or not self.thresholdPercent3 == ''\
		or not self.threshold4 == '' or not self.thresholdPercent4 == '':
			mlab.clf(figure = self.scene1.mayavi_scene)	
			mlab.clf(figure = self.scene2.mayavi_scene)	
			mlab.clf(figure = self.scene3.mayavi_scene)	
			mlab.clf(figure = self.scene4.mayavi_scene)	
		
		# Change self.whichTimex and trigger time_changedx
		self.whichTime1 = self.whichTimeGlobal
		self.whichTime2 = self.whichTimeGlobal
		self.whichTime3 = self.whichTimeGlobal
		self.whichTime4 = self.whichTimeGlobal
		
		
