
from typing import Dict, Any

class Movie:
    def __init__(self, movie: Dict[str, Any]) -> None:
        self.id: int = movie["id"]
        self.name: str = movie["name"]
        self.genres: str = movie["genres"]
        self.rating_quant: int = movie["rating_quant"]
        self.rating_mean: float = movie["rating_mean"]

    def __str__(self) -> str:
        return (
            f"Movie(id={self.id}, name='{self.name}', genres='{self.genres}', "
            f"rating_quant={self.rating_quant}, rating_mean={self.rating_mean})"
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "genres": self.genres,
            "rating_quant": self.rating_quant,
            "rating_mean": self.rating_mean
        }

    @classmethod
    def from_dict(cls, movie_dict: Dict[str, Any]) -> "Movie":
        return cls(movie_dict)
