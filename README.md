# labpy03

## LATIHAN 1 : Program mencetak n bilangan acak kurang dari 0.5


````
Penjelasan program :

- Input bilanga n
- masukan perulangan for i in range(n)
- inputkan a=random.uniform(0.0 , 0.5) untuk menghitung bilangan agar hasilnya <0.5
- print data ke :"i" => , a untuk menampilkan string saat n runtime
- masukkan bilangan n untuk menentukan tampilan 
````
**berikut ini program lengkapnya :**
````
# mencari nilai n bilangan acak < 0.5 dengan fungsi random
print()
print("=================================================")
print("Program menampilkan bilangan acak kurang dari 0.5")
print("=================================================")
print()

import random

print ("bilangan random antara 0 <= n < 0.5 :")
random.random()

import random

n = int(input("Masukan nilai N : "))
for i in range(n) :
    a=random.uniform(0.0,0.5)
    print ("Data ke : ", i, "=> ", a)
````
**hasil program :**

![img]https://raw.githubusercontent.com/RAIS14/labpy03/master/hasil_latihan1.png

### LATIHAN 2 : Program menampilkan bilangan terbesar saat angka 0 diinputkan

````
**penjelasan program :**
- deklarasikan n=1 , max=0
- masukan perulangan dengan while n!=0
- inputkan if n>max untuk menentukan nilai n lebih besar dari max ,maka cetak n
- inputkan if n==0 :  break => untuk berhentikan program saat diinputkan angka nol
- print(max) => untuk menampilkan bilangan terbesar 
````
**berikut program lengkapnya :**
````
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
````
**hasil program latihan 2 :**

![img]https://raw.githubusercontent.com/RAIS14/labpy03/master/hasil_latihan2.png

#### Program1 : Menghitung jumlah total laba selama 8 bulan

````
**penjelasan program :**
- deklarasikan n=25 juta , sum=0 , y=0
- inputkan rumus laba=[int(0),int(0), int(n)*0.01, int(n)*0.01, int(n)*0.05, int(n)*0.05, int(n)*0.05, int(n)*0.03]
ini untuk menghitung persentase laba =
25000000 x laba=[int(0)= 0 ,untuk bulan pertama dan kedua
25000000 x laba=[int(n)*0.01= 250.000 untuk bulan ketiga-keempat
25000000 x laba=[int(n)*0.05= 1.250.000 utk buln kelima-ketujuh
25000000 x laba=[int(n)*0.03= 750.000 utk bulan kedelapan
- inputkan rumus perulangan
for i in laba : , sum=sum+1 , y+=1   untuk menampilkan perulangan saat runtime
- print(i) untuk laba bulan ke :"i"
- print(sum) untuk total laba selama 8 bulan
````
**berikut program lengkapnya :**
````
print()
print("+++++++++++++++++++++++++++++++++++++++++++++")
print("Program menghitung jumlah total laba selama 8 bulan")
print("+++++++++++++++++++++++++++++++++++++++++++++")
print()

n=25000000
sum=0
y=0

laba= [int(0), int(0), int(n) * 0.01, int(n) * 0.01, int(n) * 0.05, int(n) * 0.05, int(n) * 0.05, int(n) * 0.03]
print('Modal Pertama seorang pengusaha properti       :',n)
print()

for i in laba :
    sum=sum+i
    y+=1
    print('Laba bulan ke-', y ,'sebesar            :', i)

print()
print('Total laba yang didapat adalah   :', sum)
````
**hasil program :**

![img]https://raw.githubusercontent.com/RAIS14/labpy03/master/hasil_program1.png
