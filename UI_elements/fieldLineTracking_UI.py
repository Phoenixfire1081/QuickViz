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

visibilityFLT = 'allModeOptions == "Analysis" and allAnalysisOptions == "Fieldline tracking"'
visibilityFLTX_fl1 = visibilityFLT + ' and planeOrientation_fl1 == "X"'
visibilityFLTY_fl1 = visibilityFLT + ' and planeOrientation_fl1 == "Y"'
visibilityFLTZ_fl1 = visibilityFLT + ' and planeOrientation_fl1 == "Z"'
visibilityFLTX_fl2 = visibilityFLT + ' and planeOrientation_fl2 == "X"'
visibilityFLTY_fl2 = visibilityFLT + ' and planeOrientation_fl2 == "Y"'
visibilityFLTZ_fl2 = visibilityFLT + ' and planeOrientation_fl2 == "Z"'

fieldLineTrackingUIelements = Group(

HGroup(
Item("trackFieldLinesTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = visibilityFLT),
),

HGroup(
Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -50, visible_when=visibilityFLT),
Item("whichVector_flt", show_label = False, visible_when = visibilityFLT, style = 'custom'),
),

HGroup(
Item("fieldLine1Txt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = visibilityFLT),
),

HGroup(
Item("seedScaleTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLT),
Item("seedScale_fl1", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("seedResolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("seedResolution_fl1", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("seedRegionVisibleTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when=visibilityFLT),
Item("seedRegionVisible_fl1", show_label = False, visible_when = visibilityFLT),
),

HGroup(
Item("lineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when=visibilityFLT),
Item("lineWidth_fl1", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("colorFLTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("red_fl1", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw),
Item("green_fl1", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw),
Item("blue_fl1", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw)
),

HGroup(
Item("whichScalarSliceflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("whichScalarSlice_fl1", show_label = False, visible_when=visibilityFLT),
),

HGroup(
Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when=visibilityFLT),
Item("planeOrientation_fl1", show_label = False, visible_when=visibilityFLT, style = 'custom'),
),

HGroup(
Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("whichSliceX_fl1", show_label = False, visible_when = visibilityFLTX_fl1, width = sliderw),
Item("whichSliceY_fl1", show_label = False, visible_when = visibilityFLTY_fl1, width = sliderw),
Item("whichSliceZ_fl1", show_label = False, visible_when = visibilityFLTZ_fl1, width = sliderw),
),

HGroup(
Item("ThresholdPercentflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("thresholdPercent1_fl1", show_label = False, visible_when=visibilityFLT, height = longh, width = longw), 
Item("setThresholdPercent1_fl1", show_label = False, visible_when=visibilityFLT, height = buttonh, width = buttonw),
),

HGroup(
Item("fieldLine2Txt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = visibilityFLT),
),

HGroup(
Item("seedScaleTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLT),
Item("seedScale_fl2", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("seedResolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("seedResolution_fl2", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("seedRegionVisibleTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when=visibilityFLT),
Item("seedRegionVisible_fl2", show_label = False, visible_when = visibilityFLT),
),

HGroup(
Item("lineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when=visibilityFLT),
Item("lineWidth_fl2", show_label = False, visible_when = visibilityFLT, width = tinyw, height = tinyh),
),

HGroup(
Item("colorFLTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("red_fl2", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw),
Item("green_fl2", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw),
Item("blue_fl2", show_label = False, visible_when=visibilityFLT, height = tinyh, width = tinyw)
),

HGroup(
Item("whichScalarSliceflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("whichScalarSlice_fl2", show_label = False, visible_when=visibilityFLT),
),

HGroup(
Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when=visibilityFLT),
Item("planeOrientation_fl2", show_label = False, visible_when=visibilityFLT, style = 'custom'),
),

HGroup(
Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLT),
Item("whichSliceX_fl2", show_label = False, visible_when = visibilityFLTX_fl2, width = sliderw),
Item("whichSliceY_fl2", show_label = False, visible_when = visibilityFLTY_fl2, width = sliderw),
Item("whichSliceZ_fl2", show_label = False, visible_when = visibilityFLTZ_fl2, width = sliderw),
),

HGroup(
Item("ThresholdPercentflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("thresholdPercent1_fl2", show_label = False, visible_when=visibilityFLT, height = longh, width = longw), 
Item("setThresholdPercent1_fl2", show_label = False, visible_when=visibilityFLT, height = buttonh, width = buttonw),
),

),
