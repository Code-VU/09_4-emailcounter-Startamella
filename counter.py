def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    who = dict()
    for line in handle :
        line = line.rstrip()
        if line.startswith("From:") :
            continue 
        if line.startswith("From") :
            line = line.split()
            if line[1] not in who : 
                who[line[1]] = 1
            else : 
                who[line[1]] = who[line[1]] + 1 

    bigcount = None
    bigword = None
    for word,count in who.items() : 
        if bigcount is None or count > bigcount : 
            bigcount = count 
            bigword = word 
    print(bigword, bigcount)   


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
