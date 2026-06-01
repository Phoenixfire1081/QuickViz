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
			self.structVolumeAct = str(np.sum(self.structuredGrid == self.chooseStructure))
			
			self.structure1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1, 
			color = (1, 0, 0), line_width = 2, opacity = 1, extent = [xmin, xmax, ymin, ymax, zmin, zmax])
			
			# Calculate structure properties (mean velocity and vorticity within structure)
			
			if 'Vector' in self.ts1Type:
			
				if self.altBBox:
				
					xmin_reconn = self.whichSliceX1_reconn
					xmax_reconn = self.whichSliceX2_reconn
					ymin_reconn = self.whichSliceY1_reconn
					ymax_reconn = self.whichSliceY2_reconn
					zmin_reconn = self.whichSliceZ1_reconn
					zmax_reconn = self.whichSliceZ2_reconn
				
					ubox = self.u1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					vbox = self.v1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					wbox = self.w1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					
					om1box = self.omega1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					om2box = self.omega2[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
					om3box = self.omega3[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1]
				
					structuredGridBox = np.reshape(self.structuredGrid, np.shape(self.u1[:, :, :, self.whichTime1]))
					structuredGridBox = structuredGridBox[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn].ravel()
				
				else:
					
					ubox = self.u1[:, :, :, self.whichTime1]
					vbox = self.v1[:, :, :, self.whichTime1]
					wbox = self.w1[:, :, :, self.whichTime1]
					
					om1box = self.omega1[:, :, :, self.whichTime1]
					om2box = self.omega2[:, :, :, self.whichTime1]
					om3box = self.omega3[:, :, :, self.whichTime1]
				
					structuredGridBox = self.structuredGrid
				
				self.meanVelocityWithinStructure = str(np.mean(ubox.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.mean(vbox.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.mean(wbox.ravel()[structuredGridBox == self.chooseStructure]))
				self.maxVelocityWithinStructure = str(np.max(ubox.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.max(vbox.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.max(wbox.ravel()[structuredGridBox == self.chooseStructure]))
				
				structuredGridBoxGrid = np.reshape(structuredGridBox, np.shape(om1box))
				
				# Calculate peak circulation along all directions
				
				peakom1 = 0
				peakom2 = 0
				peakom3 = 0
				
				xlenB, ylenB, zlenB = np.shape(om1box)
				
				for i in range(xlenB):
					
					if np.abs(np.sum(om1box[i, :, :].ravel()[structuredGridBoxGrid[i, :, :].ravel() == self.chooseStructure]) * self.dy_data1 * self.dz_data1) > np.abs(peakom1):
						peakom1 = np.sum(om1box[i, :, :].ravel()[structuredGridBoxGrid[i, :, :].ravel() == self.chooseStructure]) * self.dy_data1 * self.dz_data1
				
				xlenB, ylenB, zlenB = np.shape(om2box)
				
				for i in range(ylenB):
					
					if np.abs(np.sum(om2box[:, i, :].ravel()[structuredGridBoxGrid[:, i, :].ravel() == self.chooseStructure]) * self.dx_data1 * self.dz_data1) > np.abs(peakom2):
						peakom2 = np.sum(om2box[:, i, :].ravel()[structuredGridBoxGrid[:, i, :].ravel() == self.chooseStructure]) * self.dx_data1 * self.dz_data1
				
				xlenB, ylenB, zlenB = np.shape(om3box)
				
				for i in range(zlenB):
					
					if np.abs(np.sum(om3box[:, :, i].ravel()[structuredGridBoxGrid[:, :, i].ravel() == self.chooseStructure]) * self.dx_data1 * self.dy_data1) > np.abs(peakom3):
						peakom3 = np.sum(om3box[:, :, i].ravel()[structuredGridBoxGrid[:, :, i].ravel() == self.chooseStructure]) * self.dx_data1 * self.dy_data1
				
				self.meanVorticityWithinStructure = str(peakom1) + ' ' + str(peakom2) + ' ' + str(peakom3)
				# self.maxVorticityWithinStructure = str(np.max(om1box.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.max(om2box.ravel()[structuredGridBox == self.chooseStructure])) + ' ' + str(np.max(om3box.ravel()[structuredGridBox == self.chooseStructure]))
				
				# This is polStrength in the log lattice simulations. polStrength = u_z / \int u_z d^2x = peak axial flow / peak axial flow rate, where u_z is the axial velocity
				# We will calculate the peak velocity and along all directions calculate the flow rate
				
				peakVelx = np.max(np.abs(ubox.ravel()[structuredGridBox == self.chooseStructure]))
				peakVely = np.max(np.abs(vbox.ravel()[structuredGridBox == self.chooseStructure]))
				peakVelz = np.max(np.abs(wbox.ravel()[structuredGridBox == self.chooseStructure]))
				
				peakVelx_loc = np.where(np.abs(ubox) == peakVelx)
				peakVely_loc = np.where(np.abs(vbox) == peakVely)
				peakVelz_loc = np.where(np.abs(wbox) == peakVelz)
				
				self.polStrengthWithinStructureX = str(np.sum(om1box[peakVelx_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(ubox[peakVelx_loc[0], :, :]) * self.dy_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om1box[peakVelx_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(ubox[:, peakVelx_loc[1], :]) * self.dx_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om1box[peakVelx_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(ubox[:, :, peakVelx_loc[2]]) * self.dx_data1 * self.dy_data1)
				
				self.polStrengthWithinStructureY = str(np.sum(om2box[peakVely_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(vbox[peakVely_loc[0], :, :]) * self.dy_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om2box[peakVely_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(vbox[:, peakVely_loc[1], :]) * self.dx_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om2box[peakVely_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(vbox[:, :, peakVely_loc[2]]) * self.dx_data1 * self.dy_data1)
				
				self.polStrengthWithinStructureZ = str(np.sum(om3box[peakVelz_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(wbox[peakVelz_loc[0], :, :]) * self.dy_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om3box[peakVelz_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(wbox[:, peakVelz_loc[1], :]) * self.dx_data1 * self.dz_data1) + ' ' +\
				str(np.sum(om3box[peakVelz_loc[0], :, :]) * self.dy_data1 * self.dz_data1/np.sum(wbox[:, :, peakVelz_loc[2]]) * self.dx_data1 * self.dy_data1)
				
				print(peakVelx, peakVely, peakVelz)
				print(peakVelx_loc, peakVely_loc, peakVelz_loc)
				print(np.sum(ubox[peakVelx_loc[0], :, :]) * self.dy_data1 * self.dz_data1, np.sum(ubox[:, peakVelx_loc[1], :]) * self.dx_data1 * self.dz_data1, np.sum(ubox[:, :, peakVelx_loc[2]]) * self.dx_data1 * self.dy_data1)
				print(np.sum(vbox[peakVely_loc[0], :, :]) * self.dy_data1 * self.dz_data1, np.sum(vbox[:, peakVely_loc[1], :]) * self.dx_data1 * self.dz_data1, np.sum(vbox[:, :, peakVely_loc[2]]) * self.dx_data1 * self.dy_data1)
				print(np.sum(wbox[peakVelz_loc[0], :, :]) * self.dy_data1 * self.dz_data1, np.sum(wbox[:, peakVelz_loc[1], :]) * self.dx_data1 * self.dz_data1, np.sum(wbox[:, :, peakVelz_loc[2]]) * self.dx_data1 * self.dy_data1)
		
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
		
		if self.thresholdExtractionSet == '':
			self.chosenThreshold = float(self.thresholdPercentExtractionSet) * self.thresholdMaximum1
		else:
			self.chosenThreshold = float(self.thresholdExtractionSet)
		
		self.structuredGrid = self.actualExtraction(self.chosenThreshold, self._dataTs1[:, :, :, self.whichTime1], 
		self.xlength_data1, self.ylength_data1, self.zlength_data1, True, self.verboseStructureExtraction,
		True, False, self.useMarchingCubes)
		
		# Update total number of extracted structures
		
		self.totalNumberOfExtractedStructures = int(np.max(self.structuredGrid))
		
		
