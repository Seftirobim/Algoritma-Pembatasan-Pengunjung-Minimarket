import math
import os

def clearTerminal() :

   if os.name == "nt" :
      return os.system("cls")
   elif os.name == "posix" or os.name == "macOS" :
      return os.system("clear")

def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

maks_kapasitas = 50
# dibulatkan ke atas
batas = math.ceil(maks_kapasitas * (75/100))
print(f"Pembatasan kapasitas minimarket 75% dari total kapasitas 50 orang")
print(drawLine("-"))
print(f"Batas minimarket : {batas} orang")
print(f"Total kapasitas minimarket : {maks_kapasitas} orang")
print(drawLine("-"))


antrian = 0
orang_masuk = 0
count = 0

kapasitas_sekarang = int(input("Berapa orang di minimarket sekarang ? : "))
if kapasitas_sekarang > 38 :
   print("Kapasitas pertama kali tidak boleh lebih dari batas")
   exit() 
while True:
   
   if count >= 1 :
      pmt_orang_masuk = int(input("Berapa lagi orang yang ingin masuk ? [enter untuk 0] : ")or "0") # deafult 0
   else:
      pmt_orang_masuk = int(input("Berapa orang yang ingin masuk ? [enter untuk 0] : ")or "0") #default 0

   clearTerminal()

   total_orang = kapasitas_sekarang + pmt_orang_masuk + antrian 
   
   if total_orang >= batas: 
      
      selisih_batas = total_orang - batas # cari selisihnya
      antrian = selisih_batas # yang harus antri
      
      if kapasitas_sekarang < batas : 
         
         orang_masuk =  abs(antrian - pmt_orang_masuk) # abs = absolut | menghilangkan tanda minus,angkanya positif terus

         print(f"\n  - Total semua orang, [{total_orang}] orang") 
         print(f"\n  - Antrian [{antrian}] orang") 
         print(f"\n  - Yang boleh masuk [{orang_masuk}] orang") 
         print(f"\n  - Kapasitas minimarket saat ini [{kapasitas_sekarang}] orang")
         print(drawLine("="))

         kapasitas_sekarang += orang_masuk # total-kan kapasitas dengan orang yang boleh masuk
      
      else :
        
         if total_orang != batas :
            print(f"\n  - Total semua orang, [{total_orang}] orang")
         
         print(f"\n  - Antrian [{antrian}] orang") 
         print(f"\n  - Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang")
         print(drawLine("="))

         pmt_selesai = input("\nKapasitas penuh, apakah sudah ada yang selesai belanja ? [y/n] ")
         if pmt_selesai.lower() == 'y':
            pmt_orang_keluar = int(input("Berapa orang ? : "))
            clearTerminal()

            if pmt_orang_keluar > 0 :
               # cek kapasitas lagi karena ada yang keluar
               kapasitas_sekarang = kapasitas_sekarang - pmt_orang_keluar 
               
               # update total orangnya 
               total_orang = kapasitas_sekarang + antrian        

               #cari selisihnya 
               selisih_batas = total_orang - batas
               
               # karena selisih gaboleh minus, jadi di fix ke 0 
               if(selisih_batas < 0 ) :
                  selisih_batas = 0
               
               # orang yang bisa masuk = antrian sekarang - selisih batas
               # update orang yang bisa masuk
               orang_masuk = antrian - selisih_batas
               
               # update antrian
               antrian = selisih_batas
               
               # update kapasitas sekarang dan masukan orang antri yang bisa masuk
               kapasitas_sekarang = kapasitas_sekarang + orang_masuk 

               #update lagi total orangnya
               total_orang = kapasitas_sekarang + antrian 

               print(f"\n  - Total semua orang [{total_orang}] orang")
               print(f"\n  - Antrian [{antrian}] orang")  
               print(f"\n  - Antrian masuk [{orang_masuk}] orang") 
               print(f"\n  - Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang") 
               print(drawLine("="))
             
            orang_masuk = 0 #reset orang masuk
      count =+ 1         
   
   else: # kalo pertama kali input total kurang dari batas

      kapasitas_sekarang = kapasitas_sekarang + pmt_orang_masuk # update kapasitas
      print(drawLine("="))
      print(f"Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang kurang dari batas")
      print(drawLine("="))
      
      total_orang = kapasitas_sekarang # update total

      pmt_selesai = input("\napakah sudah ada yang selesai belanja ? [y/n] ")
      if (pmt_selesai.lower() == 'y'):
         pmt_orang_keluar = int(input("Berapa orang ? : "))
         print(drawLine("="))
         if pmt_orang_keluar > 0 :
            kapasitas_sekarang = kapasitas_sekarang - pmt_orang_keluar # update kapasitas lagi
            total_orang = kapasitas_sekarang # update total

            pmt_orang_keluar = 0 # reset orang yang keluar  

      if kapasitas_sekarang == 3 :
         print(drawLine("="))
         print(f"Sepertinya tersisa pegawai saja {kapasitas_sekarang} orang")
         break
      elif kapasitas_sekarang == 0 :
         print(drawLine("="))
         print(f"Sepertinya Toko tutup")
         print(f"Bye !")
         break   
      elif kapasitas_sekarang < 0 :
         print(drawLine("="))
         print(f"Sepertinya Anda keliru")
         print(f"Bye !")
         break
