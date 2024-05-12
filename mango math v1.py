print("mango math menu v1.01 (python edition)")
print("options = 1.addition 2.subtraction 3.multiplication 4.division")
type = int(input("input: "))
if type == 1:
    print("--addition--")
    intOne = int(input("intiger one: "))
    intTwo = int(input("intiger two: "))
    answer = intOne + intTwo
    print("answer =",answer)
elif type == 2:
    print("--subtraction--")
    intOne = int(input("intiger one: "))
    intTwo = int(input("intiger two: "))
    answer = intOne - intTwo
    print("answer =",answer)
elif type == 3:
    print("--multiplication--")
    intOne = int(input("intiger one: "))
    intTwo = int(input("intiger two: "))
    answer = intOne * intTwo
    print("answer =",answer) 
elif type == 4:
    print("--division--")
    intOne = int(input("intiger one: "))
    intTwo = int(input("intiger two: "))
    answer = intOne / intTwo
    print("answer =",answer) 