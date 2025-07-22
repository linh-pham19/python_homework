# TASK 1:
def hello():
    return "Hello!"

hello()

# TASK 2:
def greet(name):
    return f"Hello, {name}!"

greet("James")

# TASK 3:
def calc(a, b, operation="multiply"):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        return "You can't multiply those values!"
    if operation == "multiply":
        return a * b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "divide":
        if b == 0:
            return "You can't divide by 0!"
        return a / b
    elif operation == "modulo":
        return a % b 
   
    
print(calc(5, 0,"divide"))

#TASK 4:
def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
            return float(value)
        elif type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
print(data_type_conversion("16", "str"))


# TASK 5:
def grade(*args):
    try:
        args = [float(score) for score in args]
    except ValueError:
        return "Invalid data was provided."
    
    average = sum(args) / len(args)
    
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
print(grade(75, 85, 95))

#TASK 6
def repeat(string, times):
    return string * times

print(repeat("hi",3))

# TASK 7:
def student_scores(operation, **kwrags):
    if operation == "mean":
        return sum(kwrags.values()) / len(kwrags)
    elif operation == "best":
        return max(kwrags, key=kwrags.get)
    else:
        return "Invalid operation"
    
print(student_scores("best", Coco=75, Angel=89, Jupy=91))

# TASK 8
def titleize(title):
    words = title.split()
    capitalized_words = []
    little_words = {"a", "an", "on", "the", "and", "in", "of", "to", "for", "at", "by", "with"}
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1 or word.lower() not in little_words:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())
    return ' '.join(capitalized_words)

print(titleize("an in in"))

#TASK 9:
def hangman(secret, guess):
    display=[]
    for letter in secret:
        if letter in guess:
            display.append(letter)
        else:
            display.append('_')
    return ''.join(display)
    
print(hangman("python", "no"))

#TASK 10:
def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    vowels = 'aeiou'

    for word in words:
        word = word.lower()
        if word.startswith('qu'):
            pig_latin_word = word[2:] + 'quay'
        elif word[0] in vowels:
            pig_latin_word = word + 'ay'
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == 'qu':
                    i += 2
                    break
                i += 1
            pig_latin_word = word[i:] + word[:i] + 'ay'
        pig_latin_words.append(pig_latin_word)

    return ' '.join(pig_latin_words)

print(pig_latin("square quiet apple banana cherry"))