import os
import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on  # นำเข้า server_on

# กำหนด Intents
intents = discord.Intents.default()
intents.message_content = True  # เปิดการอ่านข้อความ (ต้องเปิดใน Discord Developer Portal ด้วย)

# สร้าง instance ของบอท
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        await bot.tree.sync()  # ซิงค์คำสั่ง Slash
        print("✅ Slash Commands Synced!")
    except Exception as e:
        print(f"⚠️ Error syncing commands: {e}")

    await load_cogs()

# โหลด Cog จากโฟลเดอร์ cogs
async def load_cogs():
    await bot.load_extension("cogs.boss_commands")
    await bot.load_extension("cogs.image_handler")
    await bot.load_extension("cogs.sheet_handler")  # โหลดคำสั่ง /sheetdata

@bot.tree.command(name="check_sheet", description="เช็คว่า Google Sheets ID ถูกตั้งค่าหรือยัง")
async def check_sheet(interaction: discord.Interaction):
    sheet_id = bot.sheet_id
    if sheet_id:
        await interaction.response.send_message(f"✅ Google Sheets ID ที่ใช้: `{sheet_id}`", ephemeral=True)
    else:
        await interaction.response.send_message("❌ ยังไม่มีการตั้งค่า Google Sheets ID!", ephemeral=True)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await load_cogs()  # โหลดคำสั่งบอท

# เปิดเซิร์ฟเวอร์ Flask เพื่อให้บอทออนไลน์เสมอ (จำเป็นสำหรับ Replit / Heroku ฟรี)
server_on()

# เริ่มรันบอท
bot.run(os.getenv('TOKEN'))