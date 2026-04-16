# Day 02 - Operators & Conditions

# 🧠 What are Operators?

Operators are symbols used to perform operations on values and variables.

Example:

```python id="j3t8w5"
a = 10
b = 5

print(a + b)
```

Output:

```text id="g2p7m4"
15
```

---

# 📌 Types of Operators

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators

---

# 🔹 1. Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning        | Example |
| -------- | -------------- | ------- |
| +        | Addition       | 10 + 5  |
| -        | Subtraction    | 10 - 5  |
| *        | Multiplication | 10 * 5  |
| /        | Division       | 10 / 5  |
| //       | Floor Division | 10 // 3 |
| %        | Modulus        | 10 % 3  |
| **       | Power          | 2 ** 3  |

---

## Example

```python id="q9w4e2"
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 🔹 2. Comparison Operators

Used to compare values. Returns `True` or `False`.

| Operator | Meaning               |
| -------- | --------------------- |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |
| ==       | Equal                 |
| !=       | Not equal             |

---

## Example

```python id="k7p1x9"
age = 18

print(age >= 18)
print(age == 18)
print(age != 20)
```

---

# 🔹 3. Logical Operators

Used to combine conditions.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| and      | Both conditions must be True |
| or       | At least one True            |
| not      | Reverse result               |

---

## Example

```python id="p2m8z4"
cpu = 85
memory = 70

print(cpu > 80 and memory > 80)
print(cpu > 80 or memory > 80)
print(not cpu < 80)
```

---

# 🧠 Conditions in Python

Used for decision making.

---

# 🔹 if Statement

```python id="v6r3n1"
age = 20

if age >= 18:
    print("Adult")
```

---

# 🔹 if else

```python id="t9m4q7"
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# 🔹 if elif else

```python id="f1k5w8"
marks = 78

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

---

# 🔹 Nested if

```python id="n7z2m5"
logged_in = True
role = "admin"

if logged_in:
    if role == "admin":
        print("Admin Access")
    else:
        print("User Access")
else:
    print("Login First")
```

---

# 💻 Real-Time DevOps Examples

## CPU Alert

```python id="d4x7p2"
cpu = 85

if cpu > 80:
    print("High CPU Alert")
else:
    print("CPU Normal")
```

---

## Login Check

```python id="r8t3k1"
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Success")
else:
    print("Login Failed")
```

---

# 📌 Summary

* Operators perform actions on data.
* Comparison operators return True/False.
* Logical operators combine conditions.
* if/else used for decision making.
* Nested if handles multi-step checks.
