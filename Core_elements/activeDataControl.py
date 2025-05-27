# Supplement to Mayavi Visualization
# Control all active data

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab

class activeDataControlClass:

	@on_trait_change('screen1_ts1')
	def sc1_ts1_changed1(self):
		
		if self.screen1_ts1 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc1.contour.contours = []
				
				if self.colorFieldSet_sc1:
					self.mesh1.remove() # remove mesh if already exists
					self.colorFieldSet_sc1 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				try:
					self.vol1_sc1.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc1.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender1_actual(1, self.scene1.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(1, self.scene1.mayavi_scene)
	
	@on_trait_change('screen2_ts1')
	def sc2_ts1_changed1(self):
		
		if self.screen2_ts1 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc2.contour.contours = []
				
				if self.colorFieldSet_sc2:
					self.mesh2.remove() # remove mesh if already exists
					self.colorFieldSet_sc2 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol1_sc2.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc2.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
				
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender1_actual(2, self.scene2.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(2, self.scene2.mayavi_scene)
	
	@on_trait_change('screen3_ts1')
	def sc3_ts1_changed1(self):
		
		if self.screen3_ts1 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc3.contour.contours = []
				
				if self.colorFieldSet_sc3:
					self.mesh3.remove() # remove mesh if already exists
					self.colorFieldSet_sc3 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol1_sc3.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc3.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender1_actual(3, self.scene3.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(3, self.scene3.mayavi_scene)
	
	@on_trait_change('screen4_ts1')
	def sc4_ts1_changed1(self):
		
		if self.screen4_ts1 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc4.contour.contours = []
				
				if self.colorFieldSet_sc4:
					self.mesh4.remove() # remove mesh if already exists
					self.colorFieldSet_sc4 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol1_sc4.remove()
				except AttributeError:
					pass # Set volume rendering first
				
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender1_actual(4, self.scene4.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(4, self.scene4.mayavi_scene)
	
	@on_trait_change('screen1_ts2')
	def sc1_ts2_changed1(self):
		
		if self.screen1_ts2 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso2_sc1.contour.contours = []
				
				if self.colorFieldSet_sc1:
					self.mesh1.remove() # remove mesh if already exists
					self.colorFieldSet_sc1 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				try:
					self.vol2_sc1.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc1.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender2_actual(1, self.scene1.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(1, self.scene1.mayavi_scene)
	
	@on_trait_change('screen2_ts2')
	def sc2_ts2_changed1(self):
		
		if self.screen2_ts2 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc2.contour.contours = []
				
				if self.colorFieldSet_sc2:
					self.mesh2.remove() # remove mesh if already exists
					self.colorFieldSet_sc2 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol2_sc2.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc2.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
				
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender2_actual(2, self.scene2.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(2, self.scene2.mayavi_scene)
	
	@on_trait_change('screen3_ts2')
	def sc3_ts2_changed1(self):
		
		if self.screen3_ts2 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc3.contour.contours = []
				
				if self.colorFieldSet_sc3:
					self.mesh3.remove() # remove mesh if already exists
					self.colorFieldSet_sc3 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol2_sc3.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc3.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender2_actual(3, self.scene3.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(3, self.scene3.mayavi_scene)
	
	@on_trait_change('screen4_ts2')
	def sc4_ts2_changed1(self):
		
		if self.screen4_ts2 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso2_sc4.contour.contours = []
				
				if self.colorFieldSet_sc4:
					self.mesh4.remove() # remove mesh if already exists
					self.colorFieldSet_sc4 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol1_sc4.remove()
				except AttributeError:
					pass # Set volume rendering first
				
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender2_actual(4, self.scene4.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(4, self.scene4.mayavi_scene)
	
	@on_trait_change('screen1_ts3')
	def sc1_ts3_changed1(self):
		
		if self.screen1_ts3 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso3_sc1.contour.contours = []
				
				if self.colorFieldSet_sc1:
					self.mesh1.remove() # remove mesh if already exists
					self.colorFieldSet_sc1 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				try:
					self.vol3_sc1.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc1.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender3_actual(1, self.scene1.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(1, self.scene1.mayavi_scene)
	
	@on_trait_change('screen2_ts3')
	def sc2_ts3_changed1(self):
		
		if self.screen2_ts3 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso3_sc2.contour.contours = []
				
				if self.colorFieldSet_sc2:
					self.mesh2.remove() # remove mesh if already exists
					self.colorFieldSet_sc2 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol3_sc2.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc2.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
				
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender3_actual(2, self.scene2.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(2, self.scene2.mayavi_scene)
	
	@on_trait_change('screen3_ts3')
	def sc3_ts3_changed1(self):
		
		if self.screen3_ts3 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso3_sc3.contour.contours = []
				
				if self.colorFieldSet_sc3:
					self.mesh3.remove() # remove mesh if already exists
					self.colorFieldSet_sc3 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol3_sc3.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc3.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender3_actual(3, self.scene3.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(3, self.scene3.mayavi_scene)
	
	@on_trait_change('screen4_ts3')
	def sc4_ts3_changed1(self):
		
		if self.screen4_ts3 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso3_sc4.contour.contours = []
				
				if self.colorFieldSet_sc4:
					self.mesh4.remove() # remove mesh if already exists
					self.colorFieldSet_sc4 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol3_sc4.remove()
				except AttributeError:
					pass # Set volume rendering first
				
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender3_actual(4, self.scene4.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(4, self.scene4.mayavi_scene)
	
	@on_trait_change('screen1_ts4')
	def sc1_ts4_changed1(self):
		
		if self.screen1_ts4 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso4_sc1.contour.contours = []
				
				if self.colorFieldSet_sc1:
					self.mesh1.remove() # remove mesh if already exists
					self.colorFieldSet_sc1 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				try:
					self.vol4_sc1.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc1.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender4_actual(1, self.scene1.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(1, self.scene1.mayavi_scene)
	
	@on_trait_change('screen2_ts4')
	def sc2_ts4_changed1(self):
		
		if self.screen2_ts4 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso1_sc2.contour.contours = []
				
				if self.colorFieldSet_sc2:
					self.mesh2.remove() # remove mesh if already exists
					self.colorFieldSet_sc2 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol4_sc2.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc2.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
				
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender4_actual(2, self.scene2.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(2, self.scene2.mayavi_scene)
	
	@on_trait_change('screen3_ts4')
	def sc3_ts4_changed1(self):
		
		if self.screen3_ts4 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso4_sc3.contour.contours = []
				
				if self.colorFieldSet_sc3:
					self.mesh3.remove() # remove mesh if already exists
					self.colorFieldSet_sc3 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol4_sc3.remove()
				except AttributeError:
					pass # Set volume rendering first
			
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc3.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender4_actual(3, self.scene3.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(3, self.scene3.mayavi_scene)
	
	@on_trait_change('screen4_ts4')
	def sc4_ts4_changed1(self):
		
		if self.screen4_ts4 == False:
			
			if self.allLocalOptions == "Isosurface":
			
				# Set new threshold data
				self.iso4_sc4.contour.contours = []
				
				if self.colorFieldSet_sc4:
					self.mesh4.remove() # remove mesh if already exists
					self.colorFieldSet_sc4 = False
			
			elif self.allLocalOptions == "Volume Rendering":
				
				try:
					self.vol4_sc4.remove()
				except AttributeError:
					pass # Set volume rendering first
				
			elif self.allLocalOptions == "Slice":
				try:
					self.volSlice1_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				self.setThreshold_fired1()
			
			if not self.thresholdPercent1 == '':
				
				self.setThresholdPercent_fired1()
			
			if self.allLocalOptions == "Volume Rendering":
				
				self.volRender4_actual(4, self.scene4.mayavi_scene)
			
			if self.allLocalOptions == "Slice":
				
				self.setSlice1_actual(4, self.scene4.mayavi_scene)
	
	@on_trait_change('radioButton1')
	def radioButton1_changed(self):
		
		if self.radioButton1 == 'Y':
			self.radioButton2 = 'N'
			self.radioButton3 = 'N'
			self.radioButton4 = 'N'
	
	@on_trait_change('radioButton2')
	def radioButton2_changed(self):
		
		if self.radioButton2 == 'Y':
			self.radioButton1 = 'N'
			self.radioButton3 = 'N'
			self.radioButton4 = 'N'
			
			if not self.out2_sc1.actor.actor.visibility:
				
				# Enable outline
				self.out2_sc1.actor.actor.visibility = True
				
				# Set camera similar to scene 1
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene1.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=self.scene2.mayavi_scene)
				viewControlRoll = mlab.roll(camRoll, figure=self.scene2.mayavi_scene)
	
	@on_trait_change('radioButton3')
	def radioButton3_changed(self):
		
		if self.radioButton3 == 'Y':
			self.radioButton1 = 'N'
			self.radioButton2 = 'N'
			self.radioButton4 = 'N'
			
			if not self.out3_sc1.actor.actor.visibility:
				
				# Enable outline
				self.out3_sc1.actor.actor.visibility = True
				
				# Set camera similar to scene 1
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene1.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=self.scene3.mayavi_scene)
				viewControlRoll = mlab.roll(camRoll, figure=self.scene3.mayavi_scene)
			
	@on_trait_change('radioButton4')
	def radioButton4_changed(self):
		
		if self.radioButton4 == 'Y':
			self.radioButton1 = 'N'
			self.radioButton2 = 'N'
			self.radioButton3 = 'N'
			
			if not self.out4_sc1.actor.actor.visibility:
				
				# Enable outline
				self.out4_sc1.actor.actor.visibility = True
				
				# Set camera similar to scene 1
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene1.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=self.scene4.mayavi_scene)
				viewControlRoll = mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
