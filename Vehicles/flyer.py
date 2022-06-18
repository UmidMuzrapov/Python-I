size=int(input("Wright flyer size:\n"))
number_panels=int(1.2*size)
height=(int(size/5)+1)
panel="    |"
panel_right="|    "
print("   "+number_panels*5*" "+"     #     ")
print("   "+number_panels*5*" "+"#---------#")
print("   "+number_panels*5*" "+"#---------#")
print("=="+number_panels*5*"="+13*"="+"=="+number_panels*5*"=")
for i in range (0,height):
    print(" H" + panel * number_panels + "  |  %H%  |  " + panel_right * number_panels + "H")
print(" H"+panel*number_panels+"**|**%H%**|**"+panel_right*number_panels+"H")
for i in range (0,height):
    print(" H" + panel * number_panels + "  |  %H%  |  " + panel_right * number_panels + "H")
print("=="+number_panels*5*"="+5*"="+"%H%"+5*"="+number_panels*5*"="+"==")
print("  "+5*number_panels*" "+" "+"|         |")
print("  "+5*number_panels*" "+" "+"+#########+")