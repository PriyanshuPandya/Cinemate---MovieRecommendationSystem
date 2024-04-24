# Cinemate Movie Recommender System

Cinemate is an interactive movie recommender system designed to help users discover new films based on their preferences and interests. Leveraging the power of machine learning and natural language processing, Cinemate provides personalized movie recommendations by analyzing movie attributes such as genre, cast, and keywords.

## Introduction

In today's vast landscape of streaming platforms and digital movie libraries, finding the perfect movie to watch can be overwhelming. Cinemate aims to simplify this process by offering a user-friendly interface where users can explore a curated selection of movies tailored to their tastes.

Whether you're a cinephile seeking hidden gems or a casual viewer looking for your next weekend binge, Cinemate has you covered. With a diverse database of movies spanning various genres and styles, there's something for everyone to enjoy.

## Features

- **Interactive Interface**: Cinemate features a sleek and intuitive interface that allows users to easily browse and select movies.
- **Personalized Recommendations**: Using advanced algorithms, Cinemate generates customized movie recommendations based on user preferences.
- **Rich Movie Information**: Users can access detailed information about each recommended movie, including summaries, cast lists, and more.
- **Responsive Design**: Cinemate is designed to work seamlessly across devices, from desktop computers to mobile phones, ensuring a consistent experience for all users.

## Installation

To run the Cinemate Movie Recommender System locally, follow these steps:

1. Follow the `config.ipynb` for Data Processing and Model Defination.
2. Use `app.py` for streamlit setup.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Streamlit application using `streamlit run app.py`.
5. Access the application in your web browser at `http://localhost:8501`.

## Data Sources

- The movie data used in this project was sourced from the TMDB API.
- Link : `https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata` 
- Two datasets were utilized: "tmdb_5000_movies.csv" and "tmdb_5000_credits.csv".
- These datasets contain information about movies, including their titles, overviews, genres, keywords, cast, and crew.

## Methodology

The Cinemate Movie Recommender System employs a combination of data preprocessing, natural language processing, and machine learning techniques:

1. **Data Collection**: Movie data is collected from the TMDB API and stored in Pandas DataFrames.
2. **Data Preprocessing**: The collected data is cleaned, processed, and transformed to extract relevant features such as genres, keywords, cast, and crew.
3. **Vectorization**: Text data is vectorized using the CountVectorizer to convert movie attributes into numerical representations.
4. **Similarity Calculation**: Cosine similarity is calculated between movie vectors to identify similar movies.
5. **Recommendation Generation**: Based on user-selected preferences, the system generates recommendations by selecting movies with the highest cosine similarity scores.
