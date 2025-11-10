# QuickViz core
# Define all traits here

def include_all_traits(self):
	
	# Explicitly register observers from other files
	# allBackgroundOptions
	self.on_trait_change(self.background_changed, "BGColorRed")
	self.on_trait_change(self.background_changed, "BGColorGreen")
	self.on_trait_change(self.background_changed, "BGColorBlue")
	
	# allPlaybackOptions
	self.on_trait_change(self.next_timeseries_button_fired, "next_timeSeries")
	self.on_trait_change(self.previous_timeseries_button_fired, "previous_timeSeries")
	self.on_trait_change(self.play_timeseries_button_fired, "play_timeSeries")
	self.on_trait_change(self.stop_timeseries_button_fired, "stop_timeSeries")
	self.on_trait_change(self.play_timeseries_reverse_button_fired, "play_timeSeries_reverse")
	
	# allSaveMovieOptions
	self.on_trait_change(self.save_timeseries_button_fired, "save_timeSeries")
	self.on_trait_change(self.save_snapshot_button_fired, "save_snapshot")
	self.on_trait_change(self.choose_folder_button_fired, "choose_folder")
	
	# allCameraOptions
	self.on_trait_change(self.updateCurrentVals_button_fired, "updateCurrentVals")
	self.on_trait_change(self.saveCam1_fired, "saveCam1")
	self.on_trait_change(self.saveCam2_fired, "saveCam2")
	self.on_trait_change(self.saveCam3_fired, "saveCam3")
	self.on_trait_change(self.saveCam4_fired, "saveCam4")
	self.on_trait_change(self.saveCam5_fired, "saveCam5")
	self.on_trait_change(self.camReset_fired, "camReset")
	self.on_trait_change(self.cam_angle_changed, "camAzimuthS")
	self.on_trait_change(self.cam_angle_changed, "camElevationS")
	self.on_trait_change(self.cam_angle_changed, "camDistanceS")
	self.on_trait_change(self.cam_angle_changed, "focalPointS1")
	self.on_trait_change(self.cam_angle_changed, "focalPointS2")
	self.on_trait_change(self.cam_angle_changed, "focalPointS3")
	self.on_trait_change(self.cam_angle_changed, "camRollS")
	
	# allPathControlsClass
	self.on_trait_change(self.camPathTypeChanged, "camPathType")
	self.on_trait_change(self.addCamPathChanged, "addCamPath")
	self.on_trait_change(self.finishCamPathChanged, "finishCamPath")
	self.on_trait_change(self.resetCamPathChanged, "resetCamPath")
	
	# fileChooserClass
	self.on_trait_change(self.select_files_toggled, "select_files")
	
	# ------------------- CHANGEABLE FOR EACH TIME SERIES ------------------- #
	
	# allContourOptions
	self.on_trait_change(self.outline_changed1, "outlineWidth1")
	self.on_trait_change(self.outline_changed1, "outlineColorRed1")
	self.on_trait_change(self.outline_changed1, "outlineColorGreen1")
	self.on_trait_change(self.outline_changed1, "outlineColorBlue1")
	self.on_trait_change(self.outline_changed1, "outlineToggle1")
	self.on_trait_change(self.contour_changed1, "contourOpacity1")
	self.on_trait_change(self.contour_changed1, "contourRepresentation1")
	self.on_trait_change(self.contour_changed1, "contourColormap1")
	self.on_trait_change(self.contour_changed1, "colormapMin1")
	self.on_trait_change(self.contour_changed1, "colormapMax1")
	
	self.on_trait_change(self.outline_changed2, "outlineWidth2")
	self.on_trait_change(self.outline_changed2, "outlineColorRed2")
	self.on_trait_change(self.outline_changed2, "outlineColorGreen2")
	self.on_trait_change(self.outline_changed2, "outlineColorBlue2")
	self.on_trait_change(self.outline_changed2, "outlineToggle2")
	self.on_trait_change(self.contour_changed2, "contourOpacity2")
	self.on_trait_change(self.contour_changed2, "contourRepresentation2")
	self.on_trait_change(self.contour_changed2, "contourColormap2")
	self.on_trait_change(self.contour_changed2, "colormapMin2")
	self.on_trait_change(self.contour_changed2, "colormapMax2")
	
	self.on_trait_change(self.outline_changed3, "outlineWidth3")
	self.on_trait_change(self.outline_changed3, "outlineColorRed3")
	self.on_trait_change(self.outline_changed3, "outlineColorGreen3")
	self.on_trait_change(self.outline_changed3, "outlineColorBlue3")
	self.on_trait_change(self.outline_changed3, "outlineToggle3")
	self.on_trait_change(self.contour_changed3, "contourOpacity3")
	self.on_trait_change(self.contour_changed3, "contourRepresentation3")
	self.on_trait_change(self.contour_changed3, "contourColormap3")
	self.on_trait_change(self.contour_changed3, "colormapMin3")
	self.on_trait_change(self.contour_changed3, "colormapMax3")
	
	self.on_trait_change(self.outline_changed4, "outlineWidth4")
	self.on_trait_change(self.outline_changed4, "outlineColorRed4")
	self.on_trait_change(self.outline_changed4, "outlineColorGreen4")
	self.on_trait_change(self.outline_changed4, "outlineColorBlue4")
	self.on_trait_change(self.outline_changed4, "outlineToggle4")
	self.on_trait_change(self.contour_changed4, "contourOpacity4")
	self.on_trait_change(self.contour_changed4, "contourRepresentation4")
	self.on_trait_change(self.contour_changed4, "contourColormap4")
	self.on_trait_change(self.contour_changed4, "colormapMin4")
	self.on_trait_change(self.contour_changed4, "colormapMax4")
	
	# allIsosurfaceOptions
	self.on_trait_change(self.threshold_changed1, "threshold1")
	self.on_trait_change(self.setThreshold_fired1, "setThreshold1")
	self.on_trait_change(self.threshold_changed1, "thresholdPercent1")
	self.on_trait_change(self.setThresholdPercent_fired1, "setThresholdPercent1")
	
	self.on_trait_change(self.threshold_changed2, "threshold2")
	self.on_trait_change(self.setThreshold_fired2, "setThreshold2")
	self.on_trait_change(self.threshold_changed2, "thresholdPercent2")
	self.on_trait_change(self.setThresholdPercent_fired2, "setThresholdPercent2")
	
	self.on_trait_change(self.threshold_changed3, "threshold3")
	self.on_trait_change(self.setThreshold_fired3, "setThreshold3")
	self.on_trait_change(self.threshold_changed3, "thresholdPercent3")
	self.on_trait_change(self.setThresholdPercent_fired3, "setThresholdPercent3")
	
	self.on_trait_change(self.threshold_changed4, "threshold4")
	self.on_trait_change(self.setThreshold_fired4, "setThreshold4")
	self.on_trait_change(self.threshold_changed4, "thresholdPercent4")
	self.on_trait_change(self.setThresholdPercent_fired4, "setThresholdPercent4")
	
	# allVolRenderingOptions
	self.on_trait_change(self.enableVolRenderingChanged, "enableVolRendering")
	self.on_trait_change(self.removeVolRenderChanged, "removeVolRender")
	
	# allSliceOptions
	self.on_trait_change(self.enableSliceChanged, "enableSlice")
	self.on_trait_change(self.removeSliceChanged, "removeSlice")
	# self.on_trait_change(self.enableSliceChanged, "whichSliceX")
	# self.on_trait_change(self.enableSliceChanged, "whichSliceY")
	# self.on_trait_change(self.enableSliceChanged, "whichSliceZ")
	
	# allStreamlineOptions
	self.on_trait_change(self.enableStreamlinesChanged, "enableStreamlines")
	self.on_trait_change(self.removeStreamlinesChanged, "removeStreamlines")
	
	# allSurfaceExtractionOptions
	self.on_trait_change(self.enableExtractStructures, "extractStructures")
	self.on_trait_change(self.extractSpecificStructure, "chooseStructure")
	
	# allPlaygroundOptions
	self.on_trait_change(self.generateStructureChanged, "GenerateStructure")
	# self.on_trait_change(self.removeStructure, "removeStructure")
	
	# allRealSpaceVisualizationOptions
	self.on_trait_change(self.computeLL_fired, "computeLL")
	
	# allAnalysisOptions
	self.on_trait_change(self.calculateQtensorChanged, "calculateQtensor")
	
	# timeUpdateBehavior
	self.on_trait_change(self.time_changed1, "whichTime1")
	self.on_trait_change(self.time_changed2, "whichTime2")
	self.on_trait_change(self.time_changed3, "whichTime3")
	self.on_trait_change(self.time_changed4, "whichTime4")
	self.on_trait_change(self.time_changedGlobal, "whichTimeGlobal")
	
	# activeDataControlClass
	# self.on_trait_change(self.chkbox_changed1, "chkBox1")
	self.on_trait_change(self.sc1_ts1_changed1, "screen1_ts1")
	self.on_trait_change(self.sc2_ts1_changed1, "screen2_ts1")
	self.on_trait_change(self.sc3_ts1_changed1, "screen3_ts1")
	self.on_trait_change(self.sc4_ts1_changed1, "screen4_ts1")
	
	self.on_trait_change(self.sc1_ts2_changed1, "screen1_ts2")
	self.on_trait_change(self.sc2_ts2_changed1, "screen2_ts2")
	self.on_trait_change(self.sc3_ts2_changed1, "screen3_ts2")
	self.on_trait_change(self.sc4_ts2_changed1, "screen4_ts2")
	
	self.on_trait_change(self.sc1_ts3_changed1, "screen1_ts3")
	self.on_trait_change(self.sc2_ts3_changed1, "screen2_ts3")
	self.on_trait_change(self.sc3_ts3_changed1, "screen3_ts3")
	self.on_trait_change(self.sc4_ts3_changed1, "screen4_ts3")
	
	self.on_trait_change(self.sc1_ts4_changed1, "screen1_ts4")
	self.on_trait_change(self.sc2_ts4_changed1, "screen2_ts4")
	self.on_trait_change(self.sc3_ts4_changed1, "screen3_ts4")
	self.on_trait_change(self.sc4_ts4_changed1, "screen4_ts4")
	
	self.on_trait_change(self.radioButton1_changed, "radioButton1")
	self.on_trait_change(self.radioButton2_changed, "radioButton2")
	self.on_trait_change(self.radioButton3_changed, "radioButton3")
	self.on_trait_change(self.radioButton4_changed, "radioButton4")
