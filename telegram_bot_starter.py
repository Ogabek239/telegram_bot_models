from bot import TelegramBot
import time

# Main bot loop
def main():
    # Replace with your bot token from @BotFather
    BOT_TOKEN = "8016350842:AAEvU0fcRkhyo9qzKCBCZwIwIBWE3KUKeW4"
    bot = TelegramBot(BOT_TOKEN)
    
    print("Bot started. Send messages to test...")
    
    while True:
        updates = bot.get_updates()
        
        for update in updates:
            if update.message:
                print(f"Received: {update}")
                
                # Echo back a response for text messages
                if update.message.text:
                    bot.send_message(
                        update.message.chat.id, 
                        f"{update.message.text}"
                    )
                
                # TODO: Students will add handling for voice, photo, and dice messages here
                # For example:
                if update.message.voice:
                    print(f"Voice message received: {update.message.voice}")
                    bot.send_voice(
                        update.message.chat.id,
                        voice_file_id=update.message.voice.file_id
                    )
                if update.message.photo:
                    print(f"Photo message received: {update.message.photo}")
                    bot.send_photo(
                        update.message.chat.id,
                        photo_file_id=update.message.photo.file_id
                    )
                if update.message.dice:
                    print(f"Dice rolled: {update.message.dice.value} with emoji {update.message.dice.emoji}")
                    bot.send_dice(
                        update.message.chat.id,
                        emoji=update.message.dice.emoji
                    )

        time.sleep(1)

if __name__ == "__main__":
    main()