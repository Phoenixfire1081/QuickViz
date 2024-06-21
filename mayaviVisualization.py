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

# Last updated: 21-06-2024
# MayaviVisualizeTimeSeries and mayaviVisualizeTimeSeries2
# are the only updated classes as of now. 
# Once the base UI has been created, then everything else can be 
# updated. 

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
	chkBox1 = Bool()
	
	# Create radio button
	radioButton1 = Enum('')
	
	# Global options
	# Create background color floats
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Create next time button
	next_timeSeries  = Button('Next')
	
	# Create previous time button
	previous_timeSeries  = Button('Previous')
	
	# Create play time series button
	play_timeSeries  = Button('Play >')
	
	# Create play time series button - reverse
	play_timeSeries_reverse  = Button('Play <')
	
	# Create stop time series button
	stop_timeSeries  = Button('Stop')
	
	# Create save movie button
	save_timeSeries  = Button('Save movie')
	
	# Set framerate
	framerate = Float(15)
	
	# Camera options
	camAzimuthG = Float(0.0)
	camElevationG = Float(0.0)
	camDistanceG = Float(0.0)
	focalPointG1 = Float(0.0)
	focalPointG2 = Float(0.0)
	focalPointG3 = Float(0.0)
	camRollG = Float(0.0)
	camAzimuthS = Range(-180., 180., 0.0, )
	camElevationS = Range(0., 180., 0.0, )
	camDistanceS = Float(0.0)
	focalPointS1 = Float(0.0)
	focalPointS2 = Float(0.0)
	focalPointS3 = Float(0.0)
	camRollS = Range(-180., 180., 0.0, )
	updateCurrentVals = Button('Update')
	setCurrentVals = Button('Set')
	
	# Individual options
	# Create outline width range
	outlineWidth = Range(0., 10., 2.0, ) 
	
	# Create colormap range
	colormapMin = Float(0.0)
	colormapMax = Float(1.0)
	
	# Create outline color floats
	outlineColorRed = Float(0.0)
	outlineColorGreen = Float(0.0)
	outlineColorBlue = Float(0.0)	
	
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
		
		self._dataTs = args[-1]
		
		# Check if data is 4d
		
		if not len(np.shape(self._dataTs)) == 4:
			raise ValueError
		
		# Create time series range
		
		self.add_trait("whichTime", Range(int(0.0), int(np.shape(self._dataTs)[-1]-1), int(1)))
		
		# By default, choose the first time instance
		_data = self._dataTs[:, :, :, 0]
		
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
			self.gridFlag = True
		
		else:
			
			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(_data, figure=self.scene.mayavi_scene)
			self.gridFlag = False
		
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
		
		# Set checkbox1 by default 
		self.chkBox1 = True
		
		# Set initial threshold as the same string 
		self.threshold = 'Enter thresholds separated by comma within box bracket'
		
		# Set stopPlayback
		self.stopPlayback = 0
		
	@on_trait_change('whichTime')
	def time_changed(self):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
			camRoll = mlab.roll()
		
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

		if self.gridFlag:
		
			# Plot the isosurface with minimum value from data
			self.sf = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data, figure=self.scene.mayavi_scene)
		
		else:
			
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
				# Keep the previous view
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
				viewControlRoll = mlab.roll(camRoll)
		
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
			
			# Update camera values
			self.updateCurrentVals_button_fired()
		
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
	
	@on_trait_change('chkBox1')
	def chkbox_changed(self):
		
		if self.chkBox1 == False:
			
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
		
		# Update camera values
		self.updateCurrentVals_button_fired()
		
	@on_trait_change('previous_timeSeries')
	def previous_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		if self.whichTime > 0:
			self.whichTime = current_time - 1
		
		# Update camera values
		self.updateCurrentVals_button_fired()	
	
	@on_trait_change('play_timeSeries')
	def play_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs)[-1]-1)
		
		# Fire next time series button
		for i in range(current_time, total_time):
			
			if i == current_time:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.next_timeseries_button_fired()
				GUI.process_events()
	
	@on_trait_change('stop_timeSeries')
	def stop_timeseries_button_fired(self):
		
		# Stop playback
		self.stopPlayback = 1
	
	@on_trait_change('play_timeSeries_reverse')
	def play_timeseries_reverse_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs)[-1]-1)
		
		# Fire previous time series button
		for i in range(current_time):
			
			if i == 0:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.previous_timeseries_button_fired()
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
		os.system('ffmpeg -y -framerate ' + str(int(self.framerate)) + ' -i img_%05d.png -vf "format=yuv420p, pad=ceil(iw/2)*2:ceil(ih/2)*2" video.mp4')
		
		# Remove all png files
		os.system('rm -rf img*.png')
	
	@on_trait_change('updateCurrentVals')
	def updateCurrentVals_button_fired(self):
		
		# Get current cam values and update
		self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view()	
		self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
		self.camRollG = mlab.roll()
		
		# Update setting options too
		self.camAzimuthS = self.camAzimuthG
		self.camElevationS = self.camElevationG
		self.camDistanceS = self.camDistanceG
		self.focalPointS1 = self.focalPointG1
		self.focalPointS2 = self.focalPointG2
		self.focalPointS3 = self.focalPointG3
		self.camRollS = self.camRollG
	
	@on_trait_change('camAzimuthS, camElevationS, camDistanceS, \
	focalPointS1, focalPointS2, focalPointS3, camRollS')
	def cam_angle_changed(self):
		
		# Update camera view
		mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3])
		mlab.roll(self.camRollS)
		

	view = View(
	
	VGroup(
	
	HSplit(
	
	VGroup(Group(label = 'Active time series'),
	
	HGroup(Item("chkBox1", label = 'Time series 1', width=0.05),
	Item("radioButton1", label = ': Control', style='custom', width=0.05)),
	
	),
	
	Item('scene', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, width=0.75), 
	
	# NOTE: width in the Hsplit controls the ratio of split
	
	VGroup(
	
	# Global options
	
	Group(label = 'Global options:'),
	
	Group(
	Group(label = 'Background options:'),
	
	HGroup(Item("BGColorRed", label = 'BG color (r, g, b) '),
	Item("BGColorGreen", label = ' '),
	Item("BGColorBlue", label = ' ')),
	
	# Time options
	
	Group(label = 'Time options:'),
	
	Item("whichTime", label = 'Select time step:'), 
	HGroup(Item("next_timeSeries", label = 'Animate'),
	Item("previous_timeSeries", label = ' '),
	Item("play_timeSeries", label = ' '),
	Item("play_timeSeries_reverse", label = ' '),
	Item("stop_timeSeries", label = ' '),
	Item("save_timeSeries", label = ' '),
	Item("framerate", label = 'Frame rate:'),),
	show_border = True),
	
	# Changeable for each time series
	
	Group(label = 'Local options:'),
	
	Group(
	Group(label = 'Outline options:'),
	
	Item("outlineWidth", label = 'Outline width:'),
	HGroup(Item("outlineColorRed", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen", label = ' '),
	Item("outlineColorBlue", label = ' ')),
	
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
	
	show_border = True),
	
	)
	),
	
	# Camera options
	Group(label = 'Camera options:'),
	Group(
	
	HGroup(
	Group(label = 'Current values:'),
	Item("camAzimuthG", label = 'Azimuth:', style='readonly'), 
	Item("camElevationG", label = 'Elevation:', style='readonly'), 
	Item("camRollG", label = 'Roll:', style='readonly'), 
	Item("camDistanceG", label = 'Distance:', style='readonly'), 
	Item("focalPointG1", label = ' Focal point:', style='readonly'),
	Item("focalPointG2", label = ' ', style='readonly'),
	Item("focalPointG3", label = ' ', style='readonly'),
	Item("updateCurrentVals", label = ' ')),
	
	HGroup(
	Item("camAzimuthS", label = 'Azimuth:'), 
	Item("camElevationS", label = 'Elevation:'), 
	Item("camRollS", label = 'Roll:')),
	HGroup(
	Item("camDistanceS", label = 'Distance:'), 
	Item("focalPointS1", label = ' Focal point:'),
	Item("focalPointS2", label = ' '),
	Item("focalPointS3", label = ' '),
	),
	
	show_border = True),
	)
	
	,resizable=True, width=1, height=1)
	
class mayaviVisualizeTimeSeries2(HasTraits):
	
	# Create checkbox
	chkBox1 = Bool()
	chkBox2 = Bool()
	
	# Create radio button
	radioButton1 = Enum('n', 'y')
	radioButton2 = Enum('n', 'y')
	
	# Global options
	# Create background color floats
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Create next time button
	next_timeSeries  = Button('Next')
	
	# Create previous time button
	previous_timeSeries  = Button('Previous')
	
	# Create play time series button
	play_timeSeries  = Button('Play >')
	
	# Create play time series button - reverse
	play_timeSeries_reverse  = Button('Play <')
	
	# Create stop time series button
	stop_timeSeries  = Button('Stop')
	
	# Create save movie button
	save_timeSeries  = Button('Save movie')
	
	# Set framerate
	framerate = Float(15)
	
	# Camera options
	camAzimuthG = Float(0.0)
	camElevationG = Float(0.0)
	camDistanceG = Float(0.0)
	focalPointG1 = Float(0.0)
	focalPointG2 = Float(0.0)
	focalPointG3 = Float(0.0)
	camRollG = Float(0.0)
	camAzimuthS = Range(-180., 180., 0.0, )
	camElevationS = Range(0., 180., 0.0, )
	camDistanceS = Float(0.0)
	focalPointS1 = Float(0.0)
	focalPointS2 = Float(0.0)
	focalPointS3 = Float(0.0)
	camRollS = Range(-180., 180., 0.0, )
	updateCurrentVals = Button('Update')
	setCurrentVals = Button('Set')
	
	# Individual options
	# Create outline width range
	outlineWidth1 = Range(0., 10., 2.0, ) 
	outlineWidth2 = Range(0., 10., 2.0, ) 
	
	# Create colormap range
	colormapMin1 = Float(0.0)
	colormapMax1 = Float(1.0)
	colormapMin2 = Float(0.0)
	colormapMax2 = Float(1.0)
	
	# Create outline color floats
	outlineColorRed1 = Float(0.0)
	outlineColorGreen1 = Float(0.0)
	outlineColorBlue1 = Float(0.0)	
	outlineColorRed2 = Float(0.0)
	outlineColorGreen2 = Float(0.0)
	outlineColorBlue2 = Float(0.0)	
	
	# Set opacity of contour
	contourOpacity1 = Float(1.0)
	contourOpacity2 = Float(1.0)
	
	# Set representation
	contourRepresentation1 = Enum(['points', 'surface', 'wireframe'])
	contourRepresentation2 = Enum(['points', 'surface', 'wireframe'])
	
	# Set colormap
	contourColormap1 = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
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
	contourColormap2 = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
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
		
		self._dataTs1 = args[-2]
		self._dataTs2 = args[-1]
		
		# Check if data is 4d
		
		if not len(np.shape(self._dataTs1)) == 4:
			raise ValueError
		
		if not len(np.shape(self._dataTs2)) == 4:
			raise ValueError
		
		# Create time series range
		
		self.add_trait("whichTime", Range(int(0.0), int(np.shape(self._dataTs1)[-1]-1), int(1)))
		
		# By default, choose the first time instance
		_data1 = self._dataTs1[:, :, :, 0]
		_data2 = self._dataTs2[:, :, :, 0]
		
		# Modify threshold range based on data
		# For some reason, Range doesn't like numpy float32
		# Using float instead
		self.add_trait("threshold1", Str('Enter thresholds separated by comma within box bracket'))
		self.add_trait("thresholdMinimum1", Float(np.floor(float(_data1.min()))))
		self.add_trait("thresholdMaximum1", Float(np.ceil(float(_data1.max()))))
		
		self.add_trait("threshold2", Str('Enter thresholds separated by comma within box bracket'))
		self.add_trait("thresholdMinimum2", Float(np.floor(float(_data2.min()))))
		self.add_trait("thresholdMaximum2", Float(np.ceil(float(_data2.max()))))
		
		if len(args) > 1:
			
			self.x = args[0]
			self.y = args[1]
			self.z = args[2]

			# Plot the isosurface with minimum value from data
			self.sf1 = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data1, figure=self.scene.mayavi_scene)
			self.sf2 = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data2, figure=self.scene.mayavi_scene)
			self.gridFlag = True
		
		else:
			
			# Plot the isosurface with minimum value from data
			self.sf1 = mlab.pipeline.scalar_field(_data1, figure=self.scene.mayavi_scene)
			self.sf2 = mlab.pipeline.scalar_field(_data2, figure=self.scene.mayavi_scene)
			self.gridFlag = False
		
		# Set the threshold
		self.iso1 = mlab.pipeline.iso_surface(self.sf1, contours=[_data1.min()])
		self.iso2 = mlab.pipeline.iso_surface(self.sf2, contours=[_data2.min()])
		
		# Plot the outline
		self.out1 = mayavi.tools.pipeline.outline(self.iso1)
		self.out2 = mayavi.tools.pipeline.outline(self.iso2)
		
		# Set min, max, data
		self.thresholdMin1 = _data1.min()
		self.thresholdMax1 = _data1.max()
		self.OrigData1 = deepcopy(_data1)
		self.thresholdMin2 = _data2.min()
		self.thresholdMax2 = _data2.max()
		self.OrigData2 = deepcopy(_data2)
		
		# Set contour representation
		self.contourRepresentation1 = 'surface'
		self.contourRepresentation2 = 'surface'
		
		# Set contour colormap
		self.contourColormap1 = 'viridis'
		self.contourColormap2 = 'viridis'
		
		# Set outline color
		self.out1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
		
		# Set background color
		self.iso1.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		
		# Set checkboxes by default 
		self.chkBox1 = True
		self.chkBox2 = True
		
		# Set initial threshold as the same string 
		self.threshold1 = 'Enter thresholds separated by comma within box bracket'
		self.threshold2 = 'Enter thresholds separated by comma within box bracket'
		
		# Set stopPlayback
		self.stopPlayback = 0
		
		# Set radiobutton1 by default
		self.radioButton1 = 'y'
		self.radioButton2 = 'n'
		
	@on_trait_change('whichTime')
	def time_changed(self):
		
		# Get camera view
		if not mlab.view() is None:
			camAzimuth, camElevation, camDistance, focalPoint = mlab.view()
			camRoll = mlab.roll()
			
		# Activate all checkboxes if time is changed
		# This is a global control anyway
		self.chkBox1 = True
		self.chkBox2 = True
		
		# Choose data at other timestep
		_data1 = self._dataTs1[:, :, :, self.whichTime]
		_data2 = self._dataTs2[:, :, :, self.whichTime]
		
		# Update min, max data
		self.thresholdMinimum1 = np.floor(float(_data1.min()))
		self.thresholdMaximum1 = np.ceil(float(_data1.max()))
		self.thresholdMinimum2 = np.floor(float(_data2.min()))
		self.thresholdMaximum2 = np.ceil(float(_data2.max()))
		
		try:
			
			if ']' in self.threshold1:
				mlab.clf()	
			elif ']' in self.threshold2:
				mlab.clf()
				
		except AttributeError:
			
			# Wait until user enters the values
			pass	
		
		# With same threshold update contour

		if self.gridFlag:
		
			# Plot the isosurface with minimum value from data
			self.sf1 = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data1, figure=self.scene.mayavi_scene)
			self.sf2 = mlab.pipeline.scalar_field(self.x, self.y, self.z, _data2, figure=self.scene.mayavi_scene)
		
		else:
			
			# Plot the isosurface with minimum value from data
			self.sf1 = mlab.pipeline.scalar_field(_data1, figure=self.scene.mayavi_scene)
			self.sf2 = mlab.pipeline.scalar_field(_data2, figure=self.scene.mayavi_scene)
		
		# Set the threshold
		self.iso1 = mlab.pipeline.iso_surface(self.sf1, contours=[_data1.min()])
		self.iso2 = mlab.pipeline.iso_surface(self.sf2, contours=[_data2.min()])
		
		# Plot the outline
		self.out1 = mayavi.tools.pipeline.outline(self.iso1)
		self.out2 = mayavi.tools.pipeline.outline(self.iso2)
		
		# Change outline width
		self.out1.actor.property.line_width = self.outlineWidth1
		self.out2.actor.property.line_width = self.outlineWidth2
		
		# Set outline color
		self.out1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
		
		# Change contour opacity
		self.iso1.actor.property.opacity = self.contourOpacity1
		self.iso2.actor.property.opacity = self.contourOpacity2
		
		# Change contour representation
		self.iso1.actor.property.representation = self.contourRepresentation1
		self.iso2.actor.property.representation = self.contourRepresentation2
		
		# Change contour colormap
		self.iso1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
		self.iso2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
		
		# Change colormap range
		self.iso1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
		self.iso2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
		
		try:
		
			# Set new threshold data once ] is detected
			if ']' in self.threshold1:
				tmpthreshvals = self.threshold1[1:-1].split(',')
				self.iso1.contour.contours = [np.float32(i) for i in tmpthreshvals]
				# Keep the previous view
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
				viewControlRoll = mlab.roll(camRoll)
			if ']' in self.threshold2:
				tmpthreshvals = self.threshold2[1:-1].split(',')
				self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
				# Keep the previous view
				viewControl = mlab.view(camAzimuth, camElevation, camDistance, focalPoint)
				viewControlRoll = mlab.roll(camRoll)
		
		except ValueError:
			
			# Wait until user enters the values
			pass
		
		except AttributeError:
			
			# Wait until user enters the values
			pass

	@on_trait_change('threshold1')
	def threshold1_changed(self):
		
		if self.chkBox1:
		
			try:
			
				# Set new threshold data once ] is detected
				if ']' in self.threshold1:
					# First reset all contours
					self.iso1.contour.contours = []
					
					tmpthreshvals = self.threshold1[1:-1].split(',')
					self.iso1.contour.contours = [np.float32(i) for i in tmpthreshvals]
				
				# Update camera values
				self.updateCurrentVals_button_fired()
			
			except ValueError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('threshold2')
	def threshold2_changed(self):
	
		if self.chkBox2:
		
			try:
				
				if ']' in self.threshold2:
					# First reset all contours
					self.iso2.contour.contours = []
					
					tmpthreshvals = self.threshold2[1:-1].split(',')
					self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
				
				# Update camera values
				self.updateCurrentVals_button_fired()
			
			except ValueError:
				
				# Wait until user enters the values
				pass
	
	@on_trait_change('outlineWidth1, outlineColorRed1, outlineColorGreen1,\
	outlineColorBlue1')
	def outline1_changed(self):
			
		# Change outline width
		self.out1.actor.property.line_width = self.outlineWidth1
		
		# Change outline color
		self.out1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
	
	@on_trait_change('outlineWidth2, outlineColorRed2, outlineColorGreen2,\
	outlineColorBlue2')
	def outline2_changed(self):
			
		# Change outline width
		self.out2.actor.property.line_width = self.outlineWidth2
		
		# Change outline color
		self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
	
	@on_trait_change('BGColorRed, BGColorGreen, BGColorBlue')
	def background_changed(self):
		
		# Change background color
		self.iso1.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
	
	@on_trait_change('contourOpacity1, contourRepresentation1, contourColormap1, colormapMin1, colormapMax1')
	def contour1_changed(self):
		
		# Change contour opacity
		self.iso1.actor.property.opacity = self.contourOpacity1
		
		# Change contour representation
		self.iso1.actor.property.representation = self.contourRepresentation1
		
		# Change contour colormap
		self.iso1.module_manager.scalar_lut_manager.lut_mode = self.contourColormap1
		
		# Change colormap range
		self.iso1.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin1, self.colormapMax1])
	
	@on_trait_change('contourOpacity2, contourRepresentation2, contourColormap2, colormapMin2, colormapMax2')
	def contour2_changed(self):
		
		# Change contour opacity
		self.iso2.actor.property.opacity = self.contourOpacity2
		
		# Change contour representation
		self.iso2.actor.property.representation = self.contourRepresentation2
		
		# Change contour colormap
		self.iso2.module_manager.scalar_lut_manager.lut_mode = self.contourColormap2
		
		# Change colormap range
		self.iso2.module_manager.scalar_lut_manager.data_range = np.array([self.colormapMin2, self.colormapMax2])
	
	@on_trait_change('chkBox1')
	def chkbox1_changed(self):
		
		if self.chkBox1 == False:
			
			# Set new threshold data
			self.iso1.contour.contours = []
		
		else:
			
			# Set current threshold data
			if ']' in self.threshold1:
				tmpthreshvals = self.threshold1[1:-1].split(',')
				self.iso1.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
	@on_trait_change('chkBox2')
	def chkbox2_changed(self):
		
		if self.chkBox2 == False:
			
			# Set new threshold data
			self.iso2.contour.contours = []
		
		else:
			
			# Set current threshold data
			if ']' in self.threshold2:
				tmpthreshvals = self.threshold2[1:-1].split(',')
				self.iso2.contour.contours = [np.float32(i) for i in tmpthreshvals]
	
	@on_trait_change('next_timeSeries')
	def next_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		if self.whichTime < int(np.shape(self._dataTs1)[-1]-1):
			self.whichTime = current_time + 1
		
		# Update camera values
		self.updateCurrentVals_button_fired()
		
	@on_trait_change('previous_timeSeries')
	def previous_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		if self.whichTime > 0:
			self.whichTime = current_time - 1
		
		# Update camera values
		self.updateCurrentVals_button_fired()	
	
	@on_trait_change('play_timeSeries')
	def play_timeseries_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs1)[-1]-1)
		
		# Fire next time series button
		for i in range(current_time, total_time):
			
			if i == current_time:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.next_timeseries_button_fired()
				GUI.process_events()
	
	@on_trait_change('stop_timeSeries')
	def stop_timeseries_button_fired(self):
		
		# Stop playback
		self.stopPlayback = 1
	
	@on_trait_change('play_timeSeries_reverse')
	def play_timeseries_reverse_button_fired(self):
		
		# Get current time first
		current_time = self.whichTime
		
		# Get total time
		total_time = int(np.shape(self._dataTs1)[-1]-1)
		
		# Fire previous time series button
		for i in range(current_time):
			
			if i == 0:
				
				self.stopPlayback = 0
			
			if not self.stopPlayback:
			
				self.previous_timeseries_button_fired()
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
		os.system('ffmpeg -y -framerate ' + str(int(self.framerate)) + ' -i img_%05d.png -vf "format=yuv420p, pad=ceil(iw/2)*2:ceil(ih/2)*2" video.mp4')
		
		# Remove all png files
		os.system('rm -rf img*.png')
	
	@on_trait_change('updateCurrentVals')
	def updateCurrentVals_button_fired(self):
		
		# Get current cam values and update
		self.camAzimuthG, self.camElevationG, self.camDistanceG, fp = mlab.view()	
		self.focalPointG1, self.focalPointG2, self.focalPointG3 = fp
		self.camRollG = mlab.roll()
		
		# Update setting options too
		self.camAzimuthS = self.camAzimuthG
		self.camElevationS = self.camElevationG
		self.camDistanceS = self.camDistanceG
		self.focalPointS1 = self.focalPointG1
		self.focalPointS2 = self.focalPointG2
		self.focalPointS3 = self.focalPointG3
		self.camRollS = self.camRollG
	
	@on_trait_change('camAzimuthS, camElevationS, camDistanceS, \
	focalPointS1, focalPointS2, focalPointS3, camRollS')
	def cam_angle_changed(self):
		
		# Update camera view
		mlab.view(self.camAzimuthS, self.camElevationS, self.camDistanceS, [self.focalPointS1, self.focalPointS2, self.focalPointS3])
		mlab.roll(self.camRollS)
	
	@on_trait_change('radioButton1')
	def radio_button1_changed(self):
		
		# Only one radio button may be active at a time
		if self.radioButton1 == 'y':
			self.radioButton2 = 'n'
		else:
			self.radioButton2 = 'y'
	
	@on_trait_change('radioButton2')
	def radio_button2_changed(self):
		if self.radioButton2 == 'y':
			self.radioButton1 = 'n'
		else:
			self.radioButton1 = 'y'
		
		# GUI.process_events()

	view = View(
	
	VGroup(
	
	HSplit(
	
	VGroup(Group(label = 'Active time series'),
	
	HGroup(Item("chkBox1", label = 'Time series 1', width=0.05),
	Item("radioButton1", label = ': Control', style='custom', width=0.05)),
	
	HGroup(Item("chkBox2", label = 'Time series 2', width=0.05),
	Item("radioButton2", label = ': Control', style='custom', width=0.05)),
	
	),
	
	Item('scene', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, width=0.65), 
	
	# NOTE: width in the Hsplit controls the ratio of split
	
	VGroup(
	
	# Global options
	
	Group(label = 'Global options:'),
	
	Group(
	Group(label = 'Background options:'),
	
	HGroup(Item("BGColorRed", label = 'BG color (r, g, b) '),
	Item("BGColorGreen", label = ' '),
	Item("BGColorBlue", label = ' ')),
	
	# Time options
	
	Group(label = 'Time options:'),
	
	Item("whichTime", label = 'Select time step:'), 
	HGroup(Item("next_timeSeries", label = 'Animate'),
	Item("previous_timeSeries", label = ' '),
	Item("play_timeSeries", label = ' '),
	Item("play_timeSeries_reverse", label = ' '),
	Item("stop_timeSeries", label = ' '),
	Item("save_timeSeries", label = ' '),
	Item("framerate", label = 'Frame rate:'),),
	show_border = True),
	
	# Changeable for each time series
	
	Group(label = 'Local options:'),
	
	Group(
	Group(label = 'Outline options 1:'),
	
	Item("outlineWidth1", label = 'Outline width:'),
	HGroup(Item("outlineColorRed1", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen1", label = ' '),
	Item("outlineColorBlue1", label = ' ')),
	
	Group(label = 'Isosurface options 1:'),
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:'), style='readonly'),
	Item("threshold1", label = 'Set thresholds:'), 
	
	
	Group(label = 'Contour options 1:'),
	
	HGroup(Item("contourOpacity1", label = 'Opacity '),
	Item("contourRepresentation1", label = 'Representation ')),
	
	HGroup(Item("contourColormap1", label = 'Colormap '),
	Item("colormapMin1", label = 'Colormap (min, max)'),
	Item("colormapMax1", label = ' ')),
	
	show_border = True, visible_when = "radioButton1 == 'y'"),
	
	Group(
	Group(label = 'Outline options 2:'),
	
	Item("outlineWidth2", label = 'Outline width:'),
	HGroup(Item("outlineColorRed2", label = 'Outline color (r, g, b) '),
	Item("outlineColorGreen2", label = ' '),
	Item("outlineColorBlue2", label = ' ')),
	
	Group(label = 'Isosurface options 2:'),
	
	HGroup(Item("thresholdMinimum2", label = 'Minimum threshold:', style='readonly'), 
	Item("thresholdMaximum2", label = ', Maximum threshold:'), style='readonly'),
	Item("threshold2", label = 'Set thresholds:'), 
	
	
	Group(label = 'Contour options 2:'),
	
	HGroup(Item("contourOpacity2", label = 'Opacity '),
	Item("contourRepresentation2", label = 'Representation ')),
	
	HGroup(Item("contourColormap2", label = 'Colormap '),
	Item("colormapMin2", label = 'Colormap (min, max)'),
	Item("colormapMax2", label = ' ')),
	
	show_border = True, visible_when = "radioButton2 == 'y'"),
	
	)
	),
	
	# Camera options
	Group(label = 'Camera options:'),
	Group(
	
	HGroup(
	Group(label = 'Current values:'),
	Item("camAzimuthG", label = 'Azimuth:', style='readonly'), 
	Item("camElevationG", label = 'Elevation:', style='readonly'), 
	Item("camRollG", label = 'Roll:', style='readonly'), 
	Item("camDistanceG", label = 'Distance:', style='readonly'), 
	Item("focalPointG1", label = ' Focal point:', style='readonly'),
	Item("focalPointG2", label = ' ', style='readonly'),
	Item("focalPointG3", label = ' ', style='readonly'),
	Item("updateCurrentVals", label = ' ')),
	
	HGroup(
	Item("camAzimuthS", label = 'Azimuth:'), 
	Item("camElevationS", label = 'Elevation:'), 
	Item("camRollS", label = 'Roll:')),
	HGroup(
	Item("camDistanceS", label = 'Distance:'), 
	Item("focalPointS1", label = ' Focal point:'),
	Item("focalPointS2", label = ' '),
	Item("focalPointS3", label = ' '),
	),
	
	show_border = True),
	)
	
	,resizable=True, width=1, height=1)


# NOTE: Setting width and height as 1 means maximized window 

# May implement these later but not immediately necessary
# iso.actor.property.specular
# iso.actor.property.specular_color
