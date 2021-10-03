from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("المطور", url="https://t.me/aymanegy")],
    ])
    welcomed = f"<b> مرحبا {message.from_user.first_name} \n \n في بوت التحميل من اليوتيوب 🎤 \n يمكنك من خلال البوت التحميل من \n اليوتيوب فيديو وصوت عن طريق ارسال الرابط \n [😍رسائل حب و رومانسيه😍](https://t.me/lloveMessages)</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
