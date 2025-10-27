# Lab 5: Static Code Analysis

## Overview
Completed Lab 5 assignment on Static Code Analysis using Pylint, Flake8, and Bandit.

## Files
- `inventory_system.py` - Fixed and optimized inventory management system
- `Lab5` - Lab instructions

## Tools Used
1. **Pylint** - Code quality analysis
2. **Flake8** - PEP 8 style enforcement
3. **Bandit** - Security vulnerability scanning

## How to Run

### Install Tools
```bash
pip install pylint flake8 bandit
```

### Run Static Analysis
```bash
pylint inventory_system.py
flake8 inventory_system.py
bandit inventory_system.py
```

### Run the Code
```bash
python inventory_system.py
```

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.80/10 | 10.00/10 ✅ |
| Flake8 | 11 issues | 0 issues ✅ |
| Bandit | 2 vulnerabilities | 0 vulnerabilities ✅ |

## Major Fixes
- Added module and function docstrings
- Renamed functions to snake_case
- Fixed mutable default argument
- Used f-strings for formatting
- Specified exception types
- Used context managers for file operations
- Added encoding parameters
- **Removed eval()** (security vulnerability)
- Removed unused imports
- PEP 8 compliance

## Status
✅ **COMPLETED** - All static analysis tools report zero issues.

