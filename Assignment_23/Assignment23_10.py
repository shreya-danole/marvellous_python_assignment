import pandas as pd 
import matplotlib.pyplot as plt

def main():
        data1 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
    }
        df = pd.DataFrame(data1)
        print("Dataframe after remove column English")
        df_new = df.drop('English', axis=1) 
        print(df_new)

 
if __name__ =="__main__":
        main()
