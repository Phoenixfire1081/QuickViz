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

volumeRenderingUIelements = Group(

HGroup(
Item("enableVolRendering", label = "Define options below and set:", visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("removeVolRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
),
HGroup(
Item("EnableShadowsTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("shade_volRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
),
HGroup(
Item("AmbientOcclusionsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("ambient_volRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"', height = tinyh, width = tinyw),
),
HGroup(
Item("DiffuseReflectionTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("diffuse_volRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"', height = tinyh, width = tinyw),
),
HGroup(
Item("SpecularHighlightsTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("specular_volRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"', height = tinyh, width = tinyw),
),
HGroup(
Item("OpacityFallOffTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"'),
Item("opacityFallOff_volRender", show_label = False, visible_when = 'allLocalOptions == "Volume Rendering" and allModeOptions == "Visualization"', height = tinyh, width = tinyw),
),

),
