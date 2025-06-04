#!/usr/bin/env python3
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple average score per submission")
    parser.add_argument("input_file", help="Input Excel file path")
    parser.add_argument("output_file", help="Output Excel file path")
    args = parser.parse_args()

    # Read Excel
    df = pd.read_excel(args.input_file)
    df['Overall'] = pd.to_numeric(df['Overall'], errors='coerce')

    # Group and average
    grouped = df.groupby(
        ['Submission ID', 'Submission Title', 'Acceptance Status', 'Primary Track'],
        as_index=False
    ).agg(
        Num_of_Reviews=('Overall', 'count'),
        Average_Overall=('Overall', 'mean')
    )

    grouped['Average_Overall'] = grouped['Average_Overall'].round(2)
    grouped = grouped.rename(columns={'Num_of_Reviews': 'Num of Reviews', 'Average_Overall': 'Average Overall'})

    # Save to Excel
    grouped.to_excel(args.output_file, index=False)
    print(f"Simple average saved to {args.output_file}")

if __name__ == "__main__":
    main()
