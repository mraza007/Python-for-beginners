# Iterators and Generators

### Iterator
Iterator is an object that can be iterated upon. An object which returns data,one element at a time when next() is called on it.

### Iterable
An object which will return an Iterator when `iter()` is called on it.

For example `"HELLO"` is an iterable but its not an iterator but `iter("HELLO")` returns an iterator.

### `NEXT()`
When `next()` is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a `StopIteration` error.

```python
def custom_iter(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(interator))
        except StopIteration:
            print("END")
            break
```

### Generators
- Generators are iterators.
- Generator can be created with generator functions