import asyncio
from decouple import config

from Bot import Bot

bot: Bot = Bot()

async def main() -> None:
    async with bot:
        await bot.start(config('BOT_TOKEN'))

asyncio.run(main())