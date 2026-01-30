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

# Set visibility options
localDatasetVisibility = 'allModeOptions == "Dataset" and allDatasetOptions == "Local"'
localDatasetVisibilityBBox = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and altBBox == True'
localDatasetVisibilityRaw3D = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "Raw 3D"'
localDatasetVisibilitynetCDF = 'allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "netCDF"'

datasetUIelements = Group( 
	
	Group(
	Item("allDatasetOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Dataset"')
	),
	
	# Local data
	
	HGroup(
	Item("allLocalDatasetOptions", show_label = False, style = 'custom', visible_when = localDatasetVisibility)
	),
	
	HGroup(
	Item("LoadLocalDataTxt", style = 'readonly', show_label = False, height = smallh, width = -100, visible_when = localDatasetVisibility),
	Item("LocalData_path", show_label = False, height = longh, width = longw, visible_when = localDatasetVisibility),
	Item("choose_folder_LocalDataPath", show_label = False, height = buttonh, width = buttonw, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("assignTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("availableAttributesTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = localDatasetVisibilitynetCDF),
	Item("allAttributes", style = 'readonly', show_label = False, height = smallh, width = -1000, visible_when = localDatasetVisibilitynetCDF),
	),
	
	HGroup(
	Item("velxTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velxLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("velyTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velyLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	HGroup(
	Item("velzTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilitynetCDF),
	Item("velzLabel", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibilitynetCDF),
	),
	
	HGroup(
	Item("adjustTxt", style = 'readonly', show_label = False, height = smallh, width = -200, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("minExtentTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("xmin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("ymin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zmin_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),

	HGroup(
	Item("maxExtentTxt", style = 'readonly', show_label = False, height = tinyh, width = -80, visible_when = localDatasetVisibility),
	Item("xmax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("ymax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zmax_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("dxdydzTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("dx_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("dy_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("dz_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),

	HGroup(
	Item("resolutionTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("xres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("yres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	Item("zres_Local", show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("timestepsTxt", style = 'readonly', show_label = False, height = smallh, width = -140, visible_when = localDatasetVisibility),
	Item("timeSteps_LocalData", style = 'readonly', show_label = False, height = tinyh, width = tinyw , visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("whichTimeStepLLTxt", style = 'readonly', show_label = False, height = smallh, width = -130, visible_when = localDatasetVisibility),
	Item("timeStep_LocalData", show_label = False, height = longh, width = longw , visible_when = localDatasetVisibility),
	Item("exampleTSTxt", style = 'readonly', show_label = False, height = smallh, width = -160, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("precisionTxt", style = 'readonly', show_label = False, height = smallh, width = -60, visible_when = localDatasetVisibilityRaw3D),
	Item("precision_LocalData", show_label = False, style = 'custom' , visible_when = localDatasetVisibilityRaw3D),
	),
	
	HGroup(
	Item("trimDatasetTxt", style = 'readonly', show_label = False, height = smallh, width = -80, visible_when = localDatasetVisibility),
	Item("altBBox", show_label = False, visible_when = localDatasetVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=localDatasetVisibilityBBox, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=localDatasetVisibilityBBox, width = sliderw),
	),
	
	HGroup(
	Item("whichScalarTxt", style = 'readonly', height = smallh, width = -100, show_label = False, visible_when = localDatasetVisibility),
	Item("whichScalar_LocalData", show_label = False, visible_when = localDatasetVisibility),
	Item("load_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	Item("cancel_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	),

),
