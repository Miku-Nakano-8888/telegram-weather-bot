import telebot
from telebot import types
import requests as r
from langdetect import detect

request_headers = {
    "Accept-Language": "be"
}

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
    'p': ''
}

standart_weather_parameters = {
    '0': '',
    'T': '',
    'M': ''
}
properties = {"F": "", "p": ""}

l_i_s_t = ["አማርኛ", "عرب", "Afrikaans", "Беларускі", "বাংলা", "català", "dansk", "Deutsch", "Ελληνικά",
           "eesti keel",
           "Français", "Farsi", "galego", "हिंदी", "Magyar", "Interlingua", "bahasa Indonesia", "Italiano",
           "lietuvių",
           "Malagasy", "norsk", "Nederlands", "Occitan", "Português", "Română", "Tamil", "Türk",
           "Tswana",
           "Український", "Tiếng Việt", "English"]

langs_main = {
    "አማርኛ": "የአየር ሁኔታን ለማወቅ የሚፈልጉትን ቦታ ይምረጡ",
    "عرب": "اختر مكانًا تريد معرفة الطقس فيه",
    "Afrikaans": "Kies 'n plek waar jy die weer wil weet",
    "Беларускі": "Выберы месца, у якім хочаш даведацца пра надвор'е",
    "বাংলা": "আপনি আবহাওয়া জানতে চান যেখানে জায়গা চয়ন করুন",
    "català": "Tria un lloc on vulguis conèixer el temps",
    "dansk": "Vælg et sted, hvor du vil vide vejret",
    "Deutsch": "Wählen Sie einen Ort, an dem Sie das Wetter wissen möchten",
    "Ελληνικά": "Επιλέξτε ένα μέρος όπου θέλετε να μάθετε τον καιρό",
    "eesti keel": "Valige koht, kus soovite ilma teada saada",
    "Français": "Choisissez un endroit où vous voulez connaître la météo",
    "Farsi": "مکانی را انتخاب کنید که می خواهید از آب و هوا مطلع شوید",
    "galego": "Escolle un lugar onde queres coñecer o tempo",
    "हिंदी": "ऐसी जगह चुनें जहां आप मौसम जानना चाहते हैं",
    "Magyar": "Válasszon egy helyet, ahol tudni szeretné az időjárást",
    "Interlingua": "Choose a place where you want to know the weather",
    "bahasa Indonesia": "Pilih tempat di mana Anda ingin mengetahui cuaca",
    "Italiano": "Scegli un luogo in cui vuoi conoscere il tempo",
    "lietuvių": "Pasirinkite vietą, kurioje norite sužinoti orą",
    "Malagasy": "Misafidiana toerana tianao ho fantatra ny toetrandro",
    "norsk": "Velg et sted der du vil vite været",
    "Nederlands": "Kies een plek waarvan je het weer wilt weten",
    "Occitan": "Choose a place where you want to know the weather",
    "Português": "Escolha um lugar onde você quer saber o tempo",
    "Română": "Alegeți un loc unde doriți să aflați vremea",
    "Tamil": "நீங்கள் வானிலை அறிய விரும்பும் இடத்தைத் தேர்ந்தெடுக்கவும்",
    "Türk": "Hava durumunu öğrenmek istediğiniz bir yer seçin",
    "Tswana": "Choose a place where you want to know the weather",
    "Український": "Вибери місце, де хочеш дізнатися погоду",
    "Tiếng Việt": "Chọn một nơi mà bạn muốn biết thời tiết",
    "English": "Choose a place where you want to know the weather"
}
langs = {
    "አማርኛ": "am",
    "عرب": "ar",
    "Afrikaans": "af",
    "Беларускі": "be",
    "বাংলা": "bn",
    "català": "ca",
    "dansk": "da",
    "Deutsch": "de",
    "Ελληνικά": "el",
    "eesti keel": "et",
    "Français": "fr",
    "Farsi": "fa",
    "galego": "gl",
    "हिंदी": "hi",
    "Magyar": "hu",
    "Interlingua": "ia",
    "bahasa Indonesia": "id",
    "Italiano": "it",
    "lietuvių": "lt",
    "Malagasy": "mg",
    "norsk": "nb",
    "Nederlands": "nl",
    "Occitan": "oc",
    "Português": "pl",
    "Română": "ro",
    "Tamil": "ta",
    "Türk": "tr",
    "Tswana": "th",
    "Український": "uk",
    "Tiếng Việt": "vi",
    "English": "en"
}

