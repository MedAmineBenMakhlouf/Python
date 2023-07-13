from game_characters import barberian,character,elf,seer
base_character = Character("john")
conan = barbarian("Conan")
elon = Seer()

elon.hidden_type.attack(conan)

print("Conan health:", conan.health)
conan.attack(base_character)

