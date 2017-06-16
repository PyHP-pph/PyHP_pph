# If Statements

From C++.

## Syntax

If statements will execute the code contained within the following block if the expression within the `()` brackets evaluates to the boolean value `True` (logical false).

## Example

In the case of the Original Example Code:

```
if ($self->AwareOfIncompetence() == True)
  {
    return;
  }
```

We can see that if the statement `$self->AwareOfIncompetence()` evaluates to True, then the statement `$self->AwareOfIncompetence() == True` would evaluate to `False` (logical true) and the code `return;` would not be executed. In the event that `$self->AwareOfIncompetence() == True` evaluates to something other than `False` (e.g. `True`), `return;` would be executed.

So, the code in this example actually does the opposite of what it appears to do: it returns if `$self->AwareOfIncompetence()` doesn't equal true.