url = 'https://wttr.in/'

keyboard_hider = types.ReplyKeyboardRemove()
bot = telebot.TeleBot('5616011803:AAHm55FkyzqOzZhV8AtS-66G1lKy0gwV1tg')


@bot.message_handler(commands=['start'])
def start(message):
    global properties
    global weather_parameters
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row("Let's go!", "Info")
    markup.row("Settings")
    message = bot.send_message(message.chat.id,
                               "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                               "coordinats!\nwhatever you want...\nFor morе"
                               "information click *Info*\nTo start click *Let's Go!* ", reply_markup=markup,
                               parse_mode="Markdown")
    bot.register_next_step_handler(message, language)


def language(message):
    if message.text == "Let's go!":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)
        bot.register_next_step_handler(send, check)
    elif message.text == "Info":
        bot.send_message(message.chat.id,
                         "What do you want to know:?\n/1. What can i do with this bot?\n/2. What are location types "
                         "support?\n/3. What languages are support?\n/4. What are view options support")
    elif message.text == "Settings":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Commands', 'View options')
        send = bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
        bot.register_next_step_handler(send, check_2)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start", "Return")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)


@bot.message_handler(commands=["1"])
def one(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row('Return', 'Start')
    message = bot.send_message(message.chat.id,
                               "*You can find weather of any location*\n    supporting location types like:\n        "
                               "_city_\n        _any location_\n        _unicode name of any location in any "
                               "language_\n        _ICAO airport code (3 letters)_\n        _zip code (US only)_\n    "
                               "    _GPS coordinates_\n*You can know the moon phase:*\n    _Moon Phase_\n    _Moon "
                               "phase for the date (moon@2016-10-25)_",
                               reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(message, info_step_2)


@bot.message_handler(commands=["2"])
def two(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row('Return', 'Start')
    message = bot.send_message(message.chat.id,
                               "*Supported location types:*\n    _city_\n    _any location_\n    _unicode name of any "
                               "location in any language(except Russian)vz_\n    _ICAO airport code (3 letters)_\n    "
                               "_zip code (US"
                               "only)_\n    _GPS coordinates_",
                               reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(message, info_step_2)


@bot.message_handler(commands=["3"])
def three(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row('Return', 'Start')
    message = bot.send_message(message.chat.id,
                               "*Supported languages:*\n    _አማርኛ_\n    _عرب_\n    _Afrikaans_\n    _Беларускі_\n    "
                               "_বাংলা_\n    _català_\n    _dansk_\n    _Deutsch_\n    _Ελληνικά_\n    _eesti keel_\n "
                               "   _Français_\n    _Farsi_\n    _galego_"
                               "\n    हिंदी\n    Magyar\n    Interlingua\n    bahasa Indonesia\n    Italian\n    "
                               "lietuvių\n    Malagasy\n    norsk\n    Nederlands\n    Occitan\n    Português\n    "
                               "Română"
                               "\n    Tamil\n    Türk\n    Tswana\n    Український\n    Tiếng Việt\n    English",
                               reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(message, info_step_2)


@bot.message_handler(commands=["4"])
def four(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row('Return', 'Start')
    markup.add('Experiment')
    message = bot.send_message(message.chat.id,
                               "*Supported view options:*\n    *0* : _only current weather_\n    *1* : _current "
                               "weather + today's forecast_\n"
                               "*2* : _current weather + today's + tomorrow's forecast_\n    *n* : _narrow version ("
                               "only day and night)_\n"
                               "*q* : _quiet version (no 'Weather report' text)_\n    *Q* : _superquiet version (no "
                               "'Weather report', no city name)_\n"
                               "    *T* : _switch terminal sequences off (no colors)_", reply_markup=markup,
                               parse_mode="Markdown")
    bot.register_next_step_handler(message, info_step_2)


@bot.message_handler(commands=["reset"])
def reset(message):
    global weather_parameters
    weather_parameters = standart_weather_parameters
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.row("Start", "Return")
    message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
    bot.register_next_step_handler(message, info_step_3)


def info_step_2(message):
    if message.text == "Return":
        bot.send_message(message.chat.id,
                         "What do you want to know:?\n/1. What can i do with this bot?\n/2. What are location types "
                         "support?\n/3. What languages are support?\n/4. What are display options there")
    elif message.text == "Start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)
        bot.register_next_step_handler(send, check)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "Experiment":
        global properties
        properties = {"F": "", "p": ""}
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("0", "1", "2", "n", "q", "Q", "T")
        markup.add("Stop")
        abilities = bot.send_message(message.chat.id, "Choose what you want to add\n", reply_markup=markup)
        bot.register_next_step_handler(abilities, check_4)
    elif message.text == "/1":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Return', 'Start')
        message = bot.send_message(message.chat.id,
                                   "*You can find weather of any location*\n    supporting location types like:\n"
                                   "_city_\n        _any location_\n        _unicode name of any location in any "
                                   "language_\n        _ICAO airport code (3 letters)_\n        _zip code (US only)_\n"
                                   "    _GPS coordinates_\n*You can know the moon phase:*\n    _Moon Phase_\n    _Moon "
                                   "phase for the date (moon@2016-10-25)_",
                                   reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_2)
    elif message.text == "/2":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Return', 'Start')
        message = bot.send_message(message.chat.id,
                                   "*Supported location types:*\n    _city_\n    _any location_\n    _unicode name of "
                                   "any"
                                   "location in any language(except Russian)vz_\n    _ICAO airport code (3 letters)_\n"
                                   "_zip code (US"
                                   "only)_\n    _GPS coordinates_",
                                   reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_2)
    elif message.text == "/3":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Return', 'Start')
        message = bot.send_message(message.chat.id,
                                   "*Supported languages:*\n    _አማርኛ_\n    _عرب_\n    _Afrikaans_\n    _Беларускі_\n"
                                   "_বাংলা_\n    _català_\n    _dansk_\n    _Deutsch_\n    _Ελληνικά_\n    _eesti "
                                   "keel_\n"
                                   "   _Français_\n    _Farsi_\n    _galego_"
                                   "\n    हिंदी\n    Magyar\n    Interlingua\n    bahasa Indonesia\n    Italian\n    "
                                   "lietuvių\n    Malagasy\n    norsk\n    Nederlands\n    Occitan\n    Português\n    "
                                   "Română"
                                   "\n    Tamil\n    Türk\n    Tswana\n    Український\n    Tiếng Việt\n    English",
                                   reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_2)
    elif message.text == "/4":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Return', 'Start')
        markup.add('Experiment')
        message = bot.send_message(message.chat.id,
                                   "*Supported view options:*\n    *0* : _only current weather_\n    *1* : _current "
                                   "weather + today's forecast_\n"
                                   "*2* : _current weather + today's + tomorrow's forecast_\n    *n* : _narrow "
                                   "version ("
                                   "only day and night)_\n"
                                   "*q* : _quiet version (no 'Weather report' text)_\n    *Q* : _superquiet version (no"
                                   "'Weather report', no city name)_\n"
                                   "    *T* : _switch terminal sequences off (no colors)_", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_2)
    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)


def info_step_3(message):
    if message.text == "Return":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add('View options')
        send = bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
        bot.register_next_step_handler(send, check_2)

    elif message.text == "Start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)
        bot.register_next_step_handler(send, check)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)

    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)


def check(message):
    if message.text == "Other":
        bot.send_message(message.chat.id, "Available languages:")
        message = bot.send_message(message.chat.id, "አማርኛ\nعرب\nAfrikaans\nБеларускі\nবাংলা\ncatalà\ndansk\n"
                                                    "Deutsch\nΕλληνικά\neesti keel\nFrançais\nFarsi\ngalego\nहिंदी\n"
                                                    "Magyar\nInterlingua\nbahasa "
                                                    "Indonesia\nItaliano\nlietuvių\nMalagasy\n"
                                                    "norsk\nNederlands\nOccitan\nPortuguês\nRomână\nTamil\nT"
                                                    "ürk\n"
                                                    "Tswana\nУкраїнський\nTiếng Việt\nEnglish",
                                   reply_markup=keyboard_hider)
        bot.register_next_step_handler(message, answer)
    elif message.text in l_i_s_t:
        active_lang_main = langs_main[message.text]
        active_lang = langs[message.text]
        al = {"Accept-Language": active_lang}
        request_headers.update(al)
        bot.send_message(message.chat.id, active_lang_main, reply_markup=keyboard_hider)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "I cannot understand you, sorry", reply_markup=markup)
        bot.register_next_step_handler(send, check)


def check_2(message):
    if message.text == "View options":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Set your view options", "RESET OPTIONS")
        markup.add("Return")
        message = bot.send_message(message.chat.id, "Choose:", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, check_3)
    elif message.text == "Commands":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Return", "Start")
        message = bot.send_message(message.chat.id, "*Commands:*\n    _/start_\n    _/reset_", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, check_3)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)


def check_3(message):
    if message.text == "Set your view options":
        global properties
        properties = {"F": "", "p": ""}
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("0", "1", "2", "n", "q", "Q", "T")
        markup.add("Stop")
        abilities = bot.send_message(message.chat.id, "Choose your view properties\n", reply_markup=markup)
        bot.register_next_step_handler(abilities, check_4)

    elif message.text == "Return":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('Commands', 'View options')
        send = bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
        bot.register_next_step_handler(send, check_2)
    elif message.text == "Start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "Choose language:", reply_markup=markup)
        bot.register_next_step_handler(send, check)
    elif message.text == "RESET OPTIONS":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start", "Return")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)
    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "/reset":
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)


def check_4(message):
    if message.text in ["0", "1", "2", "n", "q", "Q", "T"]:
        global properties
        properties[message.text] = ""
        if message.text != "Stop":
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.row("0", "1", "2", "n", "q", "Q", "T")
            markup.add("Stop")
            abilities = bot.send_message(message.chat.id, "Choose what you want to add\n", reply_markup=markup)
            bot.register_next_step_handler(abilities, check_4)
    else:
        if message.text == "/start":
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.row("Let's go!", "Info")
            markup.add("Settings")
            message = bot.send_message(message.chat.id,
                                       "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                       "coordinats!\nwhatever you want...\nFor morе"
                                       "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                       parse_mode="Markdown")
            bot.register_next_step_handler(message, language)
        elif message.text == "/reset":
            global weather_parameters
            weather_parameters = standart_weather_parameters
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.row("Start")
            message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup,
                                       parse_mode="Markdown")
            bot.register_next_step_handler(message, info_step_3)
        elif message.text == "Stop":
            weather_parameters = properties
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.row("Start", "Return")
            message = bot.send_message(message.chat.id, "Choose:", reply_markup=markup)
            bot.register_next_step_handler(message, info_step_3)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.row("0", "1", "2", "n", "q", "Q", "T")
            markup.add("Stop")
            abilities = bot.send_message(message.chat.id, "I can't get you, sorry\n", reply_markup=markup)
            bot.register_next_step_handler(abilities, check_4)


def answer(message):
    if message.text in l_i_s_t:
        active_lang_main = langs_main[message.text]
        active_lang = langs[message.text]
        al = {"Accept-Language": active_lang}
        request_headers.update(al)
        bot.send_message(message.chat.id, active_lang_main, reply_markup=keyboard_hider)

    elif message.text == "/start":
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Let's go!", "Info")
        markup.add("Settings")
        message = bot.send_message(message.chat.id,
                                   "*I'm Weather_Bot*\nYou can get the weather and not only just type your city or "
                                   "coordinats!\nwhatever you want...\nFor morе"
                                   "information click *info*\nTo start click *Let's Go* ", reply_markup=markup,
                                   parse_mode="Markdown")
        bot.register_next_step_handler(message, language)
    elif message.text == "/reset":
        global weather_parameters
        weather_parameters = standart_weather_parameters
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row("Start")
        message = bot.send_message(message.chat.id, "*VIEW OPTIONS RESET*", reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, info_step_3)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.row('English', 'Беларускі')
        markup.add("Other")
        send = bot.send_message(message.chat.id, "I cannot understand you, sorry", reply_markup=markup)
        bot.register_next_step_handler(send, check)


@bot.message_handler(content_types=["text"])
def weather(message):
    det = detect(message.text)
    if det == "ru":
        bot.send_message(message.chat.id, "Sorry, system ain't support this language")
    elif det == "bg":
        bot.send_message(message.chat.id, "Sorry, system ain't support this language")
    else:
        urler = url + message.text + ".png"
        response = r.get(urler, params=weather_parameters, headers=request_headers)
        bot.send_photo(message.chat.id, response.content)


bot.infinity_polling()
