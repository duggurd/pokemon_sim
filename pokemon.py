import random

class Pokemon:
    def __init__(self, type1, type2, max_tot_stats):
        self.stats = PokemonStats(max_tot_stats)

# This class manages pokemon stats
class PokemonStats:
    # Kwargs 
    def __init__(self, max_tot_stats):
        stats = constrained_sum(9, max_tot_stats).__iter__()
        self._hp=stats.__next__()
        self._attack=stats.__next__()
        self._defense=stats.__next__()
        self._special=stats.__next__()
        self._special_attack=stats.__next__()
        self._special_defense=stats.__next__()
        self._speed=stats.__next__()
        self._accuracy=stats.__next__()
        self._evasion=stats.__next__()
    
    def mutate(self, mutation_prob, mutation_range):
        self._hp=stats.__next__()
        self._attack=stats.__next__()
        self._defense=stats.__next__()
        self._special=stats.__next__()
        self._special_attack=stats.__next__()
        self._special_defense=stats.__next__()
        self._speed=stats.__next__()
        self._accuracy=stats.__next__()
        self._evasion=stats.__next__()


def constrained_sum(n, total):
    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


stats = PokemonStats(10)