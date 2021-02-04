


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
print(sys.getsizeof(mything))
# 72
mystring = 'my name is ...'
print(sys.getsizeof(mystring))
# 63
```

flatten list

```python
"""
Example:
    [[1, 2,] [4, 7], [3, 17]]
    # after flatten
    [1, 2, 4, 7, 3, 17]
"""

x = [[1, 2], [4, 7], [3, 17]]

# with list comprehension
print([i for sub in x for i in sub])
# [1, 2, 4, 7, 3, 17]

# with itertools 
import itertools

print(list(itertools.chain(*x)))  # unpacking
# [1, 2, 4, 7, 3, 17]
print(list(itertools.chain.from_iterable(x)))
# [1, 2, 4, 7, 3, 17]
```