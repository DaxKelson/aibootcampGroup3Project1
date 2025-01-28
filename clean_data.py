import pandas as pd

#
imbd_df = pd.read_csv('Resources/imdb_all_years.csv')
imbd_df.to_csv('Resources/cleaned_data.csv', index=False)