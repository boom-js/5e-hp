name = "Lee"

level = 7 
# replace with level

conmod = 2 
# replace with Consitution modifier

barbHP = (12 + conmod) + ((7 + conmod) * (level - 1))
# calculation for barbarian 5e HP - using averages, not rolls

status = "very tiny and cute."


print(name, "is level", level, "and has", barbHP , "health points. They are, also,", status)