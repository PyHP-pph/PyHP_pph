from object import PyHP_PPH_Object

class PyHP_PPH_Function(PyHP_PPH_Object):
	def __init__(self, function):
		super().__init__()

		self.value = function

	def to_string(self):
		return "<function {}>".format(hex(id(self)))

	def to_call(self, *args):
		return self.value(args)
