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