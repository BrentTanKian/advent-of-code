def battle_simulate(player_damage, player_armor):
    player_health, boss_health = 100, 103
    boss_dies = False
    while True:
        boss_health = boss_health - (player_damage - 2)
        if boss_health <= 0:
            boss_dies = True
            break
        player_health = player_health - (9 - player_armor)
        if player_health <= 0:
            break
    if boss_dies:
        return 'Boss dies first'
    return 'Player dies first'


if __name__ == "__main__":
    # Optimal breakpoint for damage and armor to lose
    print(battle_simulate(7, 4))
    # Maximum cost for this damage and armor is Dagger, Damage (+3) ring, Defense (+3) ring and leather
    print(8 + 100 + 80 + 13)

