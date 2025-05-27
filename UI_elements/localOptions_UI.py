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

localUIelements = (Group(label = 'Local options:'),

	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #

	Group(
	# Group(Item("OutOptionsTxt", show_label = False, style = 'readonly')),
	# Group(label = 'Outline options:'),
	
	HGroup(Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='radioButton1 == "Y"'),
	Item("outlineToggle1", show_label = False, visible_when='radioButton1 == "Y"'),
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton1 == "Y"'),
	Item("outlineWidth1", show_label = False, visible_when='radioButton1 == "Y"', height = slidertinyh, width = slidertinyw)),
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton1 == "Y"'),
	Item("outlineColorRed1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='radioButton2 == "Y"'),
	Item("outlineToggle2", show_label = False, visible_when='radioButton2 == "Y"'),
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton2 == "Y"'),
	Item("outlineWidth2", show_label = False, visible_when='radioButton2 == "Y"', height = slidertinyh, width = slidertinyw)),
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton2 == "Y"'),
	Item("outlineColorRed2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='radioButton3 == "Y"'),
	Item("outlineToggle3", show_label = False, visible_when='radioButton3 == "Y"'),
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton3 == "Y"'),
	Item("outlineWidth3", show_label = False, visible_when='radioButton3 == "Y"', height = slidertinyh, width = slidertinyw)),
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton3 == "Y"'),
	Item("outlineColorRed3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when='radioButton4 == "Y"'),
	Item("outlineToggle4", show_label = False, visible_when='radioButton4 == "Y"'),
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton4 == "Y"'),
	Item("outlineWidth4", show_label = False, visible_when='radioButton4 == "Y"', height = slidertinyh, width = slidertinyw)),
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton4 == "Y"'),
	Item("outlineColorRed4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw)),
	
	show_border = True, orientation = 'vertical', scrollable = True),),
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
