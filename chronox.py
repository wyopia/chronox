# chronox.py
import re
import pandas as pd
from docx import Document
import os
import argparse
import logging
from datetime import datetime

# Configure logging for better feedback
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DateExtractor:
    """
    A class to extract dates and associated event descriptions from a Word document
    and output them into a pandas DataFrame.
    """

    def __init__(self):
        """
        Initializes the DateExtractor.
        Defines a list of common date regex patterns.
        """
        # Define a list of common date regex patterns.
        # This is a starting point and can be expanded.
        # Patterns are ordered from most specific to more general to avoid partial matches.
        self.date_patterns = [
            # DD/MM/YYYY or DD-MM-YYYY
            r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{4})\b',
            # YYYY-MM-DD
            r'\b(\d{4}[-/]\d{1,2}[-/]\d{1,2})\b',
            # Month DD, YYYY (e.g., January 1, 2023)
            r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}\b',
            # DD Month YYYY (e.g., 1 January 2023)
            r'\b\d{1,2}\s+(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b',
            # Month YYYY (e.g., January 2023)
            r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b',
            # YYYY (as a standalone year, might be too broad for 'events' without context)
            # r'\b\d{4}\b' # Excluded for MVP to avoid too many false positives without context.
        ]

    def extract_dates_from_docx(self, docx_path: str) -> pd.DataFrame:
        """
        Reads a Word document, extracts dates, and the sentence containing each date.

        Args:
            docx_path (str): The file path to the Word document (.docx).

        Returns:
            pd.DataFrame: A DataFrame with columns 'Date Found' and 'Event Description'.
                          Returns an empty DataFrame if no dates are found or on error.
        """
        # Define expected columns for the DataFrame
        expected_columns = ['Date Found', 'Event Description']

        if not os.path.exists(docx_path):
            logging.error(f"Error: Document not found at '{docx_path}'")
            return pd.DataFrame(columns=expected_columns)

        if not docx_path.lower().endswith('.docx'):
            logging.error(f"Error: '{docx_path}' is not a .docx file.")
            return pd.DataFrame(columns=expected_columns)

        extracted_data = []
        try:
            document = Document(docx_path)
            logging.info(f"Processing document: {docx_path}")

            for para in document.paragraphs:
                text = para.text.strip()
                if not text:
                    continue

                # Split text into sentences for better event description context
                sentences = re.split(r'(?<=[.!?])\s+', text)
                for sentence in sentences:
                    for pattern in self.date_patterns:
                        matches = re.findall(pattern, sentence)
                        for match in matches:
                            # Basic cleaning for the date match
                            date_str = match.strip()
                            # For MVP, the 'event description' is the sentence containing the date.
                            event_description = sentence.strip()
                            extracted_data.append({'Date Found': date_str, 'Event Description': event_description})
                            logging.debug(f"Found date: '{date_str}' in sentence: '{event_description}'")

        except Exception as e:
            logging.error(f"An error occurred while reading the document: {e}")
            return pd.DataFrame(columns=expected_columns)

        if not extracted_data:
            logging.info("No dates found in the document.")
            # Ensure an empty DataFrame with correct columns is returned even if no data
            return pd.DataFrame(columns=expected_columns)
        else:
            logging.info(f"Successfully extracted {len(extracted_data)} date entries.")
            return pd.DataFrame(extracted_data, columns=expected_columns) # Ensure columns are always set

    def save_to_spreadsheet(self, df: pd.DataFrame, output_path: str):
        """
        Saves the extracted data DataFrame to a spreadsheet (CSV or Excel).

        Args:
            df (pd.DataFrame): The DataFrame containing 'Date Found' and 'Event Description'.
            output_path (str): The desired output file path (e.g., 'output.csv' or 'output.xlsx').
        """
        # Removed the 'if df.empty: return' check.
        # Pandas to_csv/to_excel will correctly write headers for an empty DataFrame.
        try:
            if output_path.lower().endswith('.csv'):
                df.to_csv(output_path, index=False, encoding='utf-8')
                logging.info(f"Data successfully saved to CSV: '{output_path}'")
            elif output_path.lower().endswith('.xlsx'):
                df.to_excel(output_path, index=False, engine='openpyxl')
                logging.info(f"Data successfully saved to Excel: '{output_path}'")
            else:
                logging.error("Unsupported output file format. Please use .csv or .xlsx.")
        except Exception as e:
            logging.error(f"An error occurred while saving the spreadsheet: {e}")

def main():
    """
    Main function to parse command-line arguments and run the date extraction process.
    """
    parser = argparse.ArgumentParser(
        description="Extracts dates and associated event descriptions from a Word document (.docx) "
                    "and outputs them to a spreadsheet (.csv or .xlsx)."
    )
    parser.add_argument(
        '--input',
        '-i',
        type=str,
        required=True,
        help="Path to the input Word document (.docx)."
    )
    parser.add_argument(
        '--output',
        '-o',
        type=str,
        default='extracted_events.csv',
        help="Path for the output spreadsheet file (.csv or .xlsx). Defaults to 'extracted_events.csv'."
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help="Enable verbose logging for debugging."
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Verbose logging enabled.")

    extractor = DateExtractor()
    extracted_df = extractor.extract_dates_from_docx(args.input)

    # The save_to_spreadsheet method now handles empty DataFrames correctly,
    # so we can always attempt to save.
    extractor.save_to_spreadsheet(extracted_df, args.output)


if __name__ == "__main__":
    main()
