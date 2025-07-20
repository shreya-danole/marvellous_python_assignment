import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    # Plot histogram of Math marks
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    plt.title('Histogram of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()
