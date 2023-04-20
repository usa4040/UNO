import random


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def play_card(self, card_index, deck):
        return self.hand.pop(card_index)


class Deck:
    def __init__(self):
        self.cards = [Card(color, value) for color in ["赤", "緑", "青", "黄"]
                      for value in list(range(0, 10)) + ["スキップ", "リバース", "プラス2"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


def valid_play(card1, card2):
    return card1.color == card2.color or card1.value == card2.value


def uno_game():
    players = [Player("あなた"), Player("コンピュータ1"),
               Player("コンピュータ2"), Player("コンピュータ3")]
    deck = Deck()
    deck.shuffle()

    for player in players:
        for _ in range(7):
            player.draw(deck)

    pile = [deck.draw_card()]

    while True:
        for player in players:
            print(f"{player}のターンです。")
            print(f"現在のカード: {pile[-1]}")
            print(f"{player}の手札: {', '.join(str(card) for card in player.hand)}")

            if player.name == "あなた":
                valid_indices = [i for i, card in enumerate(
                    player.hand) if valid_play(card, pile[-1])]

                if not valid_indices:
                    print("プレイできるカードがありません。カードを引きます。")
                    player.draw(deck)
                    continue

                while True:
                    try:
                        card_index = int(input("プレイするカードのインデックスを入力してください: "))
                        if card_index not in valid_indices:
                            raise ValueError
                        break
                    except ValueError:
                        print("無効なインデックスです。有効なインデックスを入力してください。")
            else:
                valid_indices = [i for i, card in enumerate(
                    player.hand) if valid_play(card, pile[-1])]

                if not valid_indices:
                    player.draw(deck)
                    continue

                card_index = random.choice(valid_indices)

            card_played = player.play_card(card_index, deck)
            print(f"{player}が {card_played} をプレイしました。")
            pile.append(card_played)

            if not player.hand:
                print(f"{player}が勝ちました！")
                return


if __name__ == "__main__":
    uno_game()
