# Strings

From all inspiration languages.

## Syntax and semantics

There SHALL be a type `singleString` and `DOUBLE_STRING`. Single strings MUST be enclosed in single quotes and vice versa.

There SHALL be a type `char` which MUST hold exactly one byte. Chars SHALL be represented as either a one-character string or an integer -127 to 128. The number given to a char MUST be treated as a hexadecimal, but is still represented as a decimal number and therefore cannot allow the numbers A-F. 

Characters in a string or char SHALL be escaped within strings with backslashes.

## Examples

Here is an example of a basic string declaration.

```
DOUBLE_STRING $str1 = new DOUBLE_STRING("TOP TEN LIST of CLICKBAIT STRINGS! You'll NEVER BELIEVE the 3rd!!!");
singleString $str2 = new singleString('Doctors HATE him. Click >>>here<<< to find out his one weird trick.');
```

Here are two examples of the same char declaration.

```
char $a1 = new char("a");
char $a2 = new char(61); //#* 0x61 is the hex ASCII code for "a".
```
