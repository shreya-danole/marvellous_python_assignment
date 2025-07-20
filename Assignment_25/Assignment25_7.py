import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Age': [18,22,25,30,35]
    }
    df = pd.DataFrame(data)
    print("Original dataframe:")
    print(df)

    df['Age_normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

    print(df)

   
if __name__ == "__main__":
    main()
