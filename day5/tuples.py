my_tuple=(1,2,3)
# my_tuple[1]=5 nie dziala
still_tuple=(4,5,6,[7,8])
still_tuple[-1].append(9)
print(still_tuple)

my_tuple=my_tuple+(4,) #(4) to oznacza intiger ale (4,) to juz jest tupe jednoelementowe zawierajace integer
print(my_tuple)


