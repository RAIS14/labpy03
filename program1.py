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