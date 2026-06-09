# Supplement to Mayavi Visualization
# All blender export options are defined here

from traits.api import on_trait_change
import numpy as np
import mayavi
from mayavi import mlab
import os
from skimage import measure
from scipy.ndimage import map_coordinates
from matplotlib import colormaps
from .isosurfaceOptions import allIsosurfaceOptions
try:
	from stl import mesh
except:
	print('Please run pip install stl.')
try:
	from plyfile import PlyData, PlyElement
except:
	print('Please run pip install plyfile.')

whichColorFields = allIsosurfaceOptions.whichColorFields

class allBlenderExportOptions:	
	
	@on_trait_change('exportSTLBlender')
	def exportSTLBlenderChanged(self):
		
		if self.screen1_ts1:
			
			if not self.thresholdPercent1 == '' or not self.threshold1 == '': # Ensures some threshold value is entered
				
				if not self.timeStep_LocalData == '': # Ensure user enters some time data
		
					if '-' in self.timeStep_LocalData:
						minTs = int(self.timeStep_LocalData.split('-')[0])
						maxTs = int(self.timeStep_LocalData.split('-')[1])
						
						# Check if skip values are provided
						try: 
							skipTs = int(self.timeStep_LocalData.split('-')[2])
						except:
							skipTs = 1
						
					else:
						minTs = int(self.timeStep_LocalData)
						maxTs = int(self.timeStep_LocalData)
						skipTs = 1
					
					for ts in range(minTs, maxTs+1, skipTs):
						
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
						
							verts, faces, _, _ = measure.marching_cubes(self._dataTs1[xmin_reconn:xmax_reconn, ymin_reconn:ymax_reconn, zmin_reconn:zmax_reconn, ts], 
							threshVal, spacing = (self.dx_data1, self.dy_data1, self.dz_data1))
						
						else:
						
							verts, faces, _, _ = measure.marching_cubes(self._dataTs1[:, :, :, ts], 
							threshVal, spacing = (self.dx_data1, self.dy_data1, self.dz_data1))
						
						# Create the mesh
						finalMesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
						for i, f in enumerate(faces):
							for j in range(3):
								finalMesh.vectors[i][j] = verts[f[j],:]
							
						# Save it to the preferred location
						finalMesh.save(self.save_path + '/sequence_'+str(ts).zfill(4)+'.stl')
				
	
	@on_trait_change('exportPLYBlender')
	def exportPLYBlenderChanged(self):
		
		if self.screen1_ts1:
			
			if not self.thresholdPercent1 == '' or not self.threshold1 == '': # Ensures some threshold value is entered
				
				if not self.timeStep_LocalData == '': # Ensure user enters some time data
		
					if '-' in self.timeStep_LocalData:
						minTs = int(self.timeStep_LocalData.split('-')[0])
						maxTs = int(self.timeStep_LocalData.split('-')[1])
						
						# Check if skip values are provided
						try: 
							skipTs = int(self.timeStep_LocalData.split('-')[2])
						except:
							skipTs = 1
						
					else:
						minTs = int(self.timeStep_LocalData)
						maxTs = int(self.timeStep_LocalData)
						skipTs = 1
					
					for ts in range(minTs, maxTs+1, skipTs):
						
						self.whichTime1 = ts
				
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
						
						if not self.colorFields1 == 'None':
							
							# Get the correct scalar data from whichColorfields
							scalar = self.whichColorFields(self.colorFields1, 1)
							
							# Use interpolation to map it to the verts
							vertex_values = map_coordinates(scalar, [verts[:, 0], verts[:, 1], verts[:, 2]], order=3, mode="nearest")
							vmin, vmax = self.mesh1.module_manager.scalar_lut_manager.data_range
							
							# vertex_values_clipped = np.clip(vertex_values, vmin, vmax)
							
							# # vmin, vmax = self.mesh1.module_manager.scalar_lut_manager.data_range

							# norm = (vertex_values_clipped - vmin) / (vmax - vmin)
							
							# # Get the cmap data from mayavi itself
							lut_table = self.mesh1.module_manager.scalar_lut_manager.lut.table.to_array()
							# print(self.mesh1.module_manager.scalar_lut_manager.data_range)
							# print(self.mesh1.module_manager.scalar_lut_manager.lut_mode)
							# idx = np.clip((norm * 255).astype(np.int32), 0, 255)
							norm = np.clip((vertex_values - vmin) / (vmax - vmin), 0.0, 1.0)
							idx = np.round(norm * 255).astype(np.uint8)
							rgb = lut_table[idx, :3]
							
							print(np.shape(vertex_values), np.shape(lut_table), np.shape(rgb))
							print(rgb[:10])

							# Create vertex table
							vertex_dtype = np.dtype([
								("x", "f4"),
								("y", "f4"),
								("z", "f4"),
								("red", "u1"),
								("green", "u1"),
								("blue", "u1"),
							])
							
							vertex_data = np.empty(len(verts), dtype=vertex_dtype)

							vertex_data["x"] = verts[:, 0]
							vertex_data["y"] = verts[:, 1]
							vertex_data["z"] = verts[:, 2]

							vertex_data["red"] = rgb[:, 0]
							vertex_data["green"] = rgb[:, 1]
							vertex_data["blue"] = rgb[:, 2]
						
						else:
						
							vertex_dtype = np.dtype([
								("x", "f4"),
								("y", "f4"),
								("z", "f4"),
							])

							vertex_data = np.empty(len(verts), dtype=vertex_dtype)

							vertex_data["x"] = verts[:, 0]
							vertex_data["y"] = verts[:, 1]
							vertex_data["z"] = verts[:, 2]

						# Assign the face values
						face_data = np.empty(len(faces), dtype=[("vertex_indices", "i4", (3,))])
						face_data["vertex_indices"] = faces

						# Write data to file
						PlyData([PlyElement.describe(vertex_data, "vertex"),PlyElement.describe(face_data, "face"),], text=False).write(self.save_path + '/sequence_'+str(ts).zfill(4)+'.ply')
				
		
		
		
