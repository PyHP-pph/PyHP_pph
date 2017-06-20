__PLEASE NOTE: THIS NEEDS TO BE CHANGED TO COMPLY WITH RFC 2119!__
# Output
Taken from all inspiration languages. Style taken from all but PHP.

## Syntax
### Text to Standard Output
'Printing' text to standard output is done like so:
```
    Console.StandardOutputStream >> disp("text") >> Console.Characters.EndLine();
```
- `Console.StandatdOutputStream` is a special language feature that is not a stream.
- The `>>` chevrons are facing forwards to indicate a progressive language but have the same function as C++ backwards-facing chevrons.
- disp("text") creates a value that can go to `Console.StandatdOutputStream`. Simply using `"text"` will yeild a runtime error.
- `Console.Characters.EndLine()` is a function that returns a newline. There is no other way to append a newline. Using `"\n"` will append "newline" to your text.
