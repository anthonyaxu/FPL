import unidecode

# Convert string into lowercase
def lowercase(string):
    return string.lower()

# Removes all accents and special alphabet characters
def deaccent(string):
    return unidecode.unidecode(string)

# Convert player's element type to position
def convert_position(position):
    position_dictionary = {
        1: "Goalkeeper",
        2: "Defender",
        3: "Midfielder",
        4: "Forward"
    }
    return position_dictionary[position]