import pandas as pd 
def main():
        data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }
        df = pd.DataFrame(data)
        # Min-Max Normalization for 'Math' column
        math_min = df['Math'].min()
        math_max = df['Math'].max()

        df['Math_Normalized'] = (df['Math'] - math_min) / (math_max - math_min)

        # Print the updated DataFrame
        print("DataFrame with Normalized Math Scores:")
        print(df[['Name', 'Math', 'Math_Normalized']])


if __name__ =="__main__":
    main()
