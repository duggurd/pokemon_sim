import random


class Entity:
    def __init__(self):
        self.val = random.random()

    def __lt__(self, __o: object) -> bool:
        return self.val < __o.val
    
    def __le__(self, __o: object) -> bool:
        return self.val <= __o.val
    
    def __gt__(self, __o: object) -> bool:
        return self.val > __o.val
    
    def __ge__(self, __o: object) -> bool:
        return self.val >= __o.val
    
    def __eg__(self, __o: object) -> bool:
        return self.val == __o.val
    
    def __ne__(self, __o: object) -> bool:
        return self.val != __o.val


class World:
    def __init__(self, n_agents):
        self._agents={Entity():0 for _ in range(n_agents)}


class GeneticAlgorithm:
    # Initialises the genetic algorithm
    # world is World and contains the agents original
    # num_rounds is the number of rounds per epoch (should at least 3x the count of agents)
    # epochs is the number of epochs
    def __init__(self, world, num_rounds=20, epochs=10):
        self._world = world
        self._num_rounds=num_rounds
        self.epochs = epochs

    def next_round(self):
        agent1, agent2 = random.sample(self._world._agents, 2)
        if agent1 > agent2:
            agent1.val += 1
        elif agent1 < agent2:
            agent2.val += 1
        

    def _next_iteration(self):
        ...
