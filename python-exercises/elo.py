def elo(player_rating, opponent_rating, won, k=32):
    q1 = 10**(player_rating / 400)
    q2 = 10**(opponent_rating / 400)

    expected_score = q1 / (q1 + q2)
    true_score = int(won)

    final_score = player_rating + k * (true_score - expected_score)
    return int(final_score)


rating1 = int(input('First player score: '))
rating2 = int(input('Second player score: '))
player1_won = int(input('Which player won? [1/2]: ')) == 1

new_rating1 = elo(rating1, rating2, player1_won)
new_rating2 = elo(rating2, rating1, not player1_won)

print('Player 1 new score: {}. Change: {}'.format(new_rating1, new_rating1 - rating1))
print('Player 2 new score: {}. Change: {}'.format(new_rating2, new_rating2 - rating2))
