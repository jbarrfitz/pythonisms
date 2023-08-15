# Pythonisms

## Jerry Barrows-Fitzgerald

dunder.py creates a class (Movie) and assigns several dunder methods to that class, including


- __str__: provides a user-friendly string for use in the print command
- __hash__: instructs Python how to create a hash from the object, allowing it to be used in dictionaries and other collections that require hashable objects

### Comparison Operators
For the Movie class, all comparison operators are performed using the rating attribute. For example, 
If object_1 is greater than object_2, it means that object_1's rating attribute is higher than 
object_2's rating property.

- __gt__: Is the object in question greater than the one it is being compared to?
- __ge__: Is the object in question greater than or equal to the one it is being compared to?
- __eq__: Is the object in question equal to the one it is being compared to?
- __ne__: Is the object in question not equal to the one it is being compared to?
- __lt__: Is the object in question less than the one it is being compared to?
- __le__: Is the object in question less than or equal to the one it is being compared to?

### To Install:
Clone this repository and open a virtual environment

```
pip install -r requirements.txt
```

### To Test:

```
pytest
```