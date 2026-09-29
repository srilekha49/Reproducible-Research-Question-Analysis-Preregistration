import os
import pandas as pd
import numpy as np

def load_and_validate_data(filepath: str) -> pd.DataFrame:
    """Loads raw daily demand data and checks schema contract."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found at: {filepath}")
    
    df = pd.read_csv(filepath)
    
    # Contract validation
    expected_columns = {'date', 'demand', 'marketing_event', 'holiday'}
    if not expected_columns.issubset(set(df.columns)):
        missing = expected_columns - set(df.columns)
        raise ValueError(f"Schema violation: Missing columns {missing}")
    
    if df['demand'].isnull().any():
        raise ValueError("Data quality error: Missing values found in 'demand'")
        
    return df

def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    """Applies log transformation and categorical factor creation."""
    df_proc = df.copy()
    df_proc['log_demand'] = np.log(df_proc['demand'])
    
    def label_group(row):
        if row['marketing_event'] == 1 and row['holiday'] == 0:
            return 'Marketing Only'
        elif row['marketing_event'] == 0 and row['holiday'] == 1:
            return 'Holiday Only'
        elif row['marketing_event'] == 1 and row['holiday'] == 1:
            return 'Marketing + Holiday'
        else:
            return 'Standard Day'
            
    df_proc['group_type'] = df_proc.apply(label_group, axis=1)
    return df_proc

if __name__ == "__main__":
    raw_path = os.path.join("data", "raw", "daily-demand-series.csv")
    if os.path.exists("daily-demand-series.csv"):
        raw_path = "daily-demand-series.csv"
        
    df_raw = load_and_validate_data(raw_path)
    df_processed = transform_features(df_raw)
    
    os.makedirs(os.path.join("data", "processed"), exist_ok=True)
    df_processed.to_csv(os.path.join("data", "processed", "processed_demand.csv"), index=False)
    print("Pipeline execution complete! Processed dataset saved to data/processed/processed_demand.csv")