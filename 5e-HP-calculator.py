name = "Lee" # character's name, Lee by default
level = 7 # replace with level
conmod = 2 # replace with Consitution modifier
barbHP = (12 + conmod) + ((7 + conmod) * (level - 1)) # calculation for barbarian 5e HP (averaged)
status = "very tiny and cute." # just fluff to make wifey smile

###

print(name, "is level", level, "and has", barbHP , "HP. They are, also,", status)
# HP calculation for a 5e barbarian without feats or racial bonuses

print("If", name, "is a Hill Dwarf, their HP is", barbHP + level, "instead - nice beard.")
# HP calculation for a 5e barbarian with the Hill Dwarf racial bonus

print("If", name, "has the Tough feat, they have", barbHP + (level * 2), "HP and sick muscles.")
# HP calculation for a 5e barbarian with Tough feat

print("If", name, "is a Tough Hill Dwarf, their HP is", barbHP + level + (level * 2), "and they should be the party's tank.")
# HP calculation for a 5e barbarian with both Hill Dwarf and Tough bonuses