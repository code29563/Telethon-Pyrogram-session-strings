#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.
# Inspired by Spechide

print("AN ONLINE STRING SESSION GENERATOR\n")
print("1. Pyrogram (USER)")
print("2. Telethon (USER)")
print("3. Pyrogram (BOT)")
print("4. Telethon (BOT)")


def main():
  user_input = input("\nEnter a number: ")
  if user_input == "1":
    print("\nYou selected Pyrogram.\nLogin as USER\n")
    APP_ID = int(input("Enter API ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    import pyrogram
    with pyrogram.Client(
      ":memory:",
      api_id=APP_ID,
      api_hash=API_HASH
    ) as app:
      session_str = app.export_session_string()
      send_message = app.send_message("me", "`{}`".format(session_str))
      send_message.reply_text("Here is your Session String for Pyrogram (USER)", quote=True)
      print("\nPlease check your Telegram Saved Messages for the StringSession.")

  elif user_input == "2":
    print("\nYou selected Telethon.\nLogin as USER\n")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    APP_ID = int(input("Enter API ID: "))
    API_HASH = input("\nEnter API HASH: ")
    with TelegramClient(
        StringSession(), 
        APP_ID, 
        API_HASH
      ) as client:
      session_str = client.session.save()
      send_message = client.send_message('me', '`{}`'.format(session_str))
      send_message.reply("Here is your Session String for Telethon (USER)")
      print("\nPlease check your Telegram Saved Messages for the StringSession.")

  elif user_input == "3":
    print("\nYou selected Pyrogram\nLogin as a Bot.\n")
    APP_ID = int(input("Enter API ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    BOT_TOKEN = input("\nEnter Bot token here:")
    USER = input("\nEnter your username or user id: ")
    try:
      USER = int(USER)
    except ValueError:
      USER = str(USER)
    import pyrogram
    with pyrogram.Client(
        ":memory:",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
      ) as app:
      session_str = app.export_session_string()
      send_message = app.send_message(USER, "`{}`".format(session_str))
      send_message.reply_text("Here is your String Session for Pyrogram (BOT)", quote=True)
      print("\nPlease check your chat with the bot for the StringSession.")

  elif user_input == "4":
    print("\nYou selected Telethon.\nLogin as BOT\n")
    # (c) https://t.me/TelethonChat/37677
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    APP_ID = int(input("Enter API ID: "))
    API_HASH = input("\nEnter API HASH: ")
    USER = input("\nEnter your username or user id: ")
    try:
      USER = int(USER)
    except ValueError:
      USER = str(USER)
    with TelegramClient(
        StringSession(), 
        APP_ID, 
        API_HASH
      ) as client:
      session_str = client.session.save()
      send_message = client.send_message(USER, '`{}`'.format(session_str))
      send_message.reply("Here is your Session String for Telethon (BOT)")
      print("\nPlease check your BOT Messages for the StringSession.")

  else:
    print("\nInvalid Input ! Select between 1, 2, 3 and 4")
    main()

main()