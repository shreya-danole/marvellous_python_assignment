import pandas as pd 

def main():
    data = {
        'Name': ['A','B','C'],
        'Age':[21.0,22.0,23.0]
    }
    df = pd.DataFrame(data)

    print("Data type of column are:")
    print(df['Name'].dtype)
    print(df['Age'].dtype)

    df['Age'] = df['Age'].astype(int)

    print("Datat type of age is:",df['Age'].dtype)


    
    

if __name__ == "__main__":
    main()
