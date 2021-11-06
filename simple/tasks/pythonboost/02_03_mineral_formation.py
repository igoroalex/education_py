def mineral_formation(cave: list) -> str:
    """get presence of stalactites and stalagmites"""
    scheme_cave = {(True, True): 'both',
                   (True, False): 'stalactites',
                   (False, True): 'stalagmites',
                   (False, False): 'no rocks'}

    return scheme_cave[(any(cave[0]), any(cave[-1]))]

# assert mineral_formation([
#     [0, 1, 0, 1],
#     [0, 1, 0, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0]
# ]) == "stalactites"
#
# assert mineral_formation([
#     [0, 0, 0, 0],
#     [0, 1, 0, 1],
#     [0, 1, 1, 1],
#     [0, 1, 1, 1]
# ]) == "stalagmites"
#
# assert mineral_formation([
#     [1, 0, 1, 0],
#     [1, 1, 0, 1],
#     [0, 1, 1, 1],
#     [0, 1, 1, 1]
# ]) == "both"
