# import random for choices

bow_sets = ["Boko",
            "Lizalfos",
            "Rito",
            "Hylian",
            #"Lynel",
            "Royal/Guard",
            "Gerudo/Zora/Korok",
            "Sheikah/Yiga/Korok",
            ]
weapon_sets = ["Boko",
               "Moblin",
               "Hylian",
               "Royal/Guard",
               #"Lynel",
               "Guardian/Ancient",
               "Gerudo/Zora/Korok",
               "Sheikah/Yiga/Korok/Rito",
               "Everyday Goods",
               ]
shield_sets = ["Boko",
               "Hylian",
               "Royal/Guard",
               #"Lynel",
               "Guardian/Ancient",
               "Gerudo/Zora/Korok",
               "Sheikah/Pot Lid",
               ]
armor_sets = ["Basic",
              "Stealth",
              "Soldier",
              "Barbarian",
              "Zora",
              #"Gerudo",
              #"Phantom",
              #"Desert Voe",
              #"Ancient",
              #"Dark",
              "Snowquill",
              "Flamebreaker",
              "Rubber",
              "Climber",
              "Royal Guard",
              ]

objectives = ["20 Korok Seeds",
              "30 Korok Seeds",
              "20 Shrines",
              "2 Divine Beasts",
              "Defeat Ganon",
              "4 Masks",
              "4 Special Armor Pieces",
              "5 Taluses",
              "4 Hinoxes",
              "3 Lynels",
              "Master Sword + Hylian Shield"
              ]

output_template = """
Restrictions:
Weapons: {weapon}
Bows: {bow}
Shields: {shield}

Objectives:
Armor: {armor}
1: {objective1}
2: {objective2}
                  """

def generate_randomizer_seed():
    """
    Uses globals/imports to get sets of bows, shields, weapons, armor, and
    objectives. Returns a dict of 1 of bow, shield, weapons, armor, and 2 of
    objectives.
    """
    seed = {}
    
    global bow_sets
    global weapon_sets
    global shield_sets
    global armor_sets
    global objectives
    
    
    return seed

def write_to_file(seed={}, filename="botw_rando_gen.txt"):
    """
    Takes a dict (from generate_randomizer_seed),
    Writes out to a file (UTF-8 encoding). Optionally, provide
    filename (default is "botw_rando_gen.txt"). 
    """
    global output_template
    output = output_template.format(
        weapon = seed["weapon"],
        bow = seed["bow"],
        shield = seed["shield"],
        armor = seed["armor"],
        objective1 = seed["objective1"],
        objective2 = seed["objective2"],
        )
    with open(filename, "w") as f:
        f.write(output)

if __name__ == "__main__":
    seed = generate_randomizer_seed()
    write_to_file(seed)