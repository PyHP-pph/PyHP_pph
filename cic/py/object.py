from exception import PyHP_PPH_Exception

# All objects in PyHP++# extend this. As more features are added to the spec, this will get updated and extended.
class PyHP_PPH_Object:
	# WARN: A specification for unhandled number conversion is not set.
	def to_number(self):
		raise PyHP_PPH_Exception("Attempt to convert a non-number object to a number.")

	# WARN: A specification for string conversion is not set.
	def to_string(self):
		return str(self.value)

	# WARN: A specification for unhandled calling is not set.
	def call(self, *args):
		return PyHP_PPH_Exception("Attempt to call a non-function object.")
