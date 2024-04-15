'''This is a python program to create a Fibonacci generator.
Fibonacci is a sequence of adding the two preceding numbers.
Like - 0, 1, 1, 2, 3, 5, 8, 13, 21....'''

def fibonacciGenerator(n):
    firstNo = 0
    secondNo = 0
    newNo = 1
    for i in range(n):
        firstNo = secondNo + newNo
        newNo = secondNo
        secondNo = firstNo
        print(firstNo)

if __name__ == "__main__":
    nterms = int(input("Enter the number: "))
    fibonacciGenerator(nterms)