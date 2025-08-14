# Data Profiling and Anomaly Detection Assignment

## Problem Description

In this assignment, you will perform data profiling and implement a simple anomaly detection technique on a dataset. Data profiling involves summarizing the characteristics of a dataset, while anomaly detection aims to identify unusual patterns or outliers. These techniques are crucial for understanding data quality and identifying potential issues.

## Learning Objectives

By completing this assignment, you will learn:
- How to calculate basic descriptive statistics for numerical columns
- How to identify unique values and their counts for categorical columns
- How to detect anomalies using a simple statistical method (e.g., Z-score)
- How to summarize data characteristics for profiling

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   pandas (>=1.3.0)
    -   scipy (>=1.9.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find a function definition: `profile_and_detect_anomalies(df)`.
3.  The function takes a pandas DataFrame as input.
4.  Your tasks are to:
    *   **Task 1 (Profiling)**: Calculate descriptive statistics (mean, median, std, min, max) for the `transaction_amount` column.
    *   **Task 2 (Profiling)**: Get the count of unique values for the `transaction_type` column.
    *   **Task 3 (Anomaly Detection)**: Identify anomalies in the `transaction_amount` column using the Z-score method. Mark transactions with a Z-score greater than 3 or less than -3 as anomalies.
5.  The function should return a dictionary containing the profiling results and a DataFrame with the identified anomalies.

## Hints

*   For Task 1, use `df['transaction_amount'].describe()` or individual aggregation functions.
*   For Task 2, use `df['transaction_type'].value_counts()`.
*   For Task 3, calculate the Z-score for each `transaction_amount` using `(x - mean) / std`. You can use `scipy.stats.zscore`.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That the function returns a dictionary and a DataFrame
-   That the profiling results are accurate
-   That the anomaly detection correctly identifies outliers

## Expected Output

The function should return a tuple containing two elements:
1.  A dictionary with profiling results (e.g., `{'transaction_amount_stats': {...}, 'transaction_type_counts': {...}}`).
2.  A pandas DataFrame containing only the anomalous transactions.

## Sample Data Format

The input DataFrame will have the following columns:

-   `transaction_id` (integer)
-   `transaction_amount` (float)
-   `transaction_type` (string)

## Troubleshooting

### Common Errors

-   `ZeroDivisionError`: This can happen if the standard deviation is zero (e.g., all values are the same). Consider adding a check for this.

## Further Exploration (Optional)

*   Explore other anomaly detection techniques, such as Isolation Forest or Local Outlier Factor.
*   How would you visualize the anomalies in the data?
*   Can you extend the profiling to include more metrics, such as skewness and kurtosis?

## Resources

-   [Data Profiling Explained](https://www.talend.com/resources/what-is-data-profiling/)
-   [Anomaly Detection Tutorial](https://www.datacamp.com/community/tutorials/anomaly-detection-python)
-   [Scipy Z-score Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html)
