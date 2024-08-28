import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result = None
    DF  = employee.sort_values(['salary'], ascending = False)
    DF_nodup = DF.drop_duplicates(subset = 'salary')
    for i in range(len(DF_nodup)):
        if  (N == i+1) :
            result = DF_nodup['salary'].iloc[i]
    return pd.DataFrame({result}, columns = [f'getNthHighestSalary({N})'])