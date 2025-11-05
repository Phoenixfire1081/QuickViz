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

LLPlayGroundUIelements = Group(
	Group(
	Item("allPlaygroundOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"')
	),
	
	HGroup(
	Item("defineStructureTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),
	),
	HGroup(
	Item("defineStructureDescriptionVorticityTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),
	),
	HGroup(
	Item("defineStructureDescriptionVelocityTxt", style = 'readonly', show_label = False, visible_when='allModeOptions == "Log Lattice" and allLLOptions == "Playground"'),
	),
	HGroup(
	Item("initCondition1", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = hugeh, width = hugew),
	),
	
	HGroup(
	Item("GenerateStructure", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = buttonh, width = buttonw),
	Item("ResetStructure", show_label = False, visible_when = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground"', height = buttonh, width = buttonw),
	),
	),
