from typing import Dict, Any, List

class Rating:
    def __init__(self, movie_id, rating, user_id=None):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
    
    def __str__(self) -> str:
        return f"Rating(movie_id={self.movie_id}, rating={self.rating}), user_id={self.user_id})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "movie_id": self.movie_id,
            "rating": self.rating,
            "user_id": self.user_id
        }
    
    @classmethod
    def from_dict(cls, rating_dict: Dict[str, Any]) -> "Rating":
        return cls(movie_id=rating_dict["movie_id"], rating=rating_dict["rating"],  user_id=rating_dict["user_id"])

class User:
    def __init__(self, user_id: int, ratings: List[Rating]) -> None:
        self.id: int = user_id
        self.ratings: list = ratings

    def __str__(self) -> str:
        return f"User(id={self.id}, ratings={self.ratings})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "ratings": self.ratings
        }

    @classmethod
    def from_dict(cls, user_dict: Dict[str, Any]) -> "User":
        return cls(user_id=user_dict["id"], ratings=user_dict["ratings"])


    

