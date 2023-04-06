import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from MukeshRobot import telethn as bot
from MukeshRobot import telethn as tgbot
from MukeshRobot.events import register

edit_time = 5
""" =======================𝗦𝗛𝗜𝗩 𝗥𝗢𝗕𝗢𝗧====================== """
file1 = "https://telegra.ph/file/1a2db3329d7a3b35d5ef1.jpg"
file2 = "https://telegra.ph/file/c4c74ca853dbe426b5075.jpg"
file3 = "https://telegra.ph/file/1ba7c540462dc0c6d13cd.jpg"
file4 = "https://telegra.ph/file/ff8228a476d1fc73ab8fe.jpg"
file5 = "https://telegra.ph/file/9584b19633bf5b31faa12.jpg"
""" =======================𝗦𝗛𝗜𝗩 𝗥𝗢𝗕𝗢𝗧====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ 𝗩𝗜𝗣 𝗕𝗢𝗬\n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ: {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ: {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
        LILIE += f"ᴜsᴇʀ ɪᴅ: {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
__mod_name__ = "📍ɪɴғᴏ📍"
__help__ = """
 /myinfo  ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ 

☆............𝙱𝚈 » [𝚂𝙷𝙸𝚅 𝙾𝙿](https://t.me/THA_SHIV_OP)............☆"""
