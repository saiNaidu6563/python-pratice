#program for names of weeks and its nature
# w=input("enter a week day:")
# match(w.upper()):
#     case "MONDAY" :
#         print("{} it is a working day".format(w))
#     case "TUESDAY":
#         print("{} it is a working day".format(w))
#     case "WEDNESDAY":
#         print("{} it is a working day".format(w))
#     case "THURSDAY":
#         print("{} it is a working day".format(w))
#     case "FRIDAY":
#         print("{} it is a working day".format(w))
#     case "SATURDAY":
#         print("{} it is a weekend".format(w))
#     case "SUNDAY":
#         print("{} it is a  Holyday".format(w))
#     case _:
#         print("{} not a week day".format(w))
#procees 2:

# w=input("enter a week day:")
# match(w.upper()):
#     case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
#         print("{} is a working day".format(w))
#     case "SATURDAY":
#         print("{} it is a weekend".format(w))
#     case "SUNDAY":
#             print("{} it is a  Holyday".format(w))
#     case _:
#             print("{} not a week day".format(w))

#process 3:

w=input("enter a week day:")
if w.upper() in ["MONDAY" , "TUESDAY" , "WEDNESDAY" , "THURSDAY" , "FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THUR","FRI","SAT","SUN"]:
    match (w.upper()):
        case "MON" | "TUE" | "WEDNE" | "THURS" | "FRI":
            print("{} is a working day".format(w))
        case "SAT":
            print("{} it is a weekend".format(w))
        case "SUN":
            print("{} it is a  Holyday".format(w))
        case _:
            print("{} not a week day".format(w))