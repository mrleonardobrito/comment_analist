import pandas as pd
from typing import List
from src.user.model import Rating

class UserRepository:
    def get_users_ratings(self) -> List[Rating]:
        ratings = pd.read_csv("data/ratings.csv", nrows=10000)
        return [Rating(movie_id=rating["movieId"], rating=rating["rating"], user_id=rating["userId"]) for rating in ratings.to_dict("records")]
    
    def get_user_ratings(self, user_id) -> List[Rating]:
        ratings = pd.read_csv("data/ratings.csv", nrows=10000)
        ratings = ratings[ratings["userId"] == user_id]

        return [Rating(movie_id=rating["movieId"], rating=rating["rating"], user_id=rating["userId"]) for rating in ratings.to_dict("records")]