# Static Code Analysis Tool

## Overview

This project is a simple static code analysis tool written in Python. It scans Python source code files for the use of potentially unsafe functions by converting the source code into an Abstract Syntax Tree (AST). The tool is intended to demonstrate how static analysis can be used to identify basic security vulnerabilities without executing the code.

## Features

- Recursively searches a directory for Python (`.py`) files.
- Parses each Python file into an Abstract Syntax Tree (AST).
- Detects the use of unsafe functions such as:
  - `eval`
  - `exec`
  - `pickle.loads`
- Reports the file name, line number, and the detected issue.

## Requirements

- Python 3.x

The script only uses built-in Python modules:

- `os`
- `ast`

## Project Structure

```
project/
│
├── static_final.py
└── README.md
```

## How to Run

1. Open a terminal.
2. Navigate to the project directory.
3. Run the script:

```bash
python3 static_final.py
```

4. Edit the last line of the script if needed:

```python
main("your_source_code_directory")
```

Replace `"your_source_code_directory"` with the path to the folder you want to scan.

Example:

```python
main("sample_code")
```

## Example Output

```
Vulnerabilities found:
File: sample_code/test.py, Line: 8, Issue: Use of unsafe function 'eval'
File: sample_code/example.py, Line: 14, Issue: Use of unsafe function 'exec'
```

If no issues are found:

```
No vulnerabilities found.
```

---

# Code Explanation

## Import Statements

```python
import os
import ast
```

- `os` is used to navigate directories and locate Python files.
- `ast` converts Python source code into an Abstract Syntax Tree, making it easier to inspect the structure of the code.

---

## unsafe_functions

```python
unsafe_functions = ["eval", "exec", "pickle.loads"]
```

This list contains the function names that the analyzer considers unsafe. The script checks source code for calls to these functions.

---

## collect_source_files()

```python
collect_source_files(directory)
```

This function searches through the specified directory and all of its subdirectories for files ending in `.py`.

It returns a list containing the paths of all Python files found.

---

## parse_source_code()

```python
parse_source_code(file_path)
```

This function:

1. Opens a Python source file.
2. Reads its contents.
3. Converts the source code into an Abstract Syntax Tree (AST).
4. Returns the AST for further analysis.

If the source code contains syntax errors, the function returns `None`.

---

## is_vulnerable_function()

```python
is_vulnerable_function(node)
```

This helper function examines AST nodes.

If a node represents a function call and the function matches one of the unsafe functions, it returns:

- `True`
- the name of the unsafe function

Otherwise, it returns:

- `False`
- `None`

---

## analyze_ast()

```python
analyze_ast(tree, file_path)
```

This function walks through every node in the AST.

Whenever it detects an unsafe function call, it records:

- the file name
- the line number
- a description of the issue

All detected issues are stored in a list and returned.

---

## main()

```python
main(directory)
```

The `main()` function coordinates the entire scanning process.

It:

1. Collects all Python source files.
2. Parses each file into an AST.
3. Analyzes each AST for unsafe function calls.
4. Prints a report showing any vulnerabilities that were found.

---

# Limitations

This project is intended as a basic educational example of static code analysis.

Current limitations include:

- Only checks for a small set of unsafe functions.
- Does not analyze variables or data flow.
- Does not detect complex security vulnerabilities.
- Does not automatically fix detected issues.

---

# Future Improvements

Possible enhancements include:

- Detect additional security vulnerabilities.
- Support scanning multiple programming languages.
- Export results to CSV or JSON.
- Generate HTML security reports.
- Add severity levels to detected vulnerabilities.

---

# License

Provided by Moringa School.