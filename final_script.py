from section_maker import *

input_section = ""

input_section = input("Which section would you like to shuffle (A, B, or C)? ")
if input_section == "A":
    sectiona.shuffle()
    print(sectiona)
elif input_section == "B":
    sectionb.shuffle()
    print(sectionb)
elif input_section == "C":
    sectionc.shuffle()
    print(sectionc)
else:
    print("You entered an invalid input!")

        
