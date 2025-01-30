from mainmenu import menu
import circle,square,rectangle,triangle
while(True):
    menu()
    ch=input("enter  ur choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                circle.area()
                circle.peri()
            case 2:
                square.area()
                square.peri()
            case 3:
                rectangle.area()
                rectangle.peri()
            case 4:
                triangle.area()
                triangle.peri()
            case 5:
                print("thx for using program")
                break
            case _:
                print("u r option is wrong-->try agian:")
    else:
        print("don't enter alnum,symbols-->try again")
