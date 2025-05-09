# Supplement to Mayavi Visualization
# Control all active data

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab

class activeDataControlClass:

	@on_trait_change('screen1_ts1')
	def sc1_ts1_changed1(self):
		
		if self.screen1_ts1 == False:
			
			# Set new threshold data
			self.iso1_sc1.contour.contours = []
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				# Set threshold range
				tmpthreshvals = self.threshold1.split(',')
				self.iso1_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			if not self.thresholdPercent1 == '':
				
				# Set threshold range
				tmpthreshvals = self.thresholdPercent1.split(',')
				self.iso1_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
	
	@on_trait_change('screen2_ts1')
	def sc2_ts1_changed1(self):
		
		if self.screen2_ts1 == False:
			
			# Set new threshold data
			self.iso1_sc2.contour.contours = []
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				# Set threshold range
				tmpthreshvals = self.threshold1.split(',')
				self.iso1_sc2.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			if not self.thresholdPercent1 == '':
				
				# Set threshold range
				tmpthreshvals = self.thresholdPercent1.split(',')
				self.iso1_sc2.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
	
	@on_trait_change('screen3_ts1')
	def sc3_ts1_changed1(self):
		
		if self.screen3_ts1 == False:
			
			# Set new threshold data
			self.iso1_sc3.contour.contours = []
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				# Set threshold range
				tmpthreshvals = self.threshold1.split(',')
				self.iso1_sc3.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			if not self.thresholdPercent1 == '':
				
				# Set threshold range
				tmpthreshvals = self.thresholdPercent1.split(',')
				self.iso1_sc3.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
	
	@on_trait_change('screen4_ts1')
	def sc4_ts1_changed1(self):
		
		if self.screen4_ts1 == False:
			
			# Set new threshold data
			self.iso1_sc4.contour.contours = []
		
		else:
			
			# Set current threshold data
			if not self.threshold1 == '':
					
				# Set threshold range
				tmpthreshvals = self.threshold1.split(',')
				self.iso1_sc4.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			if not self.thresholdPercent1 == '':
				
				# Set threshold range
				tmpthreshvals = self.thresholdPercent1.split(',')
				self.iso1_sc4.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
	
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
			
			if not self.out2.actor.actor.visibility:
				
				# Enable outline
				self.out2.actor.actor.visibility = True
				
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
			
			if not self.out3.actor.actor.visibility:
				
				# Enable outline
				self.out3.actor.actor.visibility = True
				
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
			
			if not self.out4.actor.actor.visibility:
				
				# Enable outline
				self.out4.actor.actor.visibility = True
				
				# Set camera similar to scene 1
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=self.scene1.mayavi_scene)
				camRoll = mlab.roll(figure=self.scene1.mayavi_scene)
				
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=self.scene4.mayavi_scene)
				viewControlRoll = mlab.roll(camRoll, figure=self.scene4.mayavi_scene)
