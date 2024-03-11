import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = { row.letter:row.code for (index, row) in data.iterrows() }
print(nato_dict)

word = input("Enter a name: ").upper()
try:
    output = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry only letters are allowed.")
else:
    print(output)
