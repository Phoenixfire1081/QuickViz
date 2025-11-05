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

sliceUIelements = Group(

HGroup(
Item("ChooseSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='allLocalOptions == "Slice" and allModeOptions == "Visualization"'),
Item("sliceType", show_label = False, visible_when = 'allLocalOptions == "Slice" and allModeOptions == "Visualization"'),
),
HGroup(
Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Slice" and sliceType != "Contour slice" and sliceType != "None" and allModeOptions == "Visualization"'),
Item("whichVector", show_label = False, visible_when = 'allLocalOptions == "Slice" and sliceType != "Contour slice" and sliceType != "None" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("whichScalarSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Slice" and sliceType == "Contour slice" and sliceType != "None" and allModeOptions == "Visualization"'),
Item("whichScalarSlice", show_label = False, visible_when = 'allLocalOptions == "Slice" and sliceType == "Contour slice" and sliceType != "None" and allModeOptions == "Visualization"'),
),
HGroup(
Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType != "None" and allModeOptions == "Visualization"'),
Item("planeOrientation", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType != "None" and allModeOptions == "Visualization"'),
Item("whichSliceX", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and planeOrientation == "X" and allModeOptions == "Visualization"', width = sliderw),
Item("whichSliceY", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and planeOrientation == "Y" and allModeOptions == "Visualization"', width = sliderw),
Item("whichSliceZ", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and planeOrientation == "Z" and allModeOptions == "Visualization"', width = sliderw),
),
HGroup(
Item("scaleFactorTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType == "Vector slice" and allModeOptions == "Visualization"'),
Item("scaleFactorSlice", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType == "Vector slice" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Slice" and sliceType == "Vector slice" and allModeOptions == "Visualization"'),
Item("resolutionSlice", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType == "Vector slice" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("kernelLengthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allLocalOptions == "Slice" and sliceType == "Fieldlines" and allModeOptions == "Visualization"'),
Item("kernelLengthSlice", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType == "Fieldlines" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("noiseImageDimensionTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='allLocalOptions == "Slice" and sliceType == "Fieldlines" and allModeOptions == "Visualization"'),
Item("noiseImageDimensionSliceX", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType == "Fieldlines" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
Item("noiseImageDimensionSliceY", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType == "Fieldlines" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("setSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='allLocalOptions == "Slice" and sliceType != "None" and allModeOptions == "Visualization"'),
Item("enableSlice", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and allModeOptions == "Visualization"'),
Item("removeSlice", show_label = False, visible_when = 'allLocalOptions == "Slice"  and sliceType != "None" and allModeOptions == "Visualization"'),
),

),
