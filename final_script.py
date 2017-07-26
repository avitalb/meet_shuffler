from section_maker import *

input_section = ""
while input != "Q":
    input_section = input("Which section would you like to shuffle (A,B,or C)? Press Q to quit: ")
    if input_section == "A":
        sectiona.shuffle()
        print(sectiona)
    elif input_section == "B":
        sectionb.shuffle()
        print(sectionb)
    elif input_section == "C":
        sectionc.shuffle()
        print(sectionc)
    elif input_section == "Q":
        break
    else:
        print("You entered an invalid input!")

        
