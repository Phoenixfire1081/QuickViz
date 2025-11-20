# Supplement to Mayavi Visualization
# All playground options are defined here

from traits.api import on_trait_change
import numpy as np

class allPlaygroundOptions:
		
	@on_trait_change('GenerateStructure')
	def generateStructureChanged(self):
		
		# TODO - Show dialog box that this will overwrite time series 1
		
		print(self.initCondition1)
		
		
		
		
