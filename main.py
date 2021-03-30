import random
def Xx(number):
    wrong=random.randint(1,9)
    table=[i*number for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,10)
    return table







def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1
    return None




if __name__=="__main__":
    number=int(input())
    v=Xx(number)
    print(v)
    wrongindex=iscorrect(v,number)
    print(f"wrong index in {wrongindex}")
