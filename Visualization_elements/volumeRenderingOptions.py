# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from tvtk.util.ctf import PiecewiseFunction
from tvtk.util.ctf import ColorTransferFunction

class allVolRenderingOptions:

	@on_trait_change('enableVolRendering')
	def enableVolRenderingChanged(self):
		
		if self.screen1_ts1:
			
			try:
				self.vol1_sc1.remove()
			except AttributeError:
				pass # Set volume rendering first
		
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
			otf.add_point(self.colormapMin1, self.contourOpacity1)
			otf.add_point(self.colormapMax1, self.contourOpacity1)
			self.vol1_sc1._volume_property.set_scalar_opacity(otf)
			
			# Additional customizations
			# vol._volume_property.shade = True
			# vol._volume_property.ambient = 0.1
			# vol._volume_property.diffuse = 0.9
			# vol._volume_property.specular = 0.2
			
