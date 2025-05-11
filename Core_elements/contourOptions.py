# Supplement to Mayavi Visualization
# All contour options are defined here

from traits.api import on_trait_change
import numpy as np

class allContourOptions:

	@on_trait_change('outlineWidth1, outlineColorRed1, outlineColorGreen1,\
	outlineColorBlue1, outlineToggle1')
	def outline_changed1(self):
		
		# Toggle outline
		if not self.outlineToggle1:
			self.out1_sc1.actor.actor.visibility = False
		else:
			self.out1_sc1.actor.actor.visibility = True
			
			# Change outline width
			self.out1_sc1.actor.property.line_width = self.outlineWidth1
			
			# Change outline color
			self.out1_sc1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
	
	@on_trait_change('contourOpacity1, contourRepresentation1, contourColormap1, colormapMin1, colormapMax1')
	def contour_changed1(self):
		
		# Change contour opacity
		self.iso1_sc1.actor.property.opacity = self.contourOpacity1
		
		# Change contour representation
		self.iso1_sc1.actor.property.representation = self.contourRepresentation1
		
		# Change contour colormap
		self.iso1_sc1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
		
		# Change colormap range
		self.iso1_sc1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
	
	@on_trait_change('outlineWidth2, outlineColorRed2, outlineColorGreen2,\
	outlineColorBlue2, outlineToggle2')
	def outline_changed2(self):
		
		# Toggle outline
		if not self.outlineToggle2:
			self.out2.actor.actor.visibility = False
		else:
			self.out2.actor.actor.visibility = True
			
			# Change outline width
			self.out2.actor.property.line_width = self.outlineWidth2
			
			# Change outline color
			self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
	
	@on_trait_change('contourOpacity2, contourRepresentation2, contourColormap2, colormapMin2, colormapMax2')
	def contour_changed2(self):
		
		# Change contour opacity
		self.iso2.actor.property.opacity = self.contourOpacity2
		
		# Change contour representation
		self.iso2.actor.property.representation = self.contourRepresentation2
		
		# Change contour colormap
		self.iso2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
		
		# Change colormap range
		self.iso2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
	
	@on_trait_change('outlineWidth3, outlineColorRed3, outlineColorGreen3,\
	outlineColorBlue3, outlineToggle3')
	def outline_changed3(self):
		
		# Toggle outline
		if not self.outlineToggle3:
			self.out3.actor.actor.visibility = False
		else:
			self.out3.actor.actor.visibility = True
			
			# Change outline width
			self.out3.actor.property.line_width = self.outlineWidth3
			
			# Change outline color
			self.out3.actor.property.color = (self.outlineColorRed3, self.outlineColorGreen3, self.outlineColorBlue3)
	
	@on_trait_change('contourOpacity3, contourRepresentation3, contourColormap3, colormapMin3, colormapMax3')
	def contour_changed3(self):
		
		# Change contour opacity
		self.iso3.actor.property.opacity = self.contourOpacity3
		
		# Change contour representation
		self.iso3.actor.property.representation = self.contourRepresentation3
		
		# Change contour colormap
		self.iso3.module_manager.scalar_lut_manager.lut_mode = self.contourColormap3
		
		# Change colormap range
		self.iso3.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin3, self.colormapMax3])
	
	@on_trait_change('outlineWidth4, outlineColorRed4, outlineColorGreen4,\
	outlineColorBlue4, outlineToggle4')
	def outline_changed4(self):
		
		# Toggle outline
		if not self.outlineToggle4:
			self.out4.actor.actor.visibility = False
		else:
			self.out4.actor.actor.visibility = True
			
			# Change outline width
			self.out4.actor.property.line_width = self.outlineWidth4
			
			# Change outline color
			self.out4.actor.property.color = (self.outlineColorRed4, self.outlineColorGreen4, self.outlineColorBlue4)
	
	@on_trait_change('contourOpacity4, contourRepresentation4, contourColormap4, colormapMin4, colormapMax4')
	def contour_changed4(self):
		
		# Change contour opacity
		self.iso4.actor.property.opacity = self.contourOpacity4
		
		# Change contour representation
		self.iso4.actor.property.representation = self.contourRepresentation4
		
		# Change contour colormap
		self.iso4.module_manager.scalar_lut_manager.lut_mode = self.contourColormap4
		
		# Change colormap range
		self.iso4.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin4, self.colormapMax4])
