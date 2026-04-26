import pandas as pd

def clean_data(df):
    # Assignment 2
    # fill missing age with median
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
        # Fix decimal Age
        df['Age'] = df['Age'].astype(int)
    
    # fill missing embarked with most common port
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # drop cabin
    if 'Cabin' in df.columns:
        df = df.drop(columns=['Cabin'])
        
    return df

if __name__ == "__main__":
    import os
    data_dir = "data"
    if not os.path.exists(data_dir):
        data_dir = "../data"
    
    # Clean train
    train_path = os.path.join(data_dir, "train.csv")
    if os.path.exists(train_path):
        train_df = pd.read_csv(train_path)
        cleaned_train = clean_data(train_df)
        cleaned_train.to_csv(os.path.join(data_dir, "cleaned_train.csv"), index=False)
        print("Train data cleaned.")

    # Clean test
    test_path = os.path.join(data_dir, "test.csv")
    if os.path.exists(test_path):
        test_df = pd.read_csv(test_path)
        # Handle potential missing Fare in test set
        if 'Fare' in test_df.columns:
            test_df['Fare'] = test_df['Fare'].fillna(test_df['Fare'].median())
        cleaned_test = clean_data(test_df)
        cleaned_test.to_csv(os.path.join(data_dir, "cleaned_test.csv"), index=False)
        print("Test data cleaned.")
