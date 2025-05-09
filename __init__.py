import numpy as np
from mayavi import mlab
import mayavi
from copy import deepcopy
from traits.api import HasTraits, Range, Instance, on_trait_change, Float, Enum, Bool, Str
from traits.api import Button, Int
from traitsui.api import View, Item, HGroup, HSplit, VGroup, Heading, Group
from mayavi.core.ui.api import MayaviScene, SceneEditor, MlabSceneModel
from pyface.api import GUI
from PIL import Image
import os

from .backgroundOptions import allBackgroundOptions
from .playbackOptions import allPlaybackOptions
from .saveMovieOptions import allSaveMovieOptions
from .timeUpdate import timeUpdateBehavior
from .contourOptions import allContourOptions
from .cameraOptions import allCameraOptions
from .activeDataControl import activeDataControlClass
from .chooseFileDialog import fileChooserClass
from .camPathControls import allPathControlsClass

# Import Visualization elements
from .Visualization_elements.isosurfaceOptions import allIsosurfaceOptions
from .Visualization_elements.volumeRenderingOptions import allVolRenderingOptions

# Import UI elements
from .UI_elements.activeData_UI import activeDataUIelements
from .UI_elements.scene_UI import sceneUIelements
from .UI_elements.globalOptions_UI import globalUIelements
from .UI_elements.localOptions_UI import localUIelements
from .UI_elements.isosurface_UI import isoUIelements
from .UI_elements.contourOptions_UI import contourUIelements
from .UI_elements.cameraOptions_UI import cameraUIelements

# Allow for a maximum of 4 scalar time series data

class mayaviVisualizeTimeSeries(HasTraits, allIsosurfaceOptions,\
	allBackgroundOptions, allPlaybackOptions, allSaveMovieOptions, \
	timeUpdateBehavior, allContourOptions, allCameraOptions, \
	activeDataControlClass, fileChooserClass, allPathControlsClass,\
	allVolRenderingOptions):
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	# Clamp for changing all TS
	clamp = Bool()
	
	# Create radio button
	radioButton1 = Enum('N', 'Y')
	radioButton2 = Enum('N', 'Y')
	radioButton3 = Enum('N', 'Y')
	radioButton4 = Enum('N', 'Y')
	
	# Create outline width range
	outlineWidth1 = Range(0., 10., 2.0, ) 
	outlineToggle1 = Bool(True)
	outlineWidth2 = Range(0., 10., 2.0, ) 
	outlineToggle2 = Bool(True)
	outlineWidth3 = Range(0., 10., 2.0, ) 
	outlineToggle3 = Bool(True)
	outlineWidth4 = Range(0., 10., 2.0, ) 
	outlineToggle4 = Bool(True)
	
	# Create outline color floats
	outlineColorRed1 = Float(0.0)
	outlineColorGreen1 = Float(0.0)
	outlineColorBlue1 = Float(0.0)
	outlineColorRed2 = Float(0.0)
	outlineColorGreen2 = Float(0.0)
	outlineColorBlue2 = Float(0.0)
	outlineColorRed3 = Float(0.0)
	outlineColorGreen3 = Float(0.0)
	outlineColorBlue3 = Float(0.0)
	outlineColorRed4 = Float(0.0)
	outlineColorGreen4 = Float(0.0)
	outlineColorBlue4 = Float(0.0)	
	
	# All options
	allLocalOptions = Enum(['Isosurface', 'Volume Rendering', 'Slice'], cols=3)
	
	# Isosurface options
	hideShowIsosurface = Bool()
	
	# Volume rendering options
	enableVolRendering = Button('Set')
	
	# Create colormap range
	colormapMin1 = Float(0.0)
	colormapMax1 = Float(1.0)
	colormapMin2 = Float(0.0)
	colormapMax2 = Float(1.0)
	colormapMin3 = Float(0.0)
	colormapMax3 = Float(1.0)
	colormapMin4 = Float(0.0)
	colormapMax4 = Float(1.0)
	
	# Set opacity of contour
	contourOpacity1 = Float(1.0)
	contourOpacity2 = Float(1.0)
	contourOpacity3 = Float(1.0)
	contourOpacity4 = Float(1.0)
	
	# Set representation
	contourRepresentation1 = Enum(['points', 'surface', 'wireframe'])
	contourRepresentation2 = Enum(['points', 'surface', 'wireframe'])
	contourRepresentation3 = Enum(['points', 'surface', 'wireframe'])
	contourRepresentation4 = Enum(['points', 'surface', 'wireframe'])
	
	# Set threshold
	setThreshold1  = Button('Set')
	setThresholdPercent1  = Button('Set')
	setThreshold2  = Button('Set')
	setThresholdPercent2  = Button('Set')
	setThreshold3  = Button('Set')
	setThresholdPercent3  = Button('Set')
	setThreshold4  = Button('Set')
	setThresholdPercent4  = Button('Set')
	
	# Initialize set threshold button press event
	setThresholdFired1 = False
	setThresholdFired2 = False
	setThresholdFired3 = False
	setThresholdFired4 = False
	
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
	contourColormap3 = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
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
	contourColormap4 = Enum(['Accent', 'Blues', 'BrBG', 'BuGn', 'BuPu', \
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
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	# Global options
	
	# Layout options (Split the area with up to 4 screens)
	layout = Enum(['1', '2', '3', '4'], cols=4)
	
	# Show hide controls
	showHideGlobal = Bool()
	showHideLocal = Bool()
	
	# Create checkboxes for every screen and every TS
	# These are global controls which turn off everything
	# TODO - add local controls for iso, vol rendering, slice etc.
	screen1_ts1 = Bool()
	screen2_ts1 = Bool()
	screen3_ts1 = Bool()
	screen4_ts1 = Bool()
	screen1_ts2 = Bool()
	screen2_ts2 = Bool()
	screen3_ts2 = Bool()
	screen4_ts2 = Bool()
	screen1_ts3 = Bool()
	screen2_ts3 = Bool()
	screen3_ts3 = Bool()
	screen4_ts3 = Bool()
	screen1_ts4 = Bool()
	screen2_ts4 = Bool()
	screen3_ts4 = Bool()
	screen4_ts4 = Bool()
	
	# Create background color floats
	BGtext = Str('BG color (r, g, b) ')
	BGColorRed = Float(1.0)
	BGColorGreen = Float(1.0)
	BGColorBlue = Float(1.0)
	
	# Text for all
	TStext = Str('Select time step:')
	SaveTxt = Str('Save location:')
	StartTxt = Str('Start:')
	StopTxt = Str('Stop:')
	FRTxt = Str('Frame rate:')
	SaveImgTxt = Str('Save images:')
	OutlineWidthTxt = Str('Outline width:')
	OutlineColorTxt = Str('Outline color (r,g,b):')
	ThresholdTxt = Str('Threshold(s):')
	ThresholdPercentTxt = Str('Threshold(s) percent:')
	OpacityTxt = Str('Opacity:')
	ColormapTxt = Str('Colormap:')
	RepresentationTxt = Str('Representation:')
	ColormapMinMaxTxt = Str('Colormap(min, max):')
	ShowHideOutlineTxt = Str('Show/Hide outline:')
	ActiveDataTxt = Str('Active data:')
	IsoOptionsTxt = Str('Isosurface options:')
	ContourOptionsTxt = Str('Contour options:')
	OutOptionsTxt = Str('Outline options:')
	
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
	
	# Create save snapshot button
	save_snapshot  = Button('Snapshot')
	
	# Movie save path
	save_path = Str(os.getcwd())
	choose_folder = Button('Choose')
	
	# Set start ts, stop ts, framerate, save_images
	startMovie = Float(0)
	stopMovie = Float(-1)
	framerate = Float(15)
	save_images = Bool(True)
	
	# Camera options
	showHideCamera = Bool()
	camAzimuthG = Float(0.0)
	camElevationG = Float(0.0)
	camDistanceG = Float(0.0)
	focalPointG1 = Float(0.0)
	focalPointG2 = Float(0.0)
	focalPointG3 = Float(0.0)
	camRollG = Float(0.0)
	camAzimuthS = Range(-360., 360., 0.0, )
	camElevationS = Range(-180., 180., 0.0, )
	camDistanceS = Float(0.0)
	focalPointS1 = Float(0.0)
	focalPointS2 = Float(0.0)
	focalPointS3 = Float(0.0)
	camRollS = Range(-180., 180., 0.0, )
	updateCurrentVals = Button('Update current values')
	saveCam1 = Button('Camera 1')
	saveCam2 = Button('Camera 2')
	saveCam3 = Button('Camera 3')
	saveCam4 = Button('Camera 4')
	saveCam5 = Button('Camera 5')
	camReset = Button('Reset')
	setCurrentVals = Button('Set')
	
	# Camera path control options
	camPathType = Enum(['None', 'Circle', 'Linear'])
	startCamPath = Float(0)
	stopCamPath = Float(-1)
	addCamPath = Button('Add')
	finishCamPath = Button('Finish')
	resetCamPath = Button('Reset')
	
	# Create choose files button
	select_files  = Button('Select')
	
	# Create number of grid points in each direction
	xlength = Int(0)
	ylength = Int(0)
	zlength = Int(0)
	numComponents = Enum(['1', '3'])
	
	# Bounding box values
	bbxmin = Float(0.0)
	bbxmax = Float(1.0)
	bbymin = Float(0.0)
	bbymax = Float(1.0)
	bbzmin = Float(0.0)
	bbzmax = Float(1.0)
	
	# Array order
	arrayOrder = Enum(['x fastest', 'z fastest'])
	
	# Set data precision
	dataPrecision = Enum(['float', 'double'])
	
	# Load data button
	read_data  = Button('Select')
	
	# Initiate scene (up to 4)
	scene1 = Instance(MlabSceneModel, ())
	scene2 = Instance(MlabSceneModel, ())
	scene3 = Instance(MlabSceneModel, ())
	scene4 = Instance(MlabSceneModel, ())

	def __init__(self, *args):
		
		HasTraits.__init__(self)
		
		# Explicitly register observers from other files
		
		# allBackgroundOptions
		self.on_trait_change(self.background_changed, "BGColorRed")
		self.on_trait_change(self.background_changed, "BGColorGreen")
		self.on_trait_change(self.background_changed, "BGColorBlue")
		
		# allPlaybackOptions
		self.on_trait_change(self.next_timeseries_button_fired, "next_timeSeries")
		self.on_trait_change(self.previous_timeseries_button_fired, "previous_timeSeries")
		self.on_trait_change(self.play_timeseries_button_fired, "play_timeSeries")
		self.on_trait_change(self.stop_timeseries_button_fired, "stop_timeSeries")
		self.on_trait_change(self.play_timeseries_reverse_button_fired, "play_timeSeries_reverse")
		
		# allSaveMovieOptions
		self.on_trait_change(self.save_timeseries_button_fired, "save_timeSeries")
		self.on_trait_change(self.save_snapshot_button_fired, "save_snapshot")
		self.on_trait_change(self.choose_folder_button_fired, "choose_folder")
		
		# allCameraOptions
		self.on_trait_change(self.updateCurrentVals_button_fired, "updateCurrentVals")
		self.on_trait_change(self.saveCam1_fired, "saveCam1")
		self.on_trait_change(self.saveCam2_fired, "saveCam2")
		self.on_trait_change(self.saveCam3_fired, "saveCam3")
		self.on_trait_change(self.saveCam4_fired, "saveCam4")
		self.on_trait_change(self.saveCam5_fired, "saveCam5")
		self.on_trait_change(self.camReset_fired, "camReset")
		self.on_trait_change(self.cam_angle_changed, "camAzimuthS")
		self.on_trait_change(self.cam_angle_changed, "camElevationS")
		self.on_trait_change(self.cam_angle_changed, "camDistanceS")
		self.on_trait_change(self.cam_angle_changed, "focalPointS1")
		self.on_trait_change(self.cam_angle_changed, "focalPointS2")
		self.on_trait_change(self.cam_angle_changed, "focalPointS3")
		self.on_trait_change(self.cam_angle_changed, "camRollS")
		
		# allPathControlsClass
		self.on_trait_change(self.camPathTypeChanged, "camPathType")
		self.on_trait_change(self.addCamPathChanged, "addCamPath")
		self.on_trait_change(self.finishCamPathChanged, "finishCamPath")
		self.on_trait_change(self.resetCamPathChanged, "resetCamPath")
		
		# fileChooserClass
		self.on_trait_change(self.select_files_toggled, "select_files")
		
		# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
		
		# allContourOptions
		self.on_trait_change(self.outline_changed1, "outlineWidth1")
		self.on_trait_change(self.outline_changed1, "outlineColorRed1")
		self.on_trait_change(self.outline_changed1, "outlineColorGreen1")
		self.on_trait_change(self.outline_changed1, "outlineColorBlue1")
		self.on_trait_change(self.outline_changed1, "outlineToggle1")
		self.on_trait_change(self.contour_changed1, "contourOpacity1")
		self.on_trait_change(self.contour_changed1, "contourRepresentation1")
		self.on_trait_change(self.contour_changed1, "contourColormap1")
		self.on_trait_change(self.contour_changed1, "colormapMin1")
		self.on_trait_change(self.contour_changed1, "colormapMax1")
		
		self.on_trait_change(self.outline_changed2, "outlineWidth2")
		self.on_trait_change(self.outline_changed2, "outlineColorRed2")
		self.on_trait_change(self.outline_changed2, "outlineColorGreen2")
		self.on_trait_change(self.outline_changed2, "outlineColorBlue2")
		self.on_trait_change(self.outline_changed2, "outlineToggle2")
		self.on_trait_change(self.contour_changed2, "contourOpacity2")
		self.on_trait_change(self.contour_changed2, "contourRepresentation2")
		self.on_trait_change(self.contour_changed2, "contourColormap2")
		self.on_trait_change(self.contour_changed2, "colormapMin2")
		self.on_trait_change(self.contour_changed2, "colormapMax2")
		
		self.on_trait_change(self.outline_changed3, "outlineWidth3")
		self.on_trait_change(self.outline_changed3, "outlineColorRed3")
		self.on_trait_change(self.outline_changed3, "outlineColorGreen3")
		self.on_trait_change(self.outline_changed3, "outlineColorBlue3")
		self.on_trait_change(self.outline_changed3, "outlineToggle3")
		self.on_trait_change(self.contour_changed3, "contourOpacity3")
		self.on_trait_change(self.contour_changed3, "contourRepresentation3")
		self.on_trait_change(self.contour_changed3, "contourColormap3")
		self.on_trait_change(self.contour_changed3, "colormapMin3")
		self.on_trait_change(self.contour_changed3, "colormapMax3")
		
		self.on_trait_change(self.outline_changed4, "outlineWidth4")
		self.on_trait_change(self.outline_changed4, "outlineColorRed4")
		self.on_trait_change(self.outline_changed4, "outlineColorGreen4")
		self.on_trait_change(self.outline_changed4, "outlineColorBlue4")
		self.on_trait_change(self.outline_changed4, "outlineToggle4")
		self.on_trait_change(self.contour_changed4, "contourOpacity4")
		self.on_trait_change(self.contour_changed4, "contourRepresentation4")
		self.on_trait_change(self.contour_changed4, "contourColormap4")
		self.on_trait_change(self.contour_changed4, "colormapMin4")
		self.on_trait_change(self.contour_changed4, "colormapMax4")
		
		# allIsosurfaceOptions
		self.on_trait_change(self.threshold_changed1, "threshold1")
		self.on_trait_change(self.setThreshold_fired1, "setThreshold1")
		self.on_trait_change(self.threshold_changed1, "thresholdPercent1")
		self.on_trait_change(self.setThresholdPercent_fired1, "setThresholdPercent1")
		
		self.on_trait_change(self.threshold_changed2, "threshold2")
		self.on_trait_change(self.setThreshold_fired2, "setThreshold2")
		self.on_trait_change(self.threshold_changed2, "thresholdPercent2")
		self.on_trait_change(self.setThresholdPercent_fired2, "setThresholdPercent2")
		
		self.on_trait_change(self.threshold_changed3, "threshold3")
		self.on_trait_change(self.setThreshold_fired3, "setThreshold3")
		self.on_trait_change(self.threshold_changed3, "thresholdPercent3")
		self.on_trait_change(self.setThresholdPercent_fired3, "setThresholdPercent3")
		
		self.on_trait_change(self.threshold_changed4, "threshold4")
		self.on_trait_change(self.setThreshold_fired4, "setThreshold4")
		self.on_trait_change(self.threshold_changed4, "thresholdPercent4")
		self.on_trait_change(self.setThresholdPercent_fired4, "setThresholdPercent4")
		
		# allVolRenderingOptions
		self.on_trait_change(self.enableVolRenderingChanged, "enableVolRendering")
		
		# timeUpdateBehavior
		self.on_trait_change(self.time_changed1, "whichTime1")
		self.on_trait_change(self.time_changed2, "whichTime2")
		self.on_trait_change(self.time_changed3, "whichTime3")
		self.on_trait_change(self.time_changed4, "whichTime4")
		self.on_trait_change(self.time_changedGlobal, "whichTimeGlobal")
		
		# activeDataControlClass
		# self.on_trait_change(self.chkbox_changed1, "chkBox1")
		self.on_trait_change(self.sc1_ts1_changed1, "screen1_ts1")
		self.on_trait_change(self.sc2_ts1_changed1, "screen2_ts1")
		self.on_trait_change(self.sc3_ts1_changed1, "screen3_ts1")
		self.on_trait_change(self.sc4_ts1_changed1, "screen4_ts1")
		self.on_trait_change(self.radioButton1_changed, "radioButton1")
		self.on_trait_change(self.radioButton2_changed, "radioButton2")
		self.on_trait_change(self.radioButton3_changed, "radioButton3")
		self.on_trait_change(self.radioButton4_changed, "radioButton4")
		
		# Define dummy time series - TODO: move elsewhere to keep __init__ clean
		
		self._dataTs1 = np.zeros((3, 3, 3, 1), dtype = np.float32)
		self._dataTs2 = np.zeros((3, 3, 3, 1), dtype = np.float32)
		self._dataTs3 = np.zeros((3, 3, 3, 1), dtype = np.float32)
		self._dataTs4 = np.zeros((3, 3, 3, 1), dtype = np.float32)
		
		# Number of input time series
		self.nts = int(args[0])
		# self.nts = 4
		
		# Get data first
		self._dataTs1 = args[-1]
		self._dataTs2 = args[-1]
		self._dataTs3 = args[-1]
		self._dataTs4 = args[-1]
		
		# Check if data is 4d
		
		if not len(np.shape(self._dataTs1)) == 4:
			raise ValueError
		
		# Create time series range
		
		self.numTs1 = int(np.shape(self._dataTs1)[-1]-1)
		self.numTs2 = int(np.shape(self._dataTs2)[-1]-1)
		self.numTs3 = int(np.shape(self._dataTs3)[-1]-1)
		self.numTs4 = int(np.shape(self._dataTs4)[-1]-1)
		
		self.add_trait("whichTime1", Range(int(0.0), self.numTs1, int(0)))
		self.add_trait("whichTime2", Range(int(0.0), self.numTs2, int(0)))
		self.add_trait("whichTime3", Range(int(0.0), self.numTs3, int(0)))
		self.add_trait("whichTime4", Range(int(0.0), self.numTs4, int(0)))
		self.add_trait("whichTimeGlobal", Range(int(0.0), self.numTs1, int(0))) # This assumes all TS have same length
		
		# By default, choose the first time instance
		_data1 = self._dataTs1[:, :, :, 0]
		_data2 = self._dataTs2[:, :, :, 0]
		_data3 = self._dataTs3[:, :, :, 0]
		_data4 = self._dataTs4[:, :, :, 0]
		
		# Modify threshold range based on data
		# For some reason, Range doesn't like numpy float32
		# Using float instead
		self.add_trait("threshold1", Str(''))
		self.add_trait("thresholdPercent1", Str(''))
		self.add_trait("thresholdMinimum1", Float(np.floor(float(_data1.min()))))
		self.add_trait("thresholdMaximum1", Float(np.ceil(float(_data1.max()))))
		
		self.add_trait("threshold2", Str(''))
		self.add_trait("thresholdPercent2", Str(''))
		self.add_trait("thresholdMinimum2", Float(np.floor(float(_data2.min()))))
		self.add_trait("thresholdMaximum2", Float(np.ceil(float(_data2.max()))))
		
		self.add_trait("threshold3", Str(''))
		self.add_trait("thresholdPercent3", Str(''))
		self.add_trait("thresholdMinimum3", Float(np.floor(float(_data3.min()))))
		self.add_trait("thresholdMaximum3", Float(np.ceil(float(_data3.max()))))
		
		self.add_trait("threshold4", Str(''))
		self.add_trait("thresholdPercent4", Str(''))
		self.add_trait("thresholdMinimum4", Float(np.floor(float(_data4.min()))))
		self.add_trait("thresholdMaximum4", Float(np.ceil(float(_data4.max()))))
		
		# DATA 1
		
		self.x1 = args[1]
		self.y1 = args[2]
		self.z1 = args[3]

		# Plot the isosurface with minimum value from data
		self.sf1_sc1 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene1.mayavi_scene)
		self.sf1_sc2 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene2.mayavi_scene)
		self.sf1_sc3 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene3.mayavi_scene)
		self.sf1_sc4 = mlab.pipeline.scalar_field(self.x1, self.y1, self.z1, _data1, figure=self.scene4.mayavi_scene)
		
		# Set the threshold
		self.iso1_sc1 = mlab.pipeline.iso_surface(self.sf1_sc1, contours=[_data1.min()])
		self.iso1_sc2 = mlab.pipeline.iso_surface(self.sf1_sc2, contours=[_data1.min()])
		self.iso1_sc3 = mlab.pipeline.iso_surface(self.sf1_sc3, contours=[_data1.min()])
		self.iso1_sc4 = mlab.pipeline.iso_surface(self.sf1_sc4, contours=[_data1.min()])
		
		# Plot the outline
		self.out1_sc1 = mayavi.tools.pipeline.outline(self.iso1_sc1)
		self.out1_sc2 = mayavi.tools.pipeline.outline(self.iso1_sc2)
		self.out1_sc3 = mayavi.tools.pipeline.outline(self.iso1_sc3)
		self.out1_sc4 = mayavi.tools.pipeline.outline(self.iso1_sc4)
		
		# DATA 2
		
		self.x2 = args[1]
		self.y2 = args[2]
		self.z2 = args[3]

		# Plot the isosurface with minimum value from data
		self.sf2 = mlab.pipeline.scalar_field(self.x2, self.y2, self.z2, _data2, figure=self.scene1.mayavi_scene)
		
		# Set the threshold
		self.iso2 = mlab.pipeline.iso_surface(self.sf2, contours=[_data2.min()])
		
		# Plot the outline
		self.out2 = mayavi.tools.pipeline.outline(self.iso2)
		
		# DATA 3
		
		self.x3 = args[1]
		self.y3 = args[2]
		self.z3 = args[3]

		# Plot the isosurface with minimum value from data
		self.sf3 = mlab.pipeline.scalar_field(self.x3, self.y3, self.z3, _data3, figure=self.scene1.mayavi_scene)
		
		# Set the threshold
		self.iso3 = mlab.pipeline.iso_surface(self.sf3, contours=[_data3.min()])
		
		# Plot the outline
		self.out3 = mayavi.tools.pipeline.outline(self.iso3)
		
		# DATA 4
		
		self.x4 = args[1]
		self.y4 = args[2]
		self.z4 = args[3]

		# Plot the isosurface with minimum value from data
		self.sf4 = mlab.pipeline.scalar_field(self.x4, self.y4, self.z4, _data4, figure=self.scene1.mayavi_scene)
		
		# Set the threshold
		self.iso4 = mlab.pipeline.iso_surface(self.sf4, contours=[_data4.min()])
		
		# Plot the outline
		self.out4 = mayavi.tools.pipeline.outline(self.iso4)
		
		# By default, turn off other outlines
		self.out2.actor.actor.visibility = False
		self.out3.actor.actor.visibility = False
		self.out4.actor.actor.visibility = False
		
		# Set default contour representation
		self.contourRepresentation1 = 'surface'
		self.contourRepresentation2 = 'surface'
		self.contourRepresentation3 = 'surface'
		self.contourRepresentation4 = 'surface'
		
		# Set default contour colormap
		self.contourColormap1 = 'viridis'
		self.contourColormap2 = 'viridis'
		self.contourColormap3 = 'viridis'
		self.contourColormap4 = 'viridis'
		
		# Set checkbox1 by default 
		self.chkBox1 = True
		self.chkBox2 = False
		self.chkBox3 = False
		self.chkBox4 = False
		
		# Activate radiobutton1 by default
		self.radioButton1 = 'Y'
		self.radioButton2 = 'N'
		self.radioButton3 = 'N'
		self.radioButton4 = 'N'
		
		# Set outline color
		self.out1_sc1.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out1_sc2.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out1_sc3.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out1_sc4.actor.property.color = (self.outlineColorRed1, self.outlineColorGreen1, self.outlineColorBlue1)
		self.out2.actor.property.color = (self.outlineColorRed2, self.outlineColorGreen2, self.outlineColorBlue2)
		self.out3.actor.property.color = (self.outlineColorRed3, self.outlineColorGreen3, self.outlineColorBlue3)
		self.out4.actor.property.color = (self.outlineColorRed4, self.outlineColorGreen4, self.outlineColorBlue4)
		
		# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
		
		# Set background color for all scenes by default
		self.iso1_sc1.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc2.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc3.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso1_sc4.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso2.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso3.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		self.iso4.scene.background = (self.BGColorRed, self.BGColorGreen, self.BGColorBlue)
		
		# By default, set clamp to True if there are more than 1 TS
		if self.nts > 1:
			self.clamp = True
		else:
			self.clamp = False
		
		# By default, choose 1 screen
		self.layout = '1'
		
		# By default, choose screen 1 for all TS
		self.screen1_ts1 = True
		self.screen1_ts2 = True
		self.screen1_ts3 = True
		self.screen1_ts4 = True
				
	view = View(
	
	VGroup(
	HSplit(
	activeDataUIelements,
	sceneUIelements,
	VGroup(
	
	# Layout options
	Group(label = 'Screen layout:'),
	Item("layout", label = 'Number of split screens:', style='custom'),
	
	globalUIelements,
	localUIelements,
	isoUIelements,
	contourUIelements,
	)
	),
	cameraUIelements,
	),
	
	width=1, height=1, title='QuickViz')

