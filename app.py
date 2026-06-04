import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Cache karo taaki baar baar load na ho
@st.cache_data
def load_data():
    ratings = pd.read_csv('data/u.data', sep='\t',
                          names=['userId', 'movieId', 'rating', 'timestamp'])
    movies = pd.read_csv('data/u.item', sep='|', encoding='latin-1',
                         names=['movieId', 'title', 'release_date', 'video_release',
                                'imdb_url'] + [f'genre_{i}' for i in range(19)])
    return ratings, movies

@st.cache_data
def build_matrix(ratings):
    user_item_matrix = ratings.pivot_table(
        index='userId', columns='movieId', values='rating').fillna(0)
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(user_similarity,
                                       index=user_item_matrix.index,
                                       columns=user_item_matrix.index)
    return user_item_matrix, user_similarity_df

def get_recommendations(user_id, n, user_item_matrix, user_similarity_df, movies):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:11]
    watched_movies = user_item_matrix.loc[user_id]
    watched_movies = watched_movies[watched_movies > 0].index.tolist()

    recommended = {}
    for similar_user, similarity_score in similar_users.items():
        similar_user_movies = user_item_matrix.loc[similar_user]
        unwatched = similar_user_movies[
            (similar_user_movies > 0) &
            (~similar_user_movies.index.isin(watched_movies))
        ]
        for movie_id, rating in unwatched.items():
            if movie_id not in recommended:
                recommended[movie_id] = 0
            recommended[movie_id] += similarity_score * rating

    recommended = sorted(recommended.items(), key=lambda x: x[1], reverse=True)[:n]

    recommended_movies = []
    for movie_id, score in recommended:
        title = movies[movies['movieId'] == movie_id]['title'].values[0]
        recommended_movies.append({'Movie': title, 'Score': round(score, 2)})

    return pd.DataFrame(recommended_movies)

# UI
st.title("🎬 Movie Recommendation System")
st.write("Loading data... please wait!")

ratings, movies = load_data()
user_item_matrix, user_similarity_df = build_matrix(ratings)

st.success("✅ Ready!")

user_id = st.selectbox("Select User ID", sorted(ratings['userId'].unique()))
n = st.slider("Number of Recommendations", 1, 10, 5)

if st.button("Get Recommendations"):
    results = get_recommendations(user_id, n, user_item_matrix, user_similarity_df, movies)
    st.dataframe(results)