# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28187462"))
API_HASH = getenv("API_HASH", "0159fbade6b803a808fbc5e248d52b87")
BOT_TOKEN = getenv("BOT_TOKEN", "7924605822:AAFc7To_ndjnk47DTPZKRu4apXTGYQiXwks")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1291491834").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://divyeshkalleda445:DbytYwTnK0rYszMA@cluster0.g9gon.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002320155220")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002281348453"))
