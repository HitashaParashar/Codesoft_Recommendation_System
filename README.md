# 🎬 Movie Recommendation System

A collaborative filtering based movie recommendation system built using Python.

## 📌 Project Overview
This project recommends movies to users based on their past ratings and the ratings of similar users (User-Based Collaborative Filtering).

## 🛠️ Tech Stack
- Python 3.11
- Pandas & NumPy
- Scikit-learn (Cosine Similarity)
- Matplotlib & Seaborn
- Streamlit (UI)
- Jupyter Notebook

## 📁 Project Structure
Codesoft_Recommendation_System/
├── data/
│   ├── u.data
│   └── u.item
├── main.ipynb
├── app.py
└── README.md

## 📊 Dataset
- Source: MovieLens 100K
- Total Ratings: 1,00,000
- Total Users: 943
- Total Movies: 1,682

## ⚙️ How to Run

Install Dependencies:
pip install pandas numpy scikit-learn matplotlib seaborn streamlit

Run Streamlit App:
streamlit run app.py

## 📈 Model Performance
- Algorithm: User-Based Collaborative Filtering
- Similarity Metric: Cosine Similarity
- RMSE: 1.1077

## 🔮 How It Works
1. Load user ratings data
2. Build User-Item Matrix
3. Compute Cosine Similarity between users
4. Find top similar users
5. Recommend movies that similar users liked

