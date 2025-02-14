# aibootcampGroup3Project1
data analysis of IMDB movie data

## Kaggle dataset: 
https://www.kaggle.com/datasets/raedaddala/imdb-movies-from-1960-to-2023

## Presentation
Presenation Slides located in file "IMBD Movies - AI Group 3 Project 1 Presentation.pdf"

## Project Description:
We are using this data scraped from the IMBD website. Our goal is to iddentify which movies performed the best in the box office given a low budget. We hope to identify a base threshold of budget for creating a movie that will lead to the best probability of making the money back in the box office.

## Usage and Installation Instructions
Min: Python 3.10
Instructions for running: Use Python to launch python script to obtain matplot graphs of analysis

## Credits
Inflation Dataset: https://www.kaggle.com/datasets/pavankrishnanarne/us-inflation-dataset-1947-present
1. Dax Kelson               |   Profitability By Genre & Popularity of Genre by Year -> Genre_KPI_Dax.ipynb
2. Hunter Klinglesmith      |   Do Directors and/or their actors have the biggest influence on movie success? -> Directors_Actors_KPI.ipynb
3. William Sloan            |   Profitability By Rating -> Rating_Profitability_KPI_Liam.ipynb
4. Milad Tanha              |   IMDB Rating vs Budget -> IMBD_Rating_Budget_KPI_Milad.ipynb
5. Donald Harrison          |   Is there a range of budgets that ensured a movie was successful in the box office? -> Budget_PI_Don.ipynb

## Additional Questions
1. Are there directors that direct movies that have higher revenues
2. Are Movies more or less profitable when taking ratings into account ie. are pg-13 movies more profitable than rated R movies? Group by rating column "mpa" and sort by difference between budget and grossing worldwide vs US to see if movies make more money dependent on their rating
3. Popularity of Genre by year
4. IMDB Rating vs Budget. Did lower budget movies do better with IMBD rating?
5. Take buckets to see what percentage of movies did well with different buckets of budget amounts

Figure out what minimum budget you need to get a movie with the best chances of success
Group everything by year
add column with percentage of movie budget vs budget for movies that year
add column with percentage of movie grossing worldwide vs grossing worldwide for movies that year
add column that does a ratio for percent budget and percent grossing. budget % / grossing %. sort lowest to greatest to get movies that did the best with lower budgets.
