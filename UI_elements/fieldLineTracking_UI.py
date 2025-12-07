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

visibilityFLTM_fl1 = visibilityFLT + ' and trackingOptions_fl1 == "Manual"'
visibilityFLTMM_fl1 = visibilityFLT + ' and trackingOptions_fl2 == "Manual" and Mirror_fl1 == True'
visibilityFLTT_fl1 = visibilityFLT + ' and trackingOptions_fl1 == "Auto"'

visibilityFLTX_fl1 = visibilityFLTT_fl1 + ' and planeOrientation_fl1 == "X"'
visibilityFLTY_fl1 = visibilityFLTT_fl1 + ' and planeOrientation_fl1 == "Y"'
visibilityFLTZ_fl1 = visibilityFLTT_fl1 + ' and planeOrientation_fl1 == "Z"'

visibilityFLTM_fl2 = visibilityFLT + ' and trackingOptions_fl2 == "Manual"'
visibilityFLTMM_fl2 = visibilityFLT + ' and trackingOptions_fl2 == "Manual" and Mirror_fl2 == True'
visibilityFLTT_fl2 = visibilityFLT + ' and trackingOptions_fl2 == "Auto"'

visibilityFLTX_fl2 = visibilityFLTT_fl2 + ' and planeOrientation_fl2 == "X"'
visibilityFLTY_fl2 = visibilityFLTT_fl2 + ' and planeOrientation_fl2 == "Y"'
visibilityFLTZ_fl2 = visibilityFLTT_fl2 + ' and planeOrientation_fl2 == "Z"'



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
Item("mirrorTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("Mirror_fl1", show_label = False, visible_when=visibilityFLT),
),

HGroup(
Item("trackingTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when=visibilityFLT),
Item("trackingOptions_fl1", show_label = False, visible_when = visibilityFLT, style = 'custom'),
),

HGroup(
Item("positionTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLTM_fl1),
Item("fl1_xpos", show_label = False, visible_when=visibilityFLTM_fl1, height = tinyh, width = tinyw),
Item("fl1_ypos", show_label = False, visible_when=visibilityFLTM_fl1, height = tinyh, width = tinyw),
Item("fl1_zpos", show_label = False, visible_when=visibilityFLTM_fl1, height = tinyh, width = tinyw),
),

HGroup(
Item("positionAltTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLTM_fl2),
Item("fl1_xposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl1_yposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl1_zposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
),

HGroup(
Item("whichScalarSliceflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLTT_fl1),
Item("whichScalarSlice_fl1", show_label = False, visible_when=visibilityFLTT_fl1),
),

HGroup(
Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when=visibilityFLTT_fl1),
Item("planeOrientation_fl1", show_label = False, visible_when=visibilityFLTT_fl1, style = 'custom'),
),

HGroup(
Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLTT_fl1),
Item("whichSliceX_fl1", show_label = False, visible_when = visibilityFLTX_fl1, width = sliderw),
Item("whichSliceY_fl1", show_label = False, visible_when = visibilityFLTY_fl1, width = sliderw),
Item("whichSliceZ_fl1", show_label = False, visible_when = visibilityFLTZ_fl1, width = sliderw),
),

HGroup(
Item("ThresholdPercentflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLTT_fl1),
Item("thresholdPercent1_fl1", show_label = False, visible_when=visibilityFLTT_fl1, height = longh, width = longw), 
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
Item("mirrorTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLT),
Item("Mirror_fl2", show_label = False, visible_when=visibilityFLT),
),

HGroup(
Item("trackingTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when=visibilityFLT),
Item("trackingOptions_fl2", show_label = False, visible_when = visibilityFLT, style = 'custom'),
),

HGroup(
Item("positionTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLTM_fl2),
Item("fl2_xpos", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl2_ypos", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl2_zpos", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
),

HGroup(
Item("positionAltTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=visibilityFLTM_fl2),
Item("fl2_xposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl2_yposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
Item("fl2_zposm", show_label = False, visible_when=visibilityFLTM_fl2, height = tinyh, width = tinyw),
),

HGroup(
Item("whichScalarSliceflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLTT_fl2),
Item("whichScalarSlice_fl2", show_label = False, visible_when=visibilityFLTT_fl2),
),

HGroup(
Item("planeOrientationTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when=visibilityFLTT_fl2),
Item("planeOrientation_fl2", show_label = False, visible_when=visibilityFLTT_fl2, style = 'custom'),
),

HGroup(
Item("whichSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=visibilityFLTT_fl2),
Item("whichSliceX_fl2", show_label = False, visible_when = visibilityFLTX_fl2, width = sliderw),
Item("whichSliceY_fl2", show_label = False, visible_when = visibilityFLTY_fl2, width = sliderw),
Item("whichSliceZ_fl2", show_label = False, visible_when = visibilityFLTZ_fl2, width = sliderw),
),

HGroup(
Item("ThresholdPercentflTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when=visibilityFLTT_fl2),
Item("thresholdPercent1_fl2", show_label = False, visible_when=visibilityFLTT_fl2, height = longh, width = longw), 
Item("setThresholdPercent1_fl2", show_label = False, visible_when=visibilityFLT, height = buttonh, width = buttonw),
),

),
