import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Token สำหรับบอท
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Google Sheets Configuration
SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "service_account.json"

# เชื่อมต่อ Google Sheets
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
gc = gspread.authorize(credentials)
SHEET = gc.open_by_key(SHEET_ID).sheet1