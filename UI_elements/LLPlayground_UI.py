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

playgroundVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"'
playgroundCustomVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and allPredefinedVortices == "Custom"'
playgroundLogarithmicVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and allPlaygroundOptionsActual == "Logarithmic"'

LLPlayGroundUIelements = Group(

	HGroup(
	Item("scalarFieldOptionsTxt", style = 'readonly', show_label = False, visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("numberOfTimeStepsTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = playgroundVisibility),
	Item("timeStep_LL", show_label = False, height = longh, width = tinyw , visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("minExtentTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundVisibility),
	Item("xmin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("ymin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("zmin_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	),

	HGroup(
	Item("maxExtentTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = playgroundVisibility),
	Item("xmax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("ymax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("zmax_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	),

	HGroup(
	Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundVisibility),
	Item("xres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("yres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	Item("zres_LL", show_label = False, height = tinyh, width = tinyw , visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("GenerateTS_playground", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	Item("ResetTS_playground", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	),
	
	HGroup(
	Item("numGridPointsTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = playgroundVisibility),
	Item("numGridPoints_playground", show_label = False, height = longh, width = tinyw , visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("includeK0Txt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = playgroundVisibility),
	Item("includeK0_playground", show_label = False, height = longh, width = tinyw , visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("seedScalePGTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundVisibility),
	Item("seedScale_playground", show_label = False, visible_when = playgroundVisibility, width = tinyw, height = tinyh),
	),
	
	HGroup(
	Item("fourierGridTypeTxt", style = 'readonly', show_label = False, visible_when = playgroundVisibility),
	Item("allPlaygroundOptionsActual", show_label = False, visible_when = playgroundVisibility)
	),
	
	HGroup(
	Item("aTxt", style = 'readonly', show_label = False, height = smallh, width = -10, visible_when = playgroundLogarithmicVisibility),
	Item("a_playground", show_label = False, visible_when = playgroundLogarithmicVisibility, width = tinyw, height = tinyh),
	Item("bTxt", style = 'readonly', show_label = False, height = smallh, width = -10, visible_when = playgroundLogarithmicVisibility),
	Item("b_playground", show_label = False, visible_when = playgroundLogarithmicVisibility, width = tinyw, height = tinyh),
	),
	
	
	HGroup(
	Item("addScalarFieldTxt", style = 'readonly', show_label = False, visible_when = playgroundVisibility),
	Item("allPredefinedVortices", show_label = False, visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("defineStructureTxt", style = 'readonly', show_label = False, visible_when = playgroundCustomVisibility),
	),
	HGroup(
	Item("defineStructureDescriptionVorticityTxt", style = 'readonly', show_label = False, visible_when = playgroundCustomVisibility),
	),
	HGroup(
	Item("defineStructureDescriptionVelocityTxt", style = 'readonly', show_label = False, visible_when = playgroundCustomVisibility),
	),
	HGroup(
	Item("initCondition1", show_label = False, visible_when = playgroundCustomVisibility, height = hugeh, width = hugew),
	),
	
	HGroup(
	Item("GenerateStructure", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	Item("NextTS_playground", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	Item("ResetStructure", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	),
	),
