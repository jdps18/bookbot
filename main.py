



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    wordcount(file_contents)
    print("--- Begin a report of books/frankenstein.txt ---")
    charactercount(file_contents)
    
        

def wordcount(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    print(f"$wordcount words found in the document")

def charactercount(text):
    characters = {}
    lowered_text=text.lower()
    for char in lowered_text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] = characters[char] + 1
    report(characters)

def sort_on(dict):
    return dict["Number"]    
    
def report(chars):
    char_list = []
    for char in chars:
        if char.isalpha() is True:
            char_dict = {"Character": char,"Number": chars[char]}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    
    for char_data in char_list:
        print(f"The '{char_data['Character']}' character was found '{char_data['Number']}' times")


    
    



main()