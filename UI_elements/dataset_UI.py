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

# Set visibility options
localDatasetVisibility = 'allDatasetActions == "Import" and allModeOptions == "Dataset" and allDatasetOptions == "Local"'
localDatasetVisibilityBBox = 'allDatasetActions == "Import" and allModeOptions == "Dataset" and allDatasetOptions == "Local" and altBBox == True'
localDatasetVisibilityRaw3D = 'allDatasetActions == "Import" and allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "Raw 3D"'
localDatasetVisibilitynetCDF = 'allDatasetActions == "Import" and allModeOptions == "Dataset" and allDatasetOptions == "Local" and allLocalDatasetOptions == "netCDF"'
exportData = 'allModeOptions == "Dataset" and allDatasetActions == "Export"'
exportDataBBox = 'allModeOptions == "Dataset" and allDatasetActions == "Export" and altBBox == True'

datasetUIelements = Group( 
	
	Group(
	Item("allDatasetActions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Dataset"')
	),
	
	Group(
	Item("allDatasetOptions", show_label = False, style = 'custom', visible_when = 'allModeOptions == "Dataset" and allDatasetActions == "Import"')
	),
	
	# Export
	
	HGroup(
	Item("SaveTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Save location:'), visible_when = exportData),
	Item("save_path", show_label = False, height = longh, width = longw, visible_when = exportData),
	Item("choose_folder", show_label = False, height = buttonh, width = buttonw, visible_when = exportData),
	),
	HGroup(
	Item("folderNameExportTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Save location:'), visible_when = exportData),
	Item("folderNameExport", show_label = False, height = smallh, width = smallw, visible_when = exportData),
	),
	HGroup(
	Item("saveWhatOptionsTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Save what?'), visible_when = exportData),
	Item("assignToTS", show_label = False, visible_when = exportData),
	Item("saveWhatOptions", show_label = False, visible_when = exportData),
	),
	
	HGroup(
	Item("whichTimeStepLLTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('Which time step (s):'), visible_when = exportData),
	Item("timeStep_LocalData", show_label = False, height = longh, width = longw , visible_when = exportData),
	Item("exampleTSTxt", style = 'readonly', show_label = False, height = smallh, width = determine_width('(ex:1 or 3-6 or 1-100-10)'), visible_when = exportData),
	),
	
	HGroup(
	Item("altBBoxTxt", show_label = False, style = 'readonly', visible_when=exportData, height = smallh, width = determine_width('Use alternate bounding box:')),
	Item("altBBox", show_label = False, visible_when=exportData),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('xmin:')),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=exportDataBBox, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('xmax:')),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=exportDataBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('ymin:')),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=exportDataBBox, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('ymax:')),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=exportDataBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('zmin:')),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=exportDataBBox, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=exportDataBBox, height = smallh, width = determine_width('zmax:')),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=exportDataBBox, width = sliderw),
	),
	
	HGroup(
	Item("exportNow", show_label = False, height = buttonh, width = buttonw, visible_when = exportData),
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
	Item("assignToTSTxt", show_label = False, style = 'readonly', visible_when=localDatasetVisibility, height = smallh, width = determine_width("Assign to:")),
	Item("assignToTS", show_label = False, visible_when=localDatasetVisibility),
	),
	
	HGroup(
	Item("whichScalarTxt", style = 'readonly', height = smallh, width = -100, show_label = False, visible_when = localDatasetVisibility),
	Item("whichScalar_LocalData", show_label = False, visible_when = localDatasetVisibility),
	Item("load_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	Item("cancel_LocalData", height = buttonh, width = buttonw, show_label = False, visible_when = localDatasetVisibility),
	),

),
