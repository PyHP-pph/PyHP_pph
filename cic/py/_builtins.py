from function import PyHP_PPH_Function

# WARN: print is a function added by this CIC. It is not guaranteed to stay this way.
def pyhp_pph_print(*args):
	print(' '.join([x.to_string() for x in args]))

builtins = {
	"print": pyhp_pph_print
}
