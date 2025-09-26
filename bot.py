from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"7728230165")
ch = "xvwwvl" 
OWNER_USERNAME = "wwvvwt"
ST = "wwvvwt"
LT = "wwvvwt"
DEVS = []
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "ᴊᴀᴋ"

bot_token="8157343970:AAGw5gWunfa5byigpWQYazmt9QL6n5wEeo0"
bot_token2="BAB86r0AlG2Q4Zzgfl-5uPLfrO_BksKXvvIkFiSJXrr0WDel6J5y3bTsF2qNuCOBxIldEd6QwjpMSMKMv64UInijWCqjKCCfiY7LWCxnfVsoMaJdpQGRYLVR0YScZBBdzkwwtmHRfeS6yh6n9zjY3_ypF-SKX4QplEeCdnPNSR3wIPvKqw9z93x9GOmZGk5jzXrlbTdGykn08tgriH_yKTUcjONdCPOFDz5WM0DKH_5zneQUUKJH3HTgb6owfZ1Azq4y0vsRcQjWzGmiuCR6xDB9D5CkB064H-MfCeGbKj39icuFYlLUrW5gk1fgEVECsQnm0qWpM9oGVEg0MHQRzSccFiJjvQAAAAH4zF3KAQ"


bot = Client("ITA", api_id=8186557, api_hash="efd77b34c69c164ce158037ff5a0d117", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=21361986, api_hash="036c3be60b3d3bc75d83bd5b9252e5ac", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()
