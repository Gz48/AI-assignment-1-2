import pandas as pd

def engineer_features(df):
    # Assignment 2
    # make family size feature
    if 'SibSp' in df.columns and 'Parch' in df.columns:
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
        df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
        
    # convert sex to numbers
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        
    # dummy encode embarked
    if 'Embarked' in df.columns:
        df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
        
    return df

if __name__ == "__main__":
    import os
    data_dir = "data"
    if not os.path.exists(data_dir):
        data_dir = "../data"
        
    in_path = os.path.join(data_dir, "cleaned_train.csv")
    out_path = os.path.join(data_dir, "engineered_train.csv")

    if os.path.exists(in_path):
        cleaned_df = pd.read_csv(in_path)
        engineered = engineer_features(cleaned_df)
        engineered.to_csv(out_path, index=False)
        print("Feature engineering complete.")
