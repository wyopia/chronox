# Date Extractor App

This is a Minimum Viable Product (MVP) for an application designed to extract dates and their associated event descriptions from Microsoft Word (.docx) documents and output them into a structured spreadsheet (CSV or Excel) format.

## Purpose

As a barrister, you often encounter legal documents containing numerous dates, each potentially referring to a significant event. Manually identifying and compiling these can be time-consuming and prone to error. This tool aims to automate that process, providing a quick and reliable way to generate a summary of events based on dates found within a document.

## Features (MVP)

- **Word Document Input:** Reads text from `.docx` files.
- **Date Extraction:** Identifies common date formats (e.g., DD/MM/YYYY, YYYY-MM-DD, Month DD, YYYY).
- **Event Description:** Extracts the full sentence containing the identified date as the "event description."
- **Spreadsheet Output:** Generates a `.csv` or `.xlsx` file with two columns: "Date Found" and "Event Description."
- **Command-Line Interface (CLI):** Simple to use from the terminal.

## Requirements

- Python 3.8+
- `python-docx` library
- `pandas` library
- `openpyxl` library (for `.xlsx` output)

# Contributing to Date Extractor App

We welcome contributions to improve the Date Extractor App! Whether it's bug reports, feature suggestions, or code contributions, your help is valuable.

## How to Contribute

### 1. Reporting Bugs

If you find a bug, please open an issue on the GitHub repository (if applicable) or describe it clearly. Include:

- A clear and concise description of the bug.
- Steps to reproduce the behavior.
- Expected behavior.
- Screenshots or error messages if applicable.
- Your operating system and Python version.

### 2. Suggesting Enhancements

We're always looking for ways to make the app more useful. If you have an idea for a new feature or an improvement to existing functionality, please open an issue. Describe:

- The problem you're trying to solve.
- How your suggested enhancement would solve it.
- Any alternative solutions you've considered.

### 3. Code Contributions

If you'd like to contribute code, please follow these steps:

1. **Fork the repository:** Click the "Fork" button on the GitHub page.

2. **Clone your forked repository:**
    
        git clone https://github.com/YOUR_USERNAME/date-extractor-app.git
    cd date-extractor-app
      
    

3. **Create a new branch:**
    
        git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/fix-description
      
    

4. **Make your changes:**

    - Write clean, well-commented code.

    - Follow existing code style.

    - **Write unit tests** for your new features or bug fixes. Ensure existing tests still pass.

5. **Run tests:**
    
        python -m unittest test_date_extractor_app.py
      
    

6. **Commit your changes:**
    
        git add .
    git commit -m "feat: Add new feature" # or "fix: Resolve bug"
      
    

(Use conventional commit messages if possible, e.g., `feat:`, `fix:`, `docs:`, `test:`)

7. **Push your branch to your fork:**
    
        git push origin feature/your-feature-name
      
    

8. **Open a Pull Request (PR):** Go to your forked repository on GitHub and click "New pull request." Provide a clear description of your changes.

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use clear and concise variable and function names.
- Add docstrings to all functions and classes.
- Add inline comments for complex logic.

### Testing Guidelines

- All new features or bug fixes should be accompanied by appropriate unit tests.
- Tests should be isolated and not depend on external services or specific file system states (beyond what's set up in `setUpClass`).
- Aim for good test coverage.

Thank you for contributing!