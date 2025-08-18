# Python Starter Tutorial

A beginner-friendly Python project designed to teach fundamental Python development practices, including virtual environments, external libraries, unit testing, and VS Code integration.

## Project Structure

```
python_starter/
├── .venv/                 # Virtual environment (created after setup)
├── test/                  # Unit tests directory
│   ├── __init__.py
│   └── test_utils.py      # Unit tests for main.py
├── main.py                # Main Python script
├── utils.py               # Python utility functions
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Prerequisites

- Python 3.8 or higher installed on your system
- Visual Studio Code (VS Code)
- Git (optional, for version control)

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone git@github.com:503e/python_starter.git
cd python_starter
```

Or download and extract the project files to a folder named `python_starter`.

### 2. Create a Virtual Environment

A virtual environment isolates your project dependencies from other Python projects on your system.

**Windows:**
```bash
python -m venv .venv
```

**macOS/Linux:**
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### 4. Upgrade pip and Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## VS Code Setup

### 1. Open the Project in VS Code

```bash
code .
```

Or open VS Code and use `File > Open Folder` to select the `python_starter` directory.

### 2. Select Python Interpreter

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your `.venv` folder:
   - Windows: `.venv\Scripts\python.exe`
   - macOS/Linux: `.venv/bin/python`

### 3. Recommended VS Code Extensions

Install these extensions for the best Python development experience:

- **Python** (Microsoft) - Essential Python support
- **Python Debugger** (Microsoft) - Debugging capabilities
- **autopep8** (Microsoft) - Code formatting
- **GitHub Copilot** and **GitHub Copilot Chat** (GitHub) - AI-assisted code completion and chat

## Running the Project

### Run the Main Script

**In VS Code:**
1. Open `main.py`
2. Press `F5` to run with debugger, or `Ctrl+F5` to run without debugger

**In Terminal:**
```bash
python main.py
```

### Running Tests

**Run all tests:**
```bash
python -m unittest discover test
```

**Run specific test file:**
```bash
python -m unittest test.test_utils
```

**In VS Code:**
1. Open the Testing panel (beaker icon in sidebar)
2. VS Code will automatically discover tests
3. Click the play button to run tests

## Debugging in VS Code

### Set Breakpoints
- Click in the left margin next to line numbers to set breakpoints
- Red dots indicate active breakpoints

### Start Debugging
1. Press `F5` or go to `Run > Start Debugging`
2. Choose "Python File" when prompted
3. The debugger will stop at breakpoints, allowing you to inspect variables

### Debug Configuration
The project includes a `.vscode/launch.json` file with debug configurations for:
- Running the main script
- Running unit tests

## Project Components

### main.py
The main Python script that demonstrates:
- Basic Python programming concepts
- Function usage

### utils.py
The utilities Python functions file:
- Function definitions
- Importing and using NumPy for numerical operations

### test/test_utils.py
Unit tests using Python's built-in `unittest` framework:
- Test cases for functions in `utils.py`
- Examples of assertion methods
- Test discovery and execution patterns

### requirements.txt
Lists all external dependencies:
```
numpy>=1.21.0
autopep8==2.3.2
flake8==7.3.0
```

## Virtual Environment Management

### Deactivate Virtual Environment
```bash
deactivate
```

### Reactivate Virtual Environment
Follow step 3 from the setup instructions above.

### Adding Dependencies
After adding new packages:
```bash
pip freeze > requirements.txt
```

### Install from requirements.txt (on new setup)
```bash
pip install -r requirements.txt
```

## Learning Objectives

This project teaches you:

1. **Virtual Environment Management** - Isolating project dependencies
2. **Package Management** - Using pip and requirements.txt
3. **External Libraries** - Working with NumPy for numerical computing
4. **Unit Testing** - Writing and running tests with unittest
5. **IDE Integration** - Using VS Code for Python development
6. **Code Organization** - Structuring a Python project
7. **Debugging** - Using VS Code's debugging tools

## Common Issues and Solutions

### Virtual Environment Not Activating
- Ensure you're in the project directory
- Check that Python is properly installed
- On Windows, try using Command Prompt instead of PowerShell

### VS Code Not Finding Python Interpreter
- Make sure the virtual environment is activated
- Manually select the interpreter using `Ctrl+Shift+P` > "Python: Select Interpreter"
- Restart VS Code after creating the virtual environment

### Import Errors
- Verify the virtual environment is activated
- Check that requirements are installed: `pip list`
- Ensure you're running Python from the correct environment

### Tests Not Discovered
- Check that test files start with `test_`
- Ensure `__init__.py` exists in the test directory
- Refresh the VS Code testing panel

## Next Steps

After completing this tutorial, consider exploring:

- Additional NumPy functionality for data manipulation
- Other popular libraries like pandas, matplotlib, or requests
- Advanced testing with pytest
- Code formatting with black or autopep8
- Type hints with mypy
- Creating your own Python packages

## Resources

- [Python Official Documentation](https://docs.python.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)

---

Happy coding! 🐍