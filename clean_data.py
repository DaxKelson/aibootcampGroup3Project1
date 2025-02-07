import pandas as pd
import re
#
imbd_df = pd.read_csv('Resources/imdb_all_years.csv')

#Clean Up Title Data
for i in range(0, imbd_df['Title'].count()):
    imbd_df.loc[i, 'Title'] = re.sub(r'[0-9]*[.]', '', imbd_df['Title'].iloc[i])

imbd_df['Title'] = imbd_df['Title'].astype('string')
imbd_df['Movie Link'] = imbd_df['Title'].astype('string')

#Remove rows that dont have us dollars in them
imbd_df = imbd_df[imbd_df['countries_origin'].str.contains("United States", na=False)]

imbd_df.to_csv('Resources/cleaned_data.csv', index=False)