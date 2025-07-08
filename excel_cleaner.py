import pandas as pd
import argparse


def clean_excel(input_path: str, output_path: str) -> None:
    """Load an Excel file, drop duplicate rows, remove empty rows, and save to a new file."""
    df = pd.read_excel(input_path)
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    df.to_excel(output_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean up an Excel file by removing duplicates and empty rows.")
    parser.add_argument("input", help="Path to the input Excel file")
    parser.add_argument("output", help="Path to the cleaned output Excel file")
    args = parser.parse_args()
    clean_excel(args.input, args.output)
