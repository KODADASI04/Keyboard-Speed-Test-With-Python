import constants
all_words_file = open(f"{constants.PATH}/all_words.txt","w")

alphabet = ["A","B","C","Ç","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for char in alphabet:
    with open(f"{constants.PATH}/{char}.txt" , encoding="utf8") as file:
        words = file.readlines()
        for word in words:
            word = word.strip("\n").strip(" ")
            word += "\n"
            all_words_file.write(word)