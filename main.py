import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(score1, score2):
    if score1 == score2:
        return "Draw!"
    elif score1 == 0:
        return "You Win!"
    elif score1 > 21:
        return "Computer Wins!"
    elif score2 == 0:
        return "Computer Wins!"
    elif score2 > 21:
        return "You Win!"
    elif score1 > score2:
        return "You Win!"
    else:
        return "Computer Wins!"
user_cards = []
com_cards = []
is_game_over = False

for card in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    com_cards.append(new_card)

while not is_game_over:
    user_score = calculate_score(user_cards)
    com_score = calculate_score(com_cards)

    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"Computer first card: {com_cards[0]}")

    if com_score == 0 or user_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_input = input("Do you want to select another card?: ").lower()
        if user_input == 'y':
            user_cards.append((deal_card()))
        else:
            is_game_over = True
while com_score != 0 and com_score < 17:
    com_cards.append(deal_card())
    com_score = calculate_score(com_cards)
print(compare(user_score, com_score))