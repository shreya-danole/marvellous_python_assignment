import pandas as pd 

def main():
    data = {
        'Salary': [25000, 27000, 29000, 31000, 50000, 100000]
    }
    df = pd.DataFrame(data)
    
    # Calculate Q1 and Q3
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)
    IQR = Q3 - Q1

    # Calculate bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Detect outliers
    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
    print("Outliers in Salary column using IQR method:")
    print(outliers)

if __name__ == "__main__":
    main()
