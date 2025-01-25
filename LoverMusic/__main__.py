import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from LoverMusic import LOGGER, app, userbot
from LoverMusic.core.call import Lover
from LoverMusic.misc import sudo
from LoverMusic.plugins import ALL_MODULES
from LoverMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LoverMusic.plugins" + all_module)
    LOGGER("LoverMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Lover.start()
    try:
        await Lover.stream_call("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except NoActiveGroupCall:
        LOGGER("LoverMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Lover.decorators()
    LOGGER("LoverMusic").info(
        "\x41\x76\x69\x61\x78\x20\x4d\x75\x73\x69\x63\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x0a\x0a\x44\x6f\x6e\x27\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x41\x76\x69\x61\x78\x4f\x66\x66\x69\x63\x69\x61\x6c"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("LoverMusic").info("Stopping Lover Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
