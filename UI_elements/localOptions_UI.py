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
determine_width = allUIOptions.determineWidth

localUIelements = (Group(label = 'Local options:'),

	Group(
	
	Group(label = 'Outline:'),
	
	# TS 1
	
	HGroup(
	Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='radioButton1 == "Y"'),
	Item("outlineToggle1", show_label = False, visible_when='radioButton1 == "Y"'),
	),
	HGroup(
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='radioButton1 == "Y"'),
	Item("outlineWidth1", show_label = False, visible_when='radioButton1 == "Y"', height = slidertinyh, width = slidertinyw)
	),
	
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when='radioButton1 == "Y"'),
	Item("outlineColorRed1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)),
	
	# TS 2
	
	HGroup(
	Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='radioButton2 == "Y"'),
	Item("outlineToggle2", show_label = False, visible_when='radioButton2 == "Y"'),
	),
	HGroup(
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='radioButton2 == "Y"'),
	Item("outlineWidth2", show_label = False, visible_when='radioButton2 == "Y"', height = slidertinyh, width = slidertinyw)
	),
	
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton2 == "Y"'),
	Item("outlineColorRed2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw)),
	
	# TS 3
	
	HGroup(
	Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='radioButton3 == "Y"'),
	Item("outlineToggle3", show_label = False, visible_when='radioButton3 == "Y"'),
	),
	HGroup(
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='radioButton3 == "Y"'),
	Item("outlineWidth3", show_label = False, visible_when='radioButton3 == "Y"', height = slidertinyh, width = slidertinyw)
	),
	
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton3 == "Y"'),
	Item("outlineColorRed3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw)),
	
	# TS 4
	
	HGroup(
	Item("ShowHideOutlineTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='radioButton4 == "Y"'),
	Item("outlineToggle4", show_label = False, visible_when='radioButton4 == "Y"'),
	),
	HGroup(
	Item("OutlineWidthTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when='radioButton4 == "Y"'),
	Item("outlineWidth4", show_label = False, visible_when='radioButton4 == "Y"', height = slidertinyh, width = slidertinyw)
	),
	
	HGroup(Item("OutlineColorTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when='radioButton4 == "Y"'),
	Item("outlineColorRed4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorGreen4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("outlineColorBlue4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw)),
		
	Group(label = 'Data axis:'),
	
	HGroup(
	Item("enableAxisTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Enable axis:")),
	Item("enableAxis_sc1", show_label = False, height = tinyh, width = tinyw)
	),
	
	# TS 1
	
	HGroup(Item("xyzlabel", style = 'readonly', show_label = False, height = smallh, width = determine_width("Label (x, y, z):"), visible_when='radioButton1 == "Y"'),
	Item("data_axis_x_label_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("data_axis_y_label_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("data_axis_z_label_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("AxisColorTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Axis color (r,g,b):"), visible_when='radioButton1 == "Y"'),
	Item("data_axis_color_r_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("data_axis_color_g_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("data_axis_color_b_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(
	Item("nticks", style = 'readonly', show_label = False, height = smallh, width = determine_width("Number of ticks:"), visible_when='radioButton1 == "Y"'),
	Item("data_axis_npts_sc1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)
	),
	
		
	Group(label = 'Colorbar:'),
	
	HGroup(
	Item("enableCbarTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Enable colorbar:")),
	Item("enableColorbar_sc1", show_label = False, height = tinyh, width = tinyw)
	),
	
	HGroup(
	Item("cbarTitleTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Title:")),
	Item("colorbarTitle_sc1", show_label = False, height = tinyh, width = tinyw)
	),
	
	Group(label = 'Static axis:'),
	
	HGroup(
	Item("xyzlabel", style = 'readonly', show_label = False, height = smallh, width = determine_width("Label (x, y, z):")),
	Item("default_axis_x_label", show_label = False, height = tinyh, width = tinyw),
	Item("default_axis_y_label", show_label = False, height = tinyh, width = tinyw),
	Item("default_axis_z_label", show_label = False, height = tinyh, width = tinyw)
	),
	
	HGroup(
	Item("xyzoffset", style = 'readonly', show_label = False, height = smallh, width = determine_width("Offsets (x, y, z):")),
	Item("default_axis_x_offset", show_label = False, height = sliderh, width = slidertinyw),
	Item("default_axis_y_offset", show_label = False, height = sliderh, width = slidertinyw),
	Item("default_axis_z_offset", show_label = False, height = sliderh, width = slidertinyw)
	),
	
	show_border = True, orientation = 'vertical', scrollable = True),
	),
