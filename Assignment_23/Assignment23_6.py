import pandas as pd 
import numpy as np
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

        df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

        sorted_df_desc = df.sort_values(by='Total',ascending=False)
        print("Sorted DataFrame descending by Total:\n", sorted_df_desc)
if __name__ =="__main__":
    main()
