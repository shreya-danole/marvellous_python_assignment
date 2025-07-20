import pandas as pd 
import matplotlib.pyplot as plt

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

        plt.bar(df.Name, df.Total)
        
        plt.xlabel('Name')
        plt.ylabel('Total')
        plt.title('Stutend name vs total marks')

        plt.show()

if __name__ =="__main__":
        main()
