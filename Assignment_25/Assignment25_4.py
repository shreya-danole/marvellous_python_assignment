import pandas as pd 
from sklearn.preprocessing import LabelEncoder

def main():
    data = {
        'Department': ['HR','IT','Finance','HR','IT']
    }
    df = pd.DataFrame(data)
    print("Dataframe before encoding:")
    print(df)

    df = pd.get_dummies(df, columns=['Department'], dtype=int)

    print("Dataframe after encoding:")
    print(df)



    
    

if __name__ == "__main__":
    main()
