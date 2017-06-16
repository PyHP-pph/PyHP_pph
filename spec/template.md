# Template Language

This is a potential specification meta-programming template language, as suggested by /u/alexbuzzbee. It is designed to be highly versatile, and therefore contains many concepts from traditional programming languages. It is inspired by FORTH, erlang and, of course, C++ templates.

## Syntax

The basic syntax SHALL consist of a tag surrounded by angle brackets:

```
command ::= "<" + tag + ">
```

A tag MAY be any ascii string without whitespace.

## Execution

Execution SHALL occur at compile time, before other attempts to parse the source file. When a tag is encountered, its content SHALL be compared to a list of action tags. If the tag is an action tag, the compiler SHALL perform the associated action. If the tag is not an action tag, the tag SHALL be pushed onto a stack.

A list of substitutions SHALL be maintained. When a tag is popped from the stack for any reason, it SHALL be implicitly run through this list of substitutions.

## List of default action tags

(We should add to this list as the specification grows. Also these names make way to much sense.)

`.` SHALL pop a tag from the stack and be replaced with its contents.

`^` SHALL pop two (2) tags from the stack (`trigger`, `result`) and create a substitution from `trigger` to `result`.

`if` SHALL pop two tags from the stack (`condition`, `value`) and be replaced with `value`'s contents if and only if `condition` is truthy. If `condition` is falsey, the `if` tag SHALL be deleted.

`ifn` SHALL pop two tags from the stack (`condition`, `value`) and be replaced with `value`'s contents if `condition` is falsey. If `condition` is truthy, the `ifn` tag SHALL be deleted.

`+` SHALL pop two tags from the stack (`a`, `b`), convert them to numbers, and add them, pushing the final value onto the stack.

`-` SHALL pop two tags from the stack (`a`,`b`), convert them to numbers, and subtract them, pushing the final value onto the stack.

`*` SHALL pop two tags from the stack (`a`,`b`), convert them to numbers, and multiply them, pushing the final value onto the stack.

`/` SHALL pop two tags from the stack (`a`,`b`), convert them to numbers, and divide them, pushing the final value onto the stack.

`==` SHALL pop two tags from the stack (`a`,`b`); if they are the same, the tag `true` will be pushed onto the stack, otherwise the tag `false` will be pushed.

`!=` SHALL pop two tags from the stack (`a`,`b`); if they are the same, the tag `false` will be pushed onto the stack, otherwise the tag `true` will be pushed.


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
