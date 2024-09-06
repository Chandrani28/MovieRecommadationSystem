import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" +poster_path
    return full_path
movies=pickle.load(open("movies_list.pk1", 'rb'))
similarity=pickle.load(open("similarity.pk1", 'rb'))
movies_list= movies['title'].values

st.header("Movie Recommender System")

# Create a dropdown to select a movie 
selected_movie = st.selectbox("Select a movie:", movies_list)

import streamlit.components.v1 as components



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate (similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = [] 
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id)) 
    return recommend_movie, recommend_poster
if st.button("Recommend"):
    movie_name,movie_poster=recommend(selected_movie) 
    coll, col2, col3, col4, col5 = st.columns(5)
    with coll:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1]) 
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])





