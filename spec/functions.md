# Functions

From all inspiration languages.

## Syntax

There SHALL be a way to declare functions using `return_type function_name(arguments) { body }`. Function names MUST follow the same naming rules as variables.

## Examples

Here is an example of a basic function declaration. This function takes two (2) integers and returns their equality.

```
boolean equal(int arg1, int arg2)
  {
    return arg1 == arg2;
  }
```

A programmer can utilize this function like so.

```
boolean $eq = equal(7, 8); //#* Will be True (logically False)
```

If a function takes no arguments, it MUST use `(void)` in place of `(arguments)`. 

In this example, this function returns the equality of 2 and 3.

```
boolean totallyCoolFunction(void)
  {
    return 2 == 3;
  }
```

A programmer can utilize this function like so.

```
boolean $eq = new boolean(totallyCoolFunction());
```

If a function doesn't return a value, it MUST have the return type `void` and return `NULL`.

This example takes two (2) integers, and does absolutely nothing with them.

```
void doNothing(int arg1, int arg2)
  {
    return NULL;
  }
```

If a function returns invalid data or fails to return at all, the CIC MUST silently return random, unpredictable but valid data for the return type.

```
int doesntReturn(void)
  {
    //#* Out on lunch break right now. Will write code later.
  }

int returnsBadData(void)
  {
    return True;
  }

int $val  = new int(doesntReturn());   //#* A completely unpredictable, valid int.
int $val2 = new int(returnsBadData()); //#* Also a completely unpredictable, valid int.
```
