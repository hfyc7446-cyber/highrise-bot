from highrise import BaseBot, User

class MyBot(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("تم تشغيل البوت ودخوله للغرفة بنجاح!")
    async def on_user_join(self, user: User, position) -> None:
        await self.highrise.chat(f"أهلاً وسهلاً بك في الغرفة يا {user.username}! نورتنا ✨")
