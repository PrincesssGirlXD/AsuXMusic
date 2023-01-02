from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "24762688"))
API_HASH = getenv("API_HASH","0940dc2e4b6c7fe162850723b662df82")

ASS_HANDLER = list(getenv("ASS_HANDLER", "?").split())
BOT_TOKEN = getenv("BOT_TOKEN","5473258067:AAHSqXNz6kgeogNJP6acf3NiAEAzDlMjr9M")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID","-1001791419515")"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ssid1435:liyaxlambert*143@cluster0.pqwwxie.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1145284986").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/33850ff8f4482e6d09eb4.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/33850ff8f4482e6d09eb4.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vnmbrother")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/musicupdatevnm")

STRING_SESSION = getenv("STRING_SESSION", ""BQC2jACPK80p4Ovnnw2lvZJjvimoh2SasxYQZ17jcgHa-GD0kBezUApQlzDCaGxipdB7sk16dCEQzBcF9ar9pH3RZEVDbVjKyOltCiiSNIeBxXgNa7EzTHx7ZZKve13i1swy5UrkyH9vmEbQYvnQWOkg8azO2q-TmpxYf04oJpZHooToxkaDUX1iMnWT-69KjSVB4r9vh9I6rF_sO_eEbpBhpkTsw5sdCY2DOHCD2fa-ULzgU5zoVW82KItIatqlQvFGm-KSSPxRGZ1fUDtGRg1uQ2wfYufg_42RQlOpADYKXS0mLuD9cbUNc6X9Xa_9fmrp3hWNTpesH6Sq_WBAr-asAAAAAUz1AA)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1936119750").split()))
