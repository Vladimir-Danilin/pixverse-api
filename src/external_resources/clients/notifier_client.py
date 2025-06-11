from aiogram import Bot


class NotifierClient:
    def __init__(self, token: str, chat_id: str):
        self.chat_id = chat_id
        self.bot = Bot(token=token)

    async def endpoint_pixverse_error(
            self,
            error_code: dict,
            error_message: dict,
            endpoint: str,
            method: str,
    ):

        message = (f"Notify from pixverse\n"
                   f"Method: {method.upper()}\n"
                   f"Endpoint: {endpoint}\n"
                   f"Failed with {error_code} code\n"
                   f"Error Message: {error_message}\n")

        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message[:4096])
        except Exception as e:
            print(f"[NotifierClient] Failed to send message: {e}")

    async def server_pixverse_error(self, error: str, attempt: int = None):

        message = (f"Notify from pixverse\n"
                   f"Error: {error}\n"
                   f"attempt number: {attempt}\n")

        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message[:4096])
        except Exception as e:
            print(f"[NotifierClient] Failed to send message: {e}")

    async def invalid_value_error(self, method: str, route: str, error: str):

        message = (f"Notify from FastAPI\n"
                   f"Unprocessable Entity\n"
                   f"Method: {method}\n"
                   f"Endpoint: {route}\n"
                   f"Error: {error}")

        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message[:4096])
        except Exception as e:
            print(f"[NotifierClient] Failed to send message: {e}")

    async def close(self):
        await self.bot.session.close()
