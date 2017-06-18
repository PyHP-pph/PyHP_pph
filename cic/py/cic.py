"""
PyHP++# CIC written in Python 3.
This should be constantly updated with the spec.
Until some necessary additions are made to the spec, some temporary solutions are made.
For example, there is no official out function, so print is used.
Be warned that once an official addition is made, temporary functions WILL be deprecated or changed.

This does not support templating.
"""

# PyHP++# specific
from _builtins import builtins
from exception import PyHP_PPH_Exception
from number import PyHP_PPH_Number

# Stuff for parser
from arpeggio import *
from arpeggio import RegExMatch as _

# Grammar

# WARN: A specification for symbols has not been set. 
def symbol():
	return _(r"[A-Za-z_][A-Za-z_0-9]*")

# WARN: A specification for numbers has not been set.
def number():
	return _(r"\d*\.\d*|\d+")

# TODO: String support when the spec is finished.
def literal():
	return [number]

def expression():
	return [literal, function_call]

def statement():
	return [function_call]

# WARN: A specification for expression lists has not been set. For all I know, it could end up being separated by fucking greek commas.
#		...please don't do that.
def expression_list():
	return expression, ZeroOrMore(",", expression)

# WARN: A specification for calling has not been set, but is implied from example code.
def function_call():
	return symbol, "(", Optional(expression_list), ");"

def language():
	return ZeroOrMore(statement), EOF

# TODO: Include line numbers and positions in exceptions.
class PyHP_PPH_Visitor(PTNodeVisitor):
	def __init__(self, **kwargs):
		super().__init__(kwargs)

		self.scopes = [builtins]
		self.parser = kwargs["parser"]

	def find_variable(self, variable_name):
		for scope in self.scopes:
			if variable_name in scope:
				return scope

		# WARN: A specification for referencing unknown variables has not been set.
		raise PyHP_PPH_Exception("Undefined variable {} referenced.".format(variable_name))

	def visit_number(self, node, children):
		return PyHP_PPH_Number(node.value)

	def visit_expression_list(self, node, children):
		ret = []

		for expression in node:
			if type(expression) is not Terminal:
				#import pprint; pprint.PrettyPrinter().pprint(expression)
				ret.append(visit_parse_tree(expression, self))

		return ret

	def visit_symbol(self, node, children):
		return self.find_variable(node.value)[node.value]

	def visit_function_call(self, node, children):
		children.pop(0)(*children[0])

def pyhpp_run_string(code, filename="<string>"):
	parser = ParserPython(language, ws="\n\r ")
	parse_tree = parser.parse(code, filename)
	
	visit_parse_tree(parse_tree, PyHP_PPH_Visitor(parser=parse_tree))

def pyhpp_run_file(filename):
	with open(filename, "r") as file:
		content = file.read()

	pyhpp_run_string(content, filename)

if __name__ == "__main__":
	import sys

	try:
		pyhpp_run_file(sys.argv[1])
	except KeyError:
		print("cic.py filename")
		sys.exit()
	except FileNotFoundError:
		print("Could not find file.")
		sys.exit()
