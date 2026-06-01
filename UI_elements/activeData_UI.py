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
determine_width = allUIOptions.determineWidth

activeDataUIelements = Group(
	Group(Group(label = 'Active data'),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts1", show_label = False, visible_when='nts >= 1 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts1", show_label = False, visible_when='nts >= 1 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts1", show_label = False, visible_when='nts >= 1 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts1", show_label = False, visible_when='nts >= 1 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector time series 1: '), visible_when = 'nts >= 1 and ts1Type == "VectorTs"'),
	Item("vectorField1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector field 1: '), visible_when = 'nts >= 1 and ts1Type == "VectorF"'),
	Item("StimeSeries1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar time series 1: '), visible_when = 'nts >= 1 and ts1Type == "ScalarTs"'),
	Item("scalarField1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar field 1: '), visible_when = 'nts >= 1 and ts1Type == "ScalarF"'),
	Item("LTimeSeries1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian time series 1: '), visible_when = 'nts >= 1 and ts1Type == "LagrangianTs"'),
	Item("L1Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian field 1: '), visible_when = 'nts >= 1 and ts1Type == "Lagrangian"'),
	Item("radioButton1", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 1 and numTs1 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts2", show_label = False, visible_when='nts >= 2 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts2", show_label = False, visible_when='nts >= 2 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts2", show_label = False, visible_when='nts >= 2 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts2", show_label = False, visible_when='nts >= 2 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector time series 2: '), visible_when = 'nts >= 2 and ts2Type == "VectorTs"'),
	Item("vectorField2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector field 2: '), visible_when = 'nts >= 2 and ts2Type == "VectorF"'),
	Item("StimeSeries2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar time series 2: '), visible_when = 'nts >= 2 and ts2Type == "ScalarTs"'),
	Item("scalarField2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar field 2: '), visible_when = 'nts >= 2 and ts2Type == "ScalarF"'),
	Item("LTimeSeries2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian time series 2: '), visible_when = 'nts >= 2 and ts2Type == "LagrangianTs"'),
	Item("L2Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian field 2: '), visible_when = 'nts >= 2 and ts2Type == "Lagrangian"'),
	Item("radioButton2", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 2 and numTs2 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts3", show_label = False, visible_when='nts >= 3 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts3", show_label = False, visible_when='nts >= 3 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts3", show_label = False, visible_when='nts >= 3 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts3", show_label = False, visible_when='nts >= 3 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector time series 3: '), visible_when = 'nts >= 3 and ts3Type == "VectorTs"'),
	Item("vectorField3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector field 3: '), visible_when = 'nts >= 3 and ts3Type == "VectorF"'),
	Item("StimeSeries3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar time series 3: '), visible_when = 'nts >= 3 and ts3Type == "ScalarTs"'),
	Item("scalarField3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar field 3: '), visible_when = 'nts >= 3 and ts3Type == "ScalarF"'),
	Item("LTimeSeries3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian time series 3: '), visible_when = 'nts >= 3 and ts3Type == "LagrangianTs"'),
	Item("L3Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian field 3: '), visible_when = 'nts >= 3 and ts3Type == "Lagrangian"'),
	Item("radioButton3", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 3 and numTs3 > 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts4", show_label = False, visible_when='nts >= 4 and layout >= "1"', height = tinyh, width = tinyww),
	Item("screen2_ts4", show_label = False, visible_when='nts >= 4 and layout >= "2"', height = tinyh, width = tinyww),),
	HGroup(Item("screen3_ts4", show_label = False, visible_when='nts >= 4 and layout >= "3"', height = tinyh, width = tinyww),
	Item("screen4_ts4", show_label = False, visible_when='nts >= 4 and layout >= "4"', height = tinyh, width = tinyww),),),
	Item("timeSeries4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector time series 4: '), visible_when = 'nts >= 4 and ts4Type == "VectorTs"'),
	Item("vectorField4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Vector field 4: '), visible_when = 'nts >= 4 and ts4Type == "VectorF"'),
	Item("StimeSeries4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar time series 4: '), visible_when = 'nts >= 4 and ts4Type == "ScalarTs"'),
	Item("scalarField4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Scalar field 4: '), visible_when = 'nts >= 4 and ts4Type == "ScalarF"'),
	Item("LTimeSeries4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian time series 4: '), visible_when = 'nts >= 4 and ts4Type == "LagrangianTs"'),
	Item("L4Txt", style = 'readonly', show_label = False, height = tinyh, width = determine_width('Lagrangian field 4: '), visible_when = 'nts >= 4 and ts4Type == "Lagrangian"'),
	Item("radioButton4", show_label = False, style='custom', height = tinyh, width = -70, visible_when = 'nts >= 4 and numTs4 > 0'),
	),
	show_border = True, orientation = 'vertical', scrollable = True),
	),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
