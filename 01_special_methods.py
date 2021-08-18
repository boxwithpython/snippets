import collections

# используем namedtuple для создания класса, представляющего одну карту
Card = collections.namedtuple('Card', ['rank', 'suit'])


# класс нашей колоды
class Deck:
    ranks = [str(n) for n in range(6, 11)] + list('ВДКТ')  # создаем ранги всех карт
    suits = ['червы', 'пики', 'бубны', 'трефы']  # получаем рубашки

    def __init__(self):
        # генерируем карты
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks
                       ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos: int):
        return self._cards[pos]
