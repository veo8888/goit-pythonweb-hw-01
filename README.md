# goit-pythonweb-hw-01

## 🧩 Independent Work

### as part of the _FullStack Web Development with Python_ course

**Topic:** Design Patterns and SOLID Principles

### 📘 Project Overview

This repository contains **two independent assignments**, each implemented as a separate module:

1. **Factory Pattern**

   - Demonstrates the _Factory_ design pattern for creating objects through a factory method.
   - Focuses on extensibility and simplifying code maintenance.

2. **Library (SOLID Principles)**
   - Refactored a simple library management program according to the **SOLID** principles:
     - **SRP** – each class has a single responsibility.
     - **OCP** – open for extension, closed for modification.
     - **LSP** – subclasses can substitute their base classes without breaking functionality.
     - **ISP** – interfaces are clearly separated by purpose.
     - **DIP** – high-level modules depend on abstractions, not concrete implementations.

Both projects are managed using **PIPX** and **Poetry**, and are fully compatible with **Python 3.13**.

### ⚙️ Environment Setup

#### 1. Install `pipx`

```bash
python -m pip install --user pipx
```

#### 2. Ensure the path is configured

```bash
python -m pipx ensurepath
```

#### 3. Install Poetry

```bash
pipx install poetry
```

### 🚀 Running the Projects

Each project includes its own minimal README.md
with detailed launch and cleanup instructions:

- /factory/README.md – for the Factory project
- /library/README.md – for the Library project

### 📦 Technologies Used

- Python 3.13+
- pipx
- Poetry
- Factory Design Pattern
- SOLID Principles
