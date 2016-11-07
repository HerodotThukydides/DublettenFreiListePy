# -*- coding: utf-8 -*-




# Aufgabe: Dublettenfreie Liste erzeugen. -> 3 Möglichkeiten

seq = "abc123abd2345"

print

#### Version 1 -> "Pythonesk"

print "Pythonesk ->"
print "Version 1:", sorted( set( "abc123abd2345" ) ) 
print

#### Version 2 -> "zu Fuß"

dfl = []

for i in "abc123abd2345":
	# wenn ein Element noch nicht drin ist, dann fügen wir es ein
	if i not in dfl:
		dfl.append(i)
	
print "zu Fuß ->"
print "Version 2:", sorted(dfl)
print


#### Version 3 -> als Funktion

def gen_dfl(seq):
	dfl_2 = []
	for i in seq:
		# wenn ein Element noch nicht drin ist, dann fügen wir es ein
		if i not in dfl_2:
			dfl_2.append(i)
	return dfl_2


print "mit einer Funktion ->"
## nicht vergessen: sorted() schreiben! 
print "Version 3:", sorted(gen_dfl(seq))
print

