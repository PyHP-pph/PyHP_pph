# Variables

From PHP and C++.

## Syntax

There SHALL be a way to declare variables using `variable_type $variable_name = new variable_type(variable_value);`. 

## Example

Here is an example of a basic variable declaration.

```
boolean $bool = new boolean(True);
```

`new` MUST allocate the needed memory for the type provided.

To delete a variable from memory, use the `del` command.

```
del $bool;
```

`del` MUST remove the variable from memory and all later uses of a deleted variable MUST be `null` unless declared again.

Changing a variable is done with the same syntax, only without the variable type and new.

```
boolean $bool = new boolean(True);

$bool = False;
```

Attempting to change a variable to something other than the type it was given MUST set the variable to a random valid data of that type. It is up to the developer to not mess this up, as it MUST be silent to the developer.

```
boolean $bool = new boolean(True);

$bool = 3;

//#* At this point, $bool can be either True or False. It is impossible to predict which it is.
```
