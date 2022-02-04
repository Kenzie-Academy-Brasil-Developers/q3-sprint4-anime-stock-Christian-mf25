from flask import Blueprint
from app.controllers import anime_controllers

bp = Blueprint("animes", __name__, url_prefix="/animes")

bp.get("")(anime_controllers.animes)
bp.get("/<anime_id>")(anime_controllers.select_by_id)
bp.post("")(anime_controllers.create)
bp.patch("/<anime_id>")(anime_controllers.update_anime)
bp.delete("/<anime_id>")(anime_controllers.delete_anime)