class ImageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_google_sheet(self):
        if not self.bot.sheet_id:
            return None

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
        client = gspread.authorize(creds)
        return client.open_by_key(self.bot.sheet_id)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot or not isinstance(message.channel, discord.Thread):
            return

        sheet = self.get_google_sheet()
        if not sheet:
            return

        worksheet = sheet.get_worksheet(0)
        for attachment in message.attachments:
            if attachment.content_type and attachment.content_type.startswith("image"):
                worksheet.append_row([message.author.name, attachment.url])

                await message.reply(f"✅ บันทึกหลักฐานไปยัง Google Sheets แล้ว!", mention_author=True)
