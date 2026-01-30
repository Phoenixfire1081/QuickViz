from traitsui.api import VGroup, HSplit, Group, Item, HGroup, RangeEditor
from .UICustomization import UIOptionsClass

# Initialize UI layout customization
allUIOptions = UIOptionsClass()
tinyw, tinyh = allUIOptions.textFieldTiny()
tinyww, _ = allUIOptions.textFieldTinySmallWidth()
smallw, smallh = allUIOptions.textFieldSmall()
longw, longh = allUIOptions.textFieldLong()
hugew, hugeh = allUIOptions.textFieldHuge()
sliderw, sliderh = allUIOptions.slider()
slidertinyw, slidertinyh = allUIOptions.slidertiny()
buttonw, buttonh = allUIOptions.button()
buttonLongw, buttonLongh = allUIOptions.buttonLong()

activeDataUIelements = Group(
	Group(Group(label = 'Active data'),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts1", show_label = False, visible_when='nts >= 1 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts1", show_label = False, visible_when='nts >= 1 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts1", show_label = False, visible_when='nts >= 1 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts1", show_label = False, visible_when='nts >= 1 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries1Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 1 and numTs1 > 0'),
	Item("vectorField1Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 1 and numTs1 == 0'),
	Item("radioButton1", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 1 and numTs1 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts2", show_label = False, visible_when='nts >= 2 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts2", show_label = False, visible_when='nts >= 2 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts2", show_label = False, visible_when='nts >= 2 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts2", show_label = False, visible_when='nts >= 2 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries2Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 2 and numTs2 > 0'),
	Item("vectorField2Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 2 and numTs2 == 0'),
	Item("radioButton2", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 2 and numTs2 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts3", show_label = False, visible_when='nts >= 3 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts3", show_label = False, visible_when='nts >= 3 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts3", show_label = False, visible_when='nts >= 3 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts3", show_label = False, visible_when='nts >= 3 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries3Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 3 and numTs3 > 0'),
	Item("vectorField3Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 3 and numTs3 == 0'),
	Item("radioButton3", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 3 and numTs3 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts4", show_label = False, visible_when='nts >= 4 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts4", show_label = False, visible_when='nts >= 4 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts4", show_label = False, visible_when='nts >= 4 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts4", show_label = False, visible_when='nts >= 4 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries4Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 4 and numTs4 > 0'),
	Item("vectorField4Txt", style = 'readonly', show_label = False, height = tinyh, width = -130, visible_when = 'nts >= 4 and numTs4 == 0'),
	Item("radioButton4", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 4 and numTs4 > 0'),
	),
	show_border = True, orientation = 'vertical', scrollable = True),
	),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
