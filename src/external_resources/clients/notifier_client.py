from aiogram import Bot


class NotifierClient:
    def __init__(self, token: str, chat_id: str):
        self.chat_id = chat_id
        self.bot = Bot(token=token)

    async def notify(self, message: str):
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message[:4096])  # Telegram ограничение
        except Exception as e:
            print(f"[NotifierClient] Failed to send message: {e}")

    async def close(self):
        await self.bot.session.close()
