import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    
    # Get Sagar's marks (row where Name == 'Sagar')
    sagar_marks = df.loc[df['Name'] == 'Sagar', ['Math', 'Science', 'English']].iloc[0]

    # Plot pie chart
    plt.pie(sagar_marks, labels=sagar_marks.index, startangle=90)
    plt.title("Sagar's Marks Distribution Across Subjects")
    plt.axis('equal')  # Equal aspect ratio to ensure it's a circle

    # Show plot
    plt.show()

if __name__ == "__main__":
    main()
