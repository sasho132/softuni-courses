from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_: Pokemon):
        if any([x.name == pokemon_.name for x in self.pokemons]):
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon_)
        return f"Caught {pokemon_.name} with " \
               f"health {pokemon_.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon.name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f'- {pokemon.pokemon_details()}\n'
        return result
