# Day 04 - Functions in Python

# 🧠 What is a Function?

A function is a reusable block of code used to perform a specific task.

Instead of writing same code again and again, create once and call many times.

---

# 📌 Why Functions?

Benefits:

* Reusable code
* Clean structure
* Easy maintenance
* Less repetition
* Better readability

---

# 📌 Basic Syntax

```python
def function_name():
    code
```

Call function:

```python
function_name()
```

---

# 🔹 Example 1: Simple Function

```python
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
```

---

# 🔹 Parameters and Arguments

## Parameter

Input variable inside function definition.

## Argument

Actual value passed while calling function.

```python
def greet(name):
    print(f"Hello {name}")

greet("Mabu")
```

Output:

```text
Hello Mabu
```

---

# 🔹 Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(5, 3)
```

Output:

```text
8
```

---

# 🔹 return Keyword

Used to send result back from function.

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

Output:

```text
15
```

---

# 🔹 Difference: print vs return

## print()

Displays result only.

## return()

Sends value back to caller so it can be stored or reused.

---

# 🔹 Example: Square Function

```python
def square(x):
    return x * x

print(square(4))
```

Output:

```text
16
```

---

# 💻 Real-Time DevOps Examples

## CPU Status Checker

```python
def cpu_status(cpu):
    if cpu > 80:
        return "High CPU"
    return "Normal"

print(cpu_status(85))
```

---

## Deployment Message

```python
def deploy(app):
    print(f"Deploying {app}")

deploy("payment-service")
```

---

# 📌 Important Learnings

* Function is created using `def`
* Function runs only when called
* Parameters accept inputs
* return gives back result
* Functions help in automation scripts

---

# 📌 Summary

Functions are one of the most important concepts in Python and used heavily in real-world projects, scripting, DevOps automation, APIs, and applications.
