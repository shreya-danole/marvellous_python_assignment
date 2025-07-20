import pandas as pd 
from sklearn.model_selection import train_test_split

def main():
    data = {
        'Grade': ['A+','B','A','C','B+']
    }
    df = pd.DataFrame(data)
    print("Original dataframe:")
    print(df)

    Grade_mapping = {'A+':'Excellent', 'A':'Very Good', 'B+':'Good','B':'Average','C':'Poor'}
    df['Grade'] = df['Grade'].replace(Grade_mapping)

    print("dataframe after replacement:")
    print(df)
   
if __name__ == "__main__":
    main()
