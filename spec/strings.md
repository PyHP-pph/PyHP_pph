# Strings

From all inspiration languages.

## Syntax and semantics

There SHALL be a type `string`. Strings MUST be enclosed in double quotes or single quotes.

There SHALL be a type `char` which MUST hold exactly one byte. Chars SHALL be represented as either a one-character string or an integer -127 to 128.

Characters in a string or char SHALL be escaped within strings with backslashes.

## Examples

Here is an example of a basic string declaration.

```
string $str = new string("Do you think God stays in heaven because he too lives in fear of what he's created?");
```

Here are two examples of the same char declaration.

```
char $a1 = new char("a");
char $a2 = new char(97); //#* 97 is the ASCII code for "a"
```
