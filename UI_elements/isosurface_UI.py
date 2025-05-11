from traitsui.api import VGroup, HSplit, Group, Item, HGroup
from .UICustomization import UIOptionsClass

# Initialize UI layout customization
allUIOptions = UIOptionsClass()
tinyw, tinyh = allUIOptions.textFieldTiny()
smallw, smallh = allUIOptions.textFieldSmall()
longw, longh = allUIOptions.textFieldLong()
sliderw, sliderh = allUIOptions.slider()
slidertinyw, slidertinyh = allUIOptions.slidertiny()
buttonw, buttonh = allUIOptions.button()
buttonLongw, buttonLongh = allUIOptions.buttonLong()

isoUIelements = (Group(Group(Item("allLocalOptions", show_label = False, style = 'custom')),
	
	# Group(Item("IsoOptionsTxt", show_label = False, visible_when = 'allLocalOptions == "Isosurface"', style = 'readonly')),
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly', visible_when='radioButton1 == "Y"'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:', visible_when='radioButton1 == "Y"'), style='readonly'),
	
	HGroup(Item("enableVolRendering", label = "Define options below and set:", visible_when = "allLocalOptions == 'Volume Rendering'"),),
	HGroup(
	Item("EnableShadowsTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='allLocalOptions == "Volume Rendering"'),
	Item("shade_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'"),
	),
	HGroup(
	Item("AmbientOcclusionsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering"'),
	Item("ambient_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("DiffuseReflectionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering"'),
	Item("diffuse_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("SpecularHighlightsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering"'),
	Item("specular_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	HGroup(
	Item("OpacityFallOffTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering"'),
	Item("opacityFallOff_volRender", show_label = False, visible_when = "allLocalOptions == 'Volume Rendering'", height = tinyh, width = tinyw),
	),
	
	HGroup(
	Item("ChooseSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='allLocalOptions == "Slice"'),
	Item("sliceType", show_label = False, visible_when = "allLocalOptions == 'Slice'"),
	),
	HGroup(
	Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Slice" and sliceType != "Contour slice" and sliceType != "None"'),
	Item("whichVector", show_label = False, visible_when = "allLocalOptions == 'Slice' and sliceType != 'Contour slice' and sliceType != 'None'", style = 'custom'),
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
	Item("kernelLengthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allLocalOptions == "Slice" and sliceType == "Streamlines"'),
	Item("kernelLengthSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Streamlines'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("noiseImageDimensionTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='allLocalOptions == "Slice" and sliceType == "Streamlines"'),
	Item("noiseImageDimensionSliceX", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Streamlines'", width = tinyw, height = tinyh),
	Item("noiseImageDimensionSliceY", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType == 'Streamlines'", width = tinyw, height = tinyh),
	),
	HGroup(
	Item("setSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='allLocalOptions == "Slice" and sliceType != "None"'),
	Item("enableSlice", show_label = False, visible_when = "allLocalOptions == 'Slice'  and sliceType != 'None'"),
	),
	
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum2", label = 'Minimum threshold:', style='readonly', visible_when='radioButton2 == "Y"'), 
	Item("thresholdMaximum2", label = ', Maximum threshold:', visible_when='radioButton2 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum3", label = 'Minimum threshold:', style='readonly', visible_when='radioButton3 == "Y"'), 
	Item("thresholdMaximum3", label = ', Maximum threshold:', visible_when='radioButton3 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum4", label = 'Minimum threshold:', style='readonly', visible_when='radioButton4 == "Y"'), 
	Item("thresholdMaximum4", show_label = False, visible_when='radioButton4 == "Y"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold4", label = 'Threshold(s)', visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	 
	show_border = True, orientation = 'vertical', scrollable = True)),
