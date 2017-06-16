# Indentation

From Python

## Syntax

After the start of a bracket-denoted block (square, curly or regular), lines must be indented from said brackets by whitespace in the form of a fixed, consistent number of tabs or spaces, until the end of the block. The brackets denoting the beginnings and ends of blocks must also be indented, if they are on their own lines. One line of code can, obviously, be indented multiple times.

## Example

The Original Example Code provides an example:

```
if ($self->AwareOfIncompetence() == True) //#* Code outside a block not indented.
    { //#* Start bracket indented once from surrounding code.
        return; //#* Code inside the block indented once from the brackets.
    } //#* End bracket indented once from surrounding code.
```

This would not compile:

```
if ($self->AwareOfIncompetence() == True) //#* Code outside a block not indented; valid.
{ //#* Start bracket on its own line not indented; INVALID!
    return; //#* Code inside the block indented once from the brackets; valid.
} //#* End bracket on its own line not indented; INVALID!
```

But this would:

```
if ($self->AwareOfIncompetence() == True) { //#* Start bracket on same line as other code not indented.
        return; //#* Code inside the start bracket indented once from the brackets.
    } //#* End bracket indented once from surrounding code.
```

As would this:

```
if ($self->AwareOfIncompetence() == True) //#* Code outside a block not indented.
    { //#* Start bracket indented once from surrounding code.
        return; } //#* End bracket on same line as other code not indented.
```

And so would this:
```
if ($self->AwareOfIncompetence() == True) { return; } //#* Everything on same line not indented.
```
