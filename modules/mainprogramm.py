from mainmenu import menu
from circle import area as ac,peri as ap
from square import area as sa,peri as sp
from rectangle import  area as arr ,peri as pr
from triangle import  area as ta,peri as tp
while(True):
    menu()
    ch=input("enter  ur choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                ac()
                ap()
            case 2:
                sa()
                sp()
            case 3:
                arr()
                pr()
            case 4:
                ta()
                tp()
            case 5:
                print("thx for using program")
                break
            case _:
                print("u r option is wrong-->try agian:")
    else:
        print("don't enter alnum,symbols-->try again")

