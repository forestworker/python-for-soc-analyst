# Python for SOC Analyst – Programming Fundamentals

This project contains a series of Python lessons and exercises aimed at beginners aspiring to work as SOC (Security Operations Center) Analysts. Each lesson includes explanations, source code, and practical use cases focused on cybersecurity.

---

## Table of Contents:
- [Lesson 1](#lesson-1-print-and-first-script)
- [Lesson 2](#lesson-2-variables-and-data-types)
- [Lesson 3](#lesson-3-operations-and-input)
- [Lesson 4](#lesson-4-conditional-statements-if-elif-else)
- [Lesson 5](#lesson-5-lists-loops-and-zip)
- [Lesson 6 (bonus)](#lesson-6-bonus-log-file-reading-and-error-detection)

---

## Lesson 1: `print()` and First Script

```python
print("Hello, SOC World!")
```

---

## Lesson 2: Variables and Data Types

```python
my_name = "Dawid"
age = 32
wants_to_be_soc1 = True

print(my_name)
print(age)
print(wants_to_be_soc1)
```

---

## Lesson 3: Operations and `input()`

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"{name}, in 5 years you will be {age + 5} years old.")
```

---

## Lesson 4: Conditional Statements `if`, `elif`, `else`

```python
name = input("What is your name? ")
failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins >= 5:
    print(f"ALERT! Possible brute-force attack on account {name}!")
elif failed_logins >= 3:
    print(f"Warning {name}, suspicious activity detected.")
else:
    print(f"All clear, {name}.")
```

---

## Lesson 5: Lists, Loops and `zip()`

```python
names = ["Dawid", "Ola", "Gosia"]
attempts = [1, 3, 5]

for name, num_attempts in zip(names, attempts):
    if num_attempts >= 5:
        print(f"ALERT! {name} had {num_attempts} failed login attempts!")
    elif num_attempts >= 3:
        print(f"Warning: {name} had {num_attempts} failed logins.")
    else:
        print(f"OK: {name} had only {num_attempts} attempts.")
```

---

## Lesson 6 (bonus): Log File Reading

Example contents of `logs.txt`:

```
2025-07-25 12:00 - INFO - Dawid logged in
2025-07-25 12:01 - WARNING - Ola entered wrong password
2025-07-25 12:02 - ERROR - Intrusion attempt from IP: 192.168.1.13
```

```python
with open("logs.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print("ALERT! Error found:", line.strip())
```

---
