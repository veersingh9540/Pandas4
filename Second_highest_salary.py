import pandas as pd 

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_highest = None
    sorted_df = employee.sort_values(by = "salary", ascending = False)
    df_nodup = sorted_df.drop_duplicates(subset ="salary")
    if len(df_nodup) >= 2:
        second_highest = df_nodup['salary'].iloc[1]
    return pd.DataFrame({second_highest}, columns= ['SecondHighestSalary'])