### ✅ Tuple Operations & Immutability – Day 10 Part 1


#### ✅ **Question 1: Tuple Basics**

👍 **Good**:

* Demonstrates tuple indexing, slicing, concatenation, repetition, and membership.

💡 **Suggestion**:

* Add example of `len(tup1)` and `max(tup1)` to reinforce common tuple functions.


#### ✅ **Question 2: `namedtuple` Usage**

👍 **Good**:

* Correct use of `collections.namedtuple`.

💡 **Suggestion**:

* Consider adding `_asdict()` for conversion to dictionary view:

```python
print(s1._asdict())
```


#### ✅ **Question 3: Tuple Unpacking**

👍 **Good**:

* Covers simple, nested, and starred unpacking.

💡 **Suggestion**:

* Explain how `*q` captures all middle values.


#### ✅ **Question 4: Tuples as Dictionary Keys**

👍 **Good**:

* Shows immutability use in dictionary keys.

💡 **Suggestion**:

* Add example of what happens if you try using a list as a key (i.e., will raise `TypeError`).


#### ✅ **Question 5: Tuple vs List Performance**

❗ **Improvement**:

* Missing print statements for performance comparison.

❗ **Fix**:

```python
print("Tuple creation time:", tuple_creation_time)
print("List creation time:", list_creation_time)
print("Tuple loop time:", tuple_loop_time)
print("List loop time:", list_loop_time)
```

💡 **Suggestion**:

* Use `timeit` setup strings for better benchmarking.


#### ✅ **Question 6: Geometry with Tuples**

👍 **Good**:

* Clean implementation of distance and midpoint.

💡 **Suggestion**:

* Add type hints and docstrings for better clarity.


#### ✅ **Question 7: Record Update System**

👍 **Good**:

* Shows real-world tuple record usage.

💡 **Suggestion**:

* Mention that original `records` list is reassigned after `update_age`.


#### ✅ **Question 8: Tuple Immutability Error**

👍 **Good**:

* Correctly catches immutability error.

💡 **Suggestion**:

* Briefly explain why tuples are immutable (hashable, memory optimization).


#### ✅ **Question 9: Tuple Hashing**

👍 **Good**:

* Demonstrates hash consistency with tuples.

💡 **Suggestion**:

* Explain hash difference due to ordering and nesting.


#### ✅ **Question 10: Tuple Comparison**

👍 **Good**:

* Shows pairwise comparison of tuples.

💡 **Suggestion**:

* Add return value preview of `compare_tuples`.


#### ✅ **Question 11: Tuple Serialization**

❗ **Improvement**:

* JSON doesn't preserve tuple — becomes list.

❗ **Fix**:

```python
tuple_from_json = tuple(json.loads(json_data))  # Converts back manually
```

💡 **Suggestion**:

* Mention that Pickle preserves tuple type.


#### ✅ **Question 12: Tuple Validation**

👍 **Good**:

* Covers multiple validation checks.

💡 **Suggestion**:

* Refactor into multiple helper functions for clarity.


#### ✅ **Question 13: Conversion Functions**

👍 **Good**:

* Solid type conversions.

❗ **Issue**:

* `to_dict(tup1)` will raise error since `tup1` is not key-value.

❗ **Fix**:

```python
# Add check before calling
if all(isinstance(i, tuple) and len(i) == 2 for i in tup1):
    print("Dictionary:", to_dict(tup1))
else:
    print("Invalid format for dictionary conversion")
```


#### ✅ **Question 14: Memory Comparison**

👍 **Good**:

* Accurate use of `sys.getsizeof`.

💡 **Suggestion**:

* Mention that `getsizeof()` shows only object size, not contents recursively.


#### ✅ **Question 15: Stack Using Tuples**

👍 **Good**:

* Well-implemented stack pattern using immutable structure.

💡 **Suggestion**:

* Add peek functionality as an enhancement.


### ✅ Advanced Sequence Operations – Day 10 Part 2


#### ✅ **Question 1: Advanced Slicing**

👍 **Good**:

* Uses negative stepping creatively.

💡 **Suggestion**:

* Add visual explanation of the slice `[-2:0:-3]`.


#### ✅ **Question 2: Custom List Class**

👍 **Good**:

* Implements custom iterable correctly.

💡 **Suggestion**:

* Add support for `__contains__` to allow `x in my_list_q2`.


#### ✅ **Question 3: Smart Indexer**

👍 **Good**:

* Provides flexible access with keywords.

💡 **Suggestion**:

* Add list of valid keys as class constant for clarity.


#### ✅ **Question 4: Fancy Iterator**

👍 **Good**:

* Shows custom iterator logic.

💡 **Suggestion**:

* Add note: Produces middle item once if length is odd.


#### ✅ **Question 5: Memory Efficiency**

👍 **Good**:

* Comparison of sizes among list, array, NumPy.

❗ **Fix**:

* For fair comparison, use:

```python
sys.getsizeof(array_q5.buffer_info())  # Or show length of bytes
```

💡 **Suggestion**:

* Mention NumPy uses compact C-based memory layout.


#### ✅ **Question 6: Fibonacci Generator**

👍 **Good**:

* Clear generator example.

💡 **Suggestion**:

* Add `yield from` alternative for recursion practice.


#### ✅ **Question 7: Caching Decorator**

👍 **Good**:

* Implements function memoization.

💡 **Suggestion**:

* Use `functools.lru_cache()` in real apps for simplicity.


#### ✅ **Question 8: Sequence Validator**

👍 **Good**:

* Comprehensive validation.

💡 **Suggestion**:

* Separate validations into helper functions for readability.


#### ✅ **Question 9: Functional Programming**

👍 **Good**:

* Shows map-filter-reduce effectively.

💡 **Suggestion**:

* Show intermediate values for transparency.


#### ✅ **Question 10: Run-Length Encoding**

👍 **Good**:

* Accurate implementation.

💡 **Suggestion**:

* Add decoding function for completeness.


#### ✅ **Question 11: Subsequence Check**

👍 **Good**:

* Basic substring match.

💡 **Suggestion**:

* Rename function to `is_exact_sublist()` to clarify behavior.


#### ✅ **Question 12: Sequence Difference**

👍 **Good**:

* Uses set for exclusion.

❗ **Caution**:

* Removes all occurrences even duplicates — worth noting.


#### ✅ **Question 13: Merge Sorted Lists**

👍 **Good**:

* Standard two-pointer merge.

💡 **Suggestion**:

* Add test case where one list is empty.


#### ✅ **Question 14: List Chunking**

👍 **Good**:

* Efficient chunking using step.

💡 **Suggestion**:

* Return as generator for memory efficiency.


#### ✅ **Question 15: Reversal Techniques**

👍 **Good**:

* Shows three reverse approaches.

💡 **Suggestion**:

* Time the three versions for performance insights.


### ✅ **Overall Suggestions**:

#### 🔍 Common Enhancements:

* ✅ Add `type hints` & `docstrings` for all functions.
* ✅ Use `f-strings` instead of `print("X:", x)` for cleaner output.
* ✅ Add test cases for edge cases (e.g. empty input, large input).
* ✅ Wrap all test prints inside `if __name__ == "__main__":` for better structure.
* ✅ Where possible, provide both the **concept** and a **real-life use case**.

