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
	
	@on_trait_change('threshold2, thresholdPercent2')
	def threshold_changed2(self):
		
		# Make no changes
		pass
	
	@on_trait_change('threshold3, thresholdPercent3')
	def threshold_changed3(self):
		
		# Make no changes
		pass
	
	@on_trait_change('threshold4, thresholdPercent4')
	def threshold_changed4(self):
		
		# Make no changes
		pass
	
	def plot_colorFieldData(self, scalar, colorData, tmpthreshvals, figureHandle, percent, thresholdMaximum, x, y, z):
				
		# Extract contour data first
		contour_data = mlab.pipeline.contour(scalar)
		
		if len(tmpthreshvals) > 0:
			
			# Get actual contour data
			if not percent:
				contour_data.filter.contours = [np.float32(i) for i in tmpthreshvals]
			else:
				contour_data.filter.contours = [np.float32(i)*thresholdMaximum for i in tmpthreshvals]
			
			cf0 = contour_data.outputs[0]
			actualPts = cf0.output.points.to_array()
			actualTriangles = cf0.output.polys.to_array() 
			actualTriangles = actualTriangles.reshape(actualTriangles.size//4, 4)

			# Interpolate on the points to get the scalar data
			interp0 = scipy.interpolate.NearestNDInterpolator((x.ravel(), y.ravel(), z.ravel()), \
			colorData.ravel())
			
			self.mesh1 = mlab.triangular_mesh(actualPts[:, 0], actualPts[:, 1], \
				actualPts[:, 2], actualTriangles[:, 1:], scalars = interp0(actualPts), 
				colormap = self.contourColormap1, figure = figureHandle)
			
	def whichColorFields(self, colorField, whichTs):
		
		if colorField == 'Vorticity x':
			if whichTs == 1:
				whichColorData = self.omega1[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.omega1_2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.omega1_2[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.omega1_2[:, :, :, self.whichTime4]
		elif colorField == 'Vorticity y':
			if whichTs == 1:
				whichColorData = self.omega2[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.omega2_2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.omega2_2[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.omega2_2[:, :, :, self.whichTime4]
		elif colorField == 'Vorticity z':
			if whichTs == 1:
				whichColorData = self.omega3[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.omega3_2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.omega3_2[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.omega3_2[:, :, :, self.whichTime4]
		elif colorField == 'Vorticity magnitude':
			if whichTs == 1:
				whichColorData = np.sqrt(self.omega1[:, :, :, self.whichTime1]**2 + self.omega2[:, :, :, self.whichTime1]**2 + self.omega3[:, :, :, self.whichTime1]**2)
			elif whichTs == 2:
				whichColorData = np.sqrt(self.omega1_2[:, :, :, self.whichTime2]**2 + self.omega2_2[:, :, :, self.whichTime2]**2 + self.omega3_2[:, :, :, self.whichTime2]**2)
			elif whichTs == 3:
				whichColorData = np.sqrt(self.omega1_3[:, :, :, self.whichTime3]**2 + self.omega2_3[:, :, :, self.whichTime3]**2 + self.omega3_3[:, :, :, self.whichTime3]**2)
			elif whichTs == 4:
				whichColorData = np.sqrt(self.omega1_4[:, :, :, self.whichTime4]**2 + self.omega2_4[:, :, :, self.whichTime4]**2 + self.omega3_4[:, :, :, self.whichTime4]**2)
		elif colorField == 'Velocity x':
			if whichTs == 1:
				whichColorData = self.u1[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.u2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.u3[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.u4[:, :, :, self.whichTime4]
		elif colorField == 'Velocity y':
			if whichTs == 1:
				whichColorData = self.v1[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.v2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.v3[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.v4[:, :, :, self.whichTime4]
		elif colorField == 'Velocity z':
			if whichTs == 1:
				whichColorData = self.w1[:, :, :, self.whichTime1]
			elif whichTs == 2:
				whichColorData = self.w2[:, :, :, self.whichTime2]
			elif whichTs == 3:
				whichColorData = self.w3[:, :, :, self.whichTime3]
			elif whichTs == 4:
				whichColorData = self.w4[:, :, :, self.whichTime4]
		elif colorField == 'Velocity magnitude':
			if whichTs == 1:
				whichColorData = np.sqrt(self.u1[:, :, :, self.whichTime1]**2 + self.v1[:, :, :, self.whichTime1]**2 + self.w1[:, :, :, self.whichTime1]**2)
			elif whichTs == 2:
				whichColorData = np.sqrt(self.u2[:, :, :, self.whichTime2]**2 + self.v2[:, :, :, self.whichTime2]**2 + self.w2[:, :, :, self.whichTime2]**2)
			elif whichTs == 3:
				whichColorData = np.sqrt(self.u3[:, :, :, self.whichTime3]**2 + self.v3[:, :, :, self.whichTime3]**2 + self.w3[:, :, :, self.whichTime3]**2)
			elif whichTs == 4:
				whichColorData = np.sqrt(self.u4[:, :, :, self.whichTime4]**2 + self.v4[:, :, :, self.whichTime4]**2 + self.w4[:, :, :, self.whichTime4]**2)
		
		return whichColorData
	
	@on_trait_change('setThreshold1')
	def setThreshold_fired1(self):
		
		if self.screen1_ts1:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts1:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts1:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts1:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso1_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.threshold1.split(',')
				
				if self.colorFields1 != 'None':
					self.plot_colorFieldData(self.iso1_sc1, self.whichColorFields(self.colorFields1, 1), tmpthreshvals, _figure, False, 0, self.x1, self.y1, self.z1)
				else:
					self.iso1_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('setThresholdPercent1')
	def setThresholdPercent_fired1(self):
		
		if self.screen1_ts1:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts1:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts1:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts1:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso1_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent1.split(',')
				
				if self.colorFields1 != 'None':
					self.plot_colorFieldData(self.iso1_sc1, self.whichColorFields(self.colorFields1, 1), tmpthreshvals, _figure, True, self.thresholdMaximum1, self.x1, self.y1, self.z1)
				else:
					self.iso1_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum1 for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('setThreshold2')
	def setThreshold_fired2(self):
		
		if self.screen1_ts2:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts2:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts2:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts2:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso2_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.threshold2.split(',')
				
				if self.colorFields2 != 'None':
					self.plot_colorFieldData(self.iso2_sc1, self.whichColorFields(self.colorFields2, 2), tmpthreshvals, _figure, False, 0, self.x2, self.y2, self.z2)
				else:
					self.iso2_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('setThresholdPercent2')
	def setThresholdPercent_fired2(self):
		
		if self.screen1_ts2:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts2:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts2:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts2:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso2_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent2.split(',')
				
				if self.colorFields2 != 'None':
					self.plot_colorFieldData(self.iso2_sc1, self.whichColorFields(self.colorFields2, 2), tmpthreshvals, _figure, True, self.thresholdMaximum2, self.x2, self.y2, self.z2)
				else:
					self.iso2_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum2 for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass

	@on_trait_change('setThreshold3')
	def setThreshold_fired3(self):
		
		if self.screen1_ts3:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts3:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts3:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts3:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso3_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.threshold2.split(',')
				
				if self.colorFields3 != 'None':
					self.plot_colorFieldData(self.iso3_sc1, self.whichColorFields(self.colorFields3, 2), tmpthreshvals, _figure, False, 0, self.x3, self.y3, self.z3)
				else:
					self.iso3_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
		
	@on_trait_change('setThresholdPercent3')
	def setThresholdPercent_fired3(self):
		
		if self.screen1_ts3:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts3:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts3:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts3:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso3_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent3.split(',')
				
				if self.colorFields3 != 'None':
					self.plot_colorFieldData(self.iso3_sc1, self.whichColorFields(self.colorFields3, 2), tmpthreshvals, _figure, True, self.thresholdMaximum3, self.x3, self.y3, self.z3)
				else:
					self.iso3_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum3 for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('setThreshold4')
	def setThreshold_fired4(self):
		
		if self.screen1_ts4:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts4:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts4:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts4:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso4_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.threshold2.split(',')
				
				if self.colorFields4 != 'None':
					self.plot_colorFieldData(self.iso4_sc1, self.whichColorFields(self.colorFields4, 2), tmpthreshvals, _figure, False, 0, self.x4, self.y4, self.z4)
				else:
					self.iso4_sc1.contour.contours = [np.float32(i) for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('setThresholdPercent4')
	def setThresholdPercent_fired4(self):
		
		if self.screen1_ts4:
			
			_figure = self.scene1.mayavi_scene
		
		elif self.screen2_ts4:
			
			_figure = self.scene2.mayavi_scene
		
		elif self.screen3_ts4:
			
			_figure = self.scene3.mayavi_scene
		
		elif self.screen4_ts4:
			
			_figure = self.scene4.mayavi_scene
		
		else:
			
			_figure = None
			
		if _figure is not None:
		
			# First reset all contours
			self.iso4_sc1.contour.contours = []
			
			if self.colorFieldSet_sc1:
				self.mesh1.remove() # remove mesh if already exists
				self.colorFieldSet_sc1 = False
			
			try:
			
				tmpthreshvals = self.thresholdPercent3.split(',')
				
				if self.colorFields4 != 'None':
					self.plot_colorFieldData(self.iso4_sc1, self.whichColorFields(self.colorFields4, 2), tmpthreshvals, _figure, True, self.thresholdMaximum4, self.x4, self.y4, self.z4)
				else:
					self.iso4_sc1.contour.contours = [np.float32(i)*self.thresholdMaximum4 for i in tmpthreshvals]
			
			except ValueError:
				
				# Wait until user enters the values
				pass
