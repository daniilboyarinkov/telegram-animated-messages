from pyrogram import Client, filters
from dotenv import dotenv_values
from animations.heart import heart_emoji
from animations.blinking_heart import BlinkingHeart
from animations.pulse_heart import PulseHeart
import emoji
from time import sleep

config = dotenv_values(".env")
api_id, api_hash = config['api_id'], config['api_hash']
app = Client("spammer", api_id, api_hash)

TIME_SLEEP = 0.325

@app.on_message(filters.command("❤️❤️", prefixes="") & filters.me)
def heart_animation(_, message):
    end_message = "❤"
    for i in range(len(heart_emoji)):
        message.edit(emoji.emojize(emoji.demojize(heart_emoji[i].replace("💛", "❤"))))
        sleep(TIME_SLEEP)
    message.edit(end_message)

@app.on_message(filters.command("❤️❤️❤️", prefixes="") & filters.me)
def blink_heart_animation(client, message):
    end_message = "❤"
    heart = BlinkingHeart(21)
    blinks = heart.generate_tape()
    for blink in blinks:
        message.edit(emoji.emojize(emoji.demojize(blink)))
        sleep(TIME_SLEEP)
    message.edit(end_message)

@app.on_message(filters.command("❤️❤️❤️❤️", prefixes="") & filters.me)
def pulse_heart_animation(client, message):
    heart = PulseHeart()
    pulses = heart.START
    for i in range(21):
        pulses += heart.LOOP
    pulses += heart.END
    for pulse in pulses:
        message.edit(emoji.emojize(emoji.demojize(pulse)))
        sleep(TIME_SLEEP)

if __name__ == "__main__":
    print("Bot started...")
    app.run()

