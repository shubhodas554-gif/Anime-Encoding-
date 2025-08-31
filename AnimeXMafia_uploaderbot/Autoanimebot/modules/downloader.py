import os
import aiohttp
import aiofiles
import time
from AutoAnimeBot.core.log import LOGGER
from AutoAnimeBot.modules.progress import progress_text
from pyrogram.types import Message

logger = LOGGER("Downloader")

async def downloader(message: Message, link, title, file_name):
    logger.info(f"Downloading {title}")
    if not os.path.exists("downloads"):
        os.mkdir("downloads")

    file_name = f"downloads/{file_name}"
    t1 = time.time()
    dcount = 1

    try:
        timeout = aiohttp.ClientTimeout(total=7200)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(link) as response:
                total = response.content_length / 1024 if response.content_length else 1
                done = 1
                async with aiofiles.open(file_name, "wb") as f:
                    async for chunk in response.content.iter_chunked(1024):
                        await f.write(chunk)
                        done += 1
                        t2 = time.time()
                        if t2 - t1 > 10:
                            t1 = t2
                            text = progress_text("Downloading", title, done, total, dcount)
                            await message.edit_caption(text)
                            dcount = done
    except Exception as e:
        logger.warning(str(e))
    logger.info(f"Downloaded {title}")
    return file_name
