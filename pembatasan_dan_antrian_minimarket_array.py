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
arr_kapasitas_sekarang = [] 
arr_pmt_orang_masuk = []
arr_orang_masuk = []
arr_antrian = []
arr_total_orang = []
arr_orang_keluar = []

for i in range(1,kapasitas_sekarang + 1) :
   arr_kapasitas_sekarang.append(i) 

while True:
   arr_pmt_orang_masuk = [] 
   if count >= 1 :
      pmt_orang_masuk = int(input("Berapa lagi orang yang ingin masuk ? [enter untuk 0] : ")or "0") # deafult 0
      
   else:
      pmt_orang_masuk = int(input("Berapa orang yang ingin masuk ? [enter untuk 0] : ")or "0") #default 0

   if len(arr_antrian) > 0 : 
      for i in range ( total_orang + 1, total_orang + pmt_orang_masuk + 1) : # increment dri nomor antrian terakhir
         arr_pmt_orang_masuk.append(i)
   else :                     
      for i in range (arr_kapasitas_sekarang[-1] + 1, arr_kapasitas_sekarang[-1] + pmt_orang_masuk + 1) : # increment dari nomor kapasitas terakhir
         arr_pmt_orang_masuk.append(i) 

   clearTerminal()
   #print("count :" , count)
   
   total_orang = kapasitas_sekarang + pmt_orang_masuk + antrian 
   arr_total_orang = arr_kapasitas_sekarang  + arr_antrian + arr_pmt_orang_masuk 
   
   if total_orang >= batas and len(arr_total_orang) >= batas:
      
      selisih_batas = total_orang - batas   
      antrian = selisih_batas # yang harus antri

      if(antrian <= 0) : # kalo antrian 0 arr_antrian pun []
         arr_antrian = [] 
      else :
         arr_antrian = arr_total_orang[-antrian:] # ambil indeks dri belakang sesuai selisih
      
      if kapasitas_sekarang < batas and len(arr_kapasitas_sekarang) < batas : 
         
         orang_masuk =  abs(antrian - pmt_orang_masuk) # abs = absolut | menghilangkan tanda minus,angkanya positif terus
         arr_orang_masuk = arr_pmt_orang_masuk[:orang_masuk] 

         print(f"\n  - Total semua orang, [{total_orang}] orang") 
         print(f"    - Siapa saja : {arr_total_orang}") 
         print(f"\n  - Antrian [{antrian}] orang") 
         print(f"    - Siapa saja : {arr_antrian}") 
         print(f"\n  - Yang boleh masuk [{orang_masuk}] orang") 
         print(f"    - Siapa saja : {arr_orang_masuk}") 
         print(f"\n  - Kapasitas minimarket saat ini [{kapasitas_sekarang}] orang")
         print(f"    - Siapa saja : {arr_kapasitas_sekarang}") 
         print(drawLine("="))
         

         kapasitas_sekarang += orang_masuk # total-kan kapasitas dengan orang yang boleh masuk
         arr_kapasitas_sekarang.extend(arr_orang_masuk) # masuk-kan arr_orang_masuk
      
      else :
         
         if total_orang != batas and len(arr_total_orang) != batas:
            print(f"\n  - Total semua orang, [{total_orang}] orang") 
            print(f"    - Siapa saja : {arr_total_orang}") 
         
         print(f"\n  - Antrian [{antrian}] orang") 
         print(f"    - Siapa saja : {arr_antrian}") 
         print(f"\n  - Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang")
         print(f"    - Siapa saja : {arr_kapasitas_sekarang}") 
         print(drawLine("="))
         
         pmt_selesai = input("\nKapasitas penuh, apakah sudah ada yang selesai belanja ? [y/n] ")
         if pmt_selesai.lower() == 'y':
            pmt_orang_keluar = int(input("Berapa orang ? : ")) # 1 
            clearTerminal()

            if pmt_orang_keluar > 0 :

               # tampilkan yang keluar
               arr_orang_keluar = arr_kapasitas_sekarang[:pmt_orang_keluar]

               # update kapasitas lagi karena ada yang keluar
               kapasitas_sekarang = kapasitas_sekarang - pmt_orang_keluar 
               arr_kapasitas_sekarang = arr_kapasitas_sekarang[pmt_orang_keluar:] 
               
               
               # update total orangnya 
               total_orang = kapasitas_sekarang + antrian   
               arr_total_orang = arr_kapasitas_sekarang + arr_antrian 

               #cari selisihnya 
               selisih_batas = total_orang - batas 
               
               # karena selisih gaboleh minus, jadi di fix ke 0 
               if(selisih_batas < 0 ) :
                  selisih_batas = 0
               
               # update orang yang bisa masuk
               orang_masuk = antrian - selisih_batas
               if orang_masuk <=0 :
                  # kosongkan, karena ngambil array tidak bisa dengan value selisih = 0
                  arr_orang_masuk = [] 
               else :
                  arr_orang_masuk = arr_antrian[:orang_masuk] # ambil indeks dari depan sesuai nilai selisih
               
               # update antrian
               antrian = selisih_batas
               if antrian <= 0 : # kalo antrian 0 arr_antrian pun []
                  arr_antrian = [] 
               else:
                  arr_antrian = arr_antrian[antrian:] # ambil indeks terakhir sesuai nilai selisih

               
               # update kapasitas sekarang dan masukan orang antri yang bisa masuk
               kapasitas_sekarang = kapasitas_sekarang + orang_masuk 
               arr_kapasitas_sekarang.extend(arr_orang_masuk) 

               #update lagi total orangnya
               total_orang = kapasitas_sekarang + antrian 
               arr_total_orang = arr_kapasitas_sekarang + arr_antrian 


               print(f"\n  - Total semua orang [{total_orang}] orang")
               print(f"    - Siapa saja : {arr_total_orang}\n")
               print(f"\n  - Antrian [{antrian}] orang") 
               print(f"    - Siapa saja {arr_antrian}")  
               print(f"\n  - Antrian masuk [{orang_masuk}] orang") 
               print(f"    - Siapa saja {arr_orang_masuk}") 
               print(f"\n  - Orang yang keluar {arr_orang_keluar}") 
               print(f"\n  - Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang") 
               print(f"    - Siapa saja : {arr_kapasitas_sekarang}") 
               print(drawLine("="))
               
            orang_masuk = 0 #reset orang masuk
            arr_orang_masuk = [] # reset arr_orang_masuk 
            
      count =+ 1         
   else: 
        
      kapasitas_sekarang = kapasitas_sekarang + pmt_orang_masuk # update kapasitas
      arr_kapasitas_sekarang.extend(arr_pmt_orang_masuk)

      print(f"  - Orang yang masuk : {arr_pmt_orang_masuk}")
      print(f"  - Orang yang keluar : {arr_orang_keluar}") 
      print(drawLine("="))
      print(f"Kapasitas Minimarket Saat ini [{kapasitas_sekarang}] orang kurang dari batas")
      print(f"Daftar Kapasitas : {arr_kapasitas_sekarang}")
      print(drawLine("="))

      total_orang = kapasitas_sekarang # update total
      arr_total_orang = arr_kapasitas_sekarang

      pmt_selesai = input("\napakah sudah ada yang selesai belanja ? [y/n] ")
      if (pmt_selesai.lower() == 'y'):
         pmt_orang_keluar = int(input("Berapa orang ? : "))
         print(drawLine("="))
         if pmt_orang_keluar > 0 :

            try : # karena tidak di definisikan di atas jadi pakai try
               arr_orang_keluar = arr_kapasitas_sekarang[:pmt_orang_keluar]  #tampilkan orang keluar
            except :
               pass

            kapasitas_sekarang = kapasitas_sekarang - pmt_orang_keluar # update kapasitas lagi
            arr_kapasitas_sekarang = arr_kapasitas_sekarang[pmt_orang_keluar:]

            total_orang = kapasitas_sekarang # update total lagi
            arr_total_orang = arr_kapasitas_sekarang

            pmt_orang_keluar = 0 # reset orang yang keluar  

      if kapasitas_sekarang == 3 :
         print(drawLine("="))
         print(f"Sepertinya tersisa pegawai saja {kapasitas_sekarang} orang")
         break   
      elif kapasitas_sekarang < 0 :
         print(drawLine("="))
         print(f"Sepertinya Anda keliru")
         print(f"Bye !")
         break