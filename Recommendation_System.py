import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_top_250_movies.csv')

df['Year'] = df['Year'].astype(str)

plt.scatter(df['IMDb Rating'], df['Votes'])
plt.title('IMDb Rating vs Votes')
plt.xlabel('IMDb Rating')
plt.ylabel('Votes')
for i, txt in enumerate(df['Title']):
    plt.annotate(txt, (df['IMDb Rating'][i], df['Votes'][i]))
plt.show()

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['Title'])

cosine_sim = cosine_similarity(count_matrix)

def recommend(movie_title, cosine_sim):
    idx = df[df['Title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]

movie_title = 'The Godfather'
print(f"Recommended movies similar to '{movie_title}':")
print(recommend(movie_title, cosine_sim))
