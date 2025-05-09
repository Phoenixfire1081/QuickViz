from traitsui.api import VGroup, HSplit, Group, Item, HGroup
from mayavi.core.ui.api import SceneEditor, MayaviScene

sceneUIelements = VGroup(
	HGroup(Item('scene1', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, visible_when='layout >= "1"'), 
	Item('scene2', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, visible_when='layout >= "2"'),
	),
	HGroup(Item('scene3', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, visible_when='layout >= "3"'), 
	Item('scene4', editor=SceneEditor(scene_class=MayaviScene),
	show_label = False, visible_when='layout >= "4"'),
	),
	),
