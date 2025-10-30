# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
import mayavi
from mayavi import mlab
import os
from copy import deepcopy
try:
	from extractStructuresWithMC import extractStructuresMC
except:
	print('Structure extraction will not work.. please run: pip install extractstructuresMC')

class allSurfaceExtractionOptions:
	
	def clip_grid(self, n, Q, _structValuedGrid, _lastVal, verbose):
		
		# If the structure is last [0] indexing is not necessary when reading the file
		if _lastVal:
		
			_structureExtent = np.loadtxt('NeighborInformation.txt', skiprows = n-1, dtype = int)

		else:
			
			_structureExtent = np.loadtxt('NeighborInformation.txt', skiprows = n-1, dtype = int)[0]
		
		if verbose:
			print('Original Extent:',_structureExtent)
		
		_structureExtentOrig = deepcopy(_structureExtent)
		
		# Expanded grid is necessary to read and write files properly
		_expandedGrid = 1
		
		_structureExtent[1] += -_expandedGrid
		_structureExtent[2] += _expandedGrid
		_structureExtent[3] += -_expandedGrid
		_structureExtent[4] += _expandedGrid
		_structureExtent[5] += -_expandedGrid
		_structureExtent[6] += _expandedGrid
		
		if _expandedGrid >= 1:
			
			if _structureExtent[1] < 0:
				_structureExtent[1] = 0
			
			if _structureExtent[2] > self.xlength_data1:
				_structureExtent[2] = self.xlength_data1
			
			if _structureExtent[3] < 0:
				_structureExtent[3] = 0
			
			if _structureExtent[4] > self.ylength_data1:
				_structureExtent[4] = self.ylength_data1
			
			if _structureExtent[5] < 0:
				_structureExtent[5] = 0
			
			if _structureExtent[6] > self.zlength_data1:
				_structureExtent[6] = self.zlength_data1
		
		if verbose:
			print('Modified Extent:',_structureExtent)
		
		xlen_structure = _structureExtent[2] - _structureExtent[1]
		ylen_structure = _structureExtent[4] - _structureExtent[3]
		zlen_structure = _structureExtent[6] - _structureExtent[5]
		
		_newGrid = np.zeros((xlen_structure, ylen_structure, zlen_structure), dtype = np.float32)
		_newGrid = _newGrid.ravel()
		
		Q = Q[_structureExtent[1]:_structureExtent[2], _structureExtent[3]:_structureExtent[4], _structureExtent[5]:_structureExtent[6]]
		Q = Q.ravel()
		
		_structValuedGrid = np.reshape(_structValuedGrid, [self.xlength_data1, self.ylength_data1, self.zlength_data1])
		_structValuedGrid = _structValuedGrid[_structureExtent[1]:_structureExtent[2], _structureExtent[3]:_structureExtent[4], _structureExtent[5]:_structureExtent[6]]
		_structValuedGrid = _structValuedGrid.ravel()
		
		largeArray = []
		
		# Reconstruct grid with original values
		for i, val in enumerate(_structValuedGrid):
			
			if val == n:
				
				_newGrid[i] = Q[i]
				largeArray.append(Q[i])
			
			else:
				
				_newGrid[i] = 0
				
		_newGrid = np.reshape(_newGrid, [xlen_structure, ylen_structure, zlen_structure])
		
		return _newGrid, _structureExtent, largeArray, _structureExtentOrig
	
	@on_trait_change('chooseStructure')
	def extractSpecificStructure(self):
		
		try:
			self.structure1_sc1.remove()
		except:
			pass
		
		if self.chooseStructure <= int(self.totalNumberOfExtractedStructures) and self.chooseStructure > 0:
			
			if self.chooseStructure == int(self.totalNumberOfExtractedStructures):
				_, _, largeArrayxx, largeArrayIdx = self.clip_grid(self.chooseStructure, self.x1, self.structuredGrid, True, self.verboseStructureExtraction)
				_, _, largeArrayyy, _ = self.clip_grid(self.chooseStructure, self.y1, self.structuredGrid, True, self.verboseStructureExtraction)
				_, _, largeArrayzz, _ = self.clip_grid(self.chooseStructure, self.z1, self.structuredGrid, True, self.verboseStructureExtraction)
			else:
				_, _, largeArrayxx, largeArrayIdx = self.clip_grid(self.chooseStructure, self.x1, self.structuredGrid, False, self.verboseStructureExtraction)
				_, _, largeArrayyy, _ = self.clip_grid(self.chooseStructure, self.y1, self.structuredGrid, False, self.verboseStructureExtraction)
				_, _, largeArrayzz, _ = self.clip_grid(self.chooseStructure, self.z1, self.structuredGrid, False, self.verboseStructureExtraction)
			
			xmin = np.min(largeArrayxx)
			xmax = np.max(largeArrayxx)
			xmaxOrig = xmax
			if np.allclose([xmin], [xmax]) == True:
				xmax = xmax * 1.01
				if xmax == 0:
					xmax = 0.01
			ymin = np.min(largeArrayyy)
			ymax = np.max(largeArrayyy)
			ymaxOrig = ymax
			if np.allclose([ymin], [ymax]) == True:
				ymax = ymax * 1.01
				if ymax == 0:
					ymax = 0.01
			zmin = np.min(largeArrayzz)
			zmax = np.max(largeArrayzz)
			zmaxOrig = zmax
			if np.allclose([zmin], [zmax]) == True:
				zmax = zmax * 1.01
				if zmax == 0:
					zmax = 0.01
				
			# Set extent (Idx and Act)
			self.structXminAct = str(np.round(xmin, 3))
			self.structXmaxAct = str(np.round(xmaxOrig, 3))
			self.structYminAct = str(np.round(ymin, 3))
			self.structYmaxAct = str(np.round(ymaxOrig, 3))
			self.structZminAct = str(np.round(zmin, 3))
			self.structZmaxAct = str(np.round(zmaxOrig, 3))
			
			self.structXminIdx = str(largeArrayIdx[1])
			self.structXmaxIdx = str(largeArrayIdx[2])
			self.structYminIdx = str(largeArrayIdx[3])
			self.structYmaxIdx = str(largeArrayIdx[4])
			self.structZminIdx = str(largeArrayIdx[5])
			self.structZmaxIdx = str(largeArrayIdx[6])
			
			self.structVolume = str((largeArrayIdx[2] - largeArrayIdx[1]) * (largeArrayIdx[4] - largeArrayIdx[3]) * (largeArrayIdx[6] - largeArrayIdx[5]))
			
			self.structure1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1, 
			color = (1, 0, 0), line_width = 2, opacity = 1, extent = [xmin, xmax, ymin, ymax, zmin, zmax])
		
	def actualExtraction(self, _threshVal, data, 
	xlen, ylen, zlen, _zFastest, _verbose, 
	_writeNeighborInformation, _writePercolationData, _marchingCubesExt):
		
		extractStructuresObj = extractStructuresMC(_threshVal, data, 
		xlen, ylen, zlen, _zFastest, _verbose, 
		_writeNeighborInformation, _writePercolationData, _marchingCubesExt)
		
		return extractStructuresObj.extract()
		
	@on_trait_change('extractStructures')
	def enableExtractStructures(self):
		
		# Remove NeighborInformation.txt if present
		os.system('rm -rf NeighborInformation.txt')
		
		# Perform extraction for objects on screen 1
		
		self.structuredGrid = self.actualExtraction(float(self.thresholdExtractionSet), self._dataTs1[:, :, :, self.whichTime1], 
		self.xlength_data1, self.ylength_data1, self.zlength_data1, True, self.verboseStructureExtraction,
		True, False, self.useMarchingCubes)
		
		# Update total number of extracted structures
		
		self.totalNumberOfExtractedStructures = int(np.max(self.structuredGrid))
		
		
