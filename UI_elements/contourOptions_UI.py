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

contourUIelements = (Group(Group(
	# Item("ContourOptionsTxt", show_label = False, style = 'readonly')
	label = "Contour options:"
	),
	
	HGroup(Item("OpacityTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton1 == "Y"'),
	Item("contourOpacity1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("RepresentationTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton1 == "Y"'),
	Item("contourRepresentation1", show_label = False, visible_when='radioButton1 == "Y"')),
	
	HGroup(Item("ColormapTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton1 == "Y"'),
	Item("contourColormap1", show_label = False, visible_when='radioButton1 == "Y"'),
	Item("ColormapMinMaxTxt", style = 'readonly', show_label = False, height = smallh, width = -145, visible_when='radioButton1 == "Y"'),
	Item("colormapMin1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw),
	Item("colormapMax1", show_label = False, visible_when='radioButton1 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("OpacityTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton2 == "Y"'),
	Item("contourOpacity2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("RepresentationTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton2 == "Y"'),
	Item("contourRepresentation2", show_label = False, visible_when='radioButton2 == "Y"')),
	
	HGroup(Item("ColormapTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton2 == "Y"'),
	Item("contourColormap2", show_label = False, visible_when='radioButton2 == "Y"'),
	Item("ColormapMinMaxTxt", style = 'readonly', show_label = False, height = smallh, width = -145, visible_when='radioButton2 == "Y"'),
	Item("colormapMin2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw),
	Item("colormapMax2", show_label = False, visible_when='radioButton2 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("OpacityTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton3 == "Y"'),
	Item("contourOpacity3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("RepresentationTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton3 == "Y"'),
	Item("contourRepresentation3", show_label = False, visible_when='radioButton3 == "Y"')),
	
	HGroup(Item("ColormapTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton3 == "Y"'),
	Item("contourColormap3", show_label = False, visible_when='radioButton3 == "Y"'),
	Item("ColormapMinMaxTxt", style = 'readonly', show_label = False, height = smallh, width = -145, visible_when='radioButton3 == "Y"'),
	Item("colormapMin3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw),
	Item("colormapMax3", show_label = False, visible_when='radioButton3 == "Y"', height = tinyh, width = tinyw)),
	
	HGroup(Item("OpacityTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='radioButton4 == "Y"'),
	Item("contourOpacity4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("RepresentationTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='radioButton4 == "Y"'),
	Item("contourRepresentation4", show_label = False, visible_when='radioButton4 == "Y"')),
	
	HGroup(Item("ColormapTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='radioButton4 == "Y"'),
	Item("contourColormap4", show_label = False, visible_when='radioButton4 == "Y"'),
	Item("ColormapMinMaxTxt", style = 'readonly', show_label = False, height = smallh, width = -145, visible_when='radioButton4 == "Y"'),
	Item("colormapMin4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw),
	Item("colormapMax4", show_label = False, visible_when='radioButton4 == "Y"', height = tinyh, width = tinyw)),
	show_border = True, orientation = 'vertical', scrollable = True)),
