import abc
from discord.ext import commands

import random
from datetime import date

class BuilderInterface(metaclass=abc.ABCMeta):
  @classmethod
  def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'build_answer') and 
                callable(subclass.build_answer))

  @abc.abstractmethod
  def build_answer(self, ctx: commands.Context = 0) -> [str]:
      """Return an array with response"""
      raise NotImplementedError


  def get_random_number( self, ctx: commands.Context, maxNumber: int ) -> int:
    today = date.today()
    dia = today.day
    mes = today.month
    ano = today.year
    random.seed( ctx.author.id + dia + mes + ano )
    return random.randint(1, maxNumber)