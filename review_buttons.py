import discord
from enums import BpCriteria
from config import SHEET
from discord.ui import Modal, Select, TextInput, View

class ReviewButtons(discord.ui.View):
    def __init__(self, user: discord.User, image_url: str):
        super().__init__()
        self.user = user
        self.image_url = image_url
        self.scores = {criterion.name: False for criterion in BpCriteria}

    async def update_score(self, interaction: discord.Interaction, criterion: BpCriteria):
        if self.scores[criterion.name]:
            await interaction.response.send_message(f"❌ {criterion.value[0]} ถูกเลือกไปแล้ว!", ephemeral=True)
            return
        self.scores[criterion.name] = True
        SHEET.append_row([str(self.user), self.image_url, criterion.value[0], criterion.value[1]])
        await interaction.response.send_message(f"✅ เพิ่ม {criterion.value[0]} ให้ {self.user.mention} แล้ว!", ephemeral=True)

    @discord.ui.button(label="เข้าร่วม(เสียค่าตั๋ว)", style=discord.ButtonStyle.primary)
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.update_score(interaction, BpCriteria.TICKET)

    @discord.ui.button(label="เลือดบอสมากกว่า 50%", style=discord.ButtonStyle.primary)
    async def hp_50(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.update_score(interaction, BpCriteria.HP_50)

    @discord.ui.button(label="ผู้เข้าร่วมน้อย", style=discord.ButtonStyle.primary)
    async def low_participation(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.update_score(interaction, BpCriteria.LOW_PARTICIPATION)

    @discord.ui.button(label="เวลาพิเศษ", style=discord.ButtonStyle.primary)
    async def special_time(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.update_score(interaction, BpCriteria.SPECIAL_TIME)

    @discord.ui.button(label="🔄 รีเซ็ตคะแนน", style=discord.ButtonStyle.danger)
    async def reset(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.scores = {criterion.name: False for criterion in BpCriteria}
        await interaction.response.send_message(f"🔄 คะแนนของ {self.user.mention} ถูกรีเซ็ตแล้ว!", ephemeral=True)