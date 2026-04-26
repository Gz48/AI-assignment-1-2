import pandas as pd
import os

def run_analysis(data_path):
    # Assignment 1: Football Analysis
    df = pd.read_csv(data_path)
    
    print(f"Total Matches: {df.shape[0]}")
    
    df['date'] = pd.to_datetime(df['date'])
    print(f"Earliest Year: {df['date'].dt.year.min()}")
    print(f"Latest Year: {df['date'].dt.year.max()}")
    
    unique_countries = set(df['home_team'].unique()).union(set(df['away_team'].unique()))
    print(f"Unique Countries: {len(unique_countries)}")
    
    # Goals Analysis
    df['total_goals'] = df['home_score'] + df['away_score']
    print(f"Average Goals Per Match: {df['total_goals'].mean():.2f}")
    
    # Results Analysis
    def match_result(row):
        if row['home_score'] > row['away_score']: return 'Home Win'
        elif row['home_score'] < row['away_score']: return 'Away Win'
        else: return 'Draw'
    
    df['result'] = df.apply(match_result, axis=1)
    result_pct = df['result'].value_counts(normalize=True) * 100
    print(f"Home Win Percentage: {result_pct.get('Home Win', 0):.2f}%")
    
    return df

if __name__ == "__main__":
    import os
    data_dir = "data"
    if not os.path.exists(data_dir):
        data_dir = "assignment1/data"
        if not os.path.exists(data_dir):
            data_dir = "../data"
            
    csv_path = os.path.join(data_dir, "results.csv")
    
    if os.path.exists(csv_path):
        results_df = run_analysis(csv_path)
        print("Analysis complete.")
    else:
        print(f"Error: Could not find results.csv at {csv_path}")
