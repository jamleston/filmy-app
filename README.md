# Movie Recommendation App

## Project Overview

This project is a **web-based application** that provides **movie recommendations** based on **genre similarity**. Users can enter a movie title, and the app suggests the most relevant movies based on **text-based analysis of genres**. The project utilizes **machine learning techniques** to compute similarity and delivers recommendations in an easy-to-use **Streamlit web app**.

## Features

**Movie Search & Recommendation**  
- Enter a movie title and get **5 recommended movies**.  

**Similarity-Based Recommendations**  
- Uses **genre-based similarity** to find the best matches.  

**Ratings & Popularity Display**  
- Shows **average rating** and **number of ratings** for each recommendation.  

**Fast & Efficient**  
- Precomputed **TF-IDF vectorization** for real-time recommendations.  

## Technologies Used

- **Languages**: Python  
- **Libraries**:
  - **pandas** → Data handling  
  - **scikit-learn** → Machine learning (TF-IDF, similarity metrics)  
  - **joblib** → Model saving & loading  
  - **Streamlit** → Web application  
- **Tools**:
  - **Jupyter Notebook** → Model development

## Installation

To run this project, follow these steps:

### 1️. **Clone the Repository**
```
git clone https://github.com/jamleston/filmy-app
cd filmy-app
```

### 2. **Run the Streamlit Application**
```
streamlit run app.py
```

## Usage
1. Enter a movie title in the search box.
2. The app will return 5 recommended movies based on genre similarity.
3. Additional details:
- Average rating
- Number of ratings

## Project Structure
```
├── models/                       # Saved machine learning models
│   ├── tfidf_vectorizer.joblib   # TF-IDF vectorizer for text processing
│   ├── genre_matrix.joblib       # Precomputed genre similarity matrix
├── app.py                        # Streamlit application
├── prep.ipynb                    # Data loading & preprocessing
├── movies.csv                    # Original dataset
├── ratings.csv                   # Original dataset
├── movies_with_ratings.csv       # Processed dataset
├── analysis.ipynb                # First look at datasets and first tries of app
├── model.ipynb                   # Model developing
├── README.md                     # Project documentation
```

## Developed by
- [Valeriia Alieksieienko](https://github.com/jamleston)