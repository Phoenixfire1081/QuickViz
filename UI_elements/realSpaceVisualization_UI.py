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
buttonLongerw, buttonLongerh = allUIOptions.buttonLonger()

visibilityRSV = 'allModeOptions == "Log Lattice" and allLLOptions == "Real Space Visualization"'
visibilityLP = visibilityRSV + ' and filterOptions_LL == "Low-pass"'
visibilityBP = visibilityRSV + ' and filterOptions_LL == "Band-pass"'
visibilityHP = visibilityRSV + ' and filterOptions_LL == "High-pass"'
visibilityGauss = visibilityRSV + ' and filterOptions_LL == "Gaussian"'

realSpaceVisualizationUIelements = Group(

HGroup(
Item("LoadLLTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when = visibilityRSV),
Item("LL_path", show_label = False, height = longh, width = longw, visible_when = visibilityRSV),
Item("choose_folder_LLPath", show_label = False, height = buttonh, width = buttonw, visible_when = visibilityRSV),
),

HGroup(
Item("parametersTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = visibilityRSV),
),

HGroup(
Item("whichTimeStepLLTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = visibilityRSV),
Item("timeStep_LL", show_label = False, height = longh, width = longw , visible_when = visibilityRSV),
Item("exampleTSTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when = visibilityRSV),
),

HGroup(
Item("minExtentTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = visibilityRSV),
Item("xmin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("ymin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("zmin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
),

HGroup(
Item("maxExtentTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = visibilityRSV),
Item("xmax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("ymax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("zmax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
),

HGroup(
Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = visibilityRSV),
Item("xres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("yres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
Item("zres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = visibilityRSV),
),

HGroup(
Item("samplingPointsTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when = visibilityRSV),
Item("samplingPoints_LL", style = 'custom', show_label = False, visible_when = visibilityRSV),
),

HGroup(
Item("filterOptionsTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when = visibilityRSV),
Item("filterOptions_LL", show_label = False, visible_when = visibilityRSV),
),

HGroup(
Item("whichScalarTxt", style = 'readonly', height = smallh, width = -100, show_label = False, visible_when = visibilityRSV),
Item("whichScalar_LL", show_label = False, visible_when = visibilityRSV),
Item("computeLL", height = buttonh, width = buttonw, show_label = False, visible_when = visibilityRSV),
),

),

