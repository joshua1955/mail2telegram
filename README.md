# mail2telegram
Automaticaly send your mail to telegram via proxy.

# Installing

Download repo to your PC
git clone https://github.com/joshua1955/mail2telegram

# Recommend you create a virtual env to test

virtualenv venv && source venv/bin/activate

# Install requirements

pip3 install -r requirements.txt

# Configure a script

login = 'username@example.com'
password = 'secret'
mailbox = "INBOX"

# Specify your telegram bot and id

token = "yyyy:xxxxx"
chat_id = '123456789'

# Specify your ip socks5 proxy and user/password for proxy

apihelper.proxy = {'https': 'socks5://user:passowrd@server.com:port'}

