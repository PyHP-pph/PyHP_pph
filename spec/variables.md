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

`del` MUST remove the variable from memory and all later uses of a deleted variable SHOULD be `null`.
