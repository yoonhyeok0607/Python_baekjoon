str = input().split(" ")

if(int(str[0]) < int(str[1])):
    print("<")
elif(int(str[0]) > int(str[1])):
    print(">")
elif(int(str[0]) == int(str[1])):
    print("==")
