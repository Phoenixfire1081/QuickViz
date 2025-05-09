# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from tvtk.util.ctf import PiecewiseFunction
from tvtk.util.ctf import ColorTransferFunction

class allVolRenderingOptions:
	
	def volRender1_sc1(self):
		
		# Setup scalar data
		self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=self.scene1.mayavi_scene)
		
		# Apply volume rendering on scalar data
		self.vol1_sc1 = mlab.pipeline.volume(self.sf1_sc1, vmin = self.colormapMin1, vmax = self.colormapMax1)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
		lut_manager = self.vol1_sc1.module_manager.scalar_lut_manager
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
		
		self.vol1_sc1._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin1-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin1, self.contourOpacity1)
		otf.add_point(self.colormapMax1, self.contourOpacity1)
		otf.add_point(self.colormapMax1+eps, self.opacityFallOff_volRender)
		self.vol1_sc1._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
		self.vol1_sc1._volume_property.shade = self.shade_volRender
		self.vol1_sc1._volume_property.ambient = self.ambient_volRender
		self.vol1_sc1._volume_property.diffuse = self.diffuse_volRender
		self.vol1_sc1._volume_property.specular = self.specular_volRender

	def volRender1_sc2(self):
		
		# Setup scalar data
		self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=self.scene2.mayavi_scene)
		
		# Apply volume rendering on scalar data
		self.vol1_sc2 = mlab.pipeline.volume(self.sf1_sc2, vmin = self.colormapMin1, vmax = self.colormapMax1)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
		lut_manager = self.vol1_sc2.module_manager.scalar_lut_manager
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
		
		self.vol1_sc2._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin1-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin1, self.contourOpacity1)
		otf.add_point(self.colormapMax1, self.contourOpacity1)
		otf.add_point(self.colormapMax1+eps, self.opacityFallOff_volRender)
		self.vol1_sc2._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
		self.vol1_sc2._volume_property.shade = self.shade_volRender
		self.vol1_sc2._volume_property.ambient = self.ambient_volRender
		self.vol1_sc2._volume_property.diffuse = self.diffuse_volRender
		self.vol1_sc2._volume_property.specular = self.specular_volRender
	
	def volRender1_sc3(self):
		
		# Setup scalar data
		self.sf1_sc3 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=self.scene3.mayavi_scene)
		
		# Apply volume rendering on scalar data
		self.vol1_sc3 = mlab.pipeline.volume(self.sf1_sc3, vmin = self.colormapMin1, vmax = self.colormapMax1)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
		lut_manager = self.vol1_sc3.module_manager.scalar_lut_manager
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
		
		self.vol1_sc3._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin1-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin1, self.contourOpacity1)
		otf.add_point(self.colormapMax1, self.contourOpacity1)
		otf.add_point(self.colormapMax1+eps, self.opacityFallOff_volRender)
		self.vol1_sc3._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
		self.vol1_sc3._volume_property.shade = self.shade_volRender
		self.vol1_sc3._volume_property.ambient = self.ambient_volRender
		self.vol1_sc3._volume_property.diffuse = self.diffuse_volRender
		self.vol1_sc3._volume_property.specular = self.specular_volRender
	
	def volRender1_sc4(self):
		
		# Setup scalar data
		self.sf1_sc4 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, self._dataTs1[:, :, :, self.whichTime1], figure=self.scene4.mayavi_scene)
		
		# Apply volume rendering on scalar data
		self.vol1_sc4 = mlab.pipeline.volume(self.sf1_sc4, vmin = self.colormapMin1, vmax = self.colormapMax1)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
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
		
		self.vol1_sc4._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin1-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin1, self.contourOpacity1)
		otf.add_point(self.colormapMax1, self.contourOpacity1)
		otf.add_point(self.colormapMax1+eps, self.opacityFallOff_volRender)
		self.vol1_sc4._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
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
			
			self.volRender1_sc1()
		
		if self.screen2_ts1:
			
			try:
				self.vol1_sc2.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_sc2()
		
		if self.screen3_ts1:
			
			try:
				self.vol1_sc3.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_sc3()
		
		if self.screen4_ts1:
			
			try:
				self.vol1_sc4.remove()
			except AttributeError:
				pass # Set volume rendering first
		
			self.volRender1_sc4()
