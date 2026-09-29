import pytest
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_pipeline import transform_features

@pytest.fixture
def synthetic_demand_data():
    """Generates synthetic baseline data contract for blind checks."""
    dates = pd.date_range(start="2026-06-01", periods=10)
    data = {
        'date': dates,
        'demand': np.array([120, 130, 125, 140, 150, 160, 145, 135, 128, 142]),
        'marketing_event': np.array([0, 0, 0, 1, 1, 1, 0, 0, 0, 0]),
        'holiday': np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    }
    return pd.DataFrame(data)

def test_pipeline_transformations(synthetic_demand_data):
    processed_df = transform_features(synthetic_demand_data)
    
    # Assertions on pipeline contract output
    assert 'log_demand' in processed_df.columns
    assert 'group_type' in processed_df.columns
    assert len(processed_df) == 10
    assert processed_df.loc[3, 'group_type'] == 'Marketing Only'
    assert processed_df.loc[6, 'group_type'] == 'Holiday Only'
    assert np.isclose(processed_df.loc[0, 'log_demand'], np.log(120))