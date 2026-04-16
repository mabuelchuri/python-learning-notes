# Day 01 - Variables & Data Types

# 🧠 What is Python?

Python is a high-level, easy-to-read programming language widely used in:

* Automation
* DevOps
* Web Development
* AI / Machine Learning
* Data Engineering

Python is beginner-friendly because syntax is simple and readable.

---

# 📌 Variables

Variables are containers used to store data values in memory.

## Example

```python id="m2k8w5"
name = "Mabu"
age = 28
```

## Explanation

* `name` stores text
* `age` stores number

You can reuse variables later.

```python id="g7v3q9"
print(name)
print(age)
```

---

# 📌 Rules for Variables

✅ Valid:

```python id="u8d4j2"
user_name = "Mabu"
age1 = 28
```

❌ Invalid:

```python id="h6p9r1"
1age = 28
user-name = "Mabu"
```

---

# 📌 Data Types

Different kinds of data stored in variables.

| Type  | Example | Meaning       |
| ----- | ------- | ------------- |
| str   | "hello" | Text          |
| int   | 10      | Whole numbers |
| float | 10.5    | Decimal       |
| bool  | True    | True/False    |

---

# 📌 Type Checking

Use `type()` to know variable data type.

```python id="p9x2m7"
age = 28
print(type(age))
```

Output:

```python id="t1v4c8"
<class 'int'>
```

---

# 📌 Type Conversion

Changing one data type into another.

## Example

```python id="c3n7w1"
age = "25"
age = int(age)
print(age + 1)
```

Output:

```python id="l5m8r3"
26
```

---

# 📌 Why Important?

In real world:

* User input comes as string
* Need conversion for calculations

---

# 📌 Summary

* Variables store data
* Data types define data kind
* Use `type()` to check type
* Use `int()`, `float()`, `str()` for conversion
