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

DRVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Duchon Robert"'
DRPressureVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Pressure" or allAnalysisOptions == "Duchon Robert")'
DRPressureVisibilityBBox = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Pressure" or allAnalysisOptions == "Duchon Robert") and altBBox == True'
PressureVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Pressure"'

duchonRobertPressureUIelements = Group(

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
	Item("altBBoxTxt", show_label = False, style = 'readonly', visible_when=DRPressureVisibility, height = smallh, width = -170,),
	Item("altBBox", show_label = False, visible_when=DRPressureVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=DRPressureVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=DRPressureVisibilityBBox, width = sliderw),
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
