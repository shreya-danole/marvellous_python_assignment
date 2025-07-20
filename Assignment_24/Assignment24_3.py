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
    print("Student Marks DataFrame:")
    print(df)

    df['Gender'] = ['male', 'male', 'female']
    print("After adding Gender column:")
    print(df)

    # Group by Gender and calculate average marks
    avg_by_gender = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print("Average marks by Gender:")
    print(avg_by_gender)

if __name__ == "__main__":
    main()
