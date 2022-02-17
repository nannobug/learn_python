# use \
print("1-- " + "\"Hello \" World\"")

phrase = "Hello World"
name = "John"
print("2-- " + phrase + " " + name)

# string functions
print("3-- " + phrase.upper()) # convert all letters to upper cases
print("4-- " + phrase.lower()) # convert all letters to lower cases
print(phrase.isupper()) # check if all letters are upper
print(phrase.lower().islower())
print(len(phrase))
print(phrase[0])
print(phrase.index("He")) # when passing in multi-letter word, return index where it starts 
print(phrase.replace("Hello", "Goodbye"))