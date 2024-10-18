🏗 Qazyna Telegram Bot
Qazyna Telegram Bot is a chatbot developed for the "Qazyna" construction store, providing users with an easy way to interact with the store via Telegram. The bot offers functions like viewing the product catalog, getting information about current promotions and discounts, locating the store on a map, and requesting expert consultations.

🔧 Features
🛒 View Product Catalog: Provides a link to the store's product catalog.
📦 Check Current Promotions and Discounts: Allows users to receive information about special offers.
📍 Find Our Store on the Map: Offers links to maps (2GIS, Yandex Navigator) for easy store location.
🛠 Request Expert Consultation: Allows users to submit a consultation request. The user enters their name and phone number, and the store's staff will contact them.
📋 Requests: Admins can view all consultation requests submitted by users (available only to specific administrators).
🚀 How It Works
Upon starting the bot, the user is greeted and presented with several options for interaction.
Users can choose from the following options:
View the product catalog.
Check current promotions and discounts.
Find the store on a map.
Request expert consultation.
In the consultation request flow, the bot stores the user's name and phone number in an SQLite database and confirms that the store's staff will get in touch.
An administrator with a specific username can view all submitted consultation requests, sorted by date.

🛠 Technologies
Python — the main programming language.
SQLite — database to store user information and consultation requests.
Telegram Bot API — facilitates interaction with users via Telegram.
Telebot — a Python library for creating Telegram bots.

🗃 Database Structure
Table users:
id — unique user identifier.
first_name — user's first name.
phone_number — user's phone number.
registration_date — date and time of the request submission.

📦 Installation
Clone the repository:
git clone https://github.com/username/qazyna-telegram-bot.git

Install dependencies:
pip install pyTelegramBotAPI

Set up the API token for your bot:
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

Run the bot:
python bot.py

💬 How to Use
Open Telegram and start a conversation with the bot using the /start command.
Choose one of the available options to interact with the store.
For administrators: use the "📋 Requests" button to view all submitted requests.
