# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from tvtk.util.ctf import PiecewiseFunction
from tvtk.util.ctf import ColorTransferFunction

class allVolRenderingOptions:
	
	def volRender1_actual(self, scNumber, figureHandle):
		
		# Setup scalar data
		if scNumber == 1:
			self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=figureHandle)
		if scNumber == 2:
			self.sf1_sc2 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=figureHandle)
		if scNumber == 3:
			self.sf1_sc3 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=figureHandle)
		if scNumber == 4:
			self.sf1_sc4 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=figureHandle)
		
		# Apply volume rendering on scalar data
		if scNumber == 1:
			self.vol1_sc1 = mlab.pipeline.volume(self.sf1_sc1, vmin = self.colormapMin1, vmax = self.colormapMax1)
		if scNumber == 2:
			self.vol1_sc2 = mlab.pipeline.volume(self.sf1_sc2, vmin = self.colormapMin1, vmax = self.colormapMax1)
		if scNumber == 3:
			self.vol1_sc3 = mlab.pipeline.volume(self.sf1_sc3, vmin = self.colormapMin1, vmax = self.colormapMax1)
		if scNumber == 4:
			self.vol1_sc4 = mlab.pipeline.volume(self.sf1_sc4, vmin = self.colormapMin1, vmax = self.colormapMax1)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
		if scNumber == 1:
			lut_manager = self.vol1_sc1.module_manager.scalar_lut_manager
		if scNumber == 2:
			lut_manager = self.vol1_sc2.module_manager.scalar_lut_manager
		if scNumber == 3:
			lut_manager = self.vol1_sc3.module_manager.scalar_lut_manager
		if scNumber == 4:
			lut_manager = self.vol1_sc4.module_manager.scalar_lut_manager
		lut_manager.lut_mode = self.contourColormap1
		lut = lut_manager.lut.table.to_array()
		min_val = self.colormapMin1
		max_val = self.colormapMax1
		
		num_samples = 256
		
		for i in range(num_samples):
			s = i / (num_samples - 1)
			value = min_val + s * (max_val - min_val)
			r, g, b = lut[i][:3] / 255.0
			ctf.add_rgb_point(value, r, g, b)
		
		if scNumber == 1:
			self.vol1_sc1._volume_property.set_color(ctf)
		if scNumber == 2:
			self.vol1_sc2._volume_property.set_color(ctf)
		if scNumber == 3:
			self.vol1_sc3._volume_property.set_color(ctf)
		if scNumber == 4:
			self.vol1_sc4._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin1-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin1, self.contourOpacity1)
		otf.add_point(self.colormapMax1, self.contourOpacity1)
		otf.add_point(self.colormapMax1+eps, self.opacityFallOff_volRender)
		
		if scNumber == 1:
			self.vol1_sc1._volume_property.set_scalar_opacity(otf)
		if scNumber == 2:
			self.vol1_sc2._volume_property.set_scalar_opacity(otf)
		if scNumber == 3:
			self.vol1_sc3._volume_property.set_scalar_opacity(otf)
		if scNumber == 4:
			self.vol1_sc4._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
		if scNumber == 1:
			self.vol1_sc1._volume_property.shade = self.shade_volRender
			self.vol1_sc1._volume_property.ambient = self.ambient_volRender
			self.vol1_sc1._volume_property.diffuse = self.diffuse_volRender
			self.vol1_sc1._volume_property.specular = self.specular_volRender
		if scNumber == 2:
			self.vol1_sc2._volume_property.shade = self.shade_volRender
			self.vol1_sc2._volume_property.ambient = self.ambient_volRender
			self.vol1_sc2._volume_property.diffuse = self.diffuse_volRender
			self.vol1_sc2._volume_property.specular = self.specular_volRender
		if scNumber == 3:
			self.vol1_sc3._volume_property.shade = self.shade_volRender
			self.vol1_sc3._volume_property.ambient = self.ambient_volRender
			self.vol1_sc3._volume_property.diffuse = self.diffuse_volRender
			self.vol1_sc3._volume_property.specular = self.specular_volRender
		if scNumber == 4:
			self.vol1_sc4._volume_property.shade = self.shade_volRender
			self.vol1_sc4._volume_property.ambient = self.ambient_volRender
			self.vol1_sc4._volume_property.diffuse = self.diffuse_volRender
			self.vol1_sc4._volume_property.specular = self.specular_volRender
	
	@on_trait_change('enableVolRendering')
	def enableVolRenderingChanged(self):
		
		if self.screen1_ts1:
			
			try:
				self.vol1_sc1.remove()
			except AttributeError:
				pass # Set volume rendering first
			
			self.volRender1_actual(1, self.scene1.mayavi_scene)
		
		if self.screen2_ts1:
			
			try:
				self.vol1_sc2.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_actual(2, self.scene2.mayavi_scene)
		
		if self.screen3_ts1:
			
			try:
				self.vol1_sc3.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_actual(3, self.scene3.mayavi_scene)
		
		if self.screen4_ts1:
			
			try:
				self.vol1_sc4.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_actual(4, self.scene4.mayavi_scene)
