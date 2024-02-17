from discord.ext import commands

import Bot as Bot
from classes.TextCommand import TextCommand
from classes.Builders.SimpleBuilders.SimpleBuilder import SaludarBuilder, TulaBuilder
from classes.Builders.RequestBuilders.RequestBuilders import ValorantRequestBuilder, SabiduriaRequestBuilder
from classes.Builders.RequestBuilders.RequestBuildersById import RickMortyRequestBuilderById, DisneyRequestBuilderById, MTGRequestBuilderById, PokemonRequestBuilderById


class TextBotCog(commands.Cog, name="Comandos de texto"):
  def __init__(self, bot: Bot) -> None:
    self.bot = bot
    self.answerers: dict = {
      "hola": TextCommand(SaludarBuilder()),
      "tula": TextCommand(TulaBuilder()),
      "valorant": TextCommand(ValorantRequestBuilder()),
      "sabiduria": TextCommand(SabiduriaRequestBuilder()),
      "rick": TextCommand(RickMortyRequestBuilderById()),
      "disney": TextCommand(DisneyRequestBuilderById()),
      "mtg": TextCommand(MTGRequestBuilderById()),
      "pokemon": TextCommand(PokemonRequestBuilderById())
    }


  @commands.command(aliases=["saluda"])
  async def hola(self, ctx: commands.Context) -> None:
    """Te digo hola"""
    await self.answerers["hola"].answer(ctx)


  @commands.command()
  async def tula(self, ctx: commands.Context) -> None:
    """Te digo cuánto te mide la tula hoy"""
    await self.answerers["tula"].answer(ctx)


  @commands.command()
  async def valorant(self, ctx: commands.Context) -> None:
    """Te digo qué personaje de Valorant eres hoy"""
    await self.answerers["valorant"].answer(ctx)


  @commands.command()
  async def sabiduria(self, ctx: commands.Context) -> None:
    """Te digo una frase para motivarte"""
    await self.answerers["sabiduria"].answer(ctx)


  @commands.command(aliases=["morty", "rickymorty"])
  async def rick(self, ctx: commands.Context) -> None:
    """Te enseño qué personaje de Rick y Morty eres hoy"""
    await self.answerers["rick"].answer(ctx)
  
  
  @commands.command()
  async def disney(self, ctx: commands.Context) -> None:
    """Te enseño qué personaje de Disney (incluye Disney Channel) eres hoy"""
    await self.answerers["disney"].answer(ctx)

  
  @commands.command(aliases=["poke"])
  async def pokemon(self, ctx: commands.Context) -> None:
    """Cuidado con los arbustos"""
    await self.answerers["pokemon"].answer(ctx)