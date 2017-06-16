# Template Language

This is a potential specification meta-programming template language, as suggested by /u/alexbuzzbee.
It is designed to be highly versatile, and therefor contains many concepts from traditional programming languages.
It is inspired by FORTH, erlang and, of course, the C++ templates.

## Basic Syntax

The basic syntax will consist of a tag surrounded by angle brackets.
```
command ::= "<" + tag + ">
```

A tag must be any ascii string without whitespace.
Execution

Execution will occur at compile time, before most other attempts to parse the actual content.
When a command is encountered, it's tag is compared to a list of action-tags. If the tag is an action-tag, the compiler will preform the associated action.
If the tag is not an executor, the tag is pushed onto a stack.

A list of substitutions is maintained. When a tag is popped from the stack for any reason, it is implicitly run threw this list of substitutions.

## List of default execution tags

(We should append to this list as the specification grows. Also these names make way to much sense.)

`.` pops a tag from the stack and puts it at the current commands value in the program.

`^` pops two(2) tags from the stack (source, destination) and creates a substitution from source to destination.

`if` pops two tags from the stack (condition, value) and puts value if condition is truthy.

`ifn` pops two tags from the stack (condition, value) and puts value if condition is falsey.

`+` pops two tags from the stack (a,b), courses them to numbers, and adds them, pushing the final value onto the stack.

## Example

```
<yes>
<should_print>
<^>

<1>
<b>
<^>

<b>
<1>
<+>
<should_print>
<if>
```

will output `2`
