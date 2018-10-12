import socket

while True:
    try:

        ip=input("Enter the site name you want to find ip address\n")
        addr = socket.gethostbyname(ip)
        print("Your ip address is {}\n".format(addr))
        confrim = input("Do you want to search again (y\\n)\n")
        if('n'==confrim.lower()):
                print("Thank You for staying with Debashis Gupta\n")
                break
    except Exception:
        print("Sorry !! {} site is not exist ".format(ip))
        confrim = input("Do you want to search again (y\\n)\n")
        if ('n' == confrim.lower()):
            print("Thank You for staying with deb\n")
            break