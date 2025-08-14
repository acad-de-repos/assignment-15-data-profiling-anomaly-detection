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
  anomalies_df = None  # Initialize the anomalies DataFrame

  # Task 1 (Profiling): Calculate descriptive statistics for transaction_amount
  # Hint: Use pandas describe() method to get comprehensive statistics
  # Think about: What statistical measures do you need for numerical data?
  # Additional hints:
  # - Use df['column_name'].describe() to get statistics for a specific column
  # - The describe() method returns count, mean, std, min, 25%, 50%, 75%, max
  # - Convert the result to a dictionary using .to_dict()
  # - Store in profiling_results['transaction_amount_stats']
  # - Example: profiling_results['transaction_amount_stats'] = df['transaction_amount'].describe().to_dict()
  # Your code here

  # Task 2 (Profiling): Get unique value counts for transaction_type
  # Hint: Use pandas value_counts() method to count unique values
  # Think about: How do you count occurrences of each category in categorical data?
  # Additional hints:
  # - Use df['column_name'].value_counts() to count unique values
  # - This returns a Series with values as index and counts as values
  # - Convert to dictionary using .to_dict()
  # - Store in profiling_results['transaction_type_counts']
  # - Example: profiling_results['transaction_type_counts'] = df['transaction_type'].value_counts().to_dict()
  # Your code here

  # Task 3 (Anomaly Detection): Identify anomalies in transaction_amount using Z-score
  # Hint: Use scipy.stats.zscore to calculate Z-scores and filter for anomalies
  # Think about: How do you identify data points that are statistically unusual?
  # Additional hints:
  # - Import zscore from scipy.stats (already done at the top)
  # - Calculate Z-scores: df['zscore'] = zscore(df['transaction_amount'])
  # - Z-score tells you how many standard deviations a value is from the mean
  # - Values with |Z-score| > threshold are considered anomalies
  # - Use a threshold like 1.5 or 2 (not 3, which is too strict for this data)
  # - Filter: anomalies_df = df[(df['zscore'] > threshold) | (df['zscore'] < -threshold)].copy()
  # - Remove the zscore column: anomalies_df.drop(columns=['zscore'], inplace=True)
  # - The result should identify transactions with amounts 500 and -200 as anomalies
  # Your code here

  # Expected output:
  # - profiling_results should contain 'transaction_amount_stats' and 'transaction_type_counts'
  # - anomalies_df should contain rows where transaction amounts are statistical outliers
  # - Test expects 2 anomalies: transaction amounts 500 and -200
  return profiling_results, anomalies_df
