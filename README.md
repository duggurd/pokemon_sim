# pokemon_sim
Genetic algorithm applied in the context of pokemon battles


Generates random pokemon  based on data from pokemon api, then a genetic algorithm is applied with pokemon battles as discriminators.

What kind of fields could the pokemon have?
- Stats, having maximum total sum of stats equal to x or using the IV type of stats description
- Types
- Moves, damage calculated from move, miss chance, move damage and pokemon stats


Part 2 - creating a cool UI/Interface
- Each pokemon sprite is generated from ai based on stats, type, etc. self trained image gen.
- Creating a tree of championship style, aggregated across generations showing the winner and loser of each epoch. For example epoch 1-500 "Jimbob" is the total winner and "Firebulb" is the loser.
- Different settings for initial state.
- Increase/decrease mutation rate.
- Choose min-max stats, types etc. pokemon to be generated.
