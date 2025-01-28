# Clean Votes column:
# convert numbers like 9.1K to 9100 and numbers like 9.1M to 9100000
# for i in range(0, imdb_all_years_df['Votes'].count()):  
#     if(imdb_all_years_df['Votes'].iloc[i] != 0):
#         if(imdb_all_years_df['Votes'].iloc[i][-1] == 'K'):
#             imdb_all_years_df.loc[i, 'Votes'] = float(imdb_all_years_df['Votes'].iloc[i][:-1]) * 1000
#         elif(imdb_all_years_df['Votes'].iloc[i][-1] == 'M'):
#             imdb_all_years_df.loc[i, 'Votes'] = float(imdb_all_years_df['Votes'].iloc[i][:-1]) * 1000000
#         else:
#             imdb_all_years_df.loc[i, 'Votes'] = float(imdb_all_years_df['Votes'].iloc[i])
# imdb_all_years_df['Votes']

import requests
import pandas as pd

def adjust_for_inflation(value_in_dollars, base_year, target_year, inflation_data=None):
    base_cpi = inflation_data[base_year]
    target_cpi = inflation_data[target_year]

    adjusted_income = value_in_dollars * (target_cpi / base_cpi)
    return adjusted_income

# Example usage
if __name__ == "__main__":
    cpi_data = pd.read_csv('./Resources/US_inflation_rates.csv')
    
    income_2000 = 50000  # $50,000 in the year 2000
    adjusted_income_2025 = adjust_for_inflation(income_2000, 2000, 2025, cpi_data)
    print(f"$50,000 in 2000 is equivalent to ${adjusted_income_2025:.2f} in 2025.")
