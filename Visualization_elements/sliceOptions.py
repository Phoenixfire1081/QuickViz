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
        if self.sliceType == "Fieldlines":
            # Set constant seed
            np.random.seed(12345)

            # Get camera view
            if not mlab.view() is None:
                camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
                camRoll = mlab.roll(figure=figureHandle)

            if self.planeOrientation == "X":
                scalex = self.noiseImageDimensionSliceX / self.ylength_data1
                scaley = self.noiseImageDimensionSliceY / self.zlength_data1

                tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

                if self.whichVector == "Velocity":
                    tmpVectorSlice[:, :, 0] += zoom(self.w1[self.whichSliceX, :, :, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.v1[self.whichSliceX, :, :, self.whichTime1], (scalex, scaley), order=1)

                else:
                    tmpVectorSlice[:, :, 0] += zoom(self.omega3[self.whichSliceX, :, :, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.omega2[self.whichSliceX, :, :, self.whichTime1], (scalex, scaley), order=1)

                texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

                kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
                kernel = kernel.astype(np.float32)

                image = line_integral_convolution(tmpVectorSlice, texture, kernel)
                pos = (self.whichSliceX * self.dx_data1) + self.xmin_data1

                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.imshow(image.T, colormap=self.contourColormap1, opacity=self.contourOpacity1, figure=figureHandle)

                    self.volSlice1_sc1.actor.orientation = [0, 90, 0]
                    self.volSlice1_sc1.actor.position = [pos, 0, 0]
                    self.volSlice1_sc1.actor.scale = [self.dz_data1 / scalex, self.dy_data1 / scaley, self.dx_data1]

            if self.planeOrientation == "Y":
                scalex = self.noiseImageDimensionSliceX / self.xlength_data1
                scaley = self.noiseImageDimensionSliceY / self.zlength_data1

                tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

                if self.whichVector == "Velocity":
                    tmpVectorSlice[:, :, 0] += zoom(self.w1[:, self.whichSliceY, :, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.u1[:, self.whichSliceY, :, self.whichTime1], (scalex, scaley), order=1)

                else:
                    tmpVectorSlice[:, :, 0] += zoom(self.omega3[:, self.whichSliceY, :, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.omega1[:, self.whichSliceY, :, self.whichTime1], (scalex, scaley), order=1)

                texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

                kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
                kernel = kernel.astype(np.float32)

                image = line_integral_convolution(tmpVectorSlice, texture, kernel)
                pos = (self.whichSliceY * self.dy_data1) + self.ymin_data1

                # self.dx_data1*6 corrects for a strange offset in imshow.

                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.imshow(image, colormap=self.contourColormap1, opacity=self.contourOpacity1, figure=figureHandle)

                    self.volSlice1_sc1.actor.orientation = [90, 0, 0]
                    # self.volSlice1_sc1.actor.position = [self.dx_data1*6, pos, 0]
                    self.volSlice1_sc1.actor.position = [0, pos, 0]
                    self.volSlice1_sc1.actor.scale = [self.dx_data1 / scalex, self.dz_data1 / scaley, self.dy_data1]

            if self.planeOrientation == "Z":
                scalex = self.noiseImageDimensionSliceX / self.xlength_data1
                scaley = self.noiseImageDimensionSliceY / self.ylength_data1

                tmpVectorSlice = np.zeros((self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY, 2), dtype=np.float32)

                if self.whichVector == "Velocity":
                    tmpVectorSlice[:, :, 0] += zoom(self.v1[:, :, self.whichSliceZ, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.u1[:, :, self.whichSliceZ, self.whichTime1], (scalex, scaley), order=1)

                else:
                    tmpVectorSlice[:, :, 0] += zoom(self.omega2[:, :, self.whichSliceZ, self.whichTime1], (scalex, scaley), order=1)
                    tmpVectorSlice[:, :, 1] += zoom(self.omega1[:, :, self.whichSliceZ, self.whichTime1], (scalex, scaley), order=1)

                texture = np.random.rand(self.noiseImageDimensionSliceX, self.noiseImageDimensionSliceY).astype(np.float32)

                kernel = np.sin(np.arange(self.kernelLengthSlice) * np.pi / self.kernelLengthSlice)
                kernel = kernel.astype(np.float32)

                image = line_integral_convolution(tmpVectorSlice, texture, kernel)
                pos = (self.whichSliceZ * self.dz_data1) + self.zmin_data1

                # self.dx_data1*6 corrects for a strange offset in imshow.

                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.imshow(image, colormap=self.contourColormap1, opacity=self.contourOpacity1, figure=figureHandle)

                    self.volSlice1_sc1.actor.orientation = [0, 0, 0]
                    # self.volSlice1_sc1.actor.position = [self.dx_data1*6, 0, pos]
                    self.volSlice1_sc1.actor.position = [0, 0, pos]
                    self.volSlice1_sc1.actor.scale = [self.dx_data1 / scalex, self.dy_data1 / scaley, self.dz_data1]

            # Keep the previous view
            self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)

        elif self.sliceType == "Contour slice (filled)":
            # Get camera view
            if not mlab.view() is None:
                camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
                camRoll = mlab.roll(figure=figureHandle)

            if self.whichScalarSlice == "Computed scalar (default)":
                setScalarSlice = self._dataTs1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity x":
                setScalarSlice = self.omega1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity y":
                setScalarSlice = self.omega2[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity z":
                setScalarSlice = self.omega3[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity magnitude":
                setScalarSlice = np.sqrt(
                    self.omega1[:, :, :, self.whichTime1] ** 2 + self.omega2[:, :, :, self.whichTime1] ** 2 + self.omega3[:, :, :, self.whichTime1] ** 2
                )
            elif self.whichScalarSlice == "Velocity x":
                setScalarSlice = self.u1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity y":
                setScalarSlice = self.v1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity z":
                setScalarSlice = self.w1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity magnitude":
                setScalarSlice = np.sqrt(
                    self.u1[:, :, :, self.whichTime1] ** 2 + self.v1[:, :, :, self.whichTime1] ** 2 + self.w1[:, :, :, self.whichTime1] ** 2
                )

            # Setup scalar data
            if scNumber == 1:
                self.vf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, setScalarSlice, figure=figureHandle)

            # Use image_plane_widget to show filled contour data
            if self.planeOrientation == "X":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
                        self.vf1_sc1,
                        plane_orientation="x_axes",
                        slice_index=self.whichSliceX,
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )

            elif self.planeOrientation == "Y":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
                        self.vf1_sc1,
                        plane_orientation="y_axes",
                        slice_index=self.whichSliceY,
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )

            elif self.planeOrientation == "Z":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.image_plane_widget(
                        self.vf1_sc1,
                        plane_orientation="z_axes",
                        slice_index=self.whichSliceZ,
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )

            # Keep the previous view
            self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)
        
        elif self.sliceType == "Contour slice (unfilled)":
            # Get camera view
            if not mlab.view() is None:
                camAzimuth, camElevation, camDistance, focalPoint = mlab.view(figure=figureHandle)
                camRoll = mlab.roll(figure=figureHandle)

            if self.whichScalarSlice == "Computed scalar (default)":
                setScalarSlice = self._dataTs1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity x":
                setScalarSlice = self.omega1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity y":
                setScalarSlice = self.omega2[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity z":
                setScalarSlice = self.omega3[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Vorticity magnitude":
                setScalarSlice = np.sqrt(
                    self.omega1[:, :, :, self.whichTime1] ** 2 + self.omega2[:, :, :, self.whichTime1] ** 2 + self.omega3[:, :, :, self.whichTime1] ** 2
                )
            elif self.whichScalarSlice == "Velocity x":
                setScalarSlice = self.u1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity y":
                setScalarSlice = self.v1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity z":
                setScalarSlice = self.w1[:, :, :, self.whichTime1]
            elif self.whichScalarSlice == "Velocity magnitude":
                setScalarSlice = np.sqrt(
                    self.u1[:, :, :, self.whichTime1] ** 2 + self.v1[:, :, :, self.whichTime1] ** 2 + self.w1[:, :, :, self.whichTime1] ** 2
                )

            # Setup scalar data
            if scNumber == 1:
                self.vf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, setScalarSlice, figure=figureHandle)

            # Use scalar_cut_plane to show unfilled contour data
            if self.planeOrientation == "X":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="x_axes",
                        line_width = 2,
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    # Additional options for the scalar_cut_plane
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
                    self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
                    self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
                    self.volSlice1_sc1.implicit_plane.widget.origin = np.array([np.unique(self.x1)[self.whichSliceX], 0,  0]) # Changes the origin correctly

            elif self.planeOrientation == "Y":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="y_axes",
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    # Additional options for the scalar_cut_plane
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
                    self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
                    self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
                    self.volSlice1_sc1.implicit_plane.widget.origin = np.array([0, np.unique(self.y1)[self.whichSliceY],  0]) # Changes the origin correctly

            elif self.planeOrientation == "Z":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.scalar_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="z_axes",
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    # Additional options for the scalar_cut_plane
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False # Removes the object to move around the widget
                    self.volSlice1_sc1.enable_contours = True # Enables unfilled contours
                    self.volSlice1_sc1.contour.number_of_contours = self.numberOfContours # Sets the number of contours
                    self.volSlice1_sc1.implicit_plane.widget.origin = np.array([0, 0, np.unique(self.z1)[self.whichSliceZ]]) # Changes the origin correctly

            # Keep the previous view
            self.update_camera_at_current_timestep_with_camPath(camAzimuth, camElevation, camDistance, focalPoint, camRoll, figureHandle)

        elif self.sliceType == "Vector slice":
            # Setup vector data

            if self.whichVector == "Velocity":
                if scNumber == 1:
                    self.vf1_sc1 = mlab.pipeline.vector_field(
                        self.x1,
                        self.y1,
                        self.z1,
                        self.u1[:, :, :, self.whichTime1],
                        self.v1[:, :, :, self.whichTime1],
                        self.w1[:, :, :, self.whichTime1],
                        figure=figureHandle,
                    )

            else:
                if scNumber == 1:
                    self.vf1_sc1 = mlab.pipeline.vector_field(
                        self.x1,
                        self.y1,
                        self.z1,
                        self.omega1[:, :, :, self.whichTime1],
                        self.omega2[:, :, :, self.whichTime1],
                        self.omega3[:, :, :, self.whichTime1],
                        figure=figureHandle,
                    )

            # Use image_plane_widget to show filled contour data
            if self.planeOrientation == "X":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="x_axes",
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        scale_factor=self.scaleFactorSlice,
                        mask_points = 2,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    self.volSlice1_sc1.implicit_plane.widget.origin = ((self.whichSliceX * self.dx_data1) + self.xmin_data1, 0, 0)
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False
                    self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * self.xlength_data1)

            elif self.planeOrientation == "Y":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="y_axes",
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        scale_factor=self.scaleFactorSlice,
                        mask_points = 2,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    self.volSlice1_sc1.implicit_plane.widget.origin = (0, (self.whichSliceY * self.dy_data1) + self.ymin_data1, 0)
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False
                    self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * self.ylength_data1)
                

            elif self.planeOrientation == "Z":
                if scNumber == 1:
                    self.volSlice1_sc1 = mlab.pipeline.vector_cut_plane(
                        self.vf1_sc1,
                        plane_orientation="z_axes",
                        colormap=self.contourColormap1,
                        opacity=self.contourOpacity1,
                        scale_factor=self.scaleFactorSlice,
                        mask_points = 2,
                        figure=figureHandle,
                        vmin=self.colormapMin1,
                        vmax=self.colormapMax1,
                    )
                    self.volSlice1_sc1.implicit_plane.widget.origin = (0, 0, (self.whichSliceZ * self.dz_data1) + self.zmin_data1)
                    self.volSlice1_sc1.implicit_plane.widget.enabled = False
                    self.volSlice1_sc1.glyph.mask_points.maximum_number_of_points = int(self.resolutionSlice * self.zlength_data1)
                

    @on_trait_change("enableSlice")
    def enableSliceChanged(self):
        if self.screen1_ts1:
            if not self.justRemovedSlice:
                try:
                    self.volSlice1_sc1.parent.parent.remove() # This always removes the complete tree
                    self.vf1_sc1.remove()
                except (ValueError, AttributeError):
                    pass  # Set slice first

            self.setSlice_actual(1, self.scene1.mayavi_scene)

        self.justRemovedSlice = False

    @on_trait_change("removeSlice")
    def removeSliceChanged(self):
        if self.screen1_ts1:
            try:
                self.volSlice1_sc1.parent.parent.remove()
                self.vf1_sc1()
            except (ValueError, AttributeError):
                pass  # Set slice first

        self.justRemovedSlice = True
