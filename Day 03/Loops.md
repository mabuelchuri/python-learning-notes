# Day 03 - Loops in Python

# 🧠 What is a Loop?

A loop is used to repeat a block of code multiple times without writing the same code again and again.

Used for:

* Automation
* Bulk operations
* Checking multiple servers
* Processing files
* Repeating tasks

---

# 📌 Types of Loops in Python

1. for loop
2. while loop

---

# 🔹 1. for Loop

Used when number of repetitions is known.

## Syntax

```python id="j4t8m1"
for i in range(5):
    print(i)
```

Output:

```text id="v7k2p5"
0
1
2
3
4
```

---

# 📌 range() Function

Used to generate sequence of numbers.

## Forms of range()

### range(stop)

```python id="w9m3q7"
range(5)
```

Gives:

```text id="f2x8n4"
0,1,2,3,4
```

---

### range(start, stop)

```python id="r5k1d9"
range(2,5)
```

Gives:

```text id="h6p4t1"
2,3,4
```

---

### range(start, stop, step)

```python id="g3n7w2"
range(1,10,2)
```

Gives:

```text id="m8q2z5"
1,3,5,7,9
```

---

# 🔹 Examples

## Print 1 to 5

```python id="y6v3m8"
for i in range(1,6):
    print(i)
```

---

## Print Even Numbers

```python id="x2p7k4"
for i in range(2,11,2):
    print(i)
```

---

## Reverse Numbers

```python id="d5n1q9"
for i in range(10,0,-1):
    print(i)
```

---

# 🔹 2. while Loop

Used when repetition depends on condition.

## Syntax

```python id="u7k4m2"
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text id="b9r3x6"
1
2
3
4
5
```

---

# 📌 Increment / Decrement

```python id="q4m8p1"
count += 1
```

Increase by 1

```python id="t6k2w7"
count -= 1
```

Decrease by 1

---

# 🔹 break

Stops full loop immediately.

```python id="n3v7m5"
for i in range(1,6):
    if i == 3:
        break
    print(i)
```

Output:

```text id="z8p1k4"
1
2
```

---

# 🔹 continue

Skips current iteration only.

```python id="c7m2x9"
for i in range(1,6):
    if i == 3:
        continue
    print(i)
```

Output:

```text id="r4k9t6"
1
2
4
5
```

---

# 💻 Real-Time DevOps Examples

## Checking Servers

```python id="m5q8p2"
for server in range(1,4):
    print(f"Checking server {server}")
```

---

## Retry Deployment

```python id="k2n7w4"
retry = 1

while retry <= 3:
    print(f"Retry attempt {retry}")
    retry += 1
```

---

# 📌 Summary

* Loops repeat tasks automatically.
* for loop when count known.
* while loop when condition based.
* break stops loop.
* continue skips one round.
