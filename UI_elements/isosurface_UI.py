from traitsui.api import VGroup, HSplit, Group, Item, HGroup, RangeEditor
from .UICustomization import UIOptionsClass

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

isoUIelements = (Group(

	# All mode options
	Group(
	Item("allModeOptions", label = 'Mode:')),
	
	# All analysis options
	Group(
	Item("allAnalysisOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Analysis"')
	),
	
	HGroup(Item("calculateQtensor", show_label = False, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Q-tensor"', height = buttonh, width = buttonw),),
	
	# All Log lattice options
	Group(
	Item("allLLOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Log Lattice"')
	),
	
	# Log lattice - playground
	Group(
	Item("allPlaygroundOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"')
	),
	
	HGroup(Item("defineStructureTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),),
	HGroup(Item("defineStructureDescriptionVorticityTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),),
	HGroup(Item("defineStructureDescriptionVelocityTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),),
	HGroup(Item("initCondition1", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = hugeh, width = hugew),),
	
	HGroup(
	Item("GenerateStructure", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = buttonh, width = buttonw),
	Item("ResetStructure", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = buttonh, width = buttonw),
	),
	
	# Structure extraction
	
	HGroup(
	Item("thresholdExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	Item("thresholdExtractionSet", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = longh, width = longw),
	),
	HGroup(
	Item("verboseStructureExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	Item("verboseStructureExtraction", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	),
	HGroup(
	Item("useMarchingCubesTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	Item("useMarchingCubes", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = longh, width = longw),
	),
	HGroup(
	Item("extractStructures", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = buttonh, width = buttonw),
	),
	HGroup(
	Item("totalNumberOfExtractedStructuresTxt", style = 'readonly', show_label = False, height = smallh, width = -230, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	Item("totalNumberOfExtractedStructures", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	),
	HGroup(
	Item("chooseStructureTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	Item("chooseStructure", show_label = False, editor=RangeEditor(mode='slider', low_name = 'includeEmptySpace',  high_name='totalNumberOfExtractedStructures'), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
	),
	HGroup(
	Item("structInfoTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	),
	HGroup(
	Item("extentIdxTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structXminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structXmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structYminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structYmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structZminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structZmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	),
	HGroup(
	Item("extentActTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structXminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structXmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structYminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structYmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structZminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structZmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	),
	HGroup(
	Item("structVolTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	Item("structVolume", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
	),
	Group(
	Item("allLocalOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Visualization"')
	),
	
	# Group(Item("IsoOptionsTxt", show_label = False, visible_when = 'allLocalOptions == "Isosurface"', style = 'readonly')),
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:', visible_when='radioButton1 == "Y" and allModeOptions == "Visualization"'), style='readonly'),
	
	# Volume rendering
	
	HGroup(
	Item("enableVolRendering", label = "Define options below and set:", visible_when = "allLocalOptions == 'Volume Rendering'"),
	Item("removeVolRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'"),
	),
	HGroup(
	Item("EnableShadowsTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when="allLocalOptions == 'Volume Rendering'"),
	Item("shade_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'"),
	),
	HGroup(
	Item("AmbientOcclusionsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when="allLocalOptions == 'Volume Rendering'"),
	Item("ambient_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("DiffuseReflectionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when="allLocalOptions == 'Volume Rendering'"),
	Item("diffuse_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("SpecularHighlightsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when="allLocalOptions == 'Volume Rendering'"),
	Item("specular_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("OpacityFallOffTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when="allLocalOptions == 'Volume Rendering'"),
	Item("opacityFallOff_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	
	# Slice
	
	HGroup(
	Item("ChooseSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='allLocalOptions == "Slice"'),
	Item("sliceType", show_label = False, visible_when = "allLocalOptions == 'Slice'"),
	),
	HGroup(
	Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Slice" and sliceType != "Contour slice" and sliceType != "None"'),
	Item("whichVector", show_label = False, visible_when = "allLocalOptions == 'Slice' and sliceType != 'Contour slice' and sliceType != 'None'", style = 'custom'),
	),
	HGroup(
	Item("whichScalarSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Slice" and sliceType == "Contour slice" and sliceType != "None"'),
	Item("whichScalarSlice", show_label = False, visible_when = "allLocalOptions == 'Slice' and sliceType == 'Contour slice' and sliceType != 'None'"),
	),
	HGroup(
	Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType != "None"'),
	Item("planeOrientation", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None'", style = 'custom'),
	),
	HGroup(
	Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType != "None"'),
	Item("whichSliceX", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None' and planeOrientation == 'X'", width = sliderw),
	Item("whichSliceY", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None' and planeOrientation == 'Y'", width = sliderw),
	Item("whichSliceZ", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None' and planeOrientation == 'Z'", width = sliderw),
	),
	HGroup(
	Item("scaleFactorTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType == "Vector slice"'),
	Item("scaleFactorSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Vector slice'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType == "Vector slice"'),
	Item("resolutionSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Vector slice'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("kernelLengthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allLocalOptions == "Slice" and sliceType == "Fieldlines"'),
	Item("kernelLengthSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Fieldlines'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("noiseImageDimensionTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='allLocalOptions == "Slice" and sliceType == "Fieldlines"'),
	Item("noiseImageDimensionSliceX", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Fieldlines'", width = tinyw, height = tinyh),
	Item("noiseImageDimensionSliceY", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Fieldlines'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("setSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='allLocalOptions == "Slice" and sliceType != "None"'),
	Item("enableSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None'"),
	Item("removeSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None'"),
	),
	
	# Fieldlines
	HGroup(
	Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -50, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("whichVector", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", style = 'custom'),
	),
	HGroup(
	Item("seedTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("seedType", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", style = 'custom'),
	),
	HGroup(
	Item("seedScaleTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("seedScale", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("seedResolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("seedResolution", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("seedRegionVisibleTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("seedRegionVisible", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'"),
	),
	HGroup(
	Item("lineTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("lineType", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", style = 'custom'),
	),
	HGroup(
	Item("lineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("lineWidth", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("integrationDirectionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("integrationDirection", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'", style = 'custom'),
	),
	HGroup(
	Item("setSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='allLocalOptions == "Fieldlines (3D)"'),
	Item("enableStreamlines", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'"),
	Item("removeStreamlines", show_label = False, visible_when = "allLocalOptions == 'Fieldlines (3D)'"),
	),
	
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
