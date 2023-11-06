# variables

name = "Lee" # character's name, Lee by default
level = 7 # replace with level
conmod = 2 # replace with Consitution modifier
status = "very tiny and cute." # just fluff to make wifey smile


###


#calculations

barbHP = (12 + conmod) + ((7 + conmod) * (level - 1)) # calculation for barbarian 5e HP (averaged)
bardHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for bard 5e HP (averaged)
clericHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for cleric 5e HP (averaged)
druidHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for druid 5e HP (averaged)
fighterHP = (10 + conmod) + ((6 + conmod) * (level - 1)) # calculation for fighter 5e HP (averaged)
monkHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for monk HP (averaged)
pallyHP = (10 + conmod) + ((6 + conmod) * (level - 1)) # calculation for paladin HP (averaged)
rangerHP = (10 + conmod) + ((6 + conmod) * (level - 1)) # calculation for ranger 5e HP (averaged)
rogueHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for rogue HP (averaged)
sorcHP = (6 + conmod) + ((4 + conmod) * (level - 1)) # calculation for sorcerer  HP (averaged)
warlockHP = (8 + conmod) + ((5 + conmod) * (level - 1)) # calculation for warlock HP (averaged)
wizardHP = (6 + conmod) + ((4 + conmod) * (level - 1)) # calculation for monk HP (averaged)


###

# outputs - replace xxxxHP with class calculation above

print(name, "is level", level, "and has", barbHP , "HP. They are, also,", status)
# HP calculation for a 5e character without feats or racial bonuses

print("If", name, "is a Hill Dwarf, their HP is", barbHP + level, "instead - nice beard.")
# HP calculation for a 5e character with the Hill Dwarf racial bonus

print("If", name, "has the Tough feat, they have", barbHP + (level * 2), "HP and sick muscles.")
# HP calculation for a 5e character with Tough feat

print("If", name, "is a Tough Hill Dwarf, their HP is", barbHP + level + (level * 2), "and they should be the party's tank.")
# HP calculation for a 5e character with both Hill Dwarf and Tough bonuses