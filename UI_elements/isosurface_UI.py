from traitsui.api import VGroup, HSplit, Group, Item, HGroup, RangeEditor
from .UICustomization import UIOptionsClass
from .LLPlayground_UI import LLPlayGroundUIelements
from .fieldLines_UI import fieldLinesUIelements
from .slice_UI import sliceUIelements
from .structureExtraction_UI import structureExtractionUIelements
from .volumeRendering_UI import volumeRenderingUIelements
from .realSpaceVisualization_UI import realSpaceVisualizationUIelements
from .fieldLineTracking_UI import fieldLineTrackingUIelements

# Initialize UI layout customization
allUIOptions = UIOptionsClass()
tinyw, tinyh = allUIOptions.textFieldTiny()
smallw, smallh = allUIOptions.textFieldSmall()
longw, longh = allUIOptions.textFieldLong()
hugew, hugeh = allUIOptions.textFieldHuge()
sliderw, sliderh = allUIOptions.slider()
slidertinyw, slidertinyh = allUIOptions.slidertiny()
buttonw, buttonh = allUIOptions.button()
buttonLongw, buttonLongh = allUIOptions.buttonLong()

reconnectionVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Reconnection"'
reconnectionQtensorVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Reconnection" or allAnalysisOptions == "Q-tensor"'
reconnectionQtensorBBoxVisibility = 'allModeOptions == "Analysis" and altBBox == True and (allAnalysisOptions == "Q-tensor" or allAnalysisOptions == "Reconnection")'

localDatasetVisibility = 'allModeOptions == "Dataset" and allDatasetOptions == "Local"'
localDatasetVisibilityBBox = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and altBBox == True'
localDatasetVisibilityRaw3D = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "Raw 3D"'
localDatasetVisibilitynetCDF = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "netCDF"'

DRVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Duchon Robert"'

isoUIelements = (Group(

	# All mode options
	Group(
	Item("allModeOptions", label = 'Mode:')),
	
	# All data options
	
	Group(
	Item("allDatasetOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Dataset"')
	),
	
	# Local data
	
	HGroup(
	Item("allLocalDatasetOptions", show_label = False, style = 'custom', visible_when = localDatasetVisibility)
	),
	
	HGroup(
	Item("LoadLocalDataTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when = localDatasetVisibility),
	Item("LocalData_path", show_label = False, height = longh, width = longw, visible_when = localDatasetVisibility),
	Item("choose_folder_LocalDataPath", show_label = False, height = buttonh, width = buttonw, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("assignTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("availableAttributesTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = localDatasetVisibilitynetCDF),
	Item("allAttributes", style = 'readonly', show_label = False, height = smallh, width = -1000, visible_when = localDatasetVisibilitynetCDF),
	),
	
	HGroup(
	Item("velxTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velxLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("velyTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velyLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("velzTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velzLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	
	HGroup(
	Item("adjustTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("minExtentTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("xmin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("ymin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zmin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),

	HGroup(
	Item("maxExtentTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = localDatasetVisibility),
	Item("xmax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("ymax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zmax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),

	HGroup(
	Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("xres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("yres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("timestepsTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when = localDatasetVisibility),
	Item("timeSteps_LocalData", style = 'readonly', show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("whichTimeStepLLTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = localDatasetVisibility),
	Item("timeStep_LocalData", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibility),
	Item("exampleTSTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("precisionTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilityRaw3D),
	Item("precision_LocalData", show_label = False, style = 'custom' , visible_when = localDatasetVisibilityRaw3D),
	),
	
	HGroup(
	Item("trimDatasetTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("altBBox", show_label = False, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	
	HGroup(
	Item("whichScalarTxt", style = 'readonly', height = smallh, width = -100, show_label = False, visible_when = localDatasetVisibility),
	Item("whichScalar_LocalData", show_label = False, visible_when = localDatasetVisibility),
	Item("load_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	Item("cancel_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	),
	
	# All analysis options
	Group(
	Item("allAnalysisOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Analysis"')
	),
	
	# Fieldline tracking
	fieldLineTrackingUIelements,
	
	# Reconnection
	HGroup(
	Item("altBBoxTxt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorVisibility, height = smallh, width = -170,),
	Item("altBBox", show_label = False, visible_when=reconnectionQtensorVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	
	HGroup(
	Item("calcAndPlotTxt", show_label = False, style = 'readonly', visible_when=reconnectionVisibility, height = smallh, width = -180,),
	Item("calcReconnection", show_label = False, visible_when=reconnectionVisibility, height = buttonh, width = buttonw),
	),
	
	# Q-tensor
	
	HGroup(
	Item("calculateQtensor", show_label = False, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Q-tensor"', height = buttonh, width = buttonw),
	),
	
	# Duchon Robert
	
	# cutoffTxt = Str('Prefactor (a):')
	# probedScaleTxt = Str('Probed Scale:')
	# probedScaleIdxTxt = Str('(integer values only)')
	# lcTxt = Str('l_c:')
	# etaTxt = Str('Kolmogorov scale:')
	# lcetaTxt = Str('l_c_eta:')
	# lcetaKolmogorovTxt = Str('(if eta is provided)')
	
	HGroup(
	Item("allDROptions", show_label = False, style = 'custom', format_func=lambda x: x, visible_when = DRVisibility)
	),
	
	HGroup(
	Item("cutoffTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = DRVisibility),
	Item("a_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRVisibility),
	),
	
	HGroup(
	Item("probedScaleTxt", style = 'readonly', show_label = False, height = tinyh, width = -100, visible_when = DRVisibility),
	Item("probedScale_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRVisibility),
	Item("probedScaleIdxTxt", style = 'readonly', show_label = False, height = tinyh, width = -150, visible_when = DRVisibility),
	),
	
	HGroup(
	Item("lcTxt", style = 'readonly', show_label = False, height = tinyh, width = -20, visible_when = DRVisibility),
	Item("l_c_DR", style = 'readonly', show_label = False, visible_when = DRVisibility),
	),
	
	HGroup(
	Item("etaTxt", style = 'readonly', show_label = False, height = tinyh, width = -120, visible_when = DRVisibility),
	Item("eta_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRVisibility),
	),
	
	HGroup(
	Item("lcetaTxt", style = 'readonly', show_label = False, height = tinyh, width = -50, visible_when = DRVisibility),
	Item("l_c_eta_DR", style = 'readonly', show_label = False, visible_when = DRVisibility),
	Item("lcetaKolmogorovTxt", style = 'readonly', show_label = False, height = tinyh, width = -120, visible_when = DRVisibility),
	),
	
	HGroup(
	Item("calculate_DR", show_label = False, visible_when = DRVisibility, height = buttonh, width = buttonw),
	Item("remove_DR", show_label = False, visible_when = DRVisibility, height = buttonh, width = buttonw),
	),
	
	# All Log lattice options
	Group(
	Item("allLLOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Log Lattice"')
	),
	
	# Log lattice - playground
	
	LLPlayGroundUIelements,
	
	# Structure extraction
	
	structureExtractionUIelements,
	
	# Real space visualization
	
	realSpaceVisualizationUIelements,
	
	# Group(Item("IsoOptionsTxt", show_label = False, visible_when = 'allLocalOptions == "Isosurface"', style = 'readonly')),
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), style='readonly'),
	
	# Volume rendering
	
	volumeRenderingUIelements,
	
	# Slice
	
	sliceUIelements,
	
	# Fieldlines
	
	fieldLinesUIelements,
	
	# Isosurface
	
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("threshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThreshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("thresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	HGroup(
	Item("colorFieldsTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("colorFields", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	
	HGroup(Item("thresholdMinimum2", label = 'Minimum threshold:', style='readonly', visible_when='radioButton2 == "Y"'), 
	Item("thresholdMaximum2", label = ', Maximum threshold:', visible_when='radioButton2 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("threshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThreshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("thresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum3", label = 'Minimum threshold:', style='readonly', visible_when='radioButton3 == "Y"'), 
	Item("thresholdMaximum3", label = ', Maximum threshold:', visible_when='radioButton3 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("threshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThreshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("thresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum4", label = 'Minimum threshold:', style='readonly', visible_when='radioButton4 == "Y"'), 
	Item("thresholdMaximum4", show_label = False, visible_when='radioButton4 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("threshold4", label = 'Threshold(s)', visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThreshold4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("thresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = longh, width = longw), 
	Item("setThresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"', height = buttonh, width = buttonw),
	),
	 
	show_border = True, orientation = 'vertical', scrollable = True)),
