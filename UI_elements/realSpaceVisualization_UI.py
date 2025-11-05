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

realSpaceVisualizationUIelements = Group(

HGroup(
Item("LoadLLTxt", style = 'readonly', show_label = False, height = smallh, width = -100),
Item("LL_path", show_label = False, height = longh, width = longw),
Item("choose_folder_LLPath", show_label = False, height = buttonh, width = buttonw),
),

),

