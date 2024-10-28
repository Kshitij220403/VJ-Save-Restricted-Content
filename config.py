import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28701729"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "33996a64d960bbba00d44e1e3e034318")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kshitijj522:WENSionf2TGajjya@cluster0.vghoe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
