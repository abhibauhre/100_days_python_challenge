from prettytable import PrettyTable

# table = PrettyTable()
# print(table)

x = PrettyTable()
x.add_column("Pokemon name", ["pikachu", "bulbasaur", "charmander"])
x.add_column("Type", ["Electric", "Grass/Poison", "Fire"])

print(x)