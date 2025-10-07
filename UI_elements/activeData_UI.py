from traitsui.api import VGroup, HSplit, Group, Item, HGroup

activeDataUIelements = Group(
	Group(Group(label = 'Active data'),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts1", show_label = False, visible_when='nts >= 1 and layout >= "1"'),
	Item("screen2_ts1", show_label = False, visible_when='nts >= 1 and layout >= "2"'),),
	HGroup(Item("screen3_ts1", show_label = False, visible_when='nts >= 1 and layout >= "3"'),
	Item("screen4_ts1", show_label = False, visible_when='nts >= 1 and layout >= "4"'),),),
	Item("radioButton1", label = 'Time Series 1 : Control', style='custom', visible_when='nts >= 1 and numTs1 > 0'),
	Item("radioButton1", label = 'Scalar field 1 : Control', style='custom', visible_when='nts >= 1 and numTs1 == 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts2", show_label = False, visible_when='nts >= 2 and layout >= "1"'),
	Item("screen2_ts2", show_label = False, visible_when='nts >= 2 and layout >= "2"'),),
	HGroup(Item("screen3_ts2", show_label = False, visible_when='nts >= 2 and layout >= "3"'),
	Item("screen4_ts2", show_label = False, visible_when='nts >= 2 and layout >= "4"'),),),
	Item("radioButton2", label = 'Time series 2 : Control', style='custom', visible_when='nts >= 2 and numTs2 > 0'),
	Item("radioButton2", label = 'Scalar field 2 : Control', style='custom', visible_when='nts >= 2 and numTs2 == 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts3", show_label = False, visible_when='nts >= 3 and layout >= "1"'),
	Item("screen2_ts3", show_label = False, visible_when='nts >= 3 and layout >= "2"'),),
	HGroup(Item("screen3_ts3", show_label = False, visible_when='nts >= 3 and layout >= "3"'),
	Item("screen4_ts3", show_label = False, visible_when='nts >= 3 and layout >= "4"'),),),
	Item("radioButton3", label = 'Time series 3 : Control', style='custom', visible_when='nts >= 3 and numTs3 > 0'),
	Item("radioButton3", label = 'Scalar field 3 : Control', style='custom', visible_when='nts >= 3 and numTs3 == 0'),
	),
	
	HGroup(
	VGroup(
	HGroup(Item("screen1_ts4", show_label = False, visible_when='nts >= 4 and layout >= "1"'),
	Item("screen2_ts4", show_label = False, visible_when='nts >= 4 and layout >= "2"'),),
	HGroup(Item("screen3_ts4", show_label = False, visible_when='nts >= 4 and layout >= "3"'),
	Item("screen4_ts4", show_label = False, visible_when='nts >= 4 and layout >= "4"'),),),
	Item("radioButton4", label = 'Time series 4 : Control', style='custom', visible_when='nts >= 4 and numTs4 > 0'),
	Item("radioButton4", label = 'Scalar field 4 : Control', style='custom', visible_when='nts >= 4 and numTs4 == 0'),
	),
	show_border = True, orientation = 'vertical', scrollable = True),
	),
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
