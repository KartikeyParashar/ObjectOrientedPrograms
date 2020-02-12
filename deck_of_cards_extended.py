import random
from itertools import product
from oops_utils.queue_using_linked_list import Queue


class IndividualPlayerDetails:
    """It will save each player details"""
    def __init__(self, qu):
        self.qu = qu


class DeckOfCards:
    def __init__(self):
        self.player = []
        self.suit = ["Club", "Diamond", "Heart", "Spade"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def total_cards_list(self):
        """It wil return a list containing of 36 random tuple having cards arranged randomly """
        cartesian_product = product(self.suit, self.rank)
        list_of_cards = list(cartesian_product)
        return random.sample(list_of_cards, 36)

    def card_distribution(self):
        """It will distribute the 36 cards between the four players"""
        count = 0
        for number in range(4):
            lst = []
            for card in range(9):
                lst.append(self.total_cards_list()[count])
                count += 1
            self.player.append(lst)

    def sort_players_card(self):
        """It will sort cards by rank"""
        for player_list in self.player:
            for num in range(0, len(player_list)):
                for n in range(0, len(player_list) - num - 1):
                    pos = player_list[n]
                    next_pos = player_list[n + 1]
                    if self.rank.index(pos[1]) < self.rank.index(next_pos[1]):
                        player_list[n], player_list[n + 1] = player_list[n + 1], player_list[n]

    def queue_insertion(self):
        """It will insert all the cards of players in a queue"""
        count = 1
        print("After inserting each player in a queue,we got: ")
        for lst in self.player:
            obj = Queue()
            obj.en_queue(lst)
            print(f"The cards of player {count} are: ")
            count += 1
            obj.print_list()
            print()

    def individual(self):
        """que stores each player name like player1 , player 2........"""
        que = Queue()
        for lst in self.player:
            if self.player.index(lst) == 0:
                obj = Queue()
                obj.en_queue(lst)
                player1 = IndividualPlayerDetails(obj)
                que.en_queue(player1)

            elif self.player.index(lst) == 1:
                obj = Queue()
                obj.en_queue(lst)
                player2 = IndividualPlayerDetails(obj)
                que.en_queue(player2)

            elif self.player.index(lst) == 2:
                obj = Queue()
                obj.en_queue(lst)
                player3 = IndividualPlayerDetails(obj)
                que.en_queue(player3)

            elif self.player.index(lst) == 3:
                obj = Queue()
                obj.en_queue(lst)
                player4 = IndividualPlayerDetails(obj)
                que.en_queue(player4)

        print()
        print("Finally when each player get the cards and after arranging acc. to rank,the cards in all of hands are: ")
        for i in range(4):
            x = que.de_queue_data()
            player_queue = x.qu
            print(player_queue.de_queue_data())


def main():
    obj_of_player = DeckOfCards()
    obj_of_player.total_cards_list()
    obj_of_player.card_distribution()
    obj_of_player.sort_players_card()
    obj_of_player.queue_insertion()
    obj_of_player.individual()


main()
