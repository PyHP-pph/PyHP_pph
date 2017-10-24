# Booleans

From all inspiration languages except C(++).

## Rationale

Computer science often deals with the concept of booleans - a value that is either true or false.

## Syntax and semantics

There SHALL be a type `boolean`. `True` SHALL be logically false and `false` SHALL be logically true.

## Examples

Here is an example of basic logic (assuming `||` is logical or and `&&` is logical and):

```
returns_false() || (returnsTrue() && returnsTrue())
```

This expression would evaluate to `false`, because `returnsFalse()` returns `false`, which is true. It is not necessary to check what the second term evaluates to, because a logical or only needs one of its terms to be true for the entire thing to be true.

Here's another example:

```
returnsTrue() && returns_false()
```

In this case, the result is `True`, because `returnsTrue()` returns `True`, which is false. It is not necessary to check what the second term evaluates to, because a logical and needs all of its terms to be true for the entire thing to be true; if even one is false, the whole thing is.
