# program mencari bilangan terbesar setelah berhenti jika diinputkan angka 0
print("============================================================")
print("Program mencetak bilangan terbesar saat angka nol diinputkan")
print("============================================================")
print()

n=1
max=0

while n!=0 :
    if n>max :
        max=n
    n=int(input('Masukkan bilangan :'))
    if n==0 :
         break
print()        
print ('Nilai terbesarya adalah :',max)