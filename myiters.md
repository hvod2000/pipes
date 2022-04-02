# My rethinking of iterators in python

Module giving us all operations with iterators packed into Iter class.


# Syntax

The basic syntax is something like this:

```python
>>> from myiters import Iter
>>> Iter(range(12)).map(lambda x: 1 + x * 2) / sum
144

```

# Lazy evaluation

Every method of an Iter object is evaluated lazily:

```python
>>> def tee(iterator, prompt):
...     for item in iterator:
...         print(prompt, item)
...         yield item

>>> print(Iter(range(100)).tee("tee 1:").tee("tee 2:").slice(2) / list)
tee 1: 0
tee 2: 0
tee 1: 1
tee 2: 1
[0, 1]

```
