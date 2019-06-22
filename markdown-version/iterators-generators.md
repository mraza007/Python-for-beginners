# Iterators and Generators

### Iterator
Iterator is an object that can be iterated upon. An object which returns data,one element at a time when next() is called on it.

### Iterable
An object which will return an Iterator when `iter()` is called on it.

For example `"HELLO"` is an iterable but its not an iterator but `iter("HELLO")` returns an iterator.