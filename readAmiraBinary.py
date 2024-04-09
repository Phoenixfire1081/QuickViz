import struct
import numpy as np

# Script to read Amira binary data
# Works for 3D structured grids and float data (tested - works)
# double is untested

# Last updated: 09-04-2024

class read_amira_file:
	
	def __init__(self, filename, _dtype):
		
		# Set _dtype
		self._dtype = _dtype
		
		with open(filename, "rb") as f:
			self.amFile = f.read()
		
		# Split it along the new lines
		self.amFileSplit = self.amFile.split(b'\n')
		
		ctrMin = 0
		ctrMax = 2
		encounters = 0
		
		# Determine where the data starts
		for i in range(len(self.amFile)):
			if struct.unpack('2s', self.amFile[ctrMin:ctrMax])[0] == b'@1':
				encounters += 1
				if encounters == 1:
					pass
				else:
					self.startPoint = ctrMax + 1 # skip new line
					print('Data start point: ', self.startPoint)
					break
			ctrMin += 2
			ctrMax += 2
	
	def get_data(self, xlen, ylen, zlen, _dtype):
		
		if _dtype == 'f':
			tmpArray = np.zeros((xlen * ylen * zlen), dtype = np.float32)
			xArray = np.zeros((xlen), dtype = np.float32)
			yArray = np.zeros((ylen), dtype = np.float32)
			zArray = np.zeros((zlen), dtype = np.float32)
		
		if _dtype == 'd':
			tmpArray = np.zeros((xlen * ylen * zlen), dtype = np.float64)
			xArray = np.zeros((xlen), dtype = np.float64)
			yArray = np.zeros((ylen), dtype = np.float64)
			zArray = np.zeros((zlen), dtype = np.float64)
		
		if _dtype == 'f':
			ctrMin = self.startPoint + 0
			ctrMax = self.startPoint + (4 * xlen * ylen * zlen)
			
			# print(ctr)
		
		if _dtype == 'd':
			ctrMin = self.startPoint + 0
			ctrMax = self.startPoint + (8 * xlen * ylen * zlen)
		
		# Don't use loops
		if _dtype == 'f':
			tmpArray[:] += np.array(struct.unpack(str(xlen * ylen * zlen) + 'f', self.amFile[ctrMin:ctrMax]))
		
		if _dtype == 'd':
			tmpArray[:] += np.array(struct.unpack(str(xlen * ylen * zlen) + 'd', self.amFile[ctrMin:ctrMax]))
		
		tmpArray = np.reshape(tmpArray, [xlen, ylen, zlen], order = 'F') 
		# Amira data has Fortran indexing
		
		# Keep last index to determine where the coordinate point starts
		self.startPointC = ctrMax
		print('Coordinate start point:', self.startPointC)
		
		# Get coordinate information
		
		if _dtype == 'f':
			ctrMin = self.startPointC + 4
			ctrMax = self.startPointC + 4 + (4 * xlen)
		
		if _dtype == 'd':
			ctrMin = self.startPointC + 8
			ctrMax = self.startPointC + 8 + (8 * xlen)

		if _dtype == 'f':
			xArray[:] += np.array(struct.unpack(str(xlen) + 'f', self.amFile[ctrMin:ctrMax]))
		if _dtype == 'd':
			xArray[:] += np.array(struct.unpack(str(xlen) + 'd', self.amFile[ctrMin:ctrMax]))
		
		self.startPointC = ctrMax
		
		if _dtype == 'f':
			ctrMin = self.startPointC + 0
			ctrMax = self.startPointC + (4 * ylen)
		
		if _dtype == 'd':
			ctrMin = self.startPointC + 0
			ctrMax = self.startPointC + (8 * ylen)

		if _dtype == 'f':
			yArray[:] += np.array(struct.unpack(str(ylen) + 'f', self.amFile[ctrMin:ctrMax]))
		if _dtype == 'd':
			yArray[:] += np.array(struct.unpack(str(ylen) + 'd', self.amFile[ctrMin:ctrMax]))
			
		self.startPointC = ctrMax
		
		if _dtype == 'f':
			ctrMin = self.startPointC + 0
			ctrMax = self.startPointC + (4 * zlen)
		
		if _dtype == 'd':
			ctrMin = self.startPointC + 0
			ctrMax = self.startPointC + (8 * zlen)

		if _dtype == 'f':
			zArray[:] += np.array(struct.unpack(str(zlen) + 'f', self.amFile[ctrMin:ctrMax]))
		if _dtype == 'd':
			zArray[:] += np.array(struct.unpack(str(zlen) + 'd', self.amFile[ctrMin:ctrMax]))
		
		return tmpArray, xArray, yArray, zArray
		
	
	def get_lattice_information(self):
		
		tmp = self.amFileSplit[1].split(b' ')
		
		return int(tmp[2]), int(tmp[3]), int(tmp[4])
	
	def unpack_all(self):
		
		# get xlen, ylen and zlen
		
		xlen, ylen, zlen = self.get_lattice_information()
		print('Data is of shape:', xlen, ylen, zlen)
		
		# get scalar field
		
		arr, x, y, z = self.get_data(xlen, ylen, zlen, self._dtype)
		
		return arr, x, y, z
	
# _dtype = 'f'
# obj = read_amira_file('FlowFit_000.am', _dtype)
# arr, x, y, z = obj.unpack_all()
