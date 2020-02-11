import random
from itertools import product
from oops_utils.queue_using_linked_list import Queue


class Player:
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
        for lst in self.player:
            obj = Queue()
            obj.en_queue(lst)
            print(f"The cards of player {count} are: ")
            count += 1
            obj.print_list()
            print()


obj_of_player = Player()
obj_of_player.total_cards_list()
obj_of_player.card_distribution()
obj_of_player.sort_players_card()
obj_of_player.queue_insertion()
