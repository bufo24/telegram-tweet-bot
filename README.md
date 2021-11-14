This Telegram bot is a simple gateway to Twitter. Using command `/tweet'
generates a twitter message.


## Installation and configuration

You will need Python version 3.9 or above.

1. Clone the repository.
2. Install the Python modules:
```
pip install -r requirements.txt
```
3. Make a copy of the example config:
```
cp config.example.py config.py
```
4. Contact @userinfobot on Telegram (https://t.me/userinfobot) to get your user
   ID.
5. Paste your user ID into config.py (`admin_id`).
6. Obtain a Telegram API key for your bot:
    - Contact Botfather on Telegram (https://t.me/Botfather)
    - `/newbot`
    - Follow instructions and take note of the API key and the bots name.
6. Paste the API key in config.py (`token`).
7. Create a Twitter developer account (https://developer.twitter.com/en/apply-for-access).
In the Twitter developer dashboard:
    - Create an app in the dashboard with read and write (!) permissions.
    - Generate API key and an Access token.
    - Enter those in config.py (`consumer_key` corresponds to the Twitter API key).

## Running the bot
```
python3 bot.py`
```

## Testing the bot
Contact your bot (using the name chosen in Botfather) in Telegram and use commands `/add`, `/admins` and `/tweet`.
Check contents of users.csv and output on Twitter.
