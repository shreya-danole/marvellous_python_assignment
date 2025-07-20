import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Marks': [85,None,90,None,95]
    }
    df = pd.DataFrame(data)
    print("Original dataframe:")
    print(df)

    interpolated_df = df.interpolate()
    print(interpolated_df)
   
if __name__ == "__main__":
    main()
