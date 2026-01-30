from traitsui.api import VGroup, HSplit, Group, Item, HGroup, RangeEditor
from .UICustomization import UIOptionsClass
from .LLPlayground_UI import LLPlayGroundUIelements
from .fieldLines_UI import fieldLinesUIelements
from .slice_UI import sliceUIelements
from .structureExtraction_UI import structureExtractionUIelements
from .volumeRendering_UI import volumeRenderingUIelements
from .realSpaceVisualization_UI import realSpaceVisualizationUIelements
from .fieldLineTracking_UI import fieldLineTrackingUIelements
from .dataset_UI import datasetUIelements
from .duchonRobert_UI import duchonRobertUIelements
from .reconnection_UI import reconnectionUIelements

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

reconnectionQtensorVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Reconnection" or allAnalysisOptions == "Q-tensor")'
reconnectionQtensorBBoxVisibility = 'allModeOptions == "Analysis" and altBBox == True and (allAnalysisOptions == "Q-tensor" or allAnalysisOptions == "Reconnection")'

DRPressureVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Pressure" or allAnalysisOptions == "Duchon Robert")'
PressureVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Pressure"'

isoUIelements = (Group(

	# All mode options
	Group(
	Item("allModeOptions", label = 'Mode:')),
	
	# All data options
	
	datasetUIelements,
	
	# All analysis options
	Group(
	Item("allAnalysisOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Analysis"')
	),
	
	# Fieldline tracking
	fieldLineTrackingUIelements,
	
	# Reconnection
	
	reconnectionUIelements,
	
	# Q-tensor
	
	HGroup(
	Item("calculateQtensor", show_label = False, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Q-tensor"', height = buttonh, width = buttonw),
	),
	
	# Duchon Robert
	
	duchonRobertUIelements,
	
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
