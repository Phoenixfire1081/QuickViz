# Camera options
from traitsui.api import VGroup, HSplit, Group, Item, HGroup
from .UICustomization import UIOptionsClass

# Initialize UI layout customization
allUIOptions = UIOptionsClass()
tinyw, tinyh = allUIOptions.textFieldTiny()
smallw, smallh = allUIOptions.textFieldSmall()
longw, longh = allUIOptions.textFieldLong()
sliderw, sliderh = allUIOptions.slider()
slidertinyw, slidertinyh = allUIOptions.slidertiny()
buttonw, buttonh = allUIOptions.button()
buttonLongw, buttonLongh = allUIOptions.buttonLong()

cameraUIelements = (Group(label = 'Camera control'),
	Group(
	
	HGroup(
	Group(label = 'Current values:'),
	Item("camAzimuthG", label = 'Azimuth:', style='readonly'), 
	Item("camElevationG", label = 'Elevation:', style='readonly'), 
	Item("camRollG", label = 'Roll:', style='readonly'), 
	Item("camDistanceG", label = 'Distance:', style='readonly'), 
	Item("focalPointG1", label = ' Focal point:', style='readonly'),
	Item("focalPointG2", label = ',', style='readonly'),
	Item("focalPointG3", label = ',', style='readonly'),
	Item("updateCurrentVals", show_label = False)
	),
	
	HGroup(
	Group(label = 'Store camera positions:'),
	Item("saveCam1", show_label = False, height = buttonh, width = buttonw),
	Item("saveCam2", show_label = False, height = buttonh, width = buttonw),
	Item("saveCam3", show_label = False, height = buttonh, width = buttonw),
	Item("saveCam4", show_label = False, height = buttonh, width = buttonw),
	Item("saveCam5", show_label = False, height = buttonh, width = buttonw),
	Item("camReset", show_label = False, height = buttonh, width = buttonw)
	),
	
	HGroup(
	Item("azimuthTxt", show_label = False, style = 'readonly', height = smallh, width = -60), 
	Item("camAzimuthS", show_label = False, height = sliderh, width = sliderw), 
	
	Item("elevationTxt", show_label = False, style = 'readonly', height = smallh, width = -60), 
	Item("camElevationS", show_label = False, height = sliderh, width = sliderw), 
	
	Item("rollTxt", show_label = False, style = 'readonly', height = smallh, width = -30), 
	Item("camRollS", show_label = False, height = sliderh, width = sliderw),
	
	Item("distanceTxt", show_label = False, style = 'readonly', height = smallh, width = -60),
	Item("camDistanceS", show_label = False, height = tinyh, width = tinyw), 
	
	Item("focalPointTxt", show_label = False, style = 'readonly', height = smallh, width = -70),
	Item("focalPointS1", show_label = False, height = tinyh, width = tinyw),
	Item("focalPointS2", show_label = False, height = tinyh, width = tinyw),
	Item("focalPointS3", show_label = False, height = tinyh, width = tinyw)
	)
	,show_border = True, orientation = 'vertical', scrollable = True),)
