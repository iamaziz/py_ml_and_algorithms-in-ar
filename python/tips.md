


<div dir="rtl" lang="ar">


بعض الخفايا و التلميحات


</div>


e.g.

- Unpacking with *
- *args and **kwargs
- lambda and list comprehension


timing stuff


```python
from time import time


start = time()

# do some stuff here

end = time()


print(f'took {end - start:.3f} seconds')

```

calculate memory usage for an object

```python
import sys

mything = ['Hello', 'World']
print(f'size of my list is: {mything}')

mystring = 'my name is ...'
print(f'size of my string is: {mystring}')
```

flatten list

```python
"""
Example:
    >>> [[1, 2,] [4, 7], [3, 17]]
    >>> # after flatten
    >>> [1, 2, 4, 7, 3 17]
"""

>>> x = [[1, 2], [4, 7], [3, 17]]

>>> # list comprehension
>>> [i for sub in x for i in sub]
[1, 2, 4, 7, 3, 17]

>>> # itertools 
>>> import itertools
>>> list(itertools.chain(*x))  # unpacking
[1, 2, 4, 7, 3, 17]
>>> list(itertools.chain.from_iterable(x))
[1, 2, 4, 7, 3, 17]
```