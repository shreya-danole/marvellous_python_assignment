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
        print("Student who scored more than 85 in Science:")
        high_marks = df[df['Science'] > 85]

        print("Students with more than 85 in Science:")
        print(high_marks)

        

if __name__ =="__main__":
    main()
