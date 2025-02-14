import discord
import json
import os
from discord import app_commands
from discord.ext import commands

SHEET_CONFIG_FILE = "sheets_config.json"


class SheetHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.sheet_id = self.load_sheet_id()  # โหลดค่า Sheets ID ตอนเริ่มบอท

    def load_sheet_id(self):
        """โหลด Google Sheets ID จากไฟล์ JSON"""
        if os.path.exists(SHEET_CONFIG_FILE):
            with open(SHEET_CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("SHEET_ID", None)
        return None

    def save_sheet_id(self, sheet_id):
        """บันทึก Google Sheets ID ลงไฟล์ JSON"""
        with open(SHEET_CONFIG_FILE, "w") as f:
            json.dump({"SHEET_ID": sheet_id}, f, indent=4)

    @app_commands.command(name="sheetdata", description="ตั้งค่า Google Sheets ID สำหรับบอท")
    @app_commands.describe(sheet_id="ใส่ Google Sheets ID")
    async def sheetdata(self, interaction: discord.Interaction, sheet_id: str):
        """คำสั่ง /sheetdata ให้แอดมินตั้งค่า Google Sheets ID"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ คุณไม่มีสิทธิ์ใช้คำสั่งนี้!", ephemeral=True)
            return

        self.bot.sheet_id = sheet_id  # ตั้งค่า Google Sheets ID
        self.save_sheet_id(sheet_id)  # บันทึกลงไฟล์ JSON

        await interaction.response.send_message(f"✅ ตั้งค่า Google Sheets ID สำเร็จ: `{sheet_id}`", ephemeral=True)


async def setup(bot):
    await bot.add_cog(SheetHandler(bot))