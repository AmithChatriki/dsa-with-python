
# Arrays — Linear Data Structure (DSA Notes)

## 1. Definition
An **array** is a linear data structure that stores a collection of elements in contiguous memory locations.  
Each element is identified by an **index** (typically starting at 0).

Key properties:
- Ordered collection (sequence matters).
- Random access in **O(1)** using index.
- Fixed size in static arrays.

**Python perspective:**  
Python doesn’t have raw arrays like C/C++. Instead, `list` is a dynamic array under the hood — it stores **references** to objects.

---

## 2. Advantages
- **Fast random access** → `arr[i]` is O(1).
- Simple and widely used.
- Great for implementing other data structures (heaps, hash tables).

---

## 3. Disadvantages & Fixes

### Disadvantage 1: Fixed Size
- Static arrays require size at creation.
- Resizing is costly (new allocation + copy).

**Solution → Dynamic Arrays**  
- Use a resize strategy (commonly double capacity when full).
- Amortized complexity: `append()` is O(1).

### Disadvantage 2: Homogeneous
- In low-level typed languages, all elements must be the same type (`int[]`, `float[]`).

**Solution → Referential Arrays**
- Store references instead of raw values.  
- Allows polymorphism or mixed data types.  
- Example: Python lists (`[1, "hello", 3.14]`) can hold heterogeneous values.

---

## 4. Time Complexity (Common Operations)
| Operation | Average Complexity | Notes |
|-----------|--------------------|-------|
| Access (arr[i]) | O(1) | Direct index access |
| Search (unsorted) | O(n) | Linear scan |
| Insert at end | O(1) amortized | May trigger resize |
| Insert/delete at index | O(n) | Needs shifting |
| Traverse | O(n) | Visit each element |

---

## 5. Python Examples

```python
# Create array (list)
arr = [10, 20, 30]

# Access elements
print(arr[1])       # 20
print(arr[-1])      # 30 (last element)

# Append and Pop
arr.append(40)      # [10,20,30,40]
print(arr.pop())    # removes 40

# Insert and Delete
arr.insert(1, 15)   # [10,15,20,30]
del arr[2]          # removes 20 → [10,15,30]

# Slicing
print(arr[1:3])     # [15,30]

# Iteration
for val in arr:
    print(val)
```

---

## 6. Dynamic Array Implementation (Educational)

```python
import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("index out of range")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, new_cap):
        B = self._make_array(new_cap)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = new_cap

    def _make_array(self, cap):
        return (cap * ctypes.py_object)()
```

This demonstrates **capacity doubling** when full.

---

## 7. Heterogeneous Arrays (Referential)

```python
# Mixed types
arr = [1, "hello", 3.14, {"key": "value"}]

# Polymorphism
class Animal:
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "woof"

class Cat(Animal):
    def speak(self): return "meow"

zoo = [Dog(), Cat(), Dog()]
for a in zoo:
    print(a.speak())
```

---

## 8. When to Use Arrays
- Need **fast random access** by index.
- Memory efficiency & cache friendliness matter.
- Building blocks for other DS (heaps, hash tables).

**Avoid arrays when:**
- Frequent insert/delete in middle → use linked list.  
- Need O(1) push/pop at both ends → use `collections.deque`.  
- Heavy numeric computations → use `numpy.ndarray`.

---

## 9. Practice Problems
1. Reverse an array in place.  
2. Rotate array by `k` steps.  
3. Find missing number in 1..n.  
4. Implement two-sum problem.  
5. Move all zeroes to end in-place.  

---

## 10. Summary
- **Arrays = ordered, indexable, contiguous memory.**
- Static arrays → fixed size.  
- Dynamic arrays → resizable with amortized O(1) append.  
- Homogeneous limitation → solved by referential arrays (Python `list`).  

---

*End of Arrays Notes*
