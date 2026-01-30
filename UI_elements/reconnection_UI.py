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

reconnectionVisibility = 'allModeOptions == "Analysis" and allAnalysisOptions == "Reconnection"'
reconnectionQtensorVisibility = 'allModeOptions == "Analysis" and (allAnalysisOptions == "Reconnection" or allAnalysisOptions == "Q-tensor")'
reconnectionQtensorBBoxVisibility = 'allModeOptions == "Analysis" and altBBox == True and (allAnalysisOptions == "Q-tensor" or allAnalysisOptions == "Reconnection")'

reconnectionUIelements = Group(

	HGroup(
	Item("altBBoxTxt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorVisibility, height = smallh, width = -170,),
	Item("altBBox", show_label = False, visible_when=reconnectionQtensorVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=reconnectionQtensorBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=reconnectionQtensorBBoxVisibility, width = sliderw),
	),
	
	HGroup(
	Item("calcAndPlotTxt", show_label = False, style = 'readonly', visible_when=reconnectionVisibility, height = smallh, width = -180,),
	Item("calcReconnection", show_label = False, visible_when=reconnectionVisibility, height = buttonh, width = buttonw),
	),

),
