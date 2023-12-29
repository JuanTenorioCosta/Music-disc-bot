import asyncio
import logging
from typing import cast

from decouple import config

import discord
from discord.ext import commands

import wavelink


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents: discord.Intents = discord.Intents.default()
        intents.message_content = True
        self.nightcore = 0

        discord.utils.setup_logging(level=logging.INFO)
        super().__init__(command_prefix="º", intents=intents)

    async def setup_hook(self) -> None:
        nodes = [wavelink.Node(uri="http://localhost:2333", password=config('PASSWORD'))] # port="2333"

        # cache_capacity is EXPERIMENTAL. Turn it off by passing None
        await wavelink.Pool.connect(nodes=nodes, client=self, cache_capacity=100)

    async def on_ready(self) -> None:
        logging.info(f"Logged in: {self.user} | {self.user.id}")

    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        logging.info(f"Wavelink Node connected: {payload.node!r} | Resumed: {payload.resumed}")

    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            # Handle edge cases...
            return

        original: wavelink.Playable | None = payload.original
        track: wavelink.Playable = payload.track

        embed: discord.Embed = discord.Embed(title="Estoy tocando para ti:")
        embed.description = f"**{track.title}** de `{track.author}`, te quejarás payaso"

        if track.artwork:
            embed.set_image(url=track.artwork)

        if original and original.recommended:
            embed.description += f"\n\n`Recomendación via {track.source}`"

        if track.album.name:
            embed.add_field(name="Album", value=track.album.name)

        await player.home.send(embed=embed)


bot: Bot = Bot()


@bot.command()
async def play(ctx: commands.Context, *, query: str) -> None:
    """Play a song with the given query."""
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
    elif player.home != ctx.channel:
        await ctx.send(f"No te pongas a pedirme que te ponga música si ya estoy tocando en otro lado.")
        return

    # This will handle fetching Tracks and Playlists...
    # Seed the doc strings for more information on this method...
    # If spotify is enabled via LavaSrc, this will automatically fetch Spotify tracks if you pass a URL...
    # Defaults to YouTube for non URL based queries...
    tracks: wavelink.Search = await wavelink.Playable.search(query)
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
        await ctx.send(f"Añadido **`{track}`** a la cola.")

    if not player.playing:
        # Play now since we aren't playing anything...
        await player.play(player.queue.get(), volume=30)

    # Optionally delete the invokers message...
    try:
        await ctx.message.delete()
    except discord.HTTPException:
        pass


@bot.command()
async def skip(ctx: commands.Context) -> None:
    """Skip the current song."""
    player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
    if not player:
        return

    await player.skip(force=True)
    await ctx.message.add_reaction("\u2705")


@bot.command()
async def nightcore(ctx: commands.Context) -> None:
    """Set the filter to a nightcore style."""
    player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
    if not player:
        return

    if bot.nightcore == 0:
        filters: wavelink.Filters = player.filters
        filters.timescale.set(pitch=1.2, speed=1.2, rate=1)
        await player.set_filters(filters)
        bot.nightcore = 1
    else:
        filters: wavelink.Filters = player.filters
        filters.timescale.set(pitch=1, speed=1, rate=1)
        await player.set_filters(filters)
        bot.nightcore = 0

    await ctx.message.add_reaction("\u2705")


@bot.command(aliases=["dale"])
async def pausa(ctx: commands.Context) -> None:
    """Pause or Resume the Player depending on its current state."""
    player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
    if not player:
        return

    await player.pause(not player.paused)
    await ctx.message.add_reaction("\u2705")

"""
@bot.command()
async def volume(ctx: commands.Context, value: int) -> None:
    ""Change the volume of the player.""
    player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
    if not player:
        return

    await player.set_volume(value)
    await ctx.message.add_reaction("\u2705")
"""

@bot.command(aliases=["dc"])
async def vete(ctx: commands.Context) -> None:
    """Disconnect the Player."""
    player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
    if not player:
        return

    await player.disconnect()
    await ctx.message.add_reaction("\u2705")

@bot.command(aliases=["ayuda"])
async def comandos(ctx: commands.Context) -> None:
    """Lista de comandos."""
    await ctx.send('''
Para llamarme tienes que usar **º** (La tecla que usarías para poner segundo: 2º).
**play <cancion>:** Reproduzco la canción que me pidas o la añado a la cola.
**skip:** Salto la canción que se está reproducción.
**nightcore:** Disfrute y goce, cuando te canses puedes volver a usar este comando.
**pausa | dale:** Pausar y reproducir la canción (Para quien quiera, en realidad es un toggle, puedes usar el mismo siempre)
**dc | vete:** Me desconecto.
**comandos | ayuda:** Te repito este mensaje, no sé para que querrías que te lo repitiese, así que no me toques los ovarios tampoco.''')
    


async def main() -> None:
    async with bot:
        await bot.start(config('BOT_TOKEN'))


asyncio.run(main())