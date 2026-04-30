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

structureExtractionUIelements = Group(

HGroup(
Item("thresholdExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -70, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("thresholdExtractionSet", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = longh, width = longw),
),
HGroup(
Item("thresholdPercentExtractionSetTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Threshold %:"), visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("thresholdPercentExtractionSet", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = longh, width = longw),
),
HGroup(
Item("verboseStructureExtractionTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("verboseStructureExtraction", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
),
HGroup(
Item("useMarchingCubesTxt", style = 'readonly', show_label = False, height = smallh, width = -110, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("useMarchingCubes", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = longh, width = longw),
),
HGroup(
Item("extractStructures", show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"', height = buttonh, width = buttonw),
),
HGroup(
Item("totalNumberOfExtractedStructuresTxt", style = 'readonly', show_label = False, height = smallh, width = -230, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("totalNumberOfExtractedStructures", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
),
HGroup(
Item("chooseStructureTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when='allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
Item("chooseStructure", show_label = False, editor=RangeEditor(mode='slider', low_name = 'includeEmptySpace',  high_name='totalNumberOfExtractedStructures'), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction"'),
),
HGroup(
Item("structInfoTxt", style = 'readonly', show_label = False, height = smallh, width = -150, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("extentIdxTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structXminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structXmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structYminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structYmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structZminIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structZmaxIdx", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("extentActTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structXminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structXmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structYminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structYmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structZminAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structZmaxAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("structVolTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structVolume", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("structureVolumeActualTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Structure volume (Act):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("structVolumeAct", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("meanVelocityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Mean velocity within structure (ux, uy, uz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("meanVelocityWithinStructure", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("maxVelocityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Max velocity within structure (ux, uy, uz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("maxVelocityWithinStructure", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("meanVorticityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Circulation within structure (Gx, Gy, Gz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("meanVorticityWithinStructure", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
# HGroup(
# Item("maxVorticityWithinStructureTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Max velocity within structure (ux, uy, uz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
# Item("maxVorticityWithinStructure", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
# ),
HGroup(
Item("polStrengthWithinStructureXTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("polStrengthWithinStructureX", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("polStrengthWithinStructureYTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("polStrengthWithinStructureY", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
HGroup(
Item("polStrengthWithinStructureZTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width("Polarization strength at maximum velocity in ux (qx, qy, qz):"), visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
Item("polStrengthWithinStructureZ", style = 'readonly', show_label = False, visible_when = 'allModeOptions == "Analysis" and allAnalysisOptions == "Structure extraction" and chooseStructure > 0'),
),
Group(
Item("allLocalOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Visualization"')
),

),
