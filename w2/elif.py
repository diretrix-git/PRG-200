for i in range(20):
    marks = float(input("Enter marks: "))

    if marks >= 80:
        print("Distinction")
    elif marks >= 60:
        print("First Division")
    elif marks >= 45:
        print("Second Division")
    elif marks >= 32:
        print("Third Division")
    else:
        print("Fail")