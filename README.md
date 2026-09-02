# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python, Pandas, Scikit-learn and Streamlit.

## 🚀 Live Demo

[Try the Movie Recommender System](https://movierecommendersystem-quhzkjqdp99nwwstaty4pf.streamlit.app/)

## 📌 Features

- Select a movie from the dropdown
- Get 5 similar movie recommendations
- Display movie posters
- Content-based recommendation
- Interactive Streamlit UI
- TMDB API integration

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- TMDB API
- Pickle

## 🧠 How It Works

The system uses a content-based recommendation approach.

Movie features such as genres, keywords, cast and crew are combined to create tags.

These features are converted into numerical vectors and cosine similarity is used to calculate similarity between movies.

When a user selects a movie, the system finds the most similar movies and recommends the top 5.

## 📂 Project Structure

```text
MovierecommenderSystem/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md