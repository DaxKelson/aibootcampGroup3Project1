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

def adjust_for_inflation(income, base_year, target_year, inflation_data=None):
    """
    Adjust a year's gross income for inflation.

    Parameters:
        income (float): The income to adjust.
        base_year (int): The year the income is from.
        target_year (int): The year to adjust the income to.
        inflation_data (dict, optional): A dictionary of year:CPI values. If None, retrieves data online.

    Returns:
        float: The adjusted income.

    Raises:
        ValueError: If the years are not found in the inflation data.
    """
    if inflation_data is None:
        # Fetch inflation data from an online source (e.g., US Bureau of Labor Statistics API or similar)
        try:
            response = requests.get("https://api.example.com/cpi")  # Replace with a real API endpoint
            inflation_data = response.json()
        except Exception as e:
            raise RuntimeError("Failed to retrieve inflation data.") from e

    if base_year not in inflation_data or target_year not in inflation_data:
        raise ValueError("Years not found in the provided inflation data.")

    base_cpi = inflation_data[base_year]
    target_cpi = inflation_data[target_year]

    adjusted_income = income * (target_cpi / base_cpi)
    return adjusted_income

# Example usage
if __name__ == "__main__":
    # Example inflation data (replace with real data)
    example_inflation_data = {
        2000: 172.2,
        2010: 218.1,
        2020: 258.8,
        2025: 275.0  # Hypothetical future CPI
    }

    income_2000 = 50000  # $50,000 in the year 2000
    adjusted_income_2025 = adjust_for_inflation(income_2000, 2000, 2025, example_inflation_data)
    print(f"$50,000 in 2000 is equivalent to ${adjusted_income_2025:.2f} in 2025.")
