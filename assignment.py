import pandas as pd
from scipy.stats import zscore

def profile_and_detect_anomalies(df):
  """
  Performs data profiling and anomaly detection on the input DataFrame.

  Args:
    df: A pandas DataFrame to profile and check for anomalies.

  Returns:
    A tuple containing:
    - A dictionary with profiling results.
    - A pandas DataFrame with identified anomalous transactions.
  """
  profiling_results = {}

  # Task 1 (Profiling): Calculate descriptive statistics for transaction_amount
  # Your code here

  # Task 2 (Profiling): Get unique value counts for transaction_type
  # Your code here

  # Task 3 (Anomaly Detection): Identify anomalies in transaction_amount using Z-score
  # Your code here

  return profiling_results, anomalies_df
