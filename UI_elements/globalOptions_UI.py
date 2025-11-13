from traitsui.api import VGroup, HSplit, Group, Item, HGroup, RangeEditor
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

globalUIelements = (Group(label = 'Global options:'),
Group(
Group(label = 'Background options:'),
HGroup(Item("BGtext", style='readonly', show_label=False, height = smallh, width = -120), 
Item("BGColorRed", show_label = False, height = tinyh, width = tinyw),
Item("BGColorGreen", show_label = False, height = tinyh, width = tinyw),
Item("BGColorBlue", show_label = False, height = tinyh, width = tinyw),
),

# Time options

Group(label = 'Time step control:'),

HGroup(Item("TStext", style = 'readonly', show_label = False, height = smallh, width = -80),
Item("whichTime1", show_label = False, editor=RangeEditor(mode='slider', low_name = 'includeEmptySpace',  high_name='ts1max'), visible_when = 'radioButton1 == "Y" and clamp == 0', width = sliderw),
# Item("whichTime1", label = '1', visible_when='radioButton1 == "Y" and clamp == 0', width = sliderw), 
Item("whichTime2", label = '2', visible_when='radioButton2 == "Y" and clamp == 0', width = sliderw), 
Item("whichTime3", show_label = False, visible_when='radioButton3 == "Y" and clamp == 0', width = sliderw), 
Item("whichTime4", show_label = False, visible_when='radioButton4 == "Y" and clamp == 0', width = sliderw),
Item("whichTimeGlobal", label = 'G', visible_when='clamp == 1'),
Item("clamp", label = 'All TS?', visible_when='nts > 1'),
),

Group(label = 'Animation:'),

HGroup(Item("next_timeSeries", show_label = False, height = buttonh, width = buttonw),
Item("previous_timeSeries", show_label = False, height = buttonh, width = buttonw),
Item("play_timeSeries", show_label = False, height = buttonh, width = buttonw),
Item("play_timeSeries_reverse", show_label = False, height = buttonh, width = buttonw),
Item("stop_timeSeries", show_label = False, height = buttonh, width = buttonw),
Item("save_snapshot", show_label = False, height = buttonLongh, width = buttonLongw),
),

HGroup(Item("SaveTxt", style = 'readonly', show_label = False, height = smallh, width = -100),
Item("save_path", show_label = False, height = longh, width = longw),
Item("choose_folder", show_label = False, height = buttonh, width = buttonw),
),
HGroup(Item("StartTxt", style = 'readonly', show_label = False, height = smallh, width = -30),
Item("startMovie", show_label = False, height = tinyh, width = tinyw),
Item("StopTxt", style = 'readonly', show_label = False, height = smallh, width = -30),
Item("stopMovie", show_label = False, height = tinyh, width = tinyw),
Item("FRTxt", style = 'readonly', show_label = False, height = smallh, width = -80),
Item("framerate", show_label = False, height = tinyh, width = tinyw),
Item("SaveImgTxt", style = 'readonly', show_label = False, height = smallh, width = -90),
Item("save_images", show_label = False),
Item("save_timeSeries", show_label = False, height = buttonLongh, width = buttonLongw),
),

# Camera path

Group(label = 'Animate camera path:'),

HGroup(Item("camPathType", show_label = False),
Item("StartTxt", style = 'readonly', show_label = False, height = smallh, width = -30, visible_when = 'camPathType != "None"'),
Item("startCamPath", show_label = False, height = tinyh, width = tinyw, visible_when = 'camPathType != "None"'),
Item("StopTxt", style = 'readonly', show_label = False, height = smallh, width = -30, visible_when = 'camPathType != "None"'),
Item("stopCamPath", show_label = False, height = tinyh, width = tinyw, visible_when = 'camPathType != "None"'),
Item("addCamPath", show_label = False, height = buttonh, width = buttonw, visible_when = 'camPathType != "None"'),
Item("finishCamPath", show_label = False, height = buttonh, width = buttonw, visible_when = 'camPathType != "None"'),
Item("resetCamPath", show_label = False, height = buttonh, width = buttonw, visible_when = 'camPathType != "None"'),
),

show_border = True, orientation = 'vertical', scrollable = True),),
