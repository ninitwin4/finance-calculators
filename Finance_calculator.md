# 💰 Finance Calculators

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌟 Highlights

- Choose between two financial calculators from a simple menu
- Investment calculator supports both **simple** and **compound** interest
- Bond (home loan) calculator gives you your **monthly repayment** amount
- Input is case-insensitive — type `BOND`, `bond`, or `Bond`, it all works!
- Clean error handling for invalid inputs

---

## ℹ️ Overview

**Finance Calculators** is a beginner Python project built as a capstone assignment. It simulates a real-world scenario where a small financial company needs a command-line tool that helps users make smarter financial decisions — whether they're planning an investment or figuring out their monthly home loan repayments.

The program uses core Python concepts like conditionals, user input, and the `math` module to perform accurate financial calculations.

### ✍️ Author

**NiNi** — [@ninitwin4](https://github.com/ninitwin4)

---

## 🚀 Usage

When you run the program, you'll be greeted with a menu:

```
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond':
```

**Example — Investment (Compound Interest):**
```
Enter either 'investment' or 'bond': investment
Enter the amount of money you are depositing: 1000
Enter the interest rate: 8
Enter the number of years you plan on investing: 20
Enter the type of interest, choose between 'simple' or 'compound': compound

Total amount: 4660.957...
```

**Example — Bond (Home Loan):**
```
Enter either 'investment' or 'bond': bond
Enter the present value of the house: 100000
Enter the interest rate: 7
Enter the number of months you plan to take to repay the bond: 120

Your monthly repayment is: 1161.08...
```

---

## ⬇️ Installation

### Prerequisites

- Python 3.x installed on your machine. Check by running:

```bash
python --version
```

If you don't have Python, download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/ninitwin4/finance-calculators.git
```

2. **Navigate into the project folder:**

```bash
cd finance-calculators
```

3. **Run the program:**

```bash
python finance_calculators.py
```

> No external libraries needed — the program only uses Python's built-in `math` module. ✅

---

## 🧮 The Maths Behind It

### Investment — Simple Interest
```
A = P * (1 + r * t)
```

### Investment — Compound Interest
```
A = P * (1 + r)^t
```

### Bond Repayment
```
repayment = (i * P) / (1 - (1 + i)^(-n))
```

Where:
- `P` = principal (deposit or house value)
- `r` = annual interest rate ÷ 100
- `t` = number of years
- `i` = monthly interest rate = (annual rate ÷ 100) ÷ 12
- `n` = number of months

---

