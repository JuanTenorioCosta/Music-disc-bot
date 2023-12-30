from classes.BuilderInterface import BuilderInterface
from discord.ext import commands

from FakeDBs.ids import ids

class SaludarBuilder(BuilderInterface):
  def __init__(self):
    pass

  def build_answer( self, ctx: commands.Context ) -> [str]:
    if ctx.author.id == ids["20scar"]:
      return ['¡Oscar te quiero!']
    else:
      return ['No eres Óscar :(']
    
class TulaBuilder(BuilderInterface):
  def __init__(self):
    pass

  def build_answer( self, ctx: commands.Context ) -> [str]:
    tamano_tula = self.get_random_number(ctx, 25)
    if(tamano_tula < 3):
      return [f'Hoy no salgas a la calle, que la tienes metida pa\'dentro. Solo {tamano_tula}cm.']
    if(tamano_tula < 9):
      return [f'Dios le da sus peores batallas a sus mejores gerreros. Tienes que ser un gran gerrero porque solo te mide {tamano_tula}cm.']
    if(tamano_tula < 13):
      return [f'Bueno, una tula es una tula. La tuya en concreto {tamano_tula}cm.']
    if(tamano_tula < 17):
      return [f'Hoy estás para usar eso que te cuelga crack. Vaya tula de {tamano_tula}cm.']
    if(tamano_tula < 23):
      return [f'Vaya, vaya, vaya. Casi como mi amorcito Óscar, vaya tula de {tamano_tula}cm.']
    
    return [f'Ten cuidado con Óscar, entre bomberos no pisarse la manguera. Vaya tulón de {tamano_tula}cm.']