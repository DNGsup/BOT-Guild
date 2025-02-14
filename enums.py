from enum import Enum

class BossName(Enum):
    CAVE_7 = "Cave 7"
    CAVE_8 = "Cave 8"
    CAVE_9 = "Cave 9"
    REGION_2 = "Region 2"
    REGION_3 = "Region 3"
    REGION_4 = "Region 4"
    RUINED_KNIGHT = "Ruined Knight"
    TANDALLON = "Tandallon"
    DERGIO = "Dergio"
    DUCAS = "Ducas"
    WORLD_DUNGEON = "World Dungeon"

class BpCriteria(Enum):
    TICKET = ("เข้าร่วม(เสียค่าตั๋ว)", 1)
    HP_50 = ("เลือดบอสมากกว่า 50%", 1)
    LOW_PARTICIPATION = ("ผู้เข้าร่วมน้อย", 1)
    SPECIAL_TIME = ("เวลาพิเศษ", 1)