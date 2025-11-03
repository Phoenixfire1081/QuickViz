# Supplement to Mayavi Visualization
# All UI customization options are defined here

class UIOptionsClass:
	
	def textFieldTiny(self):
		
		# For very small text field entries
		# Values with 0 - 1 
		
		width = -40
		height = -20
		
		return width, height
	
	def textFieldSmall(self):
		
		# For very long text field entries
		
		width = -150
		height = -20
		
		return width, height
	
	def textFieldLong(self):
		
		# For very long text field entries
		
		width = -150
		height = -20
		
		return width, height
	
	def textFieldHuge(self):
		
		# For huge text field entries
		
		width = -300
		height = -100
		
		return width, height
	
	def slider(self):
		
		# Slider controls
		
		width = -400
		height = -20
		
		return width, height
	
	def slidertiny(self):
		
		# Tiny sliders
		
		width = -150
		height = -20
		
		return width, height
		
	def buttonLong(self):
		
		# Longer buttons
		
		width = -100
		height = -30
		
		return width, height
		
	def button(self):
		
		# Button
		
		width = -80
		height = -30
		
		return width, height
	
	
