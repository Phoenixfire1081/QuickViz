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
determine_width = allUIOptions.determineWidth

StructureVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Single-scale" and allAnalysisOptions_feature == "Structure extraction"'
StructureVisibilityChosen = 'allModeOptions == "Analysis" and allAnalysisOptions == "Single-scale" and allAnalysisOptions_feature == "Structure extraction" and chooseStructure > 0'

structureExtractionUIelements = Group(

HGroup(
Item("thresholdExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when=StructureVisibility),
Item("thresholdExtractionSet", show_label = False, visible_when = StructureVisibility, height = longh, width = longw),
),
HGroup(
Item("thresholdPercentExtractionSetTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Threshold %:"), visible_when=StructureVisibility),
Item("thresholdPercentExtractionSet", show_label = False, visible_when = StructureVisibility, height = longh, width = longw),
),
HGroup(
Item("verboseStructureExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when=StructureVisibility),
Item("verboseStructureExtraction", show_label = False, visible_when = StructureVisibility),
),
HGroup(
Item("useMarchingCubesTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when=StructureVisibility),
Item("useMarchingCubes", show_label = False, visible_when = StructureVisibility, height = longh, width = longw),
),
HGroup(
Item("extractStructures", show_label = False, visible_when = StructureVisibility, height = buttonh, width = buttonw),
),
HGroup(
Item("totalNumberOfExtractedStructuresTxt", style = 'readonly', show_label = False, height = smallh, width = -230, visible_when=StructureVisibility),
Item("totalNumberOfExtractedStructures", style = 'readonly', show_label = False, visible_when = StructureVisibility),
),
HGroup(
Item("chooseStructureTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when=StructureVisibility),
Item("chooseStructure", show_label = False, editor=RangeEditor(mode='slider', low_name = 'includeEmptySpace',  high_name='totalNumberOfExtractedStructures'), visible_when = StructureVisibility),
),
HGroup(
Item("structInfoTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("extentIdxTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = StructureVisibilityChosen),
Item("structXminIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structXmaxIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structYminIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structYmaxIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structZminIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structZmaxIdx", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("extentActTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = StructureVisibilityChosen),
Item("structXminAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structXmaxAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structYminAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structYmaxAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structZminAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
Item("structZmaxAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("structVolTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when = StructureVisibilityChosen),
Item("structVolume", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("structureVolumeActualTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Structure volume (Act):"), visible_when = StructureVisibilityChosen),
Item("structVolumeAct", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("meanVelocityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Mean velocity within structure (ux, uy, uz):"), visible_when = StructureVisibilityChosen),
Item("meanVelocityWithinStructure", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("maxVelocityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Max velocity within structure (ux, uy, uz):"), visible_when = StructureVisibilityChosen),
Item("maxVelocityWithinStructure", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("meanVorticityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Circulation within structure (Gx, Gy, Gz):"), visible_when = StructureVisibilityChosen),
Item("meanVorticityWithinStructure", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
# HGroup(
# Item("maxVorticityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Max velocity within structure (ux, uy, uz):"), visible_when = StructureVisibilityChosen),
# Item("maxVorticityWithinStructure", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
# ),
HGroup(
Item("polStrengthWithinStructureXTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = StructureVisibilityChosen),
Item("polStrengthWithinStructureX", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("polStrengthWithinStructureYTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = StructureVisibilityChosen),
Item("polStrengthWithinStructureY", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
HGroup(
Item("polStrengthWithinStructureZTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = StructureVisibilityChosen),
Item("polStrengthWithinStructureZ", style = 'readonly', show_label = False, visible_when = StructureVisibilityChosen),
),
Group(
Item("allLocalOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Visualization"')
),

),
