from discord.ext import commands

from classes.Builders.RequestBuilders._RequestBuilders import RequestBuilderById

class RickMortyRequestBuilderById(RequestBuilderById):
  def __init__(self):
    super().__init__('https://rickandmortyapi.com/api/character/', 825)
  
  def do_request(self, ctx: commands.Context) -> dict:
    return super().do_request(ctx)
  
  def build_answer_from_json(self, json_data: dict) -> [str]:
    personaje: str = f'No creo que a Rick le vaya a gustar que tu seas {json_data["name"]}.'
    imagen: str = f'{json_data["image"]}'
    return [personaje, imagen]
  
  def build_answer(self, ctx: commands.Context) -> [str]:
    return super().build_answer(ctx)

class DisneyRequestBuilderById(RequestBuilderById):
  def __init__(self):
    super().__init__('https://api.disneyapi.dev/character/', 2585)
  
  def do_request(self, ctx: commands.Context) -> dict:
    return super().do_request(ctx)
  
  def build_answer_from_json(self, json_data: dict) -> [str]:
    json_data: dict = json_data["data"]
    personaje: str = f'El famosísimo personaje {json_data["name"]}.'
    imagen: str = f'{json_data["imageUrl"]}'
    return [personaje, imagen]
  
  def build_answer(self, ctx: commands.Context) -> [str]:
    return super().build_answer(ctx)
  
class MTGRequestBuilderById(RequestBuilderById):
  def __init__(self):
    super().__init__('https://api.magicthegathering.io/v1/cards/', 5867)
  
  def do_request(self, ctx: commands.Context) -> dict:
    return super().do_request(ctx)
  
  def build_answer_from_json(self, json_data: dict) -> [str]:
    json_data: dict = json_data["card"]
    personaje: str = f'Cartón espantoso {json_data["name"]}.'
    imagen: str = f'{json_data["imageUrl"]}'
    return [personaje, imagen]
  
  def build_answer(self, ctx: commands.Context) -> [str]:
    return super().build_answer(ctx)
