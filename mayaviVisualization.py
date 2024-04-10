import numpy as np
from mayavi import mlab
import mayavi
from copy import deepcopy
from traits.api import HasTraits, Range, Instance, on_trait_change, Float, Enum, Bool, Str
from traits.api import Button
from traitsui.api import View, Item, HGroup, HSplit, VGroup, Heading, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from pyface.api import GUI
from PIL import Image
import os

class mayaviVisualizeWithThreshold(HasTraits):
	
	# Create checkbox
	chkBox = Bool()
	
	# Create outline width range
	outlineWidth = Range(0., 10., 2.0, ) 
	
	# Create colormap range
	colormapMin = Float(0.0)
	colormapMax = Float(1.0)
	
	# Create outline color floats
	outlineColorRed = Float(0.0)
	outlineColorGreen = Float(0.0)
	outlineColorBlue = Float(0.0)
	
	# Create background color floats
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Set opacity of contour
	contourOpacity = Float(1.0)
	
	# Set representation
	contourRepresentation = Enum(['points', 'surface', 'wireframe'])
	
	# Set colormap
	contourColormap = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
	'CMRmap', 'Dark2', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', \
	'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG', 'PuBu', 'PuBuGn', \
	'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', \
	'RdYlGn', 'Reds', 'Set1', 'Set2', 'Set3', 'Spectral', 'Vega10', \
	'Vega20', 'Vega20b', 'Vega20c', 'Wistia', 'YlGn', 'YlGnBu', \
	'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'black-white', \
	'blue-red', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', \
	'cubehelix', 'file', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', \
	'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', \
	'gnuplot2', 'gray', 'hot', 'hsv', 'inferno', 'jet', 'magma', \
	'nipy_spectral', 'ocean', 'pink', 'plasma', 'prism', 'rainbow', \
	'seismic', 'spectral', 'spring', 'summer', 'terrain', 'viridis', \
	'winter'])
	
	# Initiate scene
	scene = Instance(MlabSceneModel, ())

	def __init__(self, *args):
		
		HasTraits.__init__(self)
		
		# Get data first
		
		_data = args[-1]
		
		# Modify threshold range based on data
		# For some reason, Range doesn't like numpy float32
		# Using float instead
		
		self.add_trait("threshold", Range(float(round(_data.min())), float(np.ceil(_data.max()))))
		
		# Set initial threshold value
		
		if _data.min() > 0:
			self.threshold = float(np.ceil(_data.min()))
		elif _data.max() < 0:
			self.threshold = float(np.floor(_data.max()))
		else:
			self.threshold = float(0.0)
		
		if len(args) > 1:
			
			x = args[0]
			y = args[1]
			z = args[2]

			# Plot the isosurface with minimum value from data
			sf = mlab.pipeline.scalar_field(x, y, z, _data, figure=self.scene.mayavi_scene)
		
		else:
			
			# Plot the isosurface with minimum value from data
			sf = mlab.pipeline.scalar_field(_data, figure=self.scene.mayavi_scene)
		
		# Set the threshold
		self.iso = mlab.pipeline.iso_surface(sf, contours=[_data.min()])
		
		# Plot the outline
		self.out = mayavi.tools.pipeline.outline(self.iso)
		
		# Set min, max, data
		self.thresholdMin = _data.min()
		self.thresholdMax = _data.max()
		self.OrigData = deepcopy(_data)
		
		# Set contour representation
		self.contourRepresentation = 'surface'
		
		# Set contour colormap
		self.contourColormap = 'viridis'
		
		# Set outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
		
		# Set background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		
		# Set checkbox 
		self.chkBox = True
		
	@on_trait_change('threshold')
	def threshold_changed(self):
		
		try:
			
			# First pop the previous value
			self.iso.contour.contours.pop()
			
			# Set new threshold data
			self.iso.contour.contours = [np.round(self.threshold, 2)]
			
		except AttributeError:
			
			# This probably occurs when the first threshold is set
			pass
	
	@on_trait_change('outlineWidth, outlineColorRed, outlineColorGreen,\
	outlineColorBlue')
	def outline_changed(self):
			
		# Change outline width
		self.out.actor.property.line_width = self.outlineWidth
		
		# Change outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
	
	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
	
	@on_trait_change('contourOpacity, contourRepresentation, contourColormap, colormapMin, colormapMax')
	def contour_changed(self):
		
		# Change contour opacity
		self.iso.actor.property.opacity = self.contourOpacity
		
		# Change contour representation
		self.iso.actor.property.representation = self.contourRepresentation
		
		# Change contour colormap
		self.iso.module_manager.scalar_lut_manager.lut_mode = self.contourColormap
		
		# Change colormap range
		self.iso.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin, self.colormapMax])
	
	@on_trait_change('chkBox')
	def chkbox_changed(self):
		
		if self.chkBox == False:				
			
			# Set new threshold data
			self.iso.contour.contours = []
		
		else:
			
			# Set current threshold data
			self.iso.contour.contours = [np.round(self.threshold, 2)]

	view = View(
	
	HSplit(
	
	VGroup(Group(label = 'Active scalar fields'),
	
	Item("chkBox", label = 'Scalar field', width=0.05)),
	
	Item('scene', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, width=0.75), 
	
	# NOTE: width in the Hsplit controls the ratio of split
	
	VGroup(
	
	# Global options
	
	Group(label = 'Background options:'),
	
	HGroup(Item("BGColorRed", label = 'BG color (r, g, b) '),
	Item("BGColorGreen", label = ' '),
	Item("BGColorBlue", label = ' ')),
	
	Group(label = 'Outline options:'),
	
	Item("outlineWidth", label = 'Outline width:'),
	HGroup(Item("outlineColorRed", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen", label = ' '),
	Item("outlineColorBlue", label = ' ')),
	
	# Changeable for each contour
	
	Group(label = 'Isosurface options:'),
	
	Item("threshold", label = 'Set threshold:'), 
	
	Group(label = 'Contour options:'),
	
	HGroup(Item("contourOpacity", label = 'Opacity '),
	Item("contourRepresentation", label = 'Representation ')),
	
	HGroup(Item("contourColormap", label = 'Colormap '),
	Item("colormapMin", label = 'Colormap (min, max)'),
	Item("colormapMax", label = ' ')),
	
	)
	),resizable=True, width=1, height=1)
	
class mayaviVisualizeWithMultipleThreshold(HasTraits):
	
	# Create checkbox
	chkBox = Bool()
	
	# Create outline width range
	outlineWidth = Range(0., 10., 2.0, ) 
	
	# Create colormap range
	colormapMin = Float(0.0)
	colormapMax = Float(1.0)
	
	# Create outline color floats
	outlineColorRed = Float(0.0)
	outlineColorGreen = Float(0.0)
	outlineColorBlue = Float(0.0)
	
	# Create background color floats
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Set opacity of contour
	contourOpacity = Float(1.0)
	
	# Set representation
	contourRepresentation = Enum(['points', 'surface', 'wireframe'])
	
	# Set colormap
	contourColormap = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
	'CMRmap', 'Dark2', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', \
	'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG', 'PuBu', 'PuBuGn', \
	'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', \
	'RdYlGn', 'Reds', 'Set1', 'Set2', 'Set3', 'Spectral', 'Vega10', \
	'Vega20', 'Vega20b', 'Vega20c', 'Wistia', 'YlGn', 'YlGnBu', \
	'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'black-white', \
	'blue-red', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', \
	'cubehelix', 'file', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', \
	'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', \
	'gnuplot2', 'gray', 'hot', 'hsv', 'inferno', 'jet', 'magma', \
	'nipy_spectral', 'ocean', 'pink', 'plasma', 'prism', 'rainbow', \
	'seismic', 'spectral', 'spring', 'summer', 'terrain', 'viridis', \
	'winter'])
	
	# Initiate scene
	scene = Instance(MlabSceneModel, ())

	def __init__(self, *args):
		
		HasTraits.__init__(self)
		
		# Get data first
		
		_data = args[-1]
		
		# Modify threshold range based on data
		# For some reason, Range doesn't like numpy float32
		# Using float instead
		self.add_trait("threshold", Str('Enter thresholds separated by comma within box bracket'))
		self.add_trait("thresholdMinimum", Float(np.floor(float(_data.min()))))
		self.add_trait("thresholdMaximum", Float(np.ceil(float(_data.max()))))
		
		if len(args) > 1:
			
			x = args[0]
			y = args[1]
			z = args[2]

			# Plot the isosurface with minimum value from data
			sf = mlab.pipeline.scalar_field(x, y, z, _data, figure=self.scene.mayavi_scene)
		
		else:
			
			# Plot the isosurface with minimum value from data
			sf = mlab.pipeline.scalar_field(_data, figure=self.scene.mayavi_scene)
		
		# Set the threshold
		self.iso = mlab.pipeline.iso_surface(sf, contours=[_data.min()])
		
		# Plot the outline
		self.out = mayavi.tools.pipeline.outline(self.iso)
		
		# Set min, max, data
		self.thresholdMin = _data.min()
		self.thresholdMax = _data.max()
		self.OrigData = deepcopy(_data)
		
		# Set contour representation
		self.contourRepresentation = 'surface'
		
		# Set contour colormap
		self.contourColormap = 'viridis'
		
		# Set outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
		
		# Set background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		
		# Set checkbox 
		self.chkBox = True

	@on_trait_change('threshold')
	def threshold_changed(self):
		
		# First reset all contours
		self.iso.contour.contours = []
		
		try:
		
			# Set new threshold data once ] is detected
			if ']' in self.threshold:
				tmpthreshvals = self.threshold[1:-1].split(',')
				self.iso.contour.contours = [np.float32(i) for i in tmpthreshvals]
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('outlineWidth, outlineColorRed, outlineColorGreen,\
	outlineColorBlue')
	def outline_changed(self):
			
		# Change outline width
		self.out.actor.property.line_width = self.outlineWidth
		
		# Change outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
	
	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
	
	@on_trait_change('contourOpacity, contourRepresentation, contourColormap, colormapMin, colormapMax')
	def contour_changed(self):
		
		# Change contour opacity
		self.iso.actor.property.opacity = self.contourOpacity
		
		# Change contour representation
		self.iso.actor.property.representation = self.contourRepresentation
		
		# Change contour colormap
		self.iso.module_manager.scalar_lut_manager.lut_mode = self.contourColormap
		
		# Change colormap range
		self.iso.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin, self.colormapMax])
	
	@on_trait_change('chkBox')
	def chkbox_changed(self):
		
		if self.chkBox == False:
			
			# Set new threshold data
			self.iso.contour.contours = []
		
		else:
			
			# Set current threshold data
			if ']' in self.threshold:
				tmpthreshvals = self.threshold[1:-1].split(',')
				self.iso.contour.contours = [np.float32(i) for i in tmpthreshvals]

	view = View(
	
	HSplit(
	
	VGroup(Group(label = 'Active scalar fields'),
	
	Item("chkBox", label = 'Scalar field', width=0.05)),
	
	Item('scene', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, width=0.75), 
	
	# NOTE: width in the Hsplit controls the ratio of split
	
	VGroup(
	
	# Global options
	
	Group(label = 'Background options:'),
	
	HGroup(Item("BGColorRed", label = 'BG color (r, g, b) '),
	Item("BGColorGreen", label = ' '),
	Item("BGColorBlue", label = ' ')),
	
	Group(label = 'Outline options:'),
	
	Item("outlineWidth", label = 'Outline width:'),
	HGroup(Item("outlineColorRed", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen", label = ' '),
	Item("outlineColorBlue", label = ' ')),
	
	# Changeable for each contour
	
	Group(label = 'Isosurface options:'),
	
	HGroup(Item("thresholdMinimum", label = 'Minimum threshold:', style='readonly'), 
	Item("thresholdMaximum", label = ', Maximum threshold:'), style='readonly'),
	Item("threshold", label = 'Set thresholds:'), 
	
	
	Group(label = 'Contour options:'),
	
	HGroup(Item("contourOpacity", label = 'Opacity '),
	Item("contourRepresentation", label = 'Representation ')),
	
	HGroup(Item("contourColormap", label = 'Colormap '),
	Item("colormapMin", label = 'Colormap (min, max)'),
	Item("colormapMax", label = ' ')),
	
	)
	),resizable=True, width=1, height=1)

class mayaviVisualizeTimeSeries(HasTraits):
	
	# Create checkbox
	chkBox = Bool()
	
	# Create outline width range
	outlineWidth = Range(0., 10., 2.0, ) 
	
	# Create colormap range
	colormapMin = Float(0.0)
	colormapMax = Float(1.0)
	
	# Create outline color floats
	outlineColorRed = Float(0.0)
	outlineColorGreen = Float(0.0)
	outlineColorBlue = Float(0.0)
	
	# Create background color floats
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Set opacity of contour
	contourOpacity = Float(1.0)
	
	# Set representation
	contourRepresentation = Enum(['points', 'surface', 'wireframe'])
	
	# Set colormap
	contourColormap = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
	'CMRmap', 'Dark2', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', \
	'PRGn', 'Paired', 'Pastel1', 'Pastel2', 'PiYG', 'PuBu', 'PuBuGn', \
	'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', \
	'RdYlGn', 'Reds', 'Set1', 'Set2', 'Set3', 'Spectral', 'Vega10', \
	'Vega20', 'Vega20b', 'Vega20c', 'Wistia', 'YlGn', 'YlGnBu', \
	'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'black-white', \
	'blue-red', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', \
	'cubehelix', 'file', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', \
	'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', \
	'gnuplot2', 'gray', 'hot', 'hsv', 'inferno', 'jet', 'magma', \
	'nipy_spectral', 'ocean', 'pink', 'plasma', 'prism', 'rainbow', \
	'seismic', 'spectral', 'spring', 'summer', 'terrain', 'viridis', \
	'winter'])
	
	# Create next time button
	next_timeSeries  = Button('Next')
	
	# Create previous time button
	previous_timeSeries  = Button('Previous')
	
	# Create play time series button
	play_timeSeries  = Button('Play')
	
	# Create save movie button
	save_timeSeries  = Button('Save movie')
	
	# Initiate scene
	scene = Instance(MlabSceneModel, ())

	def __init__(self, *args):
		
		HasTraits.__init__(self)
		
		# Get data first
		
		self._dataTs = args[-1]
		
		# Check if data is 4d
		
		if not len(np.shape(self._dataTs)) == 4:
			raise ValueError
		
		# Create time series range
		
		self.add_trait("whichTime", Range(int(0.0), int(np.shape(self._dataTs)[-1]-1), int(1)))
		
		# By default, choose the first time instance
		
		self.whichTime = int(0)
		_data = self._dataTs[:, :, :, self.whichTime]
		
		# Modify threshold range based on data
		# For some reason, Range doesn't like numpy float32
		# Using float instead
		self.add_trait("threshold", Str('Enter thresholds separated by comma within box bracket'))
		self.add_trait("thresholdMinimum", Float(np.floor(float(_data.min()))))
		self.add_trait("thresholdMaximum", Float(np.ceil(float(_data.max()))))
		
		if len(args) > 1:
			
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]

			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data, figure=self.scene.mayavi_scene)
		
		else:
			
			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(_data, figure=self.scene.mayavi_scene)
		
		# Set the threshold
		self.iso = mlab.pipeline.iso_surface(self.sf, contours=[_data.min()])
		
		# Plot the outline
		self.out = mayavi.tools.pipeline.outline(self.iso)
		
		# Set min, max, data
		self.thresholdMin = _data.min()
		self.thresholdMax = _data.max()
		self.OrigData = deepcopy(_data)
		
		# Set contour representation
		self.contourRepresentation = 'surface'
		
		# Set contour colormap
		self.contourColormap = 'viridis'
		
		# Set outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
		
		# Set background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		
		# Set checkbox 
		self.chkBox = True
		
		# Set initial threshold as the same string 
		self.threshold = 'Enter thresholds separated by comma within box bracket'
		
	@on_trait_change('whichTime')
	def time_changed(self):
		
		# Choose data at other timestep
		_data = self._dataTs[:, :, :, self.whichTime]
		
		# Update min, max data
		self.thresholdMinimum = np.floor(float(_data.min()))
		self.thresholdMaximum = np.ceil(float(_data.max()))
		
		try:
			
			if ']' in self.threshold:
				mlab.clf()	
				
		except AttributeError:
			
			# Wait until user enters the values
			pass	
		
		# With same threshold update contour
		try:

			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data, figure=self.scene.mayavi_scene)
			
			# Set the threshold
			self.iso = mlab.pipeline.iso_surface(self.sf, contours=[_data.min()])
			
			# Plot the outline
			self.out = mayavi.tools.pipeline.outline(self.iso)
			
			# Change outline width
			self.out.actor.property.line_width = self.outlineWidth
			
			# Set outline color
			self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
			
			# Change contour opacity
			self.iso.actor.property.opacity = self.contourOpacity
			
			# Change contour representation
			self.iso.actor.property.representation = self.contourRepresentation
			
			# Change contour colormap
			self.iso.module_manager.scalar_lut_manager.lut_mode = self.contourColormap
			
			# Change colormap range
			self.iso.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin, self.colormapMax])
		
		except AttributeError:
			
			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(_data, figure=self.scene.mayavi_scene)
			
			# Set the threshold
			self.iso = mlab.pipeline.iso_surface(self.sf, contours=[_data.min()])
			
			# Plot the outline
			self.out = mayavi.tools.pipeline.outline(self.iso)
			
			# Change outline width
			self.out.actor.property.line_width = self.outlineWidth
			
			# Set outline color
			self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
			
			# Change contour opacity
			self.iso.actor.property.opacity = self.contourOpacity
			
			# Change contour representation
			self.iso.actor.property.representation = self.contourRepresentation
			
			# Change contour colormap
			self.iso.module_manager.scalar_lut_manager.lut_mode = self.contourColormap
			
			# Change colormap range
			self.iso.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin, self.colormapMax])
		
		try:
		
			# Set new threshold data once ] is detected
			if ']' in self.threshold:
				tmpthreshvals = self.threshold[1:-1].split(',')
				self.iso.contour.contours = [np.float32(i) for i in tmpthreshvals]
		
		except ValueError:
			
			# Wait until user enters the values
			pass
		
		except AttributeError:
			
			# Wait until user enters the values
			pass

	@on_trait_change('threshold')
	def threshold_changed(self):
		
		# First reset all contours
		self.iso.contour.contours = []
		
		try:
		
			# Set new threshold data once ] is detected
			if ']' in self.threshold:
				tmpthreshvals = self.threshold[1:-1].split(',')
				self.iso.contour.contours = [np.float32(i) for i in tmpthreshvals]
		
		except ValueError:
			
			# Wait until user enters the values
			pass
	
	@on_trait_change('outlineWidth, outlineColorRed, outlineColorGreen,\
	outlineColorBlue')
	def outline_changed(self):
			
		# Change outline width
		self.out.actor.property.line_width = self.outlineWidth
		
		# Change outline color
		self.out.actor.property.color = (self.outlineColorRed, self.outlineColorGreen, self.outlineColorBlue)
	
	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
	
	@on_trait_change('contourOpacity, contourRepresentation, contourColormap, colormapMin, colormapMax')
	def contour_changed(self):
		
		# Change contour opacity
		self.iso.actor.property.opacity = self.contourOpacity
		
		# Change contour representation
		self.iso.actor.property.representation = self.contourRepresentation
		
		# Change contour colormap
		self.iso.module_manager.scalar_lut_manager.lut_mode = self.contourColormap
		
		# Change colormap range
		self.iso.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin, self.colormapMax])
	
	@on_trait_change('chkBox')
	def chkbox_changed(self):
		
		if self.chkBox == False:
			
			# Set new threshold data
			self.iso.contour.contours = []
		
		else:
			
			# Set current threshold data
			if ']' in self.threshold:
				tmpthreshvals = self.threshold[1:-1].split(',')
				self.iso.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
	@on_trait_change('next_timeSeries')
	def next_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		if self.whichTime < int(np.shape(self._dataTs)[-1]-1):
			self.whichTime = current_time + 1
		
	@on_trait_change('previous_timeSeries')
	def previous_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		if self.whichTime > 0:
			self.whichTime = current_time - 1	
	
	@on_trait_change('play_timeSeries')
	def play_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs)[-1]-1)
		
		# Fire next time series button
		for i in range(current_time, total_time):
			
			self.next_timeseries_button_fired()
			GUI.process_events()
	
	@on_trait_change('save_timeSeries')
	def save_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs)[-1]-1)
		
		# Take screenshot and proceed to next frame
		for i in range(current_time, total_time):
			arr = mlab.screenshot(figure = self.scene.mayavi_scene, mode='rgba', antialiased=True)
			img = Image.fromarray(np.array(arr*255, dtype=np.uint8))
			img.save('img_'+ str(i-current_time).zfill(5) + '.png')
			self.next_timeseries_button_fired()
			GUI.process_events()
		
		# Use ffmpeg to combine into movie
		os.system('ffmpeg -framerate 5 -i img_%05d.png -vf format=yuv420p video.mp4')
		
		# Remove all png files
		os.system('rm -rf img*.png')

	view = View(
	
	HSplit(
	
	VGroup(Group(label = 'Active time series'),
	
	Item("chkBox", label = 'Time series', width=0.05)),
	
	Item('scene', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, width=0.75), 
	
	# NOTE: width in the Hsplit controls the ratio of split
	
	VGroup(
	
	# Global options
	
	Group(label = 'Background options:'),
	
	HGroup(Item("BGColorRed", label = 'BG color (r, g, b) '),
	Item("BGColorGreen", label = ' '),
	Item("BGColorBlue", label = ' ')),
	
	Group(label = 'Outline options:'),
	
	Item("outlineWidth", label = 'Outline width:'),
	HGroup(Item("outlineColorRed", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen", label = ' '),
	Item("outlineColorBlue", label = ' ')),
	
	# Time options
	
	Group(label = 'Time options:'),
	
	Item("whichTime", label = 'Select time step:'), 
	HGroup(Item("next_timeSeries", label = 'Animate'),
	Item("previous_timeSeries", label = ' '),
	Item("play_timeSeries", label = ' '),
	Item("save_timeSeries", label = ' ')),
	
	# Changeable for each contour
	
	Group(label = 'Isosurface options:'),
	
	HGroup(Item("thresholdMinimum", label = 'Minimum threshold:', style='readonly'), 
	Item("thresholdMaximum", label = ', Maximum threshold:'), style='readonly'),
	Item("threshold", label = 'Set thresholds:'), 
	
	
	Group(label = 'Contour options:'),
	
	HGroup(Item("contourOpacity", label = 'Opacity '),
	Item("contourRepresentation", label = 'Representation ')),
	
	HGroup(Item("contourColormap", label = 'Colormap '),
	Item("colormapMin", label = 'Colormap (min, max)'),
	Item("colormapMax", label = ' ')),
	
	)
	),resizable=True, width=1, height=1)


# NOTE: Setting width and height as 1 means maximized window 

# May implement these later but not immediately necessary
# iso.actor.property.specular
# iso.actor.property.specular_color
