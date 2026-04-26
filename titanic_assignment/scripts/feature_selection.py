import pandas as pd

def select_features(df):
    # Assignment 2
    # drop stuff we dont need
    drop_cols = ['PassengerId', 'Name', 'Ticket']
    drop_cols = [c for c in drop_cols if c in df.columns]
    
    if drop_cols:
        df = df.drop(columns=drop_cols)
        
    return df

if __name__ == "__main__":
    import os
    data_dir = "data"
    if not os.path.exists(data_dir):
        data_dir = "../data"
        
    in_path = os.path.join(data_dir, "engineered_train.csv")
    out_path = os.path.join(data_dir, "final_train.csv")

    if os.path.exists(in_path):
        engineered_df = pd.read_csv(in_path)
        final_df = select_features(engineered_df)
        final_df.to_csv(out_path, index=False)
        print("Feature selection complete.")
