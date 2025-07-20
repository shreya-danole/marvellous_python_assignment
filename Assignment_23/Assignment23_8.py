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

        # Plot Amit's marks across all subjects
        amit_marks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].values.flatten()
        subjects = ['Math', 'Science', 'English']
        plt.plot(subjects, amit_marks, marker='o')

        # Add labels and a title
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Amit's Marks Across All Subjects")

        # Display the plot
        plt.show()

        
if __name__ =="__main__":
        main()
