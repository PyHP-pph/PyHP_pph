# Comments

From all inspiration languages.

## Rationale

Although our code is always perfect, other people may want to read it eventually, and will not understand our flawless logic and must have our code explained to their puny brains.

## Syntax and semantics

Comments are pieces of text that are ignored by the CIC. There SHALL be comment support when the CIC reaches `//#* ` outside of a string.

## Examples

The Original Example Code provides an example:

```
if ($self->AwareOfIncompetence() == True) //#* Code outside a block not indented.
    { //#* Start bracket indented once from surrounding code.
        return; //#* Code inside the block indented once from the brackets.
    } //#* End bracket indented once from surrounding code.
```

The text "Code outside a block not indented.", "Start bracket indented once from surrounding code.", etc are ignored by the CIC.

Comments MUST be indented properly like any other PyHP++# code. For example, this would compile:

```
if(True)
    //#* Properly indented comment.
    {
    }
```

But this would not:

```
if(True)
//#* Not properly indented comment.
    {
    }
```
