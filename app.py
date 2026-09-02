import streamlit as st
import pickle
import requests
import time
from dotenv import load_dotenv
import os



load_dotenv()


api_key = os.getenv("TMDB_API_KEY")


def fetch_poster(movie_id):

    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(
        movie_id, api_key
    )

    for attempt in range(5):

        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            data = response.json()

            if data.get('poster_path'):
                return "https://image.tmdb.org/t/p/w500" + data['poster_path']

            return None

        except requests.exceptions.RequestException:

            if attempt < 4:
                time.sleep(2)
            else:
                return None

        except requests.exceptions.RequestException as e:

            if attempt == 2:
                st.error(f"Error fetching movie {movie_id}: {e}")
                return None

            time.sleep(1)


movies_list = pickle.load(open('movies.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):

    movie_index = movies_list[movies_list['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_indeces = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_indeces:

        movie_id = movies_list.iloc[i[0]].movie_id

        recommended_movies.append(
            movies_list.iloc[i[0]].title
        )

        poster = fetch_poster(movie_id)

        recommended_movies_posters.append(poster)

    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'Select an option....',
    movies_list['title'].values
)


if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.text(names[0])

        if posters[0] is not None:
            st.image(posters[0])

    with col2:

        st.text(names[1])

        if posters[1] is not None:
            st.image(posters[1])

    with col3:

        st.text(names[2])

        if posters[2] is not None:
            st.image(posters[2])

    with col4:

        st.text(names[3])

        if posters[3] is not None:
            st.image(posters[3])

    with col5:

        st.text(names[4])

        if posters[4] is not None:
            st.image(posters[4])
