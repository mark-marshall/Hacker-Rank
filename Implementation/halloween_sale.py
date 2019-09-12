# https://www.hackerrank.com/challenges/halloween-sale/problem
def howManyGames(p, d, m, s):
    first_bought = False
    num_games = 0
    cur_game_cost = p - d
    while (s > p or first_bought == True) and (s >= cur_game_cost) and (s >= m):
        if not first_bought:
            s -= p
            num_games += 1
            first_bought = True
        elif cur_game_cost > m:
            s -= cur_game_cost
            cur_game_cost -= d
            num_games += 1
        elif cur_game_cost <= m:
            s -= m
            num_games += 1
    return num_games
