# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
try:
	from extractStructuresWithMC import extractStructuresMC
except:
	print('Structure extraction will not work.. please run: pip install extractstructuresMC')

class allSurfaceExtractionOptions:
	
	@on_trait_change('chooseStructure')
	def extractSpecificStructure(self):
		
		if self.chooseStructure < int(self.totalNumberOfExtractedStructures):
			
			print(self.chooseStructure)
			self.structuredGrid == self.chooseStructure
		
	
	def actualExtraction(self, _threshVal, data, 
	xlen, ylen, zlen, _zFastest, _verbose, 
	_writeNeighborInformation, _writePercolationData, _marchingCubesExt):
		
		extractStructuresObj = extractStructuresMC(_threshVal, data, 
		xlen, ylen, zlen, _zFastest, _verbose, 
		_writeNeighborInformation, _writePercolationData, _marchingCubesExt)
		
		return extractStructuresObj.extract()
		
	@on_trait_change('extractStructures')
	def enableExtractStructures(self):
		
		# Perform extraction for objects on screen 1
		
		self.structuredGrid = self.actualExtraction(float(self.thresholdExtractionSet), self._dataTs1[:, :, :, self.whichTime1], 
		self.xlength_data1, self.ylength_data1, self.zlength_data1, True, self.verboseStructureExtraction,
		False, False, self.useMarchingCubes)
		
		# Update total number of extracted structures
		
		self.totalNumberOfExtractedStructures = str(np.max(self.structuredGrid))
		
		# Use range slider to select a particular structure
		
		
		
		# Choose extracted structure with a small box around it
		
		# Assign structValuedGrid to timeSeries2
		
		# if self.radioButton1 == 'Y' or self.clamp == 1:
			
			# if self.screen1_ts1:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol1_sc1.remove()
					# except AttributeError:
						# pass # Set volume rendering first
				
				# self.volRender1_actual(1, self.scene1.mayavi_scene)
			
			# if self.screen2_ts1:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol1_sc2.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender1_actual(2, self.scene2.mayavi_scene)
			
			# if self.screen3_ts1:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol1_sc3.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender1_actual(3, self.scene3.mayavi_scene)
			
			# if self.screen4_ts1:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol1_sc4.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender1_actual(4, self.scene4.mayavi_scene)
			
		# if self.radioButton2 == 'Y' or self.clamp == 1:
			
			# if self.screen1_ts2:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol2_sc1.remove()
					# except AttributeError:
						# pass # Set volume rendering first
				
				# self.volRender2_actual(1, self.scene1.mayavi_scene)
			
			# if self.screen2_ts2:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol2_sc2.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender2_actual(2, self.scene2.mayavi_scene)
			
			# if self.screen3_ts2:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol2_sc3.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender2_actual(3, self.scene3.mayavi_scene)
			
			# if self.screen4_ts2:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol2_sc4.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender2_actual(4, self.scene4.mayavi_scene)
		
		# if self.radioButton3 == 'Y' or self.clamp == 1:
			
			# if self.screen1_ts3:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol3_sc1.remove()
					# except AttributeError:
						# pass # Set volume rendering first
				
				# self.volRender3_actual(1, self.scene1.mayavi_scene)
			
			# if self.screen2_ts3:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol3_sc2.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender3_actual(2, self.scene2.mayavi_scene)
			
			# if self.screen3_ts3:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol3_sc3.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender3_actual(3, self.scene3.mayavi_scene)
			
			# if self.screen4_ts3:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol3_sc4.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender3_actual(4, self.scene4.mayavi_scene)
		
		# if self.radioButton4 == 'Y' or self.clamp == 1:
			
			# if self.screen1_ts4:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol4_sc1.remove()
					# except AttributeError:
						# pass # Set volume rendering first
				
				# self.volRender4_actual(1, self.scene1.mayavi_scene)
			
			# if self.screen2_ts4:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol4_sc2.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender4_actual(2, self.scene2.mayavi_scene)
			
			# if self.screen3_ts4:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol4_sc3.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender4_actual(3, self.scene3.mayavi_scene)
			
			# if self.screen4_ts4:
				
				# if not self.justRemovedVolRender:
					# try:
						# self.vol4_sc4.remove()
					# except AttributeError:
						# pass # Set volume rendering first
			
				# self.volRender4_actual(4, self.scene4.mayavi_scene)		
		
		# self.justRemovedVolRender = False

	# @on_trait_change('removeVolRender')
	# def removeVolRenderChanged(self):
		
		# if self.radioButton1 == 'Y':
			
			# if self.screen1_ts1:
			
				# try:
					# self.vol1_sc1.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen2_ts1:
			
				# try:
					# self.vol1_sc2.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen3_ts1:
			
				# try:
					# self.vol1_sc3.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen4_ts1:
			
				# try:
					# self.vol1_sc4.remove()
				# except AttributeError:
					# pass # Set slice first
		
		# if self.radioButton2 == 'Y':
			
			# if self.screen1_ts2:
			
				# try:
					# self.vol2_sc1.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen2_ts2:
			
				# try:
					# self.vol2_sc2.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen3_ts2:
			
				# try:
					# self.vol2_sc3.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen4_ts2:
			
				# try:
					# self.vol2_sc4.remove()
				# except AttributeError:
					# pass # Set slice first
		
		# if self.radioButton3 == 'Y':
			
			# if self.screen1_ts3:
			
				# try:
					# self.vol3_sc1.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen2_ts3:
			
				# try:
					# self.vol3_sc2.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen3_ts3:
			
				# try:
					# self.vol3_sc3.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen4_ts3:
			
				# try:
					# self.vol3_sc4.remove()
				# except AttributeError:
					# pass # Set slice first
		
		# if self.radioButton4 == 'Y':
			
			# if self.screen1_ts4:
			
				# try:
					# self.vol4_sc1.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen2_ts4:
			
				# try:
					# self.vol4_sc2.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen3_ts4:
			
				# try:
					# self.vol4_sc3.remove()
				# except AttributeError:
					# pass # Set slice first
			
			# if self.screen4_ts4:
			
				# try:
					# self.vol4_sc4.remove()
				# except AttributeError:
					# pass # Set slice first
			
		# self.justRemovedVolRender = True
