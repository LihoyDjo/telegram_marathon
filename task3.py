def mineralFormation(cave):
    """Returns the shape of the mineral depending on the beginning of its growth"""
    if 1 in cave[0] and 1 in cave[-1]:
        return 'both'
    elif 1 in cave[0]:
        return 'stalactites'
    elif 1 in cave[-1]:
        return 'stalagmites'


print(mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]))
print(mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))
print(mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))