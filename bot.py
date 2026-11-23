import random
from highrise import BaseBot, User

# قائمة ضخمة تضم أكثر من 50 رقصة وحركة متنوعة (رقم : معرّف الرقصة)
DANCES = {
    "1": "emote-dance-casual",
    "2": "emote-dance-tiktok2",
    "3": "emote-dance-tiktok8",
    "4": "emote-dance-tiktok9",
    "5": "emote-dance-tiktok10",
    "6": "emote-dance-tiktok11",
    "7": "emote-dance-weird",
    "8": "emote-dance-macarena",
    "9": "dance-floss",
    "10": "dance-russian",
    "11": "dance-blackpink",
    "12": "dance-pennywise",
    "13": "dance-orangejustice",
    "14": "dance-shoppingcart",
    "15": "dance-tiktok14",
    "16": "dance-breakdance",
    "17": "dance-pinguin",
    "18": "dance-aerobics",
    "19": "dance-martial-artist",
    "20": "dance-handsup",
    "21": "dance-kawai",
    "22": "dance-creepypuppet",
    "23": "dance-wrong",
    "24": "dance-zombie",
    "25": "dance-duckwalk",
    "26": "dance-voguehands",
    "27": "dance-jinglebell",
    "28": "dance-hipshake",
    "29": "dance-spiritual",
    "30": "dance-smoothwalk",
    "31": "dance-cheerleader",
    "32": "dance-twerk",
    "33": "emote-snake",
    "34": "emote-frog",
    "35": "emote-robot",
    "36": "emote-disco",
    "37": "emote-salsa",
    "38": "emote-gangnam",
    "39": "emote-moonwalk",
    "40": "emote-dab",
    "41": "emote-headbang",
    "42": "emote-model",
    "43": "emote-pose1",
    "44": "emote-pose3",
    "45": "emote-pose5",
    "46": "emote-pose7",
    "47": "emote-pose8",
    "48": "emote-superpose",
    "49": "emote-cute",
    "50": "emote-shy",
    "51": "emote-float",
    "52": "emote-teleporting",
    "53": "emote-maniac",
    "54": "emote-energyball",
    "55": "emote-astronaut",
}

# أسماء عربية مختصرة لبعض الرقصات المشهورة
NAMED_DANCES = {
    "تيك توك": "emote-dance-tiktok8",
    "ماكارينا": "emote-dance-macarena",
    "روسي": "dance-russian",
    "بلاك بينك": "dance-blackpink",
    "بريك دانس": "dance-breakdance",
    "بطريق": "dance-pinguin",
    "زومبي": "dance-zombie",
    "روبوت": "emote-robot",
    "ديسكو": "emote-disco",
    "سالسا": "emote-salsa",
    "مون ووك": "emote-moonwalk",
    "مودل": "emote-model",
    "كيوت": "emote-cute",
    "طيران": "emote-float",
    "فضاء": "emote-astronaut",
}

# رسائل ترحيب متنوعة
WELCOMES = [
    "أهلاً وسهلاً بك في الغرفة يا @{user}! نورتنا ✨",
    "يا هلا ومسهلا بـ @{user}، حياك الله في غرفتنا 🌹",
    "نورت الغرفة بوجودك يا @{user} ✨ اكتب رقم من 1 إلى 55 للرقص 💃",
    "حيّ الله @{user}! نتمنى لك وقتاً ممتعاً معنا 🎉",
]


class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("تم تشغيل البوت ودخوله للغرفة بنجاح!")
        await self.highrise.chat("تم تفعيل البوت مع 55 رقصة! اكتب (رقصات) أو رقم من 1 إلى 55 💃🕺")

    async def on_user_join(self, user: User, position) -> None:
        msg = random.choice(WELCOMES).format(user=user.username)
        await self.highrise.chat(msg)
        try:
            await self.highrise.send_emote("emote-wave")
        except Exception:
            pass

    async def on_chat(self, user: User, message: str) -> None:
        text = message.strip().lower()

        # عرض المساعدة
        if text in ["رقصات", "الرقصات", "اوامر", "أوامر", "help"]:
            await self.highrise.chat(
                "💃 اكتب أي رقم من (1) إلى (55) ليرقص البوت معك!\n"
                "أو اكتب: (عشوائي) - أو أسماء مثل: روسي، ديسكو، سالسا، مون ووك، بطريق، زومبي ✨"
            )
            return

        # رقصة عشوائية
        if text in ["عشوائي", "random", "رقص"]:
            emote_id = random.choice(list(DANCES.values()))
            await self.play_dance(user.id, emote_id)
            return

        # تشغيل بالرقم
        if text in DANCES:
            await self.play_dance(user.id, DANCES[text])
            return

        # تشغيل بالاسم العربي
        if text in NAMED_DANCES:
            await self.play_dance(user.id, NAMED_DANCES[text])

    async def play_dance(self, user_id: str, emote_id: str) -> None:
        try:
            await self.highrise.send_emote(emote_id)
            await self.highrise.send_emote(emote_id, user_id)
        except Exception:
            pass
