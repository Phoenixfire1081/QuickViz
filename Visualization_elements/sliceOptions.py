# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
import numpy.ctypeslib as npct
import numpy as np
from scipy.ndimage import zoom
import os
from .lic_internal import line_integral_convolution


class allSliceOptions:
	def update_camera_at_current_timestep_with_camPath(self, camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle):
		# If camera path is set, use that instead
		if not self.camPathType == "None":
			_, camAzimuth, camElevation, camDistance, fp1, fp2, fp3, camRoll, _ = np.loadtxt("cameraPath.txt")[self.whichTime1]
		viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint, figure=figureHandle)
		viewControlRoll = mlab.roll(camRoll, figure=figureHandle)

	def setSlice_actual(self, scNumber, figureHandle):
		
		if scNumber == 1:
			
			_data = self._dataTs1[:, :, :, self.whichTime1]
			
			_u = self.u1[:, :, :, self.whichTime1]
			_v = self.v1[:, :, :, self.whichTime1]
			_w = self.w1[:, :, :, self.whichTime1]
			
			_omega1 = self.omega1[:, :, :, self.whichTime1]
			_omega2 = self.omega2[:, :, :, self.whichTime1]
			_omega3 = self.omega3[:, :, :, self.whichTime1]
			
			_xlength_data = self.xlength_data1
			_ylength_data = self.ylength_data1
			_zlength_data = self.zlength_data1
			
			_dx_data = self.dx_data1
			_dy_data = self.dy_data1
			_dz_data = self.dz_data1
			
			_xmin_data = self.xmin_data1
			_ymin_data = self.ymin_data1
			_zmin_data = self.zmin_data1
			# _xmax_data = self.xmax_data1
			# _ymax_data = self.ymax_data1
			# _zmax_data = self.zmax_data1
			
			_colormap = self.contourColormap1
			_opacity = self.contourOpacity1
			_colormapMin = self.colormapMin1
			_colormapMax = self.colormapMax1
			
			_x = self.x1
			_y = self.y1
			_z = self.z1
		
		elif scNumber == 2:
			
			_data = self._dataTs2[:, :, :, self.whichTime2]
			
			_u = self.u2[:, :, :, self.whichTime2]
			_v = self.v2[:, :, :, self.whichTime2]
			_w = self.w2[:, :, :, self.whichTime2]
			
			_omega2 = self.omega1[:, :, :, self.whichTime2]
			_omega2 = self.omega2[:, :, :, self.whichTime2]
			_omega3 = self.omega3[:, :, :, self.whichTime2]
			
			_xlength_data = self.xlength_data2
			_ylength_data = self.ylength_data2
			_zlength_data = self.zlength_data2
			
			_dx_data = self.dx_data2
			_dy_data = self.dy_data2
			_dz_data = self.dz_data2
			
			_xmin_data = self.xmin_data2
			_ymin_data = self.ymin_data2
			_zmin_data = self.zmin_data2
			# _xmax_data = self.xmax_data2
			# _ymax_data = self.ymax_data2
			# _zmax_data = self.zmax_data2
			
			_colormap = self.contourColormap2
			_opacity = self.contourOpacity2
			_colormapMin = self.colormapMin2
			_colormapMax = self.colormapMax2
			
			_x = self.x2
			_y = self.y2
			_z = self.z2
		
		elif scNumber == 3:
			
			_data = self._dataTs3[:, :, :, self.whichTime3]
			
			_u = self.u3[:, :, :, self.whichTime3]
			_v = self.v3[:, :, :, self.whichTime3]
			_w = self.w3[:, :, :, self.whichTime3]
			
			_omega3 = self.omega1[:, :, :, self.whichTime3]
			_omega3 = self.omega2[:, :, :, self.whichTime3]
			_omega3 = self.omega3[:, :, :, self.whichTime3]
			
			_xlength_data = self.xlength_data3
			_ylength_data = self.ylength_data3
			_zlength_data = self.zlength_data3
			
			_dx_data = self.dx_data3
			_dy_data = self.dy_data3
			_dz_data = self.dz_data3
			
			_xmin_data = self.xmin_data3
			_ymin_data = self.ymin_data3
			_zmin_data = self.zmin_data3
			# _xmax_data = self.xmax_data3
			# _ymax_data = self.ymax_data3
			# _zmax_data = self.zmax_data3
			
			_colormap = self.contourColormap3
			_opacity = self.contourOpacity3
			_colormapMin = self.colormapMin3
			_colormapMax = self.colormapMax3
			
			_x = self.x3
			_y = self.y3
			_z = self.z3
		
		elif scNumber == 4:
			
			_data = self._dataTs4[:, :, :, self.whichTime4]
			
			_u = self.u4[:, :, :, self.whichTime4]
			_v = self.v4[:, :, :, self.whichTime4]
			_w = self.w4[:, :, :, self.whichTime4]
			
			_omega4 = self.omega1[:, :, :, self.whichTime4]
			_omega4 = self.omega2[:, :, :, self.whichTime4]
			_omega3 = self.omega3[:, :, :, self.whichTime4]
			
			_xlength_data = self.xlength_data4
			_ylength_data = self.ylength_data4
			_zlength_data = self.zlength_data4
			
			_dx_data = self.dx_data4
			_dy_data = self.dy_data4
			_dz_data = self.dz_data4
			
			_xmin_data = self.xmin_data4
			_ymin_data = self.ymin_data4
			_zmin_data = self.zmin_data4
			# _xmax_data = self.xmax_data4
			# _ymax_data = self.ymax_data4
			# _zmax_data = self.zmax_data4
			
			_colormap = self.contourColormap4
			_opacity = self.contourOpacity4
			_colormapMin = self.colormapMin4
			_colormapMax = self.colormapMax4
			
			_x = self.x4
			_y = self.y4
			_z = self.z4

		if self.sliceType == "Fieldlines":
			# Set constant seed
			np.random.seed(12345)
			
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
				camRoll = mlab.roll(figure=figureHandle)

			if self.planeOrientation == "X":
				scalex = self.noiseImageDimensionSliceX / _ylength_data
				scaley = self.noiseImageDimensionSliceY / _zlength_data

				tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

				if self.whichVector == "Velocity":
					tmpVectorSlice[:, :, 0] += zoom(_w[self.whichSliceX, :, :], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_v[self.whichSliceX, :, :], (scalex, scaley), order=1)

				else:
					tmpVectorSlice[:, :, 0] += zoom(_omega3[self.whichSliceX, :, :], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_omega2[self.whichSliceX, :, :], (scalex, scaley), order=1)

				texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

				kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
				kernel = kernel.astype(np.float32)

				image = line_integral_convolution(tmpVectorSlice, texture, kernel)
				pos = (self.whichSliceX * _dx_data) + _xmin_data

				self.volSlice1_sc1 = mlab.imshow(image.T, colormap=_colormap, opacity=_opacity, figure=figureHandle)
				
				self.volSlice1_sc1.actor.orientation = [0, 90, 0]
				self.volSlice1_sc1.actor.position = [pos, 0, 0]
				self.volSlice1_sc1.actor.scale = [_dz_data / scalex, _dy_data / scaley, self._dx_data]
					
			if self.planeOrientation == "Y":
				scalex = self.noiseImageDimensionSliceX / _xlength_data
				scaley = self.noiseImageDimensionSliceY / _zlength_data

				tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

				if self.whichVector == "Velocity":
					tmpVectorSlice[:, :, 0] += zoom(_w[:, self.whichSliceY, :], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_u1[:, self.whichSliceY, :], (scalex, scaley), order=1)

				else:
					tmpVectorSlice[:, :, 0] += zoom(_omega3[:, self.whichSliceY, :], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_omega1[:, self.whichSliceY, :], (scalex, scaley), order=1)

				texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

				kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
				kernel = kernel.astype(np.float32)

				image = line_integral_convolution(tmpVectorSlice, texture, kernel)
				pos = (self.whichSliceY * _dy_data) + self._ymin_data

				# self.dx_data1*6 corrects for a strange offset in imshow.

				self.volSlice1_sc1 = mlab.imshow(image, colormap=_colormap, opacity=_opacity, figure=figureHandle)

				self.volSlice1_sc1.actor.orientation = [90, 0, 0]
				# self.volSlice1_sc1.actor.position = [self.dx_data1*6, pos, 0]
				self.volSlice1_sc1.actor.position = [0, pos, 0]
				self.volSlice1_sc1.actor.scale = [_dx_data / scalex, _dz_data / scaley, _dy_data]

			if self.planeOrientation == "Z":
				scalex = self.noiseImageDimensionSliceX / _xlength_data
				scaley = self.noiseImageDimensionSliceY / _ylength_data

				tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

				if self.whichVector == "Velocity":
					tmpVectorSlice[:, :, 0] += zoom(_v[:, :, self.whichSliceZ], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_u[:, :, self.whichSliceZ], (scalex, scaley), order=1)

				else:
					tmpVectorSlice[:, :, 0] += zoom(_omega2[:, :, self.whichSliceZ], (scalex, scaley), order=1)
					tmpVectorSlice[:, :, 1] += zoom(_omega1[:, :, self.whichSliceZ], (scalex, scaley), order=1)

				texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

				kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
				kernel = kernel.astype(np.float32)

				image = line_integral_convolution(tmpVectorSlice, texture, kernel)
				pos = (self.whichSliceZ * _dz_data) + self._zmin_data

				# self.dx_data1*6 corrects for a strange offset in imshow.

				self.volSlice1_sc1 = mlab.imshow(image, colormap=_colormap, opacity=_opacity, figure=figureHandle)

				self.volSlice1_sc1.actor.orientation = [0, 0, 0]
				# self.volSlice1_sc1.actor.position = [self.dx_data1*6, 0, pos]
				self.volSlice1_sc1.actor.position = [0, 0, pos]
				self.volSlice1_sc1.actor.scale = [_dx_data / scalex, _dy_data / scaley, _dz_data]

			# Keep the previous view
			self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)

		elif self.sliceType == "Contour slice (filled)":
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
				camRoll = mlab.roll(figure=figureHandle)

			if self.whichScalarSlice == "Computed scalar (default)":
				setScalarSlice = _data
			elif self.whichScalarSlice == "Vorticity x":
				setScalarSlice = _omega1
			elif self.whichScalarSlice == "Vorticity y":
				setScalarSlice = _omega2
			elif self.whichScalarSlice == "Vorticity z":
				setScalarSlice = _omega3
			elif self.whichScalarSlice == "Vorticity magnitude":
				setScalarSlice = np.sqrt(
					_omega1 ** 2 + _omega2 ** 2 + _omega3 ** 2
				)
			elif self.whichScalarSlice == "Velocity x":
				setScalarSlice = _u
			elif self.whichScalarSlice == "Velocity y":
				setScalarSlice = _v
			elif self.whichScalarSlice == "Velocity z":
				setScalarSlice = _w
			elif self.whichScalarSlice == "Velocity magnitude":
				setScalarSlice = np.sqrt(
					_u ** 2 + _v ** 2 + _w ** 2
				)

			# Setup scalar data
			self.sf1_sc1 = mlab.pipeline.scalar_field(_x, _y, _z, setScalarSlice, figure=figureHandle)

			# Use image_plane_widget to show filled contour data
			if self.planeOrientation == "X":
					self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
						self.sf1_sc1,
						plane_orientation="x_axes",
						slice_index=self.whichSliceX,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)

			elif self.planeOrientation == "Y":
					self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
						self.sf1_sc1,
						plane_orientation="y_axes",
						slice_index=self.whichSliceY,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)

			elif self.planeOrientation == "Z":
					self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
						self.sf1_sc1,
						plane_orientation="z_axes",
						slice_index=self.whichSliceZ,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)

			# Keep the previous view
			self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)
		
		elif self.sliceType == "Contour slice (unfilled)":
			# Get camera view
			if not mlab.view() is None:
				camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
				camRoll = mlab.roll(figure=figureHandle)

			if self.whichScalarSlice == "Computed scalar (default)":
				setScalarSlice = _data
			elif self.whichScalarSlice == "Vorticity x":
				setScalarSlice = _omega1
			elif self.whichScalarSlice == "Vorticity y":
				setScalarSlice = _omega2
			elif self.whichScalarSlice == "Vorticity z":
				setScalarSlice = _omega3
			elif self.whichScalarSlice == "Vorticity magnitude":
				setScalarSlice = np.sqrt(
					_omega1 ** 2 + _omega2 ** 2 + _omega3 ** 2
				)
			elif self.whichScalarSlice == "Velocity x":
				setScalarSlice = _u
			elif self.whichScalarSlice == "Velocity y":
				setScalarSlice = _v
			elif self.whichScalarSlice == "Velocity z":
				setScalarSlice = _w
			elif self.whichScalarSlice == "Velocity magnitude":
				setScalarSlice = np.sqrt(
					_u ** 2 + _v ** 2 + _w ** 2
				)

			# Setup scalar data
			self.sf1_sc1 = mlab.pipeline.scalar_field(_x, _y, _z, setScalarSlice, figure=figureHandle)

			# Use scalar_cut_plane to show unfilled contour data
			if self.planeOrientation == "X":
					self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
						self.sf1_sc1,
						plane_orientation="x_axes",
						line_width = 2,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					# Additional options for the scalar_cut_plane
					self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
					self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
					self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
					self.volSlice1_sc1.implicit_plane.widget.origin = np.array([np.unique(_x)[self.whichSliceX], 0,  0]) # Changes the origin correctly

			elif self.planeOrientation == "Y":
					self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
						self.sf1_sc1,
						plane_orientation="y_axes",
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					# Additional options for the scalar_cut_plane
					self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
					self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
					self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
					self.volSlice1_sc1.implicit_plane.widget.origin = np.array([0, np.unique(_y)[self.whichSliceY],  0]) # Changes the origin correctly

			elif self.planeOrientation == "Z":
					self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
						self.sf1_sc1,
						plane_orientation="z_axes",
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					# Additional options for the scalar_cut_plane
					self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
					self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
					self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
					self.volSlice1_sc1.implicit_plane.widget.origin = np.array([0, 0, np.unique(_z)[self.whichSliceZ]]) # Changes the origin correctly

			# Keep the previous view
			self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)

		elif self.sliceType == "Vector slice":
			# Setup vector data

			if self.whichVector == "Velocity":
					self.sf1_sc1 = mlab.pipeline.vector_field(
						_x,
						_y,
						_z,
						_u,
						_v,
						_w,
						figure=figureHandle,
					)

			else:
					self.sf1_sc1 = mlab.pipeline.vector_field(
						_x,
						_y,
						_z,
						_omega1,
						_omega2,
						_omega3,
						figure=figureHandle,
					)

			# Use image_plane_widget to show filled contour data
			if self.planeOrientation == "X":
					self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
						self.sf1_sc1,
						plane_orientation="x_axes",
						scale_factor=self.scaleFactorSlice,
						mask_points = 2,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					self.volSlice1_sc1.implicit_plane.widget.origin = ((self.whichSliceX * _dx_data) + _xmin_data, 0, 0)
					self.volSlice1_sc1.implicit_plane.widget.enabled = False
					self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * _xlength_data)

			elif self.planeOrientation == "Y":
					self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
						self.sf1_sc1,
						plane_orientation="y_axes",
						scale_factor=self.scaleFactorSlice,
						mask_points = 2,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					self.volSlice1_sc1.implicit_plane.widget.origin = (0, (self.whichSliceY * _dy_data) + _ymin_data, 0)
					self.volSlice1_sc1.implicit_plane.widget.enabled = False
					self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * _ylength_data)
				

			elif self.planeOrientation == "Z":
					self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
						self.sf1_sc1,
						plane_orientation="z_axes",
						scale_factor=self.scaleFactorSlice,
						mask_points = 2,
						colormap=_colormap,
						opacity=_opacity,
						figure=figureHandle,
						vmin=_colormapMin,
						vmax=_colormapMax,
					)
					self.volSlice1_sc1.implicit_plane.widget.origin = (0, 0, (self.whichSliceZ * _dz_data) + _zmin_data)
					self.volSlice1_sc1.implicit_plane.widget.enabled = False
					self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * _zlength_data)
				
	@on_trait_change("enableSlice")
	def enableSliceChanged(self):
		# if not self.justRemovedSlice:
		try:
			self.volSlice1_sc1.parent.parent.remove() # This always removes the complete tree
			self.sf1_sc1.remove()
		except (ValueError, AttributeError):
			pass  # Set slice first

		if self.screen1_ts1 and self.radioButton1:
			self.setSlice_actual(1, self.scene1.mayavi_scene)
		elif self.screen1_ts2 and self.radioButton1: 
			self.setSlice_actual(2, self.scene1.mayavi_scene)
		elif self.screen1_ts3 and self.radioButton1:
			self.setSlice_actual(3, self.scene1.mayavi_scene)
		elif self.screen1_ts4 and self.radioButton1: 
			self.setSlice_actual(4, self.scene1.mayavi_scene)
		
		elif self.screen2_ts1 and self.radioButton2:
			self.setSlice_actual(1, self.scene2.mayavi_scene)
		elif self.screen2_ts2 and self.radioButton2: 
			self.setSlice_actual(2, self.scene2.mayavi_scene)
		elif self.screen2_ts3 and self.radioButton2:
			self.setSlice_actual(3, self.scene2.mayavi_scene)
		elif self.screen2_ts4 and self.radioButton2: 
			self.setSlice_actual(4, self.scene2.mayavi_scene)
		
		elif self.screen3_ts1 and self.radioButton3:
			self.setSlice_actual(1, self.scene3.mayavi_scene)
		elif self.screen3_ts2 and self.radioButton3: 
			self.setSlice_actual(2, self.scene3.mayavi_scene)
		elif self.screen3_ts3 and self.radioButton3:
			self.setSlice_actual(3, self.scene3.mayavi_scene)
		elif self.screen3_ts4 and self.radioButton3: 
			self.setSlice_actual(4, self.scene3.mayavi_scene)
		
		elif self.screen4_ts1 and self.radioButton4:
			self.setSlice_actual(1, self.scene4.mayavi_scene)
		elif self.screen4_ts2 and self.radioButton4: 
			self.setSlice_actual(2, self.scene4.mayavi_scene)
		elif self.screen4_ts3 and self.radioButton4:
			self.setSlice_actual(3, self.scene4.mayavi_scene)
		elif self.screen4_ts4 and self.radioButton4: 
			self.setSlice_actual(4, self.scene4.mayavi_scene)

		# self.justRemovedSlice = False

	@on_trait_change("removeSlice")
	def removeSliceChanged(self):
		try:
			self.volSlice1_sc1.parent.parent.remove()
			self.sf1_sc1.remove()
		except (ValueError, AttributeError):
			pass  # Set slice first

		# self.justRemovedSlice = True
