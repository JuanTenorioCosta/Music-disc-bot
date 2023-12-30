import FakeDBs.ids as usersIds

from discord.ext import commands
from classes.BuilderInterface import BuilderInterface

class TextCommand():
  def __init__(self, builder_interface: BuilderInterface) -> None:
    self.builder = builder_interface
  
  async def answer( self, ctx: commands.Context ):
    try:
      # Guardar ids de personas que realizan solicitudes al bot
      if ctx.author.name not in usersIds.ids:
        usersIds.ids[ctx.author.name] = ctx.author.id
        usersIds.write_ids(usersIds.ids)
      await self.work(ctx)
    except Exception as e:
      print(f'Excepción: {e}')
      await self.send_answer(ctx, 'Te escuché, pero no estaba atenta. Me repites lo que dijiste porfa.')

  async def work( self, ctx: commands.Context ) -> None:
    respuestas: [str] = self.builder.build_answer(ctx)
    for respuesta in respuestas:
      await self.send_answer(ctx, respuesta)
  
  async def send_answer( self, ctx: commands.Context, plain_text: str ) -> None:
    await ctx.send(plain_text)