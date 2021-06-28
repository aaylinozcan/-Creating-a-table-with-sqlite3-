import sqlite3
from tkinter import messagebox as tkMessageBox
from tkinter import *

def ÖğrenciEkleme():
    ogrenciler.insert(END, ogrNo.get() + ' ' + ogrAd.get() + ' ' + ogrSoyad.get())
    baglanti.execute("INSERT INTO Ogrenciler VALUES(?,?,?)",
                     [ogrNo.get(), ogrAd.get(), ogrSoyad.get()]) 
    baglanti.commit()

def ÖğrenciSilme():
    if tkMessageBox.askyesno("DİKKAT!", "Seçilen veriyi silmek istediğinize emin misiniz?"):
        for i in range(ogrenciler.size()):
            if ogrenciler.select_includes(i):
                baglanti.execute("DELETE FROM Ogrenciler WHERE OgrNo=?",
                                 [ogrenciler.get(i).split(' ')[0]])
                baglanti.commit()
                ogrenciler.delete(i)

def DersEkleme():
    dersler.insert(END, inputDersKod.get() + ' ' + inputDersAd.get())
    baglanti.execute("INSERT INTO Dersler VALUES(?,?)",
                     [inputDersKod.get(), inputDersAd.get()])
    baglanti.commit()

def DersSilme():
    if tkMessageBox.askyesno("DİKKAT!", "Seçilen veriyi silmek istediğinize emin misiniz?"):
        for i in range(dersler.size()):
            if dersler.select_includes(i):
                baglanti.execute("DELETE FROM Dersler WHERE DersKodu=?",
                                 [dersler.get(i).split(' ')[0]])
                baglanti.commit()
                dersler.delete(i)      
                    
def NotEkleme():
    if ogrenciler.curselection() and dersler.curselection():
        ÖğrenciNo = ogrenciler.get(ACTIVE).split()[0]
        DersKodu = dersler.get(ACTIVE).split()[0]
        notlar.insert(END, ÖğrenciNo + ' ' + DersKodu + ' ' + vizeNot.get() + ' ' + finalNot.get())
        baglanti.execute("INSERT INTO Notlar VALUES(?,?,?,?)",
                         [ÖğrenciNo, DersKodu, vizeNot.get(), finalNot.get()])
        baglanti.commit()
    else:
        tkMessageBox.showwarning("HATA","Öğrenci ve Ders seçmelisiniz!")

def NotSilme():
    if tkMessageBox.askyesno("DİKKAT!", "Seçilen veriyi silmek istediğinize emin misiniz?"):
        for i in range(notlar.size()):
            if notlar.select_includes(i):
                baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=?",
                                 [notlar.get(i).split(' ')[0], notlar.get(i).split(' ')[1]])
                baglanti.commit()
                notlar.delete(i)


pencere = Tk()

solFrame = Frame(highlightthickness=6, bd=6, relief=RAISED)
solFrame.grid(row=0, column=0)
ortaFrame = Frame(highlightthickness=6, bd=6, relief=RAISED)
ortaFrame.grid(row=0, column=1)
sağFrame = Frame(highlightthickness=6, bd=6, relief=RAISED)
sağFrame.grid(row=0, column=2)

# frame öğrenciler 

lblOgrenciler = Label(solFrame, text="ÖĞRENCİLER", font="Calibri 24")
lblOgrenciler.grid(row=0, column=0, columnspan=2)

ogrenciler = Listbox(solFrame, font="Calibri", selectmode="extended", width=30, exportselection=0)
ogrenciler.grid(row=5, column=0, columnspan=2)

lblAd = Label(solFrame, text="Öğrenci Adı :", font="Calibri", width=13, anchor='e')
lblAd.grid(row=1, column=0)
ogrAd = Entry(solFrame, font="Calibri")
ogrAd.grid(row=1, column=1)

