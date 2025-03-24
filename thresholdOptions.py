# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np

class allThresholdOptions:

	@on_trait_change('threshold1, thresholdPercent1')
	def threshold_changed1(self):
		
		# Make no changes
		pass
	
	@on_trait_change('setThreshold1')
	def setThreshold_fired1(self):
		
		# First reset all contours
		self.iso1.contour.contours = []
		
		try:
		
			tmpthreshvals = self.threshold1.split(',')
			self.iso1.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox1 == False:
				self.chkBox1 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('setThresholdPercent1')
	def setThresholdPercent_fired1(self):
		
		# First reset all contours
		self.iso1.contour.contours = []
		
		try:
		
			tmpthreshvals = self.thresholdPercent1.split(',')
			self.iso1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox1 == False:
				self.chkBox1 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('threshold2, thresholdPercent2')
	def threshold_changed2(self):
		
		# Make no changes
		pass
	
	@on_trait_change('setThreshold2')
	def setThreshold_fired2(self):
		
		# First reset all contours
		self.iso2.contour.contours = []
		
		try:
		
			tmpthreshvals = self.threshold2.split(',')
			self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox2 == False:
				self.chkBox2 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('setThresholdPercent2')
	def setThresholdPercent_fired2(self):
		
		# First reset all contours
		self.iso2.contour.contours = []
		
		try:
		
			tmpthreshvals = self.thresholdPercent2.split(',')
			self.iso2.contour.contours = [np.float32(i)*self.thresholdMaximum2 for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox2 == False:
				self.chkBox2 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('threshold3, thresholdPercent3')
	def threshold_changed3(self):
		
		# Make no changes
		pass
	
	@on_trait_change('setThreshold3')
	def setThreshold_fired3(self):
		
		# First reset all contours
		self.iso3.contour.contours = []
		
		try:
		
			tmpthreshvals = self.threshold3.split(',')
			self.iso3.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox3 == False:
				self.chkBox3 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('setThresholdPercent3')
	def setThresholdPercent_fired3(self):
		
		# First reset all contours
		self.iso3.contour.contours = []
		
		try:
		
			tmpthreshvals = self.thresholdPercent3.split(',')
			self.iso3.contour.contours = [np.float32(i)*self.thresholdMaximum3 for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox3 == False:
				self.chkBox3 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('threshold4, thresholdPercent4')
	def threshold_changed4(self):
		
		# Make no changes
		pass
	
	@on_trait_change('setThreshold4')
	def setThreshold_fired4(self):
		
		# First reset all contours
		self.iso4.contour.contours = []
		
		try:
		
			tmpthreshvals = self.threshold4.split(',')
			self.iso4.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox4 == False:
				self.chkBox4 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('setThresholdPercent4')
	def setThresholdPercent_fired4(self):
		
		# First reset all contours
		self.iso4.contour.contours = []
		
		try:
		
			tmpthreshvals = self.thresholdPercent4.split(',')
			self.iso4.contour.contours = [np.float32(i)*self.thresholdMaximum4 for i in tmpthreshvals]
	
			# Update camera values
			self.updateCurrentVals_button_fired()
			
			# If the checkbox is not active already, activate it
			if self.chkBox4 == False:
				self.chkBox4 = True
		
		except ValueError:
			
			# Wait until user enters the values
			pass
