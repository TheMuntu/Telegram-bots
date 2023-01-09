# Telegram-bots
This is a repo with various Telegram bots that I created.

To create a Telegram bot, follow these steps:

1. Install the Telegram app and sign in.
2. Search for the `BotFather` bot in the app and start a chat with it.
3. Use the `/newbot` command to create a new bot. The BotFather will ask you for a name and a username for your bot. Choose a name and a username that ends in `bot` (e.g., "Exchange Rate Alert Bot").
4. The BotFather will give you a token that you can use to access the HTTP API. Save this token, as you will need it later to communicate with your bot.
5. Use the `/setprivacy` command to disable privacy mode for your bot. This will allow your bot to receive messages from users.
6. Start a chat with your bot and send it a message.
7. Use the `/myid` command in the "BotFather" chat to get your chat ID. Save this chat ID, as you will need it later to send messages to your chat.

Now you can use the `bot_id` and `chat_id` variables in the Python script to send messages to your Telegram bot. Don't forget to replace `bot_id` and `chat_id` with the actual values for your bot and chat.
