import pandas as pd
import streamlit as st
import pickle
import requests

# Set Streamlit theme
def set_theme():
    # Set page config
    st.set_page_config(
        page_title="Cinemate-MovieRecommenderSystem",
        page_icon="🎬",
        layout="centered"
    )
    # Set custom CSS
    st.markdown(
        """
        <style>
        body, .stApp {
            margin-top:-60px;
            background-image: linear-gradient(to bottom right, #E9D8D8, #AA9696, #967474);
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #664B4B !important;
            padding: 10px;
            text-align: center;
            color: #fff !important;
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=14cb47102f782632b4f8296e0140f714".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'], data['homepage'] if 'homepage' in data else None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_homepage = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster
        fetched_poster, fetched_homepage = fetch_poster(movie_id)
        recommended_movies_posters.append(fetched_poster)
        recommended_movies_homepage.append(fetched_homepage)
    return recommended_movies, recommended_movies_posters, recommended_movies_homepage

def get_info(movie_id):
    movie_row = movie_info[movie_info['movie_id'] == movie_id]
    overview = movie_row['overview'].values[0]
    cast = ', '.join(movie_row['cast'].values[0])
    crew = ', '.join(movie_row['crew'].values[0])

    info_text = f"\n{overview}\n\n"
    info_text += f"**Star Cast:**\n{cast}\n\n"
    info_text += f"**Directed By:**\n{crew}"

    return info_text

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movie_info = pd.DataFrame(pickle.load(open('movie_info.pkl','rb')))
similarity = pickle.load(open('similarity.pkl','rb'))

set_theme()  # Apply custom theme

st.header('Cinemate - A Movie Recommender System')

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    ['Enter the Movie'] + list(movies['title'].values),
)

selected_movie_poster = None
# Check if the selected movie is the placeholder text
if selected_movie != 'Enter the Movie':
    try:
        selected_movie_poster, selected_movie_homepage = fetch_poster(movies[movies['title'] == selected_movie]['movie_id'].values[0])
    except IndexError:
        st.error("No movie has been selected.")

if selected_movie_poster is not None:
    colA, colB = st.columns([0.2,0.8])
    with colA:
        st.markdown(f'<a href="{selected_movie_homepage}" target="_blank"><img src="{selected_movie_poster}" width="100"></a>', unsafe_allow_html=True)
    with colB:
        st.caption(get_info(movies[movies['title'] == selected_movie]['movie_id'].values[0]))

if st.button('Recommend') and (selected_movie != "Enter the Movie"):
    name, poster, homepage = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(5):
        with locals()[f"col{i+1}"]:
            st.text(name[i])
            st.markdown(f'<a href="{homepage[i]}" target="_blank"><img src="{poster[i]}" width="100"></a>', unsafe_allow_html=True)

# Footer content
st.markdown('<br><div class="footer">Developed by Priyanshu Pandya</div><br>', unsafe_allow_html=True)
