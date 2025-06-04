#!/usr/bin/env python3
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Confidence-weighted average scoring.")
    parser.add_argument("input_file", help="Path to Excel review file")
    parser.add_argument("output_file", help="Path to save weighted result Excel")
    args = parser.parse_args()

    # Load data
    df = pd.read_excel(args.input_file)

    # Make sure columns are numeric
    df['Overall'] = pd.to_numeric(df['Overall'], errors='coerce')
    df['Confidence'] = pd.to_numeric(df['Confidence'], errors='coerce')

    # Drop rows with missing values
    df = df.dropna(subset=['Overall', 'Confidence'])

    # Compute weighted score
    df['Weighted'] = df['Overall'] * df['Confidence']

    # Group by each submission
    grouped = df.groupby(
        ['Submission ID', 'Submission Title', 'Acceptance Status', 'Primary Track'],
        as_index=False
    ).agg(
        Num_of_Reviews=('Overall', 'count'),
        Total_Confidence=('Confidence', 'sum'),
        Total_Weighted=('Weighted', 'sum')
    )

    # Calculate weighted average
    grouped['Weighted Overall'] = (grouped['Total_Weighted'] / grouped['Total_Confidence']).round(2)

    # Final columns
    final = grouped[['Submission ID', 'Submission Title', 'Acceptance Status', 'Primary Track',
                     'Num_of_Reviews', 'Weighted Overall']]
    final = final.rename(columns={'Num_of_Reviews': 'Num of Reviews'})

    # Save to Excel
    final.to_excel(args.output_file, index=False)
    print(f"✅ Confidence-weighted file saved to {args.output_file}")

if __name__ == "__main__":
    main()
