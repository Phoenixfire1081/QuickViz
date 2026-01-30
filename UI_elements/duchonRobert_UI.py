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

DRVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Duchon Robert"'
DRPressureVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Pressure" or allAnalysisOptions == "Duchon Robert")'
PressureVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Pressure"'

duchonRobertUIelements = Group(

	HGroup(
	Item("allDROptions", show_label = False, style = 'custom', format_func=lambda x: x, visible_when = DRVisibility)
	),
	
	HGroup(
	Item("cutoffTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = DRPressureVisibility),
	Item("a_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRPressureVisibility),
	),
	
	HGroup(
	Item("probedScaleTxt", style = 'readonly', show_label = False, height = tinyh, width = -100, visible_when = DRPressureVisibility),
	Item("probedScale_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRPressureVisibility),
	Item("probedScaleIdxTxt", style = 'readonly', show_label = False, height = tinyh, width = -150, visible_when = DRPressureVisibility),
	),
	
	HGroup(
	Item("lcTxt", style = 'readonly', show_label = False, height = tinyh, width = -20, visible_when = DRVisibility),
	Item("l_c_DR", style = 'readonly', show_label = False, visible_when = DRVisibility),
	),
	
	HGroup(
	Item("etaTxt", style = 'readonly', show_label = False, height = tinyh, width = -120, visible_when = DRVisibility),
	Item("eta_DR", show_label = False, height = tinyh, width = tinyw , visible_when = DRVisibility),
	),
	
	HGroup(
	Item("lcetaTxt", style = 'readonly', show_label = False, height = tinyh, width = -50, visible_when = DRVisibility),
	Item("l_c_eta_DR", style = 'readonly', show_label = False, visible_when = DRVisibility),
	Item("lcetaKolmogorovTxt", style = 'readonly', show_label = False, height = tinyh, width = -120, visible_when = DRVisibility),
	),
	
	HGroup(
	Item("calculate_DR", show_label = False, visible_when = DRVisibility, height = buttonh, width = buttonw),
	Item("remove_DR", show_label = False, visible_when = DRVisibility, height = buttonh, width = buttonw),
	),
	
	HGroup(
	Item("calculate_Pressure", show_label = False, visible_when = PressureVisibility, height = buttonh, width = buttonw),
	Item("remove_Pressure", show_label = False, visible_when = PressureVisibility, height = buttonh, width = buttonw),
	),

),
