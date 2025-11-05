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

fieldLinesUIelements = Group(

HGroup(
Item("whichVectorTxt", style = 'readonly', show_label = False, height = smallh, width = -50, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("whichVector", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("seedTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("seedType", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("seedScaleTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("seedScale", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("seedResolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("seedResolution", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("seedRegionVisibleTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("seedRegionVisible", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
),
HGroup(
Item("lineTypeTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("lineType", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("lineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("lineWidth", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', width = tinyw, height = tinyh),
),
HGroup(
Item("integrationDirectionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("integrationDirection", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"', style = 'custom'),
),
HGroup(
Item("setSliceTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("enableStreamlines", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
Item("removeStreamlines", show_label = False, visible_when = 'allLocalOptions == "Fieldlines (3D)" and allModeOptions == "Visualization"'),
),

),
