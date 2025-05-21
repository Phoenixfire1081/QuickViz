# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
import scipy
from mayavi import mlab

class allIsosurfaceOptions:

	@on_trait_change('threshold1, thresholdPercent1')
	def threshold_changed1(self):
		
		# Make no changes
		pass
	
	def plot_colorFieldData(self, scalar, colorData, tmpthreshvals, whichScreen, figureHandle, percent):
				
		# Extract contour data first
		contour_data = mlab.pipeline.contour(scalar)
		
		if len(tmpthreshvals) > 0:
			
			# Get actual contour data
			if not percent:
				contour_data.filter.contours = [np.float32(i) for i in tmpthreshvals]
			else:
				contour_data.filter.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
			
			cf0 = contour_data.outputs[0]
			actualPts = cf0.output.points.to_array()
			actualTriangles = cf0.output.polys.to_array() 
			actualTriangles = actualTriangles.reshape(actualTriangles.size//4, 4)

			# Interpolate on the points to get the scalar data
			interp0 = scipy.interpolate.NearestNDInterpolator((self.x1.ravel(), self.y1.ravel(), self.z1.ravel()), \
			colorData.ravel())
			
			if whichScreen == 1:
			
				# Construct the triangular_mesh with the required scalar data
				self.mesh1 = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], \
				actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts), figure = figureHandle)
				
				# Set the colormap min, max
				self.mesh1.module_manager.scalar_lut_manager.data_range = [self.colormapMin1, self.colormapMax1]
				
				# Set color field
				self.colorFieldSet_sc1 = True
			
			if whichScreen == 2:
			
				# Construct the triangular_mesh with the required scalar data
				self.mesh2 = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], \
				actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts), figure = figureHandle)
				
				# Set the colormap min, max
				self.mesh2.module_manager.scalar_lut_manager.data_range = [self.colormapMin1, self.colormapMax1]
				
				# Set color field
				self.colorFieldSet_sc2 = True
			
			if whichScreen == 3:
			
				# Construct the triangular_mesh with the required scalar data
				self.mesh3 = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], \
				actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts), figure = figureHandle)
				
				# Set the colormap min, max
				self.mesh3.module_manager.scalar_lut_manager.data_range = [self.colormapMin1, self.colormapMax1]
				
				# Set color field
				self.colorFieldSet_sc3 = True
			
			if whichScreen == 4:
			
				# Construct the triangular_mesh with the required scalar data
				self.mesh4 = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], \
				actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts), figure = figureHandle)
				
				# Set the colormap min, max
				self.mesh4.module_manager.scalar_lut_manager.data_range = [self.colormapMin1, self.colormapMax1]
				
				# Set color field
				self.colorFieldSet_sc4 = True
			
	def whichColorFields(self):
		
		if self.colorFields == 'Vorticity x':
			whichColorData = self.omega1[:, :, :, self.whichTime1]
		elif self.colorFields == 'Vorticity y':
			whichColorData = self.omega2[:, :, :, self.whichTime1]
		elif self.colorFields == 'Vorticity z':
			whichColorData = self.omega3[:, :, :, self.whichTime1]
		elif self.colorFields == 'Vorticity magnitude':
			whichColorData = np.sqrt(self.omega1[:, :, :, self.whichTime1]**2 + self.omega2[:, :, :, self.whichTime1]**2 + self.omega3[:, :, :, self.whichTime1]**2)
		elif self.colorFields == 'Velocity x':
			whichColorData = self.u1[:, :, :, self.whichTime1]
		elif self.colorFields == 'Velocity y':
			whichColorData = self.v1[:, :, :, self.whichTime1]
		elif self.colorFields == 'Velocity z':
			whichColorData = self.w1[:, :, :, self.whichTime1]
		elif self.colorFields == 'Velocity magnitude':
			whichColorData = np.sqrt(self.u1[:, :, :, self.whichTime1]**2 + self.v1[:, :, :, self.whichTime1]**2 + self.w1[:, :, :, self.whichTime1]**2)
		
		return whichColorData
	
	@on_trait_change('setThreshold1')
	def setThreshold_fired1(self):
		
		if self.screen1_ts1:
		
			# First reset all contours
			self.iso1_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.threshold1.split(',')
				
				self.iso1_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc1, self.whichColorFields(), tmpthreshvals, 1, self.scene1.mayavi_scene, False)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen2_ts1:
		
			# First reset all contours
			self.iso1_sc2.contour.contours = []
			
			if self.colorFieldSet_sc2:
				self.mesh2.remove() # remove mesh if already exists
				self.colorFieldSet_sc2 = False
			
			try:
			
				tmpthreshvals = self.threshold1.split(',')
				
				self.iso1_sc2.contour.contours = [np.float32(i) for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc2, self.whichColorFields(), tmpthreshvals, 2, self.scene2.mayavi_scene, False)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen3_ts1:
		
			# First reset all contours
			self.iso1_sc3.contour.contours = []
			
			if self.colorFieldSet_sc3:
				self.mesh3.remove() # remove mesh if already exists
				self.colorFieldSet_sc3 = False
			
			try:
			
				tmpthreshvals = self.threshold1.split(',')
				
				self.iso1_sc3.contour.contours = [np.float32(i) for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc3, self.whichColorFields(), tmpthreshvals, 3, self.scene3.mayavi_scene, False)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen4_ts1:
		
			# First reset all contours
			self.iso1_sc4.contour.contours = []
			
			if self.colorFieldSet_sc4:
				self.mesh4.remove() # remove mesh if already exists
				self.colorFieldSet_sc4 = False
			
			try:
			
				tmpthreshvals = self.threshold1.split(',')
				
				self.iso1_sc4.contour.contours = [np.float32(i) for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc4, self.whichColorFields(), tmpthreshvals, 4, self.scene4.mayavi_scene, False)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('setThresholdPercent1')
	def setThresholdPercent_fired1(self):
		
		if self.screen1_ts1:
		
			# First reset all contours
			self.iso1_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent1.split(',')
				
				self.iso1_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc1, self.whichColorFields(), tmpthreshvals, 1, self.scene1.mayavi_scene, True)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen2_ts1:
		
			# First reset all contours
			self.iso1_sc2.contour.contours = []
			
			if self.colorFieldSet_sc2:
				self.mesh2.remove() # remove mesh if already exists
				self.colorFieldSet_sc2 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent1.split(',')
				
				self.iso1_sc2.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc2, self.whichColorFields(), tmpthreshvals, 2, self.scene2.mayavi_scene, True)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen3_ts1:
		
			# First reset all contours
			self.iso1_sc3.contour.contours = []
			
			if self.colorFieldSet_sc3:
				self.mesh3.remove() # remove mesh if already exists
				self.colorFieldSet_sc3 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent1.split(',')
				
				self.iso1_sc3.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc3, self.whichColorFields(), tmpthreshvals, 3, self.scene3.mayavi_scene, True)
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
		if self.screen4_ts1:
		
			# First reset all contours
			self.iso1_sc4.contour.contours = []
			
			if self.colorFieldSet_sc4:
				self.mesh4.remove() # remove mesh if already exists
				self.colorFieldSet_sc4 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent1.split(',')
				
				self.iso1_sc4.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
				if self.colorFields != 'None':
					self.plot_colorFieldData(self.iso1_sc4, self.whichColorFields(), tmpthreshvals, 4, self.scene4.mayavi_scene, True)
			
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
