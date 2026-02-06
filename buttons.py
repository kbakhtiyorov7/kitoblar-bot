from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Aloqa")
        ],
        [
            KeyboardButton(text="✅ FOYDALI KANALLAR VA ULARDA REKLAMA")
        ],
        [
            KeyboardButton(text="🇬🇧 English")
        ],
        [
            KeyboardButton(text="📚 O'zbek adabiyoti"),
            KeyboardButton(text="📚 Jahon adabiyoti")
        ],
        [
            KeyboardButton(text="📚 Jahon adabiyoti"),
            KeyboardButton(text="📚 Mumtoz adabiyot")
        ],
        [
            KeyboardButton(text="🎧 Audio kitoblar"),
            KeyboardButton(text="💯 Top 100 kitoblar")
        ],
        [
            KeyboardButton(text="📚 Maktab darsliklari"),
            KeyboardButton(text="📚 Islomiy kitoblar")
        ],
        [
            KeyboardButton(text="🔍 Lug'atlar")
        ],
        [
           KeyboardButton(text="📝 She'riyat"),
           KeyboardButton(text="📜 Alisher Navoiy asarlari") 
        ],
        [
            KeyboardButton(text="📜O'zbekiston Milliy Ensiklopediyasi"),
            KeyboardButton(text="📋 O'zbek tilining izohli lug'atlari")
        ],
        [
            KeyboardButton(text="🔍 O'zbek tilining imlo lug'ati")
        ],
        [
            KeyboardButton(text="Islom Karimov asarlari"),
            KeyboardButton(text="Shavkat Mirziyoyev asarlari")
        ],
        [
            KeyboardButton(text="📥 Kitob o'qish uchun dasturlar")
        ],
        [
            KeyboardButton(text="🤖 Botni guruhga qo'shish"),
            KeyboardButton(text="↗️ Botni do'stlarga ulashish")
        ],
        [
            KeyboardButton(text="♻️ Takliflar"),
            KeyboardButton(text="⭐️ Botni baholash")
        ]
    ],
    resize_keyboard=True
)
