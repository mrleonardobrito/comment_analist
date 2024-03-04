from typing import List
import pandas as pd
from src.movie.model import Movie

class MovieRepository:
    def get_movies(self) -> List[Movie]:
        movies: pd.DataFrame = pd.read_csv("data/movies.csv")
        ratings: pd.DataFrame = pd.read_csv("data/ratings.csv", nrows=10000)
        movies.columns = ["id", "name", "genres"]
        ratings_mean: pd.Series = ratings.groupby("movieId")["rating"].mean()
        movies["rating_mean"] = ratings_mean

        ratings_total: pd.Series = ratings["movieId"].value_counts()
        movies["rating_quant"] = ratings_total

        return [Movie(movie=movie) for movie in movies.to_dict("records")]