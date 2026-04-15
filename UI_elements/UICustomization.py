# Supplement to Mayavi Visualization
# All UI customization options are defined here

from collections import Counter
import string

class UIOptionsClass:
	
	def __init__(self):
		
		# Number of pixels for each letter
		self.spacingFactorLetters = 6.5
		self.spacingFactorOthers = 3
	
	def count_letters(self, word, valid_letters=string.ascii_letters):
		count = Counter(word) 
		return sum(count[letter] for letter in valid_letters) 
	
	def textFieldTinySmallWidth(self):
		
		# For very small checkbox
		# Values with 0 - 1 
		
		width = -20
		height = -20
		
		return width, height
	
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
	
	def buttonLonger(self):
		
		# Longer buttons
		
		width = -150
		height = -30
		
		return width, height
		
	def button(self):
		
		# Button
		
		width = -80
		height = -30
		
		return width, height
	
	def determineWidth(self, _word):
		
		actual_letters = self.count_letters(_word)
		_diff = len(_word) - actual_letters
		
		return -actual_letters * self.spacingFactorLetters - _diff * self.spacingFactorOthers
	
	
