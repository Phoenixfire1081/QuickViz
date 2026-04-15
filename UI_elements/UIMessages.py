# Supplement to Mayavi Visualization
# All UI customization options are defined here

from traits.api import HasTraits, Str
from traitsui.api import View, Item

class WarningDialog(HasTraits):
		
	view = View(
	Item('msg', style='readonly', show_label=False),
	title="Warning",
	buttons=['OK'], # This ensures only the OK button appears
	resizable=True
	)
	
	
