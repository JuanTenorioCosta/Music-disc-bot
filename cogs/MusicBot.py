from typing import cast
import discord
from discord.ext import commands
import wavelink

import Bot as Bot

class MusicBotCog(commands.Cog, name="Emilia DJ"):
  def __init__(self, bot: Bot) -> None:
    self.bot = bot
    self.nightcore = 0
    self.loop = 0

  @commands.command(aliases=["play"])
  async def p(self, ctx: commands.Context, *, cancion: str = commands.parameter(default="se ve.mp3", description="""
  Título de la canción que quieres escuchar. Si no elige satisfactoriamente la canción puedes añadir el autor.
  También puedes enviar la URL de una canción o PLAYLIST de Youtube, Spotify o Soundcloud.""")) -> None:
      """Reproduzco la canción que me pidas."""
      if not ctx.guild:
          return

      player: wavelink.Player
      player = cast(wavelink.Player, ctx.voice_client)  # type: ignore

      if not player:
          try:
              player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # type: ignore
          except AttributeError:
              await ctx.send(f"{ctx.author.mention} bobo, como quieres que te ponga música si no estás conectado.")
              return
          except discord.ClientException:
              await ctx.send(f"{ctx.author.mention} no me pude unir a tu canal de voz, dame permisos bobo.")
              return

      # Turn on AutoPlay to enabled mode.
      # enabled = AutoPlay will play songs for us and fetch recommendations...
      # partial = AutoPlay will play songs for us, but WILL NOT fetch recommendations...
      # disabled = AutoPlay will do nothing...
      player.autoplay = wavelink.AutoPlayMode.enabled
      # Lock the player to this channel...
      if not hasattr(player, "home"):
        player.home = ctx.channel
      elif player.channel != ctx.author.voice.channel:
        await ctx.send(f'{ctx.author.mention} no te pongas a pedirme que te ponga música en "{ctx.author.voice.channel}" si ya estoy tocando en "{player.channel}".')
        return

      # This will handle fetching Tracks and Playlists...
      # Seed the doc strings for more information on this method...
      # If spotify is enabled via LavaSrc, this will automatically fetch Spotify tracks if you pass a URL...
      # Defaults to YouTube for non URL based queries...
      tracks: wavelink.Search = await wavelink.Playable.search(cancion)
      if not tracks:
          await ctx.send(f"{ctx.author.mention} - ¿Qué has puesto?, esa canción no la conoce ni el tato.")
          return

      if isinstance(tracks, wavelink.Playlist):
          # tracks is a playlist...
          added: int = await player.queue.put_wait(tracks)
          await ctx.send(f"Añadido a la lista de reproducción **`{tracks.name}`** ({added} canciones) a la cola.")
      else:
          track: wavelink.Playable = tracks[0]
          await player.queue.put_wait(track)
          await ctx.send(f"{ctx.author.mention} ha añadido **`{track}`** a la cola.")

      if not player.playing:
          # Play now since we aren't playing anything...
          await player.play(player.queue.get(), volume=30)

      # Optionally delete the invokers message...
      try:
          await ctx.message.delete()
      except discord.HTTPException:
          pass


  @commands.command(aliases=["skip"])
  async def saltar(self, ctx: commands.Context) -> None:
      """Para la canción actual."""
      player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return

      await player.skip(force=True)
      await ctx.message.add_reaction("\u2705")


  @commands.command()
  async def nightcore(self, ctx: commands.Context) -> None:
      """Activa/desactiva filtro nightcore."""
      player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return

      filters: wavelink.Filters = player.filters
      if self.nightcore == 0:
          filters.timescale.set(pitch=1.2, speed=1.2, rate=1)
          self.nightcore = 1
      else:
          filters.timescale.set(pitch=1, speed=1, rate=1)
          self.nightcore = 0

      await player.set_filters(filters)
      await ctx.message.add_reaction("\u2705")


  @commands.command(aliases=["dale"])
  async def pausa(self, ctx: commands.Context) -> None:
      """Pausar o reproducir la música (cambia el estado en el que esté)."""
      player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return

      await player.pause(not player.paused)
      await ctx.message.add_reaction("\u2705")


  @commands.command(aliases=["dc", "disconnect", "stop", "para", "leave"])
  async def vete(self, ctx: commands.Context) -> None:
      """Si te aburres puedes echarme"""
      player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return

      await player.disconnect()
      await ctx.message.add_reaction("\u2705")


  @commands.command(aliases=["queue", "siguientes"])
  async def cola(self, ctx: commands.Context, *, pagina: int = commands.parameter(default=1, description="""
  Página de siguientes cancines. Cada página muestra 10 canciones""")) -> None:
      """Lista de las siguientes canciones"""
      player : wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return
      
      inicial: int = (pagina - 1) * 10
      limite: int = (pagina - 1) * 10 + 10
      contador: int = 0
      existe: int = 0
      cola: str = f'Página número {pagina} de canciones siguientes:\n'
      for cancion in player.queue:
          if(contador >= inicial and contador < limite):
              cola += f"{contador+1}. {cancion.title}\n"
              existe = 1

          contador += 1
      if existe == 1:
        await ctx.send(cola)
      else:
        await ctx.send(f"No hay tantas canciones en cola. Solo hay {contador+1} canciones en cola.")


  @commands.command(aliases=["delete"])
  async def borrar(self, ctx: commands.Context, *, indice: int = commands.parameter(default=1, description="""
  Puesto en la cola de la canción a borrar. Tiene que ser mayor que 1""")) -> None:
      """Borro la canción que me pidas si me dices donde está en la cola. Puedes usar ºcola para ver que canciones son las siguientes"""
      player : wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return
      try:
          indice = indice - 1
          await player.queue.delete(indice)
          await ctx.message.add_reaction("\u2705")
      except IndexError:
          await ctx.send(f"{ctx.author.mention} el valor de {indice} tiene que ser válido.")


  @commands.command(aliases=["barajar", "shuffle"])
  async def aleatorio(self, ctx: commands.Context) -> None:
      """Modo aleatorio para las canciones que hay en la cola"""
      player : wavelink.Player = cast(wavelink.Player, ctx.voice_client)
      if not player:
          return
      
      player.queue.shuffle()
      await ctx.message.add_reaction("\u2705")

  @commands.command(aliases=["bucle"])
  async def loop(self, ctx: commands.Context) -> None:
        """Poner en bucle la cola actual"""
        player : wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if not player:
            return
        
        if self.loop == 0:
            player.queue.mode = wavelink.QueueMode.loop_all
            self.loop = 1
        else:
            player.queue.mode = wavelink.QueueMode.normal
            self.loop = 0
        await ctx.message.add_reaction("\u2705")