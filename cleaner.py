import argparse
from csv_cleaner import CSVDataCleaner

def main():
    parser = argparse.ArgumentParser(description="OOP CSV Cleaner Tool")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("output", help="Output cleaned CSV file")
    parser.add_argument("--sort", help="Column name to sort by", default=None)
    args = parser.parse_args()

    cleaner = CSVDataCleaner(args.input, args.output, args.sort)
    cleaner.load_data()
    cleaner.clean_data()
    cleaner.save_data()

if __name__ == "__main__":
    main()