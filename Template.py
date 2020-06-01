"""
CTEC 121
<Grant Parkinson>
<mod7 lab1>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""


def main():
    # section 1
    # define a string
    mystr = 'Hello world'

    print()
    '''
    print(mystr)
    print(mystr[6])
    print(mystr[len(mystr)-1])
    print(mystr[10])
    # print(mystr[11])
    print(mystr[0])
    print(mystr[-1])
    print(mystr[-5])
    print(mystr[-len(mystr)])
    

    word1 = "Hello"
    word2 = "World"
    mystr2 = word1 + " " + word2
    print(mystr2)

    print(mystr2[6:len(mystr2)])
    

    # section 2

    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1-12): "))
    pos = (n-1) * 3
    print(pos)
    # slice to get abbreviation
    monthabr = months[pos:pos+3]
    print(monthabr)

    print(months[(n-1)*3:(n-1)*3+3])
   

    # lists
    # create an empty list
    mylist1 = []
    print("mylist1:", mylist1)

    mylist2 = [1, 2, 3, 4]
    print("mylist2:", mylist2)

    mylist3 = [42, 'forty-two', 3.14]
    print("mylist3:", mylist3)

    print("Third element of mylist2:", mylist2[2])

    # initialization example

    for i in range(1, 6):
        mylist1.append(i)
    print('mylist1:', mylist1)

    # illustrate insert()
    mylist1.insert(2, 3.14)
    print('mylist1:', mylist1)

    # illustrate sort
    mylist1.sort()
    print('mylist1:', mylist1)
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month number (1-12): "))
    print(months[n-1])

    print("A:", ord('A'))
    print("97:", chr(97))
    print()
    '''
    # section 3
    mystr = "text   \n"
    print("*", mystr, "*", sep="")
    mystr = mystr.rstrip()
    print("*", mystr, "*", sep="")

    mystr = "CamelCase"
    print(mystr)
    s1 = mystr.upper()
    print(s1)
    s2 = mystr.lower()
    print(s2)

    mystr = "Mary had a little lamb"
    mylist = mystr.split()
    print(mylist)
    print()


main()
