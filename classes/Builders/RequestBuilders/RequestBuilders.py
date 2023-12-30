from discord.ext import commands

from classes.Builders.RequestBuilders._RequestBuilders import RequestBuilder
  
class SabiduriaRequestBuilder(RequestBuilder):
  def __init__(self):
    super().__init__("https://zenquotes.io/api/random")
  
  def do_request( self, ctx: commands.Context ) -> dict:
    return super().do_request(ctx)
  
  def build_answer_from_json(self, json_data) -> [str]:
    quote: str = json_data[0]["q"] + " -" + json_data[0]["a"]
    return [quote]
  
  def build_answer(self, ctx: commands.Context) -> str:
    return super().build_answer(ctx)
  

"""
No tomar esta clase como ejemplo. El caso de valorant es muy particular.
Debería ser RequestBuilderById pero la API no permite utilizar ids númericos planos.
Evitar usar esta clase como boilerplate
"""
class ValorantRequestBuilder(RequestBuilder):
  def __init__(self):
    super().__init__("https://valorant-api.com/v1/agents?isPlayableCharacter=true", 23)
  
  def do_request( self, ctx: commands.Context ) -> dict:
    json_data: dict = super().do_request(ctx)
    return json_data["data"][ self.get_random_number(ctx, self.maxNumber) ]
  
  def build_answer_from_json(self, json_data: dict) -> [str]:
    agente: str = f'Eres {json_data["displayName"]}. ¿Y ese rifle?:'
    imagen: str = f'{json_data["fullPortraitV2"]}'
    return [agente, imagen]
  
  def build_answer(self, ctx: commands.Context) -> [str]:
    return super().build_answer(ctx)