from flask import Flask, jsonify, request
from typing import Dict, Any, List
from src.recommendationService import RecommenderService
from src.correlationService import CorrelationService
from src.user.repo import UserRepository
from src.movie.repo import MovieRepository
from src.user.model import Rating

app = Flask(__name__)
correlation_matrix = None

@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        user_id = int(request.args.get('user'))
        recommenderService = RecommenderService(correlation_matrix=correlation_matrix)
        movies = [movie.to_dict() for movie in recommenderService.recommend(user_id)]

        return jsonify(movies)
    elif request.method == 'POST':
        ratings = request.json['ratings']
        user_id = request.json['user_id']

        rating_list = [Rating(rating["movie_id"], rating["rating"], user_id) for rating in ratings]
        recommenderService = RecommenderService(correlation_matrix=correlation_matrix)
        movies = [movie.to_dict() for movie in recommenderService.recommend_from_rating_list(rating_list)]

        return jsonify(movies)

    else:    
        return 'Método não permitido', 405

if __name__ == '__main__':
    print("Generating correlation matrix...")
    correlation_matrix= CorrelationService(UserRepository(), MovieRepository()).generate_correlation_matrix()
    print("Correlation matrix generated.")
    app.run(debug=True)
