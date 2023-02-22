import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20515805"))
    API_HASH = os.environ.get("API_HASH", "331d6eab3e285880282252b854e20975")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6059266175:AAHveGHVxwxOl-739kGwkdY9brGB9A9BvLw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJIBuyVgDY04ry3Z049w0gnMzkdQBDGFjmL9ykkD4vF0DgGPNI2U826RhvdZt8d38Gcu4YSnxtHxOJWwz1-8ULlRvMSuFDioFaOhansuuLrk7zDMFnZeRDYwM-bk9dYloyc-7FpKkIhdtIEonxiGRl5Twwi3y6rWGTYKLFavVu7TWY3EFUkFyFYmvv4tj7u6VJNKJM995werhHEhRSf6qau4LkW7lfaCYDIZkWo0hQZcI6_W9y0C2fw4162iJAj5EanGZ_MLj6q38tGqlc8R4LNelKxA8Dbb6sfBxptYwcdU0PdDyk8_S__2xDoPTxGGNTIxWDXT-uBHpqSH_gNhbvCQlFA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
