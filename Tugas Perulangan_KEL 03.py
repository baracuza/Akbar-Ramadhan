print(8*'=' ,"KASIR SEDERHANA", 8*'=','\n')
print(5*'-',"PEMBELIAN",5*'-')

x = True
totalAll = 0
while x == True :#1
   y = True
   barang = int(input("\nJUMLAH BARANG : "))
   harga = int(input("\nHARGA BARANG : Rp "))
   total = barang * harga 
   totalAll += total #2
   while y == True :
      cek = input("\nAPAKAH ADA BARANG YANG AKAN DIBELI LAGI ?\n[Y],[T]\n")
      if cek == 'y' or cek == 'Y' :
         break
      elif cek == 't' or cek == 'T':
         x = False
         break
      else:
         print("\nKODE YANG DIMASUKKAN SALAH")        
print("\nTOTAL HARGA : Rp ",totalAll)


print('\n',5*'-',"PEMBAYARAN",5*'-')
a = True
while a == True :
   b = True
   bayar = int(input("\nUANG ANDA : Rp "))
   kembalian = bayar - totalAll 
   if bayar >= totalAll :
         break
   while b == True : 
      if bayar < totalAll :
         print("\nUANG ANDA KURANG",)
         break   
print("\nKEMBALIAN = Rp ",kembalian)