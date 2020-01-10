def getchoicenumber():
    return int(input("Enter a number/limit: "))     #We return what needs to be returned, we then set a variable to what was returned, also no need to use global variable

def getnaturalnumbers():
    choicenumber = getchoicenumber()         #This is the correct way of doing it, in java i did it a bit different, this is how it suppose to be.
    number = 0
    total = 0
    if choicenumber != 0 and choicenumber > 0:
        index = 0
        for index in range(index,choicenumber):
            number += 1
            if number % 3 == 0 or number % 5 == 0 and number <= choicenumber:
                total += number
        print("The sum of all numbers from 1 - " + str(choicenumber) + " are " + str(total))
    else:
        print("The number entered is invalid")

if __name__ == "__main__":
    getnaturalnumbers()

