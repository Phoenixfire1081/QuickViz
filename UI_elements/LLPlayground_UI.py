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

LLPlayGroundUIelements = Group(

	# HGroup(
	# Item("predefinedVortexTxt", style = 'readonly', show_label = False, visible_when = playgroundVisibility),
	# ),
	
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
	Item("fourierGridTypeTxt", style = 'readonly', show_label = False, visible_when = playgroundVisibility),
	Item("allPlaygroundOptions", show_label = False, visible_when = playgroundVisibility)
	),
	
	HGroup(
	Item("GenerateStructure", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	Item("ResetStructure", show_label = False, visible_when = playgroundVisibility, height = buttonh, width = buttonw),
	),
	),
