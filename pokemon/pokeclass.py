class Pokemon:
    def __init__(self, pokemon_ordbok: dict) -> None:
        self.id: int = pokemon_ordbok
        self.name: str = pokemon_ordbok["name"]["english"]
        self.type: list = pokemon_ordbok["type"]
        self.HP: int = pokemon_ordbok["base"]["HP"]
        self.Attack: int = pokemon_ordbok["base"]["Attack"]
        self.Defense: int = pokemon_ordbok["base"]["Defense"]


    def __stats__(self):
        return f"{self.name}, ({self.HP})"
    
