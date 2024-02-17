from discord.ext import commands

from random import randint

from FakeDBs.Ruleta.RuletaModel import RuletaModel


class RuletaCommandAnswerer():
  def __init__(self):
    self.ruletaModel = RuletaModel()

  def ruleta( self, ctx: commands.Context, playersNum: int = 0 ) -> str:
    userGames: dict = self.ruletaModel.getGames( ctx.author.name, playersNum )
    return f'Vamoh a jugah a {userGames[ randint(0, (len(userGames) - 1)) ]["name"]}'
  
  def defecto( self, ctx: commands.Context, playersNum: int = 0 ) -> str:
    userGames: dict = self.ruletaModel.getGames( "default", playersNum )
    return f'Vamoh a jugah a {userGames[ randint(0, (len(userGames) - 1)) ]["name"]}'
        
      
  def lista( self, ctx: commands.Context, playersNum: int = 0 ) -> str:
    userGames: dict = self.ruletaModel.getGames( ctx.author.name, playersNum )
    answer: str = f'A menos que hayas editado tu ruleta, los juegos que se muestran son por defecto.\nRuleta de {ctx.author.mention}'
    if playersNum != 0:
      answer += 'para {playersNum} jugadores'
    answer += ":\n"

    for game in userGames:
      if "availableNumPlayers" in game:
        answer += f'{game["name"]}: Para {game["availableNumPlayers"]} jugadores\n'
      else:
        answer += f'{game["name"]}: Para cualquier número de jugadores\n'
    return answer
  

  def nuevo( self, ctx: commands.Context, nombreJuego: str, numJugadores: list[int]) -> str:
    nuevoJuego: dict
    answer: str
    if len(numJugadores) == 0:
      nuevoJuego = { "name": nombreJuego }
      answer = f'He añadido {nuevoJuego["name"]} a tu ruleta personal para cualquier número de jugadores'
    else:
      nuevoJuego = { "name": nombreJuego, "availableNumPlayers": numJugadores }
      answer = f'He añadido {nuevoJuego["name"]} a tu ruleta personal para {numJugadores}'
    self.ruletaModel.writeGame( ctx.author.name, nuevoJuego )
    return answer
  
  def eliminar( self, ctx: commands.Context, nombreJuego: str) -> str:
    try:
      self.ruletaModel.deleteGame( ctx.author.name, nombreJuego )
    except AttributeError:
      return f'{ctx.author.mention} tienes que haber personalizado tu ruleta para poder eliminar juegos. Asegúrate de haber escrito bien el nombre del juego.'
  
