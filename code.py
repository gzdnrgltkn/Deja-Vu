word=input()
letters=list(word) #converted input to a list letter by letter
sett=set(letters) #removed duplicate letters in the list so I used set function
if len(sett)!=len(letters): #ı checked if the original one and removed duplicates one have same lenght or not
 print("Deja Vu")
else:
 print("Unique")
