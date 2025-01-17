import pandas as pd

# Opening the file:

netflix_df = pd.read_csv("netflix_data.csv")

###

# Finding the most frequent movie duration in the 1990s:

netflix_movies = netflix_df[netflix_df['type'] == 'Movie']
movies_90 = netflix_movies[(netflix_movies['release_year'] >= 1990) & (netflix_movies['release_year'] < 2000)]
most_freq_movie_duration_90s = movies_90.groupby('duration')['duration'].count().idxmax()
print('The most frequent movie duration in the 1990s is ' + str(most_freq_movie_duration_90s) + ' minutes.')

###

# Counting the number of short action movies from the 1990s:

action_movies_90 = movies_90[movies_90['genre'] == 'Action']
short_movie_count = (action_movies_90['duration'] <= 90).sum()
print('The number of short action movies from the 1990s is ' + str(short_movie_count) + '.')
