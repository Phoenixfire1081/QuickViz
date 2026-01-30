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

blenderVisibility = 'allModeOptions == "Blender exports"'
blenderBBoxVisibility = 'allModeOptions == "Blender exports" and altBBox == True'

blenderExportUIelements = Group(

	HGroup(Item("SaveTxt", style = 'readonly', show_label = False, height = smallh, width = -90, visible_when = blenderVisibility),
	Item("save_path", show_label = False, height = longh, width = longw, visible_when = blenderVisibility),
	Item("choose_folder", show_label = False, height = buttonh, width = buttonw, visible_when = blenderVisibility),
	),

	HGroup(
	Item("allTimesTxt", style = 'readonly', show_label = False, height = tinyh, width = -60, visible_when = blenderVisibility),
	Item("allTimesBlender", show_label = False, height = tinyh, width = tinyw , visible_when = blenderVisibility),
	),
	
	HGroup(
	Item("altBBoxTxt", show_label = False, style = 'readonly', visible_when=blenderVisibility, height = smallh, width = -170,),
	Item("altBBox", show_label = False, visible_when=blenderVisibility),
	),
	
	HGroup(
	Item("reconnX1Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnX2Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceX2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minx1',  high_name='maxx1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY1Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnY2Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceY2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'miny1',  high_name='maxy1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ1Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ1_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	HGroup(
	Item("reconnZ2Txt", show_label = False, style = 'readonly', visible_when=blenderBBoxVisibility, height = smallh, width = -35,),
	Item("whichSliceZ2_reconn", show_label = False, editor=RangeEditor(mode='slider', low_name = 'minz1',  high_name='maxz1'), visible_when=blenderBBoxVisibility, width = sliderw),
	),
	
	
	HGroup(
	Item("exportSTLTxt", style = 'readonly', show_label = False, height = tinyh, width = -90, visible_when = blenderVisibility),
	Item("exportSTLBlender", show_label = False, visible_when = blenderVisibility, height = buttonh, width = buttonw),
	Item("adjustSurfaceTxt", style = 'readonly', show_label = False, height = tinyh, width = -500, visible_when = blenderVisibility),
	),

),
