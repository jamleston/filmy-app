import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import linear_kernel

def load_data():
    df = pd.read_csv('movies_with_ratings.csv')
    tfidf = joblib.load('models/tfidf_vectorizer.joblib')
    genre_matrix = joblib.load('models/genre_matrix.joblib')
    return df, tfidf, genre_matrix

df, tfidf, genre_matrix = load_data()

def recommend_movies(movie_title):
    # movie index
    movie_idx = df[df['title'].str.contains(movie_title, case=False, regex=False)].index
    if len(movie_idx) == 0:
        return None

    sim_scores = linear_kernel(genre_matrix[movie_idx[0]], genre_matrix).flatten()

    sorted_indices = sim_scores.argsort()[-6:-1][::-1]

    recommendations = []
    for idx in sorted_indices:
        movie_title = df.iloc[idx]['title']
        avg_rating = df.iloc[idx]['avg_rating']
        num_ratings = df.iloc[idx]['num_ratings']
        similarity = round(sim_scores[idx], 3)
        recommendations.append((movie_title, similarity, round(avg_rating, 2), int(num_ratings)))

    return recommendations


# Streamlit
st.title("🎬 Movie Recommendation App")

movie_query = st.text_input("🔍 Enter a movie name:")

if movie_query:
    results = recommend_movies(movie_query)

    if results is None or len(results) == 0:
        st.error("❌ No matching movies found. Please check the title and try again.")
    else:
        st.subheader("🎯 Recommended Movies (Best to Worst):")
        for movie_title, similarity, avg_rating, num_ratings in results:
            st.write(f"- 🎬 **{movie_title}**")
            st.write(f"   - 🔍 **Similarity Score:** {similarity}")
            st.write(f"   - ⭐ **Average Rating:** {avg_rating}")
            st.write(f"   - 👥 **Number of Ratings:** {num_ratings}")
            st.markdown("---")