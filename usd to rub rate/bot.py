import requests

def get_exchange_rate():
    # Make a request to the API to get the current exchange rate
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()

    # Get the exchange rate for RUB
    exchange_rate = data["rates"]["RUB"]
    return exchange_rate

def send_message(exchange_rate):
    # Your bot's 
    token = "YOUR_BOT_TOKEN"
    # The chat ID of the chat you want to send the message to
    chat_id = "CHAT_ID"
    # The text of the message you want to send
    text = f"The current exchange rate of USD to RUB is {exchange_rate}"

    # Send the request to the Telegram API
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

if __name__ == "__main__":
    exchange_rate = get_exchange_rate()
    send_message(exchange_rate)
