print("Hello World!")

a = 5

b = 10

c = "Selam"

d = 45.21

f =  'a'

print((a*b)*c, d)


print("\n", a ,"=", type(a),"\n",b ,"=", type(b),"\n",c , "=",type(c),"\n",d,"=",type(d))


# tür dönüşümü, türü değişmeden ve değiştiken sonraki hali
print('\n',d , "=",type(d))
d = int(d)
print("",d , "=",type(d))

# tek satırda birden fazla değişken atama işlemi
x, y, z = 42, 25, 1
print("\n", "x", "=", x, "\n", "y", "=", y,"\n", "z", "=", z)


# input alma ve tür dönüşüm işlemleri
#ycap = float(input("\nYari cap giriniz: "))
#pi = 22/7
#cevre = ycap * 2 * pi
#alan = pi*(ycap**2)
#print("Yarı Çap = ",ycap,"\nÇevre = ", cevre,"\nAlan = ", alan)



kurs = "Elginkan Vakfi"
okul = "Kocaeli Universitesi"
print("\n",kurs, okul,sep="-",end="|")
print("\n",kurs, okul, sep="\n")
print()
print(okul[8])
print(okul[-1])
print(okul[len(okul)-1])
