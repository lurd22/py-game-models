import json
import datetime
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        race_info = pdata["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")}
        )

        for skill in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj
                }
            )

        guild_obj = None
        if pdata.get("guild"):
            guild_info = pdata["guild"]
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race_obj,
                "guild": guild_obj,
                "created_at": datetime.datetime.now()
            }
        )
