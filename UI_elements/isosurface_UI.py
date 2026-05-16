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
from .duchonRobert_UI import duchonRobertPressureUIelements
from .reconnection_UI import reconnectionUIelements
from .blenderExport_UI import blenderExportUIelements

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
determine_width = allUIOptions.determineWidth

reconnectionQtensorVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Reconnection" or allAnalysisOptions == "Q-tensor")'
reconnectionQtensorBBoxVisibility = 'allModeOptions == "Analysis" and altBBox == True and (allAnalysisOptions == "Q-tensor" or allAnalysisOptions == "Reconnection")'
pdfVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Plots"'
trackingAll = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure Tracking" and totalNumberOfExtractedStructures == 0'
trackingBasicOverlap = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure Tracking" and not totalNumberOfExtractedStructures == 0'
trackingBasicOverlapStructure = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure Tracking" and chooseStructure > 0 and not totalNumberOfExtractedStructures == 0'

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
	
	# Structure tracking
	
	Group(
	Item("allStructureTrackingOptions", show_label = False, style = 'custom', format_func=lambda x: x, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure Tracking"')
	),
	HGroup(
	Item("structureExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Run structure extraction first"), visible_when = trackingAll),
	),
	HGroup(
	Item("chooseStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Select structure:"), visible_when = trackingBasicOverlap),
	Item("chooseStructure", show_label = False, editor=RangeEditor(mode='slider', low_name = 'includeEmptySpace',  high_name='totalNumberOfExtractedStructures'), visible_when = trackingBasicOverlap),
	),
	HGroup(
	Item("overlapPercentageTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Overlap percentage:"), visible_when = trackingBasicOverlap),
	Item("overlapPercentage", show_label = False, height = tinyh, width = tinyw, visible_when = trackingBasicOverlap),
	),
	HGroup(
	Item("SaveTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Save location:'), visible_when = trackingBasicOverlap),
	Item("save_path", show_label = False, height = longh, width = longw, visible_when = trackingBasicOverlap),
	Item("choose_folder", show_label = False, height = buttonh, width = buttonw, visible_when = trackingBasicOverlap),
	),
	HGroup(
	Item("folderNameExportTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Folder name:'), visible_when = trackingBasicOverlap),
	Item("folderNameExport", show_label = False, height = smallh, width = smallw, visible_when = trackingBasicOverlap),
	),
	HGroup(
	Item("whichTimeStepLLTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Which time step (s):'), visible_when = trackingBasicOverlap),
	Item("timeStep_LocalData", show_label = False, height = longh, width = longw , visible_when = trackingBasicOverlap),
	Item("exampleTSTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('(ex:1 or 3-6 or 1-100-10)'), visible_when = trackingBasicOverlap),
	),
	HGroup(
	Item("trackNow", show_label = False, height = buttonh, width = determine_width("Track selected structure"), visible_when = trackingBasicOverlapStructure),
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
	
	duchonRobertPressureUIelements,
	
	# PDF
	
	HGroup(
	Item("generatePDFTxt", style = 'readonly', show_label = False, height = tinyh, width = determine_width("Generate PDF plot:"), visible_when = pdfVisibility),
	Item("generatePDF", show_label = False, visible_when = pdfVisibility),
	),
	
	# All BS options
	Group(
	Item("allBSOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Biot-Savart"')
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
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), style='readonly'),
	
	# Volume rendering
	
	volumeRenderingUIelements,
	
	# Slice
	
	sliceUIelements,
	
	# Fieldlines
	
	fieldLinesUIelements,
	
	# Blender export
	
	blenderExportUIelements,
	
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
	Item("changeThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("changeThreshold1", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	HGroup(
	Item("finalThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True'),
	Item("finalThreshold", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True', height = longh, width = tinyw),
	Item("finalThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True'),
	Item("finalThresholdPercent", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True', height = longh, width = tinyw),
	Item("finalTimeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True'),
	Item("finalTime", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True', height = longh, width = tinyw),
	Item("changeThresholdTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -40, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True'),
	Item("changeThresholdType", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold1 == True'),
	),
	HGroup(
	Item("colorFieldsTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("colorFields1", show_label = False, visible_when = 'radioButton1 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
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
	HGroup(
	Item("changeThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("changeThreshold2", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	HGroup(
	Item("finalThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True'),
	Item("finalThreshold", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True', height = longh, width = tinyw),
	Item("finalThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True'),
	Item("finalThresholdPercent", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True', height = longh, width = tinyw),
	Item("finalTimeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True'),
	Item("finalTime", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True', height = longh, width = tinyw),
	Item("changeThresholdTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -40, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True'),
	Item("changeThresholdType", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold2 == True'),
	),
	HGroup(
	Item("colorFieldsTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("colorFields2", show_label = False, visible_when = 'radioButton2 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
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
	HGroup(
	Item("changeThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("changeThreshold3", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	HGroup(
	Item("finalThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True'),
	Item("finalThreshold", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True', height = longh, width = tinyw),
	Item("finalThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True'),
	Item("finalThresholdPercent", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True', height = longh, width = tinyw),
	Item("finalTimeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True'),
	Item("finalTime", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True', height = longh, width = tinyw),
	Item("changeThresholdTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -40, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True'),
	Item("changeThresholdType", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold3 == True'),
	),
	HGroup(
	Item("colorFieldsTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("colorFields3", show_label = False, visible_when = 'radioButton3 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
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
	HGroup(
	Item("changeThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("changeThreshold4", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	HGroup(
	Item("finalThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True'),
	Item("finalThreshold", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True', height = longh, width = tinyw),
	Item("finalThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True'),
	Item("finalThresholdPercent", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True', height = longh, width = tinyw),
	Item("finalTimeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True'),
	Item("finalTime", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True', height = longh, width = tinyw),
	Item("changeThresholdTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -40, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True'),
	Item("changeThresholdType", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization" and changeThreshold4 == True'),
	),
	HGroup(
	Item("colorFieldsTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	Item("colorFields4", show_label = False, visible_when = 'radioButton4 == "Y" and allLocalOptions == "Isosurface" and allModeOptions == "Visualization"'),
	),
	 
	show_border = True, orientation = 'vertical', scrollable = True)
	),
