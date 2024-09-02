"""
File name: cracker.py
Author: Andrew Foerst 
Created: 9/1/2024
Description: To display all possible combinations of a word lock 
"""

def main():
    # Loading dictionary of words 
    words = set()
    with open("words.txt", "rt", encoding="utf-8") as read:
        for line in read:
            words.add(line.strip())

    # Getting user input for what the combinations can be
    first = list(input("What are the options for the first letter of the lock?\n").upper())
    second = list(input("What are the options for the second letter of the lock?\n").upper())
    third = list(input("What are the options for the third letter of the lock?\n").upper())
    fourth = list(input("What are the options for the fourth letter of the lock?\n").upper())
    
    test = ["0","0","0","0"]
    possibilities = []

    # Generating all possibilities 
    for f in first:
        test[0] = f
        for s in second:
            test[1] = s
            for t in third:
                test[2] = t
                for f in fourth:
                    test[3] = f
                    word = "".join(test)
                    if word in words:
                        possibilities.append(word)
    
    # Outputting possible words for the lock into a text file 
    possibilities.sort()
    with open("possibilities.txt", "wt", encoding="utf-8") as w:
        for p in possibilities:
            w.write(p +"\n")


if __name__ == "__main__":  
    main()
    
