print("Welcome to the Data Analyzer and Transformer Program.")

while True:
    print("Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary(Built-in Function)")
    print("3.Calculate Factorial(Recursion)")
    print("4.Filter Data by Threshold (Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics(Return Multiple Values)")
    print("7.Exit Program")

    user= int(input("Please Enter your Choice:"))

    if user == 1:
        arr = list(map(int,input("Enter data for a 1D array(Separated by spaces):").split()))
        print("array",arr)
        print(type(arr))

    elif user == 2:
        print("data summary: ")
        print("Total Element:",len(arr))
        print("Minimum Value:",min(arr))
        print("Maximum Value:",max(arr))
        print("Sum Of All Value :",sum(arr))
        avg = sum(arr) / len(arr)
        print("Average Value :",avg)

    elif user == 3:
        num = int(input("enter a number : "))
        fac = 1
        for i in range(1,num + 1):
            fac *= i
        print(fac)

    elif user == 4:
        a = int(input("Enter a threshold value to filter out data above this value :"))
        data = (list(filter(lambda  x:x > a,arr)))
        print(f"Filtered Data(values>= {a})",data)
    elif user == 5:
        print("Choose Sorting Option: ")
        print("1. Ascending")
        print("2. Descending")
        user = int(input("Enter your choice :"))
        if user == 1:
            arr = sorted(arr)
            print("Ascending Array",arr)
        elif user == 2:
            arr = sorted(arr,reverse=True)
            print("Descending Array",arr)
        else:
            print("Invalid choice")

    elif user == 6:
        print("Dataset Statistics:")
        print("Minimum Value:",min(arr))
        print("Maximum Value:",max(arr))
        print("Sum Of All Values:",sum(arr))
        avg = sum(arr) / len(arr)
        print("Avaraage Value:",avg)

    elif user == 7:
        print("Exit The Program")
        break

    else:
        print("Entering A Long Number.")