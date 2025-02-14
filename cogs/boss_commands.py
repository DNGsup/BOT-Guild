import gspread
import discord

from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
from discord import app_commands
from enums import BossName  # นำเข้า Enum ที่กำหนดไว้ใน enums.py

class BossCommands(commands.Cog):  # กำหนดให้เป็น Cog
    def __init__(self, bot):
        self.bot = bot  # เก็บ instance ของ bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, world!")

    def get_google_sheet(self):
        """เชื่อมต่อ Google Sheets"""
        if not self.bot.sheet_id:
            return None

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
        client = gspread.authorize(creds)
        return client.open_by_key(self.bot.sheet_id)

    @app_commands.command(name="create_boss", description="สร้างโพสต์บอสและเปิดเธรดให้สมาชิกลงรูป")
    async def create_boss(self, interaction: discord.Interaction, name: BossName, date: str, time: str):
        sheet = self.get_google_sheet()
        if not sheet:
            await interaction.response.send_message("❌ ยังไม่มีการตั้งค่า Google Sheets ID! กรุณาใช้ `/sheetdata`",
                                                    ephemeral=True)
            return

        # ดึงชีทแรก
        worksheet = sheet.get_worksheet(0)
        worksheet.append_row([name.value, date, time, interaction.user.name])

        await interaction.response.send_message(f"✅ บันทึกข้อมูลบอส `{name.value}` ลง Google Sheets แล้ว!",
                                                ephemeral=True)
    async def setup(bot):
        await bot.add_cog(BossCommands(bot))  # ใช้ await bot.add_cog()