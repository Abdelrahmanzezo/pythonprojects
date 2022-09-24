import time
select_intro ="Welcome to sas studio"
print(select_intro.capitalize()) # make the letter capitalize
print("welcome to calculation app")
print("please wait")
time.sleep(2)
print("successfully...")   


while True:
    select =input("select your operator you want to excute [+],[-],[*],[/],[**],[//] ...")
    if select == '+':
          number1=float(input("Enter the first number......"))
          number2=float(input("Enter the second number........"))
          print(f"the result is :{number1+number2}")
          print("your operation is finished ...,thank you") 
    if select == '-':
          number1=float(input("Enter the first number...."))
          number2=float(input("Enter the second number...."))
          print(f"the result is :{number1-number2}")
          print("your operation is finished ...,thank you")
    if select == '*':
          number1=float(input("Enter the first number.."))
          number2=float(input("Enter the second number.."))
          print(f"the result is :{number1*number2}")
          print("your operation is finished ...,thank you")
    if select == '/':
          number1=float(input("Enter the first number.."))
          number2=float(input("Enter the second number.."))
          print(f"the result is :{number1/number2}")
          print("your operation is finished ...,thank you") 
    if select == '**':
          number1=float(input("Enter the first number.."))
          number2=float(input("Enter the second number.."))
          print(f"the result is :{number1**number2}")
          print("your operation is finished ...,thank you") 
    if select == '//':
          number1=float(input("Enter the first number.."))
          number2=float(input("Enter the second number.."))
          print(f"the result is :{number1//number2}")
          print("your operation is finished ...,thank you")
      
    option = input("Do you want to do another opertion..?? if Yes enter 'y' or 'Y' if No enter 'n' or 'N' ")
    if option =='y' or option =='Y':
         select =input("select your operator you want to excute [+],[-],[*],[/],[**],[//] ...")
         if select == '+':
                  number1=float(input("Enter the first number......"))
                  number2=float(input("Enter the second number........"))
                  print(f"the result is :{number1+number2}")
                  print("your operation is finished ...,thank you") 
         if select == '-':
                  number1=float(input("Enter the first number...."))
                  number2=float(input("Enter the second number...."))
                  print(f"the result is :{number1-number2}")
                  print("your operation is finished ...,thank you")
         if select == '*': 
                  number1=float(input("Enter the first number.."))
                  number2=float(input("Enter the second number.."))
                  print(f"the result is :{number1*number2}")
                  print("your operation is finished ...,thank you")
         if select == '/':
                  number1=float(input("Enter the first number.."))
                  number2=float(input("Enter the second number.."))
                  print(f"the result is :{number1/number2}")
                  print("your operation is finished ...,thank you")
         if select == '**':
                  number1=float(input("Enter the first number.."))
                  number2=float(input("Enter the second number.."))
                  print(f"the result is :{number1**number2}")
                  print("your operation is finished ...,thank you") 
         if select == '//':
                  number1=float(input("Enter the first number.."))
                  number2=float(input("Enter the second number.."))
                  print(f"the result is :{number1//number2}")
                  print("your operation is finished ...,thank you") 
    else:
         print("the program in ending ........!") 
         time.sleep(1)
         break