lblSoyad = Label(solFrame, text="Öğrenci Soyadı :", font="Calibri", width=13, anchor="e")
lblSoyad.grid(row=2, column=0)
ogrSoyad = Entry(solFrame, font="Calibri")
ogrSoyad.grid(row=2, column=1)

lblNo = Label(solFrame, text="Öğrenci No :",font="Calibri", width=13, anchor="e")
lblNo.grid(row=3, column=0)
ogrNo = Entry(solFrame, font="Calibri")
ogrNo.grid(row=3, column=1)

buttonEkle1 = Button(solFrame, text="EKLE", font="Calibri", command=ÖğrenciEkleme)
buttonEkle1.grid(row=4, column=0, columnspan=2)

buttonSil1 = Button(solFrame, text="Seçilen veriyi sil", font="Calibri", command=ÖğrenciSilme)
buttonSil1.grid(row=6, column=0, columnspan=2)

# frame dersler

lblDersler = Label(ortaFrame, text="DERSLER", font="Calibri 24")
lblDersler.grid(row=0, column=0, columnspan=2, pady=15)

dersler = Listbox(ortaFrame, font="Calibri", selectmode="extended", width=30, exportselection=0)
dersler.grid(row=4, column=0, columnspan=2)

lblDersKod = Label(ortaFrame, text="Ders Kodu :", font="Calibri", width=12, anchor="e")
lblDersKod.grid(row=1, column=0)
inputDersKod = Entry(ortaFrame, font="Calibri")
inputDersKod.grid(row=1, column=1)

lblDersAd = Label(ortaFrame, text="Ders Adı :", font="Calibri", width=12, anchor="e")
lblDersAd.grid(row=2, column=0)
inputDersAd = Entry(ortaFrame, font="Calibri")
inputDersAd.grid(row=2, column=1)

buttonEkle2 = Button(ortaFrame, text="EKLE", font="Calibri", command=DersEkleme)
buttonEkle2.grid(row=3, column=0, columnspan=2)

buttonSil2 = Button(ortaFrame, text="Seçilen veriyi sil", font="Calibri", command=DersSilme)
buttonSil2.grid(row=5, column=0, columnspan=2)

# frame notlar

lblNotlar = Label(sağFrame, text="NOTLAR", font="Calibri 24")
lblNotlar.grid(row=0, column=0, columnspan=2, pady=15)

notlar = Listbox(sağFrame, font="Calibri", selectmode="extended", width=30, exportselection=0)
notlar.grid(row=4, column=0, columnspan=2)

lblVize = Label(sağFrame, text="Vize Notu :", font="Calibri", width=10, anchor="e")
lblVize.grid(row=1, column=0)
vizeNot = Entry(sağFrame, font="Calibri")
vizeNot.grid(row=1, column=1)

lblFinal = Label(sağFrame, text="Final Notu :", font="Calibri", width=10, anchor="e")
lblFinal.grid(row=2, column=0)
finalNot = Entry(sağFrame, font="Calibri")
finalNot.grid(row=2, column=1)

buttonEkle3 = Button(sağFrame, text="EKLE", font="Calibri", command=NotEkleme)
buttonEkle3.grid(row=3, column=0, columnspan=2)

buttonSil3 = Button(sağFrame, text="Seçilen veriyi sil", font="Calibri", command=NotSilme)
buttonSil3.grid(row=5, column=0, columnspan=2)


baglanti =sqlite3.connect("data.db")

baglanti.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(OgrNo, Ad, Soyad)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Dersler(DersKodu, DersAdı)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Notlar(OgrNo DersKodu, Vize, Final)")

for kayıt in baglanti.execute("SELECT * from Ogrenciler"):
    ogrenciler.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2])

for kayıt in baglanti.execute("SELECT * from Dersler"):
    dersler.insert(END, kayıt[0] + ' ' + kayıt[1])

for kayıt in baglanti.execute("SELECT * from Notlar"):
    notlar.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2] + ' ' + kayıt[3])

pencere.mainloop()