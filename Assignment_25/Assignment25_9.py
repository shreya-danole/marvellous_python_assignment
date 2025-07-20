import pandas as pd 
import numpy as np

def main():
    data = {
        'Marks': [45,67,88,32,76]
    }
    df = pd.DataFrame(data)
    print("Original dataframe:")
    print(df)

    df['Marks'] = np.where(df['Marks'] < 50, 'Fail', df['Marks'])

    print("after replacement dataframe:")
    print(df)
   
if __name__ == "__main__":
    main()
