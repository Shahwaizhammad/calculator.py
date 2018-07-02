print("welcome to our calculator")
num1=int(input("enter your first no: "))
func=input("function- *,/+,– : ")
num2=int(input("enter your second no: "))
 
if  func == "/":
     ans=num1/num2
     print(ans)
     
if  func == "+":
     ans=num1+num2
     print(ans)

if  func == "*":
     ans=num1*num2
     print(ans)
     
if  func == "–":
    ans=num1-num2
    print(ans)    