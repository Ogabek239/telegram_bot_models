class User:
    def __init__(self, user_data):
        self.id = user_data.get("id")
        self.is_bot = user_data.get("is_bot", False)
        self.first_name = user_data.get("first_name")
        self.last_name = user_data.get("last_name")
        self.username = user_data.get("username")
        self.language_code = user_data.get("language_code")

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, name={self.first_name} {self.last_name})"


class Chat:
    def __init__(self, chat_data):
        self.id = chat_data.get("id")
        self.type = chat_data.get("type")
        self.title = chat_data.get("title")
        self.username = chat_data.get("username")
        self.first_name = chat_data.get("first_name")
        self.last_name = chat_data.get("last_name")

    def __str__(self):
        return f"Chat(id={self.id}, type={self.type}, title={self.title})"

class Voice:
    def __init__(self, voice_json):
        self.file_id = voice_json.get('file_id')
        self.file_unique_id = voice_json.get('file_unique_id')
        self.width = voice_json.get('width')
        self.height = voice_json.get('height')

class Photo:
    def __init__(self, photo_list):
        best_photo = photo_list[-1]
        self.file_id = best_photo.get('file_id')
        self.file_unique_id = best_photo.get('file_unique_id')
        self.width = best_photo.get('width')
        self.height = best_photo.get('height')

class Dice:
    def __init__(self, dice_json):
        self.emoji = dice_json.get("emoji")
        self.value = dice_json.get("value")


class Message:
    def __init__(self, message_data):
        self.message_id = message_data.get("message_id")
        self.date = message_data.get("date")
        self.text = message_data.get("text")

        # Parse user and chat objects
        if message_data.get("from"):
            self.from_user = User(message_data["from"])
        else:
            self.from_user = None

        if message_data.get("chat"):
            self.chat = Chat(message_data["chat"])
        else:
            self.chat = None
        if message_data.get('voice'):
            self.voice = Voice(message_data['voice'])
        else:
            self.voice = None
        if message_data.get("photo"):
            self.photo = Photo(message_data["photo"])
        else:
            self.photo = None
        if message_data.get('dice'):
            self.dice = Dice(message_data["dice"])
        else:
            self.dice = None

    def __str__(self):
        return (
            f"Message(id={self.message_id}, text='{self.text}', from={self.from_user})"
        )


class Update:
    def __init__(self, update_data):
        self.update_id = update_data.get("update_id")

        if update_data.get("message"):
            self.message = Message(update_data["message"])
        else:
            self.message = None

    def __str__(self):
        return f"Update(id={self.update_id}, message={self.message})"
