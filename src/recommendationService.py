from src.movie.repo import MovieRepository
from src.user.repo import UserRepository
from src.movie.model import Movie
from src.user.model import Rating
from typing import List
import pandas as pd

class RecommenderService:
    def __init__(self, correlation_matrix):
        self.user_repo = UserRepository()
        self.movie_repo = MovieRepository()
        self.item_similarity_df = correlation_matrix

    def recommend(self, user_id: int, top_n: int = 10) -> List[Movie]:
        user_ratings = self.user_repo.get_user_ratings(user_id)
        user_ratings = pd.DataFrame([rating.to_dict() for rating in user_ratings])

        user_ratings = user_ratings[user_ratings['movie_id'].isin(self.item_similarity_df.index)]

        if user_ratings.empty:
            print("Empty Ratings")
            return []

        movie_ids = user_ratings['movie_id'].tolist()
        similarity_scores = self.item_similarity_df.loc[movie_ids].T * (user_ratings['rating'].values - 2.5)

        similar_movies = similarity_scores.sum(axis=1).sort_values(ascending=False)

        recommended_movie_ids = similar_movies.index[:top_n]
        recommended_movies = [Movie(movie.to_dict()) for movie in self.movie_repo.get_movies() if movie.id in recommended_movie_ids]
        recommended_movies = sorted(recommended_movies, key=lambda x: x.rating_mean, reverse=True)

        return recommended_movies
    
    def recommend_from_rating_list(self, rating_list: List[Rating], top_n: int = 10):
        user_ratings = pd.DataFrame([rating.to_dict() for rating in rating_list])
        user_ratings = user_ratings[user_ratings['movie_id'].isin(self.item_similarity_df.index)]

        if user_ratings.empty:
            print("Empty Ratings")
            return []

        movie_ids = user_ratings['movie_id'].tolist()
        similarity_scores = self.item_similarity_df.loc[movie_ids].T * (user_ratings['rating'].values - 2.5)

        similar_movies = similarity_scores.sum(axis=1).sort_values(ascending=False)

        recommended_movie_ids = similar_movies.index[:top_n]
        recommended_movies = [Movie(movie.to_dict()) for movie in self.movie_repo.get_movies() if movie.id in recommended_movie_ids]
        recommended_movies = sorted(recommended_movies, key=lambda x: x.rating_mean, reverse=True)

        return recommended_movies   

