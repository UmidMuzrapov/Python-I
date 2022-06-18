outer_width=int(input("USS Arizona outer width:\n"))
inner_width=int(input("USS Arizona inner width:\n"))
height=int(input("USS Arizona tower height:\n"))
height_2=int((outer_width + inner_width) / 7)
for i in range (0, height_2):
    print(21*" "+outer_width*" " +"|"+2*inner_width*" "+"|"+21*" "+outer_width*" ")
print(18*" "+outer_width*" "+"|##$"+2*inner_width*" "+"$##|"+18*" "+outer_width*" ")
for i in range (0,height):
    print(19*" "+outer_width*" "+"##"+" "+2*inner_width*" "+" ##"+19*" "+outer_width*" ")
print(18*" "+outer_width*" "+"#..#"+2*inner_width*" "+"#..#"+18*" ")
print("           "+outer_width*" "+"\----. #..#"+2*inner_width*"."+"#..# .----/")
print(outer_width*" "+"     \ ***|_|    |#..#"+inner_width*"-#"+"#..#|    |_|*** /")
print(".____"+outer_width*"_"+"_|____          _"+2*inner_width*"."+"_          ____|_"+outer_width*"_"+"..")
print("`---."+outer_width*" "+"                      "+2*inner_width*" "+"             "+outer_width*" "+"--\.")
print(" <<#\\"+outer_width*"_"+ 17*"_"+2*inner_width*"_"+18*"_"+outer_width*"_"+'____\\')

