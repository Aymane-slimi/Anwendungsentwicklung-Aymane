

def Add_func():
    r=first_num + second_num
    print(f"the Result is: {r:.2f}")
def sub_func():
    r=first_num - second_num
    print(f"the Result is: {r:.2f}")
def mull_func():
    r=first_num * second_num
    print(f"the Result is: {r:.2f}")
def dev_func():
    global second_num
    if second_num == 0:
        print("Error: Division by zero!")
        try:
            second_num = float(input("Please Enter a new second number (not zero): "))
            dev_func()  
        except ValueError:
            print("Invalid input. Please enter a number.")
            dev_func()
    else:
        result = first_num / second_num
        print(f"The result is: {result:.2f}")
while True:
            print("Calculator".center( 60,"#"))

            #Here to type inputs
            first_num=float(input("Enter your first Number: "))
            second_num=float(input("Enter your second Number: "))
            print("1-addition(+) \n 2-Substraction(-) \n 3-Multiplication(×) \n 4-Devision(÷)")
            operation=input("Choose the Operation you want: ").strip().lower()

            # here beginn the calculations in the input
            if operation in["1","addition","add","+"]:
                Add_func()
            elif operation in ["2","substraction","sub","-"]:
                sub_func()
            elif operation in ["3","multiplication","mul","×","*"]:
                mull_func()
            elif operation in["4","devision","dev","/" ,"÷"]:
                dev_func()
            else:
                print("Invalid operation")

            #here to decide a new operation or exit
            end=input("0=Exit \n 1=New \n choose:")
            if end =="0":
                    print("Exiting calculator...")
                    break





