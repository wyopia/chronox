# chronox
This is a Minimum Viable Product (MVP) for an application designed to extract dates and their associated event descriptions from Microsoft Word (.docx) documents and output them into a structured spreadsheet (CSV or Excel) format.

## Purpose
As a barrister, you often encounter legal documents containing numerous dates, each potentially referring to a significant event. Manually identifying and compiling these can be time-consuming and prone to error. This tool aims to automate that process, providing a quick and reliable way to generate a summary of events based on dates found within a document.

## Features

* Word Document Input: Reads text from .docx files.
* Date Extraction: Identifies common date formats (e.g., DD/MM/YYYY, YYYY-MM-DD, Month DD, YYYY).
* Event Description: Extracts the full sentence containing the identified date as the "event description."
* Spreadsheet Output: Generates a .csv or .xlsx file with two columns: "Date Found" and "Event Description."
* Command-Line Interface (CLI): Simple to use from the terminal.

## Requirements
* Python 3.8+
* python-docx library
* pandas library
* openpyxl library (for xslx output)

## Installation
1. Clone the repository (or download the files):
git clone git@github.com/wyopia/chronox.git
cd chronox

## Installation

1. **Clone the repository (or download the files):**
    
		git clone https://github.com/wyopia/chronox.git
		cd chronox

2. **Create a virtual environment (recommended):**
    
        python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
      
    

3. **Install the required Python packages:**
    
        pip install -r requirements.txt
      
    

## Usage

The application is run from the command line.
    
    
    python chronox.py --input <path_to_your_document.docx> [--output <output_file.csv_or_xlsx>] [--verbose]
      
    

### Arguments:

- `--input` or `-i`: **(Required)** Path to the input Word document (.docx).
- `--output` or `-o`: **(Optional)** Path for the output spreadsheet file.

    - If not specified, defaults to `extracted_events.csv` in the current directory.

    - Supports `.csv` and `.xlsx` extensions. The output format is determined by the extension you provide.
- `--verbose` or `-v`: **(Optional)** Enable verbose logging for more detailed output during processing (useful for debugging).

### Examples:

1. **Extract dates and save to a CSV file (default output name):**
    
        python chronox.py -i "path/to/my_legal_document.docx"
      
    

This will create `extracted_events.csv` in the current directory.

2. **Extract dates and save to a specific Excel file:**
    
        python chronox.py -i "path/to/another_document.docx" -o "summary_of_dates.xlsx"
      
    

3. **Extract dates with verbose logging:**
    
        python chronox.py -i "path/to/document.docx" -v
      
    

## Project Structure
    
    
    chronox/
    ├── chronox.py       # Main application logic
    ├── test_chronox.py  # Unit tests for the application
    ├── README.md                   # This file
    ├── CONTRIBUTING.md             # Guidelines for contributing (future expansion)
    └── LICENSE                     # License information
      
    

## Testing

To run the unit tests, navigate to the project's root directory in your terminal (where `test_date_extractor_app.py` is located) and execute:
    
    
    python -m unittest test_date_extractor_app.py
      
    

This will run all tests defined in `test_date_extractor_app.py` and report the results.

## Future Enhancements (Roadmap)

This MVP provides a solid foundation. Here are some potential areas for future improvement:

- **Advanced Date Parsing:** Implement more sophisticated date recognition, including relative dates (e.g., "next Tuesday," "three months ago") and date ranges.
- **Contextual Event Extraction:** Use Natural Language Processing (NLP) techniques to better understand the relationship between dates and surrounding text, extracting more precise "events" rather than just the full sentence.
- **Date Normalization:** Convert all extracted dates into a consistent format (e.g., YYYY-MM-DD) for easier sorting and analysis.
- **User Interface (GUI):** Develop a desktop application with a user-friendly graphical interface (e.g., using Tkinter, PyQt, or even a simple web interface with Flask/Streamlit) for easier use by non-technical users.
- **Error Handling & Reporting:** More robust error handling and user-friendly error messages.
- **Configuration File:** Allow users to define custom date patterns or output preferences in a configuration file.
- **Batch Processing:** Ability to process multiple `.docx` files at once.

## Contributing

Contributions are welcome! Please refer to `CONTRIBUTING.md` for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.