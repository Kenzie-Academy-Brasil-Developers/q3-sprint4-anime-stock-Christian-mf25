from flask import jsonify, request
from app.models.anime_model import Anime
from psycopg2.errors import UniqueViolation, UndefinedColumn

def animes():
	animes = Anime.read_animes()
	animes_list = Anime.serialize_anime(animes)

	return jsonify({"data": animes_list}), 200

def select_by_id(anime_id):
	anime = Anime.read_by_id(anime_id)
	if not anime:
		return {"error": "Not Found"}, 404
	selected_anime = Anime.serialize_anime(anime)
	return jsonify({"data": selected_anime}), 200

def create():
	data = request.get_json()
	anime_keys = Anime.keys_to_compare
	data_keys = data.keys()
	try: 
		anime = Anime(**data)
		create_anime = anime.create_anime()
	
	except KeyError as e:
		wrong_key = list(data_keys - anime_keys)
		return jsonify({"available_keys": anime_keys, "wrong_keys_sended": wrong_key}), 422
	
	except UniqueViolation as e:
		return jsonify({"error": e.args}), 422
	
	inserted_anime = Anime.serialize_anime(create_anime)	
	return jsonify(inserted_anime), 201

def update_anime(anime_id):
	data = request.get_json()
	anime_keys = Anime.keys_to_compare
	data_keys = data.keys()

	try: 
		updated_anime = Anime.update_anime(anime_id, data)

	except KeyError as e:
		wrong_key = list(data_keys - anime_keys)
		return jsonify({"available_keys": anime_keys, "wrong_keys_sended": wrong_key}), 422
	
	except UndefinedColumn:
		return {"error": "Not Found"}, 404		

	anime = Anime.serialize_anime(updated_anime)
	return jsonify(anime), 200

def delete_anime(anime_id):
	deleted = Anime.delete_anime_by_id(anime_id)
	if not deleted:
		return {"error": "Not Found"}, 404
	anime = Anime.serialize_anime(deleted)
	return jsonify({"removed": anime})
