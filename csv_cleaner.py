import pandas as pd

class CSVDataCleaner:
    def __init__(self, input_file, output_file, sort_by=None):
        self.input_file = input_file
        self.output_file = output_file
        self.sort_by = sort_by
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.input_file)
            print("CSV loaded successfully.")

        except FileNotFoundError:
            print(f"File not found: {self.input_file}")
            raise
        except Exception as e:
            print(f"Error loading CSV: {e}")


    def clean_data(self):
        self.df.dropna(how='all', inplace=True)
        self.df.drop_duplicates(inplace=True)
        print("Empty and duplicate rows removed.")

        if self.sort_by and self.sort_by in self.df.columns:
            self.df.sort_values(by=self.sort_by, inplace=True)
            print(f"Sorted by column: {self.sort_by}")

        elif self.sort_by:
            print(f"Column '{self.sort_by}' not found. Skipping sort.")

    def save_data(self):
        self.df.to_csv(self.output_file, index=False)
        print(f"Cleaned data saved to {self.output_file}")
