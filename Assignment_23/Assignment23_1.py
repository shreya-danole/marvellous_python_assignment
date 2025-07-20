import pandas as pd 
def main():
        data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }
        df = pd.DataFrame(data)
        # Print the DataFrame
        print("Student Marks DataFrame:")
        print(df)

        # Print the shape of the DataFrame
        print("Shape of DataFrame:", df.shape)

        # Print the columns of the DataFrame
        print("Columns:", df.columns)

        # Print the datatypes of each column
        print("Data types:\n", df.dtypes)

if __name__ =="__main__":
    main()
