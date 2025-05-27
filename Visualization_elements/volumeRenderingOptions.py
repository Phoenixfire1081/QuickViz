# Supplement to Mayavi Visualization
# All threshold options are defined here

from traits.api import on_trait_change
import numpy as np
from mayavi import mlab
from tvtk.util.ctf import PiecewiseFunction
from tvtk.util.ctf import ColorTransferFunction

class allVolRenderingOptions:
	
	def volRender1_actual(self, scNumber, figureHandle):
		
		# if self.radioButton1 == 'Y':
		
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
	
	def volRender2_actual(self, scNumber, figureHandle):
		
		# if self.radioButton2 == 'Y':
		
			# Setup scalar data
			if scNumber == 1:
				self.sf2_sc1 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, self._dataTs2[:, :, :, self.whichTime2], figure=figureHandle)
			if scNumber == 2:
				self.sf2_sc2 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, self._dataTs2[:, :, :, self.whichTime2], figure=figureHandle)
			if scNumber == 3:
				self.sf2_sc3 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, self._dataTs2[:, :, :, self.whichTime2], figure=figureHandle)
			if scNumber == 4:
				self.sf2_sc4 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, self._dataTs2[:, :, :, self.whichTime2], figure=figureHandle)
			
			# Apply volume rendering on scalar data
			if scNumber == 1:
				self.vol2_sc1 = mlab.pipeline.volume(self.sf2_sc1, vmin = self.colormapMin2, vmax = self.colormapMax2)
			if scNumber == 2:
				self.vol2_sc2 = mlab.pipeline.volume(self.sf2_sc2, vmin = self.colormapMin2, vmax = self.colormapMax2)
			if scNumber == 3:
				self.vol2_sc3 = mlab.pipeline.volume(self.sf2_sc3, vmin = self.colormapMin2, vmax = self.colormapMax2)
			if scNumber == 4:
				self.vol2_sc4 = mlab.pipeline.volume(self.sf2_sc4, vmin = self.colormapMin2, vmax = self.colormapMax2)
			
			# Set colormap with ctf
			ctf = ColorTransferFunction()
			if scNumber == 1:
				lut_manager = self.vol2_sc1.module_manager.scalar_lut_manager
			if scNumber == 2:
				lut_manager = self.vol2_sc2.module_manager.scalar_lut_manager
			if scNumber == 3:
				lut_manager = self.vol2_sc3.module_manager.scalar_lut_manager
			if scNumber == 4:
				lut_manager = self.vol2_sc4.module_manager.scalar_lut_manager
			lut_manager.lut_mode = self.contourColormap2
			lut = lut_manager.lut.table.to_array()
			min_val = self.colormapMin2
			max_val = self.colormapMax2
			
			num_samples = 256
			
			for i in range(num_samples):
				s = i / (num_samples - 1)
				value = min_val + s * (max_val - min_val)
				r, g, b = lut[i][:3] / 255.0
				ctf.add_rgb_point(value, r, g, b)
			
			if scNumber == 1:
				self.vol2_sc1._volume_property.set_color(ctf)
			if scNumber == 2:
				self.vol2_sc2._volume_property.set_color(ctf)
			if scNumber == 3:
				self.vol2_sc3._volume_property.set_color(ctf)
			if scNumber == 4:
				self.vol2_sc4._volume_property.set_color(ctf)
			
			# Set opacity to vmin and vmax
			otf = PiecewiseFunction()
			eps = 1e-5
			otf.add_point(self.colormapMin2-eps, self.opacityFallOff_volRender)
			otf.add_point(self.colormapMin2, self.contourOpacity2)
			otf.add_point(self.colormapMax2, self.contourOpacity2)
			otf.add_point(self.colormapMax2+eps, self.opacityFallOff_volRender)
			
			if scNumber == 1:
				self.vol2_sc1._volume_property.set_scalar_opacity(otf)
			if scNumber == 2:
				self.vol2_sc2._volume_property.set_scalar_opacity(otf)
			if scNumber == 3:
				self.vol2_sc3._volume_property.set_scalar_opacity(otf)
			if scNumber == 4:
				self.vol2_sc4._volume_property.set_scalar_opacity(otf)
			
			# Additional customizations
			if scNumber == 1:
				self.vol2_sc1._volume_property.shade = self.shade_volRender
				self.vol2_sc1._volume_property.ambient = self.ambient_volRender
				self.vol2_sc1._volume_property.diffuse = self.diffuse_volRender
				self.vol2_sc1._volume_property.specular = self.specular_volRender
			if scNumber == 2:
				self.vol2_sc2._volume_property.shade = self.shade_volRender
				self.vol2_sc2._volume_property.ambient = self.ambient_volRender
				self.vol2_sc2._volume_property.diffuse = self.diffuse_volRender
				self.vol2_sc2._volume_property.specular = self.specular_volRender
			if scNumber == 3:
				self.vol2_sc3._volume_property.shade = self.shade_volRender
				self.vol2_sc3._volume_property.ambient = self.ambient_volRender
				self.vol2_sc3._volume_property.diffuse = self.diffuse_volRender
				self.vol2_sc3._volume_property.specular = self.specular_volRender
			if scNumber == 4:
				self.vol2_sc4._volume_property.shade = self.shade_volRender
				self.vol2_sc4._volume_property.ambient = self.ambient_volRender
				self.vol2_sc4._volume_property.diffuse = self.diffuse_volRender
				self.vol2_sc4._volume_property.specular = self.specular_volRender
	
	def volRender3_actual(self, scNumber, figureHandle):
		
			# Setup scalar data
			if scNumber == 1:
				self.sf3_sc1 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, self._dataTs3[:, :, :, self.whichTime3], figure=figureHandle)
			if scNumber == 2:
				self.sf3_sc2 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, self._dataTs3[:, :, :, self.whichTime3], figure=figureHandle)
			if scNumber == 3:
				self.sf3_sc3 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, self._dataTs3[:, :, :, self.whichTime3], figure=figureHandle)
			if scNumber == 4:
				self.sf3_sc4 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, self._dataTs3[:, :, :, self.whichTime3], figure=figureHandle)
			
			# Apply volume rendering on scalar data
			if scNumber == 1:
				self.vol3_sc1 = mlab.pipeline.volume(self.sf3_sc1, vmin = self.colormapMin3, vmax = self.colormapMax3)
			if scNumber == 2:
				self.vol3_sc2 = mlab.pipeline.volume(self.sf3_sc2, vmin = self.colormapMin3, vmax = self.colormapMax3)
			if scNumber == 3:
				self.vol3_sc3 = mlab.pipeline.volume(self.sf3_sc3, vmin = self.colormapMin3, vmax = self.colormapMax3)
			if scNumber == 4:
				self.vol3_sc4 = mlab.pipeline.volume(self.sf3_sc4, vmin = self.colormapMin3, vmax = self.colormapMax3)
			
			# Set colormap with ctf
			ctf = ColorTransferFunction()
			if scNumber == 1:
				lut_manager = self.vol3_sc1.module_manager.scalar_lut_manager
			if scNumber == 2:
				lut_manager = self.vol3_sc2.module_manager.scalar_lut_manager
			if scNumber == 3:
				lut_manager = self.vol3_sc3.module_manager.scalar_lut_manager
			if scNumber == 4:
				lut_manager = self.vol3_sc4.module_manager.scalar_lut_manager
			lut_manager.lut_mode = self.contourColormap3
			lut = lut_manager.lut.table.to_array()
			min_val = self.colormapMin3
			max_val = self.colormapMax3
			
			num_samples = 256
			
			for i in range(num_samples):
				s = i / (num_samples - 1)
				value = min_val + s * (max_val - min_val)
				r, g, b = lut[i][:3] / 255.0
				ctf.add_rgb_point(value, r, g, b)
			
			if scNumber == 1:
				self.vol3_sc1._volume_property.set_color(ctf)
			if scNumber == 2:
				self.vol3_sc2._volume_property.set_color(ctf)
			if scNumber == 3:
				self.vol3_sc3._volume_property.set_color(ctf)
			if scNumber == 4:
				self.vol3_sc4._volume_property.set_color(ctf)
			
			# Set opacity to vmin and vmax
			otf = PiecewiseFunction()
			eps = 1e-5
			otf.add_point(self.colormapMin3-eps, self.opacityFallOff_volRender)
			otf.add_point(self.colormapMin3, self.contourOpacity3)
			otf.add_point(self.colormapMax3, self.contourOpacity3)
			otf.add_point(self.colormapMax3+eps, self.opacityFallOff_volRender)
			
			if scNumber == 1:
				self.vol3_sc1._volume_property.set_scalar_opacity(otf)
			if scNumber == 2:
				self.vol3_sc2._volume_property.set_scalar_opacity(otf)
			if scNumber == 3:
				self.vol3_sc3._volume_property.set_scalar_opacity(otf)
			if scNumber == 4:
				self.vol3_sc4._volume_property.set_scalar_opacity(otf)
			
			# Additional customizations
			if scNumber == 1:
				self.vol3_sc1._volume_property.shade = self.shade_volRender
				self.vol3_sc1._volume_property.ambient = self.ambient_volRender
				self.vol3_sc1._volume_property.diffuse = self.diffuse_volRender
				self.vol3_sc1._volume_property.specular = self.specular_volRender
			if scNumber == 2:
				self.vol3_sc2._volume_property.shade = self.shade_volRender
				self.vol3_sc2._volume_property.ambient = self.ambient_volRender
				self.vol3_sc2._volume_property.diffuse = self.diffuse_volRender
				self.vol3_sc2._volume_property.specular = self.specular_volRender
			if scNumber == 3:
				self.vol3_sc3._volume_property.shade = self.shade_volRender
				self.vol3_sc3._volume_property.ambient = self.ambient_volRender
				self.vol3_sc3._volume_property.diffuse = self.diffuse_volRender
				self.vol3_sc3._volume_property.specular = self.specular_volRender
			if scNumber == 4:
				self.vol3_sc4._volume_property.shade = self.shade_volRender
				self.vol3_sc4._volume_property.ambient = self.ambient_volRender
				self.vol3_sc4._volume_property.diffuse = self.diffuse_volRender
				self.vol3_sc4._volume_property.specular = self.specular_volRender
		
	def volRender4_actual(self, scNumber, figureHandle):
	
		# Setup scalar data
		if scNumber == 1:
			self.sf4_sc1 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, self._dataTs4[:, :, :, self.whichTime4], figure=figureHandle)
		if scNumber == 2:
			self.sf4_sc2 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, self._dataTs4[:, :, :, self.whichTime4], figure=figureHandle)
		if scNumber == 3:
			self.sf4_sc3 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, self._dataTs4[:, :, :, self.whichTime4], figure=figureHandle)
		if scNumber == 4:
			self.sf4_sc4 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, self._dataTs4[:, :, :, self.whichTime4], figure=figureHandle)
		
		# Apply volume rendering on scalar data
		if scNumber == 1:
			self.vol4_sc1 = mlab.pipeline.volume(self.sf4_sc1, vmin = self.colormapMin4, vmax = self.colormapMax4)
		if scNumber == 2:
			self.vol4_sc2 = mlab.pipeline.volume(self.sf4_sc2, vmin = self.colormapMin4, vmax = self.colormapMax4)
		if scNumber == 3:
			self.vol4_sc3 = mlab.pipeline.volume(self.sf4_sc3, vmin = self.colormapMin4, vmax = self.colormapMax4)
		if scNumber == 4:
			self.vol4_sc4 = mlab.pipeline.volume(self.sf4_sc4, vmin = self.colormapMin4, vmax = self.colormapMax4)
		
		# Set colormap with ctf
		ctf = ColorTransferFunction()
		if scNumber == 1:
			lut_manager = self.vol4_sc1.module_manager.scalar_lut_manager
		if scNumber == 2:
			lut_manager = self.vol4_sc2.module_manager.scalar_lut_manager
		if scNumber == 3:
			lut_manager = self.vol4_sc3.module_manager.scalar_lut_manager
		if scNumber == 4:
			lut_manager = self.vol4_sc4.module_manager.scalar_lut_manager
		lut_manager.lut_mode = self.contourColormap4
		lut = lut_manager.lut.table.to_array()
		min_val = self.colormapMin4
		max_val = self.colormapMax4
		
		num_samples = 256
		
		for i in range(num_samples):
			s = i / (num_samples - 1)
			value = min_val + s * (max_val - min_val)
			r, g, b = lut[i][:3] / 255.0
			ctf.add_rgb_point(value, r, g, b)
		
		if scNumber == 1:
			self.vol4_sc1._volume_property.set_color(ctf)
		if scNumber == 2:
			self.vol4_sc2._volume_property.set_color(ctf)
		if scNumber == 3:
			self.vol4_sc3._volume_property.set_color(ctf)
		if scNumber == 4:
			self.vol4_sc4._volume_property.set_color(ctf)
		
		# Set opacity to vmin and vmax
		otf = PiecewiseFunction()
		eps = 1e-5
		otf.add_point(self.colormapMin4-eps, self.opacityFallOff_volRender)
		otf.add_point(self.colormapMin4, self.contourOpacity4)
		otf.add_point(self.colormapMax4, self.contourOpacity4)
		otf.add_point(self.colormapMax4+eps, self.opacityFallOff_volRender)
		
		if scNumber == 1:
			self.vol4_sc1._volume_property.set_scalar_opacity(otf)
		if scNumber == 2:
			self.vol4_sc2._volume_property.set_scalar_opacity(otf)
		if scNumber == 3:
			self.vol4_sc3._volume_property.set_scalar_opacity(otf)
		if scNumber == 4:
			self.vol4_sc4._volume_property.set_scalar_opacity(otf)
		
		# Additional customizations
		if scNumber == 1:
			self.vol4_sc1._volume_property.shade = self.shade_volRender
			self.vol4_sc1._volume_property.ambient = self.ambient_volRender
			self.vol4_sc1._volume_property.diffuse = self.diffuse_volRender
			self.vol4_sc1._volume_property.specular = self.specular_volRender
		if scNumber == 2:
			self.vol4_sc2._volume_property.shade = self.shade_volRender
			self.vol4_sc2._volume_property.ambient = self.ambient_volRender
			self.vol4_sc2._volume_property.diffuse = self.diffuse_volRender
			self.vol4_sc2._volume_property.specular = self.specular_volRender
		if scNumber == 3:
			self.vol4_sc3._volume_property.shade = self.shade_volRender
			self.vol4_sc3._volume_property.ambient = self.ambient_volRender
			self.vol4_sc3._volume_property.diffuse = self.diffuse_volRender
			self.vol4_sc3._volume_property.specular = self.specular_volRender
		if scNumber == 4:
			self.vol4_sc4._volume_property.shade = self.shade_volRender
			self.vol4_sc4._volume_property.ambient = self.ambient_volRender
			self.vol4_sc4._volume_property.diffuse = self.diffuse_volRender
			self.vol4_sc4._volume_property.specular = self.specular_volRender
	
	@on_trait_change('enableVolRendering')
	def enableVolRenderingChanged(self):
		
		if self.radioButton1 == 'Y' or self.clamp == 1:
			
			if self.screen1_ts1:
				
				if not self.justRemovedVolRender:
					try:
						self.vol1_sc1.remove()
					except AttributeError:
						pass # Set volume rendering first
				
				self.volRender1_actual(1, self.scene1.mayavi_scene)
			
			if self.screen2_ts1:
				
				if not self.justRemovedVolRender:
					try:
						self.vol1_sc2.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender1_actual(2, self.scene2.mayavi_scene)
			
			if self.screen3_ts1:
				
				if not self.justRemovedVolRender:
					try:
						self.vol1_sc3.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender1_actual(3, self.scene3.mayavi_scene)
			
			if self.screen4_ts1:
				
				if not self.justRemovedVolRender:
					try:
						self.vol1_sc4.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender1_actual(4, self.scene4.mayavi_scene)
			
		if self.radioButton2 == 'Y' or self.clamp == 1:
			
			if self.screen1_ts2:
				
				if not self.justRemovedVolRender:
					try:
						self.vol2_sc1.remove()
					except AttributeError:
						pass # Set volume rendering first
				
				self.volRender2_actual(1, self.scene1.mayavi_scene)
			
			if self.screen2_ts2:
				
				if not self.justRemovedVolRender:
					try:
						self.vol2_sc2.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender2_actual(2, self.scene2.mayavi_scene)
			
			if self.screen3_ts2:
				
				if not self.justRemovedVolRender:
					try:
						self.vol2_sc3.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender2_actual(3, self.scene3.mayavi_scene)
			
			if self.screen4_ts2:
				
				if not self.justRemovedVolRender:
					try:
						self.vol2_sc4.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender2_actual(4, self.scene4.mayavi_scene)
		
		if self.radioButton3 == 'Y' or self.clamp == 1:
			
			if self.screen1_ts3:
				
				if not self.justRemovedVolRender:
					try:
						self.vol3_sc1.remove()
					except AttributeError:
						pass # Set volume rendering first
				
				self.volRender3_actual(1, self.scene1.mayavi_scene)
			
			if self.screen2_ts3:
				
				if not self.justRemovedVolRender:
					try:
						self.vol3_sc2.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender3_actual(2, self.scene2.mayavi_scene)
			
			if self.screen3_ts3:
				
				if not self.justRemovedVolRender:
					try:
						self.vol3_sc3.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender3_actual(3, self.scene3.mayavi_scene)
			
			if self.screen4_ts3:
				
				if not self.justRemovedVolRender:
					try:
						self.vol3_sc4.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender3_actual(4, self.scene4.mayavi_scene)
		
		if self.radioButton4 == 'Y' or self.clamp == 1:
			
			if self.screen1_ts4:
				
				if not self.justRemovedVolRender:
					try:
						self.vol4_sc1.remove()
					except AttributeError:
						pass # Set volume rendering first
				
				self.volRender4_actual(1, self.scene1.mayavi_scene)
			
			if self.screen2_ts4:
				
				if not self.justRemovedVolRender:
					try:
						self.vol4_sc2.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender4_actual(2, self.scene2.mayavi_scene)
			
			if self.screen3_ts4:
				
				if not self.justRemovedVolRender:
					try:
						self.vol4_sc3.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender4_actual(3, self.scene3.mayavi_scene)
			
			if self.screen4_ts4:
				
				if not self.justRemovedVolRender:
					try:
						self.vol4_sc4.remove()
					except AttributeError:
						pass # Set volume rendering first
			
				self.volRender4_actual(4, self.scene4.mayavi_scene)		
		
		self.justRemovedVolRender = False

	@on_trait_change('removeVolRender')
	def removeVolRenderChanged(self):
		
		if self.radioButton1 == 'Y':
			
			if self.screen1_ts1:
			
				try:
					self.vol1_sc1.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen2_ts1:
			
				try:
					self.vol1_sc2.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen3_ts1:
			
				try:
					self.vol1_sc3.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen4_ts1:
			
				try:
					self.vol1_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		if self.radioButton2 == 'Y':
			
			if self.screen1_ts2:
			
				try:
					self.vol2_sc1.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen2_ts2:
			
				try:
					self.vol2_sc2.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen3_ts2:
			
				try:
					self.vol2_sc3.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen4_ts2:
			
				try:
					self.vol2_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		if self.radioButton3 == 'Y':
			
			if self.screen1_ts3:
			
				try:
					self.vol3_sc1.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen2_ts3:
			
				try:
					self.vol3_sc2.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen3_ts3:
			
				try:
					self.vol3_sc3.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen4_ts3:
			
				try:
					self.vol3_sc4.remove()
				except AttributeError:
					pass # Set slice first
		
		if self.radioButton4 == 'Y':
			
			if self.screen1_ts4:
			
				try:
					self.vol4_sc1.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen2_ts4:
			
				try:
					self.vol4_sc2.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen3_ts4:
			
				try:
					self.vol4_sc3.remove()
				except AttributeError:
					pass # Set slice first
			
			if self.screen4_ts4:
			
				try:
					self.vol4_sc4.remove()
				except AttributeError:
					pass # Set slice first
			
		self.justRemovedVolRender = True
