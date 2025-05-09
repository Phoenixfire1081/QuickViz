from traitsui.api import VGroup, HSplit, Group, Item, HGroup
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

isoUIelements = (Group(Group(Item("allLocalOptions", show_label = False, style = 'custom')),
	
	# Group(Item("IsoOptionsTxt", show_label = False, visible_when = 'allLocalOptions == "Isosurface"', style = 'readonly')),
	
	HGroup(Item("thresholdMinimum1", label = 'Minimum threshold:', style='readonly', visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'), 
	Item("thresholdMaximum1", label = ', Maximum threshold:', visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent1", show_label = False, visible_when='radioButton1 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum2", label = 'Minimum threshold:', style='readonly', visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'), 
	Item("thresholdMaximum2", label = ', Maximum threshold:', visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent2", show_label = False, visible_when='radioButton2 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum3", label = 'Minimum threshold:', style='readonly', visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'), 
	Item("thresholdMaximum3", label = ', Maximum threshold:', visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent3", show_label = False, visible_when='radioButton3 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	
	HGroup(Item("thresholdMinimum4", label = 'Minimum threshold:', style='readonly', visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'), 
	Item("thresholdMaximum4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'), style='readonly'),
	HGroup(Item("ThresholdTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'),
	Item("threshold4", label = 'Threshold(s)', visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThreshold4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	),
	HGroup(Item("ThresholdPercentTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"'),
	Item("thresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = longh, width = longw), 
	Item("setThresholdPercent4", show_label = False, visible_when='radioButton4 == "Y" and allLocalOptions == "Isosurface"', height = buttonh, width = buttonw),
	), show_border = True, orientation = 'vertical', scrollable = True)),
