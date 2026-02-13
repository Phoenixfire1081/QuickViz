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
playgroundKnotVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and allPredefinedVortices == "Vortex knot"'
playgroundTorusVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and allPredefinedVortices == "Vortex knot" and allPredefinedKnots == "(p,q) Torus"'
playgroundRingVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and not allPredefinedVortices == "Vortex tube"'
playgroundOthersVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and not allPredefinedVortices == "None"'
playgroundGridVisibility = 'allModeOptions == "Log Lattice" and allLLOptions == "Playground" and visualizeGrid_playground == True'
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
	Item("visualizeGridTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundVisibility),
	Item("visualizeGrid_playground", show_label = False, height = longh, width = tinyw , visible_when = playgroundVisibility),
	),
	
	HGroup(
	Item("seedScalePGTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundGridVisibility),
	Item("seedScale_playground", show_label = False, visible_when = playgroundGridVisibility, width = tinyw, height = tinyh),
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
	Item("ringRadiusTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = playgroundRingVisibility),
	Item("ringRadius_playground", show_label = False, height = longh, width = tinyw , visible_when = playgroundRingVisibility),
	),
	
	HGroup(
	Item("allPredefinedKnotsTxt", style = 'readonly', show_label = False, visible_when = playgroundKnotVisibility),
	Item("allPredefinedKnots", show_label = False, visible_when = playgroundKnotVisibility),
	),
	
	HGroup(
	Item("pTxt", style = 'readonly', show_label = False, height = smallh, width = -10, visible_when = playgroundTorusVisibility),
	Item("p_torus", show_label = False, visible_when = playgroundTorusVisibility, width = tinyw, height = tinyh),
	Item("qTxt", style = 'readonly', show_label = False, height = smallh, width = -10, visible_when = playgroundTorusVisibility),
	Item("q_torus", show_label = False, visible_when = playgroundTorusVisibility, width = tinyw, height = tinyh),
	),
	
	HGroup(
	Item("translatePlaygroundTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = playgroundOthersVisibility),
	),
	
	HGroup(
	Item("translatex_playground", show_label = False, editor=RangeEditor(mode='slider', low_name = 'xmin_pg',  high_name='xmax_pg'), visible_when=playgroundOthersVisibility, width = sliderw),
	),
	
	HGroup(
	Item("translatey_playground", show_label = False, editor=RangeEditor(mode='slider', low_name = 'xmin_pg',  high_name='xmax_pg'), visible_when=playgroundOthersVisibility, width = sliderw),
	),
	
	HGroup(
	Item("translatez_playground", show_label = False, editor=RangeEditor(mode='slider', low_name = 'xmin_pg',  high_name='xmax_pg'), visible_when=playgroundOthersVisibility, width = sliderw),
	),
	
	HGroup(
	Item("rotationPlaygroundTxt", style = 'readonly', show_label = False, height = smallh, width = -120, visible_when = playgroundOthersVisibility),
	Item("rotAxisX_playground", show_label = False, width = tinyw, height = tinyh, visible_when = playgroundOthersVisibility),
	Item("rotAxisY_playground", show_label = False, width = tinyw, height = tinyh, visible_when = playgroundOthersVisibility),
	Item("rotAxisZ_playground", show_label = False, width = tinyw, height = tinyh, visible_when = playgroundOthersVisibility),
	),
	
	HGroup(
	Item("rotationAnglePlaygroundTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when = playgroundOthersVisibility),
	Item("rotationAngle_playground", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minRot_pg',  high_name='maxRot_pg'), visible_when=playgroundOthersVisibility, width = sliderw),
	),
	
	HGroup(
	Item("thicknessPlaygroundTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when = playgroundOthersVisibility),
	Item("thickness_playground", show_label = False, height = longh, width = tinyw , visible_when = playgroundOthersVisibility),
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
