# Template Language

This is a potential specification meta-programming template language, as suggested by /u/alexbuzzbee. It is designed to be highly versatile, and therefore contains many concepts from traditional programming languages. It is inspired by FORTH, erlang and, of course, C++ templates.

## Syntax

The basic syntax will consist of a tag surrounded by angle brackets.

```
command ::= "<" + tag + ">
```

A tag is be any ascii string without whitespace.

## Execution

Execution occurs at compile time, before most other attempts to parse the actual content.
When a tag is encountered, its content is compared to a list of action tags. If the tag is an action tag, the compiler will perform the associated action. If the tag is not an action tag, the tag is pushed onto a stack.

A list of substitutions is maintained. When a tag is popped from the stack for any reason, it is implicitly run through this list of substitutions.

## List of default action tags

(We should add to this list as the specification grows. Also these names make way to much sense.)

`.` pops a tag from the stack and is replaced with its contents.

`^` pops two (2) tags from the stack (`trigger`, `result`) and creates a substitution from `trigger` to `result`.

`if` pops two tags from the stack (`condition`, `value`) and is replaced with `value`'s contents if `condition` is truthy.

`ifn` pops two tags from the stack (`condition`, `value`) and is replaced with `value`'s contents if `condition` is falsey.

`+` pops two tags from the stack (`a`, `b`), converts them to numbers, and adds them, pushing the final value onto the stack.

## Truthy and falsey values

All values are truthy except the following, which are falsey:

- `no`
- `false`
- `0`
- An empty tag
- The bottom of the stack

## Example

Here is an example:

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

The final output of this is:

```


2
```
