import json
from db.models import Race, Skill, Guild, Player


def main():
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for pdata in players_data:
        race_obj, _ = Race.objects.get_or_create(
            name=pdata["race"]["name"],
            defaults={"description": pdata["race"].get("description", "")}
        )

        for skill in pdata["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race_obj
                }
            )

        guild_obj = None
        if pdata.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=pdata["guild"]["name"],
                defaults={"description": pdata["guild"].get("description")}
            )

        Player.objects.get_or_create(
            nickname=pdata["nickname"],
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )