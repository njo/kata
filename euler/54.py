"""Compare poker hands. Assumes no shared cards."""


def make_value_count_dict(cards):
    """Helper method makes a dict of card value: counts."""
    d = {}  # value: count
    for card in cards:
        d[card.value] = d.get(card.value, 0) + 1

    return d


def find_value_for_count(value_count_dict, count):
    """Helper method retrieves value for given count or None."""
    for v, c in value_count_dict.iteritems():
        if c == count:
            return v
    return None

###
# Rank determination functions
###


def straight_flush(cards):
    """Are the cards a straight flush."""
    return straight(cards) and flush(cards)


def four_of_a_kind(cards):
    """Are the cards four of a kind."""
    return 4 in make_value_count_dict(cards).values()


def full_house(cards):
    """Are the cards a full house."""
    return set(make_value_count_dict(cards).values()) == set([2, 3])


def flush(cards):
    """Are the cards a flush."""
    suits = set([card.suit for card in cards])
    return len(suits) == 1


def straight(cards):
    """Are the cards a straight."""
    def _straight_numbers(numbers):
        return range(numbers[0], numbers[0] + 5) == numbers

    values = sorted([card.value for card in cards])
    if _straight_numbers(values):
        return True

    if 14 in values:  # Aces need to be tried as 1's too
        return _straight_numbers([1] + values[:-1])

    return False


def three_of_a_kind(cards):
    """Do the cards have three of a kind."""
    return 3 in make_value_count_dict(cards).values()


def two_pair(cards):
    """Do the cards contain a two pair."""
    return sorted(make_value_count_dict(cards).values()) == [1, 2, 2]


def pair(cards):
    """Do the cards contain a pair."""
    return 2 in make_value_count_dict(cards).values()


rank_to_function = {
    9: straight_flush,
    8: four_of_a_kind,
    7: full_house,
    6: flush,
    5: straight,
    4: three_of_a_kind,
    3: two_pair,
    2: pair}


def determine_rank(cards):
    """Get the 1-9 rank of a card - higher is better."""
    for rank in reversed(range(2, 10)):
        if rank_to_function[rank](cards):
            return rank
    return 1


class Card():
    """Cards have a suit and numeric value."""

    def __init__(self, value, suit):
        """Initialise card with its value and suit."""
        if not value.isdigit():
            value = {"T": 10,
                     "J": 11,
                     "Q": 12,
                     "K": 13,
                     "A": 14}[value]
        self.suit = suit
        self.value = int(value)

    def __lt__(self, other):
        """Compare this value to another."""
        return self.value < other.value

    def __eq__(self, other):
        """Compare equality of this card to another (suits don't matter)."""
        return self.value == other.value


class Hand():
    """A hand has a rank and a list of sorted cards."""

    def __init__(self, cards):
        """Make a hand from a list of cards, determine the rank."""
        self.cards = sorted(cards)
        self.rank = determine_rank(cards)

    def __lt__(self, other):
        """Compare this hand to another by rank, break ties if necessary."""
        if self.rank != other.rank:
            return self.rank < other.rank

        return self.is_hand2_stronger(self, other)

    def __eq__(self, other):
        """Compare this hand's rank to another with a tie breaker."""
        if self.rank == other.rank:
            return not self.is_hand2_stronger(self, other)
        return False

    def is_hand2_stronger(self, hand1, hand2):
        """Given two equally ranked hands, see if hand2 is stronger."""
        rank = hand1.rank

        def does_hand2_have_highest_card(h1_cards, h2_cards):
            """Tie break off who has the highest card."""
            h1_cards.sort()
            h2_cards.sort()
            while h1_cards:
                c1 = h1_cards.pop()
                c2 = h2_cards.pop()
                if c1 == c2:
                    continue
                return c1 < c2

            return False  # Cards are all the same

        # Straight flush, flush, straight, high card
        if rank in [9, 6, 5, 1]:
            return does_hand2_have_highest_card(hand1.cards, hand2.cards)

        d1 = make_value_count_dict(hand1.cards)
        d2 = make_value_count_dict(hand2.cards)
        if rank == 8:  # Four of a kind
            d1v = find_value_for_count(d1, 4)
            d2v = find_value_for_count(d2, 4)
            return d1v < d2v
        elif rank in [7, 4]:  # Full house, three of a kind
            d1v = find_value_for_count(d1, 3)
            d2v = find_value_for_count(d2, 3)
            return d1v < d2v
        elif rank == 2:  # pair
            d1v = find_value_for_count(d1, 2)
            d2v = find_value_for_count(d2, 2)
            if d1v != d2v:
                return d1v < d2v
            # Pair is the same rank
            hand1_remaining = [c for c in hand1.cards if c.value != d1v]
            hand2_remaining = [c for c in hand2.cards if c.value != d1v]
            return does_hand2_have_highest_card(
                hand1_remaining, hand2_remaining)
        elif rank == 3:  # 2 pair
            d1v1 = find_value_for_count(d1, 2)
            del d1[d1v1]
            d1v2 = find_value_for_count(d1, 2)
            d2v1 = find_value_for_count(d2, 2)
            del d2[d2v1]
            d2v2 = find_value_for_count(d2, 2)
            # Check for same rank 2 pairs
            if set([d1v1, d1v2]) == set([d2v1, d2v2]):
                d1v3 = find_value_for_count(d1, 1)
                d2v3 = find_value_for_count(d2, 1)
                if d1v3 == d2v3:
                    return False
                return d1v3 < d2v3
            d1_highest = max(d1v1, d1v2)
            d2_highest = max(d2v1, d2v2)
            if d1_highest != d2_highest:
                return d1_highest < d2_highest
            d1_low = min(d1v1, d1v2)
            d2_low = min(d2v1, d2v2)
            return d1_low < d2_low

        raise NotImplemented()

if __name__ == "__main__":

    """Reading the input, construct the two hands and compare them
    counting the first player's wins."""

    import fileinput

    p1_wins = 0
    for line in fileinput.input():
        card_text = line.split()
        hand1 = Hand([Card(*list(rank_suit)) for rank_suit in card_text[:5]])
        hand2 = Hand([Card(*list(rank_suit)) for rank_suit in card_text[5:]])

        if hand1 > hand2:
            p1_wins += 1

    print "Player 1 won", p1_wins, "hands"
