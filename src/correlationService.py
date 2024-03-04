import pandas as pd

class CorrelationService:
    def __init__(self, user_repo, movie_repo):
        self.user_repo = user_repo
        self.movie_repo = movie_repo

    def generate_correlation_matrix(self):
        all_ratings = self.user_repo.get_users_ratings()
        all_ratings = pd.DataFrame([rating.to_dict() for rating in all_ratings])
        
        all_movies =  self.movie_repo.get_movies()
        all_movies= pd.DataFrame([movie.to_dict() for movie in all_movies])
        filtered_movies = all_movies[all_movies["rating_quant"] > 0]

        all_ratings = all_ratings[all_ratings["movie_id"].isin(filtered_movies["id"])]
         
        all_user_ratings = all_ratings.pivot_table("rating", index = "user_id", columns = "movie_id")
        all_user_ratings = all_user_ratings.dropna(thresh=10, axis=1).fillna(0)

        return all_user_ratings.corr(method = "pearson").round(2)