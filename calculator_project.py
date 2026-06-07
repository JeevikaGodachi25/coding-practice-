from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

Cal_dictionary={'+':add, '-':subtract, '*':multiply, '/':divide}
def calculator():
    print(logo)
    f_num=float(input("type the first number?"))
    answer=True
    while answer:
        for i in Cal_dictionary:
            print(i)
        operation_choice=input("Pick a operation:")
        s_num=float(input("type the second number."))
        result=Cal_dictionary[operation_choice](f_num,s_num)
        print(f"{f_num} {operation_choice} {s_num}= {result}")
        opinion=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if opinion=="y":
            f_num=result
        else:
            answer=False
            print("="*200)
            print("\n"*20)
            calculator()
calculator()
