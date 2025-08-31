from modules.utils import get_duration, get_filesize, format_time, tags_generator
from modules.thumbnail import get_screenshot, get_cover
from config import COMMENTS_GROUP_LINK, INDEX_CHANNEL_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from modules.progress import upload_progress
import os, time
from core.log import LOGGER

logger = LOGGER("Uploader")

async def upload_video(app, msg, file, id, tit, title, eid):
    t1 = time.time()
    dcount = 1

    try:
        duration = get_duration(file)
        size = get_filesize(file)
        # Thumbnail generation
        ss = get_screenshot(file)
        cc = await get_cover(id)
        # Basic caption & buttons
        tags = tags_generator(tit)
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Info", url=f"https://t.me/{INDEX_CHANNEL_USERNAME}"),
             InlineKeyboardButton(text="Comments", url=COMMENTS_GROUP_LINK)]
        ])
        caption = f"🎥 **{title}**\n\n{tags}"
        video = await app.send_video(
            app.UPLOADS_CHANNEL_ID,
            file,
            caption=caption,
            duration=duration,
            thumb=ss,
            reply_markup=buttons,
            file_name=os.path.basename(file),
            progress=upload_progress,
            progress_args=(title, msg, logger)
        )
        try: os.remove(file)
        except: pass
        try: os.remove(ss)
        except: pass
        try: os.remove(cc)
        except: pass
    except Exception as e:
        logger.warning(str(e))

    return video.id
