# Supplement to Mayavi Visualization
# All background options are defined here

from traits.api import on_trait_change
import numpy as np

class allBackgroundOptions:

	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso1.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
