import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Age': [25,30,45,35,22],
        'Salary': [50000,60000,80000,65000,45000],
        'Purchased': [1,0,1,0,1]
    }
    df = pd.DataFrame(data)
    print("Original dataframe:")
    print(df)

    # independent  and deoendent
    X = df[['Age', 'Salary']]
    y = df['Purchased']

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\nX_train:")
    print(X_train)
    print("\nX_test:")
    print(X_test)
    print("\ny_train:")
    print(y_train)
    print("\ny_test:")
    print(y_test)
   
if __name__ == "__main__":
    main()
