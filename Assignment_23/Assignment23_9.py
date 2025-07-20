import pandas as pd 
import matplotlib.pyplot as plt

def main():
        data1 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }
        df1 = pd.DataFrame(data1)
        # Print the DataFrame
        print("Student Marks DataFrame:")
        print(df1)


        data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [None, 90, 78],
        'Science': [92, None, 80]
        }
        df2 = pd.DataFrame(data2)
        # Print the DataFrame
        print("Student Marks DataFrame:")
        print(df2)

        print(df2.isnull())

        Math_mean = df2['Math'].mean()
        Science_mean = df2['Science'].mean()
        
        df2['Math'].fillna(Math_mean, inplace=True)
        df2['Science'].fillna(Science_mean, inplace=True)

        print(df2)
        
if __name__ =="__main__":
        main()
