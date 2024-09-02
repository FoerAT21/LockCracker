from datetime import datetime 
def main():
    words = set()
    with open("words.txt", "rt", encoding="utf-8") as read:
        for line in read:
            words.add(line.strip())

    first = list(input("What are the options for the first letter of the lock?\n").upper())
    second = list(input("What are the options for the second letter of the lock?\n").upper())
    third = list(input("What are the options for the third letter of the lock?\n").upper())
    fourth = list(input("What are the options for the fourth letter of the lock?\n").upper())
    
    test = ["0","0","0","0"]
    possibilities = []

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
    possibilities.sort()
    with open("possibilities.txt", "wt", encoding="utf-8") as w:
        for p in possibilities:
            w.write(p +"\n")


if __name__ == "__main__":  
    main()
    
