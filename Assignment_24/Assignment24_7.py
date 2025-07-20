import pandas as pd
import numpy as np

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # Calculate Total
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    # Add Status column: Pass if Total >= 250, else Fail
    df['Status'] = np.where(df['Total'] >= 250, 'Pass', 'Fail')

    df.to_csv("student.csv", index=False)

if __name__ == "__main__":
    main()
