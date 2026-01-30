# Supplement to Mayavi Visualization
# All blender export options are defined here

from traits.api import on_trait_change
import numpy as np
import mayavi
from mayavi import mlab
import os
from skimage import measure
from stl import mesh

class allBlenderExportOptions:	
	
	@on_trait_change('exportSTLBlender')
	def exportSTLBlenderChanged(self):
		
		if self.screen1_ts1:
			
			if not self.thresholdPercent1 == '' or not self.threshold1 == '': # Ensures some threshold value is entered
				
				# Try threshold first
				# Take only the first value if multiple entires exist
				if not self.threshold1 == '':
					tmpthreshvals = self.threshold1.split(',')
					threshVal = np.float32(tmpthreshvals[0])
				else:
					tmpthreshvals = self.thresholdPercent1.split(',')
					threshVal = np.float32(tmpthreshvals[0])*self.thresholdMaximum1 
			
				# Use skimage measure to get the surface data
				
				if self.altBBox:
					
					xmin_reconn = self.whichSliceX1_reconn
					xmax_reconn = self.whichSliceX2_reconn
					ymin_reconn = self.whichSliceY1_reconn
					ymax_reconn = self.whichSliceY2_reconn
					zmin_reconn = self.whichSliceZ1_reconn
					zmax_reconn = self.whichSliceZ2_reconn
				
					verts, faces, _, _ = measure.marching_cubes(self._dataTs1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, self.whichTime1], 
					threshVal, spacing = (self.dx_data1, self.dy_data1, self.dz_data1))
				
				else:
				
					verts, faces, _, _ = measure.marching_cubes(self._dataTs1[:, :, :, self.whichTime1], 
					threshVal, spacing = (self.dx_data1, self.dy_data1, self.dz_data1))
				
				# Create the mesh
				finalMesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
				for i, f in enumerate(faces):
					for j in range(3):
						finalMesh.vectors[i][j] = verts[f[j],:]
					
				# Save it to the preferred location
				finalMesh.save(self.save_path + '/data.stl')
				
				
		
		
		
