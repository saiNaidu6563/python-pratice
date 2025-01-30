import circle,square,rectangle,triangle
from submenu  import submenu
from mainmenu import menu
while(True):
    menu()
    ch=input("enter  ur choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                while(True):
                    submenu("circle")
                    ch1=input("Enter ur choice:")
                    match(ch1.upper()):
                        case "A":
                            circle.area()
                        case "P":
                            circle.peri()
                        case "M":
                            break
                        case _:
                            print("ur option is wrong:")
            case 2:
                while(True):
                    submenu("square")
                    ch1 = input("Enter ur choice:")
                    match (ch1.upper()):
                        case "A":
                            square.area()
                        case "P":
                            square.peri()
                        case "M":
                            break
                        case _:
                            print("ur option is wrong:")

            case 3:
                while(True):
                    submenu("rectangle")
                    ch1 = input("Enter ur choice:")
                    match (ch1.upper()):
                        case "A":
                            rectangle.area()
                        case "P":
                            rectangle.peri()
                        case "M":
                            break
                        case _:
                            print("ur option is wrong:")

            case 4:
                while(True):
                    submenu("trianle")
                    ch1 = input("Enter ur choice:")
                    match (ch1.upper()):
                        case "A":
                            triangle.area()
                        case "P":
                            triangle.peri()
                        case "M":
                            break
                        case _:
                            print("ur option is wrong:")

            case 5:
                print("thx for using program")
                break
            case _:
                print("u r option is wrong-->try agian:")
    else:
        print("don't enter alnum,symbols-->try again")

