# Day 05 - Lists in Python

# 🧠 What is a List?

A list is a collection of multiple values stored in a single variable.

Instead of creating many variables:

```python id="g1"
server1 = "web1"
server2 = "web2"
server3 = "db1"
```

Use a list:

```python id="g2"
servers = ["web1", "web2", "db1"]
```

---

# 📌 Why Lists are Important?

Lists are used in real projects for:

* Server names
* Usernames
* File names
* Logs
* Pod names
* Numbers
* API response data

---

# 📌 Creating a List

```python id="g3"
names = ["Mabu", "Ravi", "Anil"]
numbers = [10, 20, 30]
mixed = ["Mabu", 28, True, 5000.5]
```

Python lists can store mixed data types.

---

# 📌 Indexing

Each item in a list has an index position.

| Index | Value |
| ----- | ----- |
| 0     | Mabu  |
| 1     | Ravi  |
| 2     | Anil  |

```python id="g4"
names = ["Mabu", "Ravi", "Anil"]

print(names[0])
print(names[1])
```

Output:

```text id="g5"
Mabu
Ravi
```

---

# 📌 Negative Indexing

Access items from the end.

| Index | Value |
| ----- | ----- |
| -1    | Anil  |
| -2    | Ravi  |
| -3    | Mabu  |

```python id="g6"
print(names[-1])
```

Output:

```text id="g7"
Anil
```

---

# 📌 Updating List Items

Lists are mutable (changeable).

```python id="g8"
names = ["Mabu", "Ravi", "Anil"]

names[1] = "Rahul"

print(names)
```

Output:

```text id="g9"
['Mabu', 'Rahul', 'Anil']
```

---

# 📌 Length of List

Use `len()` to count items.

```python id="g10"
names = ["Mabu", "Ravi", "Anil"]

print(len(names))
```

Output:

```text id="g11"
3
```

---

# 📌 Common List Methods

## append()

Adds item at end.

```python id="g12"
fruits = ["apple", "banana"]
fruits.append("mango")
```

---

## insert()

Adds item at specific position.

```python id="g13"
nums = [1, 3]
nums.insert(1, 2)
```

---

## remove()

Removes by value.

```python id="g14"
names = ["A", "B", "C"]
names.remove("B")
```

---

## pop()

Removes last item by default.

```python id="g15"
data = [10, 20, 30]
data.pop()
```

---

# 📌 Looping Through Lists

```python id="g16"
servers = ["web1", "web2", "db1"]

for server in servers:
    print(server)
```

Output:

```text id="g17"
web1
web2
db1
```

---

# 📌 Index Based Loop

```python id="g18"
names = ["Mabu", "Ravi", "Anil"]

for i in range(len(names)):
    print(i, names[i])
```

Output:

```text id="g19"
0 Mabu
1 Ravi
2 Anil
```

---

# 📌 List Slicing

Used to get part of a list.

```python id="g20"
a = [1,2,3,4,5]
```

## First 3 items

```python id="g21"
a[:3]
```

Output:

```text id="g22"
[1,2,3]
```

## From index 2 to end

```python id="g23"
a[2:]
```

Output:

```text id="g24"
[3,4,5]
```

## Middle items

```python id="g25"
a[1:4]
```

Output:

```text id="g26"
[2,3,4]
```

## Reverse list

```python id="g27"
a[::-1]
```

Output:

```text id="g28"
[5,4,3,2,1]
```

---

# 📌 Important Learnings

* List index starts from 0
* Negative index starts from end
* Lists are mutable
* Slicing stop value is excluded
* Lists are heavily used in loops and automation

---

# 📌 Summary

Lists are one of the most important Python data structures and are widely used in scripting, DevOps automation, APIs, and real-world Python programs.
