# Supplement to Mayavi Visualization
# All background options are defined here

from traits.api import on_trait_change
import numpy as np

class allBackgroundOptions:

	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso1_sc1.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc2.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc3.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc4.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
