from object import PyHP_PPH_Object

class PyHP_PPH_Number(PyHP_PPH_Object):
	def __init__(self, number):
		super().__init__()

		self.value = number

	def to_number(self):
		return self.value
