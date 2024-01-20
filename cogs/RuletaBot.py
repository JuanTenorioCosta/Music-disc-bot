from discord.ext import commands
import re

import Bot as Bot

from classes.Builders.DbBuilders.RuletaCommandAnswerer import RuletaCommandAnswerer

class RuletaBotCog(commands.Cog, name="Ruleta de videojuegos"):
  def __init__(self, bot: Bot) -> None:
    self.bot = bot
    self.answerer = RuletaCommandAnswerer()


  async def answer(self, ctx: commands.Context, message: str):
    await ctx.send(message)

  @commands.command(aliases=["quejuego", "nose"])
  async def ruleta(self, ctx: commands.Context, *, numJugadores: int = commands.parameter(default=0, description="""
  Número de jugadores para jugar.""")) -> None:
    """¿No sabes a qué jugar? Te lo digo yo."""
    answer: str = self.answerer.ruleta(ctx, numJugadores)
    await self.answer(ctx, answer)

  @commands.command()
  async def defecto(self, ctx: commands.Context, *, numJugadores: int = commands.parameter(default=0, description="""
  Número de jugadores para jugar.""")) -> None:
    """¿No sabes a qué jugar? Te lo digo yo."""
    answer: str = self.answerer.defecto(ctx, numJugadores)
    await self.answer(ctx, answer)


  @commands.command(aliases=["juegos"])
  async def lista(self, ctx: commands.Context, *, numJugadores: int = commands.parameter(default=0, description="""
  Número de jugadores para jugar.""")) -> None:
    """Lista de juegos en tu ruleta para jugar."""
    answer: str = self.answerer.lista(ctx, numJugadores)
    await self.answer(ctx, answer)

  @commands.command(aliases=["añadir"])
  async def nuevo(self, ctx: commands.Context, *, nombreJuego: str = commands.parameter(description="""
  Nombre del juego a añadir en tu ruleta.""")) -> None:
    """Añadir un nuevo juego a tu ruleta personal."""
    answer: str = self.answerer.nuevo(ctx, nombreJuego)
    await self.answer(ctx, answer)

  @commands.command(aliases=["añadir"])
  async def nuevo(self, ctx: commands.Context, nombreJuego: str = commands.parameter(description="""
  Nombre del juego a añadir en tu ruleta."""), *, numJugadores: str = commands.parameter(default= "", description="""
  Numero de jugadores disponibles.""")) -> None:
    """Añadir un nuevo juego a tu ruleta personal."""
    answer: str
    nombreJuego = nombreJuego.upper()
    if( numJugadores == "" ):
      answer = self.answerer.nuevo(ctx, nombreJuego, [])
    else:
      int_array = list(map(int, re.split(r'\D+', numJugadores)))
      answer = self.answerer.nuevo(ctx, nombreJuego, int_array)
    await self.answer(ctx, answer)

  @commands.command()
  async def eliminar(self, ctx: commands.Context, *,nombreJuego: str = commands.parameter(description="""
  Nombre del juego a eliminar de tu ruleta.""")) -> None:
    """Eliminar un juego de tu ruleta personal."""
    answer: str
    nombreJuego = nombreJuego.upper()
    answer = self.answerer.eliminar(ctx, nombreJuego)
    await self.answer(ctx, answer)