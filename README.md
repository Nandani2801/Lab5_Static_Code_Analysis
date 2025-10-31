#  Lab 5: Static Code Analysis

##  Objective
To improve Python code quality, security, and style by using **Pylint**, **Bandit**, and **Flake8** to identify and fix issues in `inventory_system.py`.

---

##  Tools Used
- **Pylint** – Code quality and logical checks  
- **Flake8** – Style and formatting compliance (PEP8)  
- **Bandit** – Security vulnerability detection  

---

##  Known Issues Table

| Issue | Type | Line(s) | Description | Fixed Approach |
|--------|------|---------|--------------|----------------|
| Missing module / function docstrings (`C0114`, `C0116`) | Style | 1, 8, 14, 22, 25, 31, 36, 41, 48 | Code lacks proper docstrings for module and functions | Added concise docstrings describing purpose and parameters |
| Invalid naming style (`C0103`) | Style | 8, 14, 22, 25, 31, 36, 41 | Function names (`addItem`, `removeItem`, etc.) didn’t follow `snake_case` | Renamed to `add_item`, `remove_item`, `get_qty`, etc. |
| Dangerous default value (`W0102`) | Bug | 8 | Mutable list `logs=[]` shared across function calls | Used `logs=None` and initialized with `logs = []` inside function |
| Bare except (`W0702`, `E722`, `B110`) | Bug / Security | 19 | `except:` catches all exceptions silently | Used `except KeyError:` for specific exception; avoided silent pass |
| Unused import (`W0611`, `F401`) | Style | 2 | `logging` imported but never used | Removed unused import |
| Use of `eval` (`W0123`, `B307`) | Security | 59 | Insecure use of `eval()` to execute string code | Removed `eval()` or replaced with safer `ast.literal_eval` if needed |
| File open without context manager (`R1732`) | Best Practice | 26, 32 | `open()` used without context manager | Replaced with `with open(file, "r", encoding="utf-8") as f:` |
| Unspecified encoding (`W1514`) | Style | 26, 32 | File operations don’t specify encoding | Added `encoding="utf-8"` |
| Missing blank lines between functions (`E302`, `E305`) | Formatting | multiple | Functions not separated by 2 blank lines | Added spacing as per PEP 8 |
| String formatting improvement (`C0209`) | Style | 12 | Using `%` formatting where f-string possible | Used f-strings for cleaner readability |

---

##  Code Improvement Summary
- All function names and formatting now follow **PEP8**  
- Added docstrings for every function  
- Replaced unsafe `eval()` with safe logic  
- Fixed file handling using `with open(..., encoding="utf-8")`  
- Improved code readability and maintainability  
- Removed unused imports and unnecessary globals  

---

##  Pylint Scores

| Version | Score |
|----------|--------|
| **Initial** | 4.96 / 10 |
| **Final (after fixes)** | 9.58 / 10 |

---

##  Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were **formatting and naming style violations** (like adding blank lines and changing function names).  
The hardest issues were **handling mutable default arguments** and **refactoring file operations** to use context managers, as they required understanding code behavior.

---

### 2. Did the static analysis tools report any false positives?
Yes. Pylint flagged a few docstring-related warnings that were not critical to functionality.  
These can be considered false positives for small scripts, though they are useful for maintaining consistency in larger projects.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?
Static analysis tools should be integrated into the **Continuous Integration (CI)** pipeline.  
- Use GitHub Actions to automatically run **Pylint**, **Flake8**, and **Bandit** on every commit or pull request.  
- Developers can also run them locally before committing code to ensure clean, consistent quality.

---

### 4. What tangible improvements did you observe in the code quality, readability, or robustness after applying the fixes?
After applying fixes, the code became much **cleaner, easier to read, and safer**.  
- Readability improved with better naming and docstrings.  
- Security improved after removing `eval()` and adding safer file handling.  
- Maintainability increased with consistent formatting and fewer warnings.

---


