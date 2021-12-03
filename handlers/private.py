from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker
    await message.reply_text(
        f"""Ben {bn} !!
Grubunuzun sesli ve görüntülü sohbetinde müzik çalmak için tasarlan bir botum, Bana Mp3 Formatında Şarkıları Veriniz. Komutlarım Aşağıdaki Gibidir:
🔥 /play - yanıtlanan ses dosyasını veya YouTube videosunu linki url aracılığıyla oynatılır. 
🔥 /Listen - YouTube üzerinden müzik bulut. 
🔥 /find - İstenilen parçayı kısa sürede bulmak için
🔥 /pause - Sesli Sohbeti durdurmak için
🔥 /resume - Sesli sohbeti devam ettirir. 
🔥 /skip - Geçerli Ses Atlanır. 
🔥 /stop - Sırayı temizler ve Sesli Sohbet Müziklerinin listesini kaldırır.
💡 /asistan - Userbot Grubunuza Katılır.
💡 /asistanby - Userbot Grubunuzdan Ayrılır. 
