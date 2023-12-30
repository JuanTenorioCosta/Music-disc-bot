from abc import abstractmethod
from discord.ext import commands

import requests
import json

from classes.BuilderInterface import BuilderInterface


class RequestBuilder(BuilderInterface):
  def __init__(self, api: str, maxNumber:int=0):
    self.api: str = api
    self.maxNumber: int = maxNumber


  def do_request( self, ctx: commands.Context = 0 ) -> dict:
    response = requests.get(f"{self.api}")
    json_data: dict = json.loads(response.text)
    return json_data


  @abstractmethod
  def build_answer_from_json( self, json_data: dict ) -> [str]:
    pass


  def build_answer( self, ctx: commands.Context ) -> [str]:
    return self.build_answer_from_json( self.do_request(ctx) )



class RequestBuilderById(RequestBuilder):
  def __init__(self, api: str, maxNumber: int):
    super().__init__(api, maxNumber)


  def do_request(self, ctx: commands.Context) -> dict:
    randNumber: int = self.get_random_number(ctx, self.maxNumber)
    response = requests.get(f"{self.api}{randNumber}")
    json_data: dict = json.loads(response.text)
    return json_data
  

  @abstractmethod
  def build_answer_from_json(self, json_data: dict) -> [str]:
    pass


  def build_answer(self, ctx: commands.Context) -> [str]:
    return super().build_answer(ctx)