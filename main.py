from datadiri import Datadiri
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector as mysql

root = Tk()
root.title("Tugas Praktikum 3 DPBO 2021")

# connect to database
con = MySQLdb.connect('localhost', 'root', '','dataPeserta')
c = con.cursor

# membuat fungsi submit
def submit():
    # insert into table
    c.execute("INSERT INTO dataPeserta VALUES (:no_peserta, :namalengkap, :tgl_lahir, :jk, :hobi, :goldar)",
        {
            'no_peserta': no_peserta.get(),
            'namalengkap': namalengkap.get(),
            'tgl_lahir': tgl_lahir.get(),
            'jk': jk.get(),
            'hobi': hobi.get(),
            'goldar': goldar.get()
        });
    messagebox.showinfo("Data berhasil dimasukkan!")

# membuat fungsi query
def query():
    # query database
    c.execute("SELECT * FROM dataPeserta")
    records = c.fetchall;
    print(records)

    top = Toplevel()
    top.title("Data Peserta: ")
    for record in records[0]:
        print_record += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=7, column=0)
    
# menghapus data 
def delete():
    c.execute("DELETE from dataPeserta WHERE oid=PLACEHOLDER")
    messagebox.showinfo("Data berhasil dihapus!")

def desc():
    tp = Toplevel()
    tp.title("About")
    l_apsname = Label(root, text="Pendaftaran Anggota Baru", font="Verdana 10 bold")
    l_apsname.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    l_desc = Label(root, text="Berikut format pendaftaran calon anggota baru Palang Merah Remaja Indonesia")
    l_desc.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    l_info = Label(root, text="Pembuat : Annisa Muja Ahidah(1902125")
    l_info.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

def exit():
    response = messagebox.askyesno("Yakin keluar?")
    if response == 1:
        root.destroy()

def filedialog():
    root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A file", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))


# application name
l_apsname = Label(root, text="Pendaftaran Anggota Baru", fg="blue", font="Verdana 15 bold")
l_apsname.grid(row=0, column=8, columnspan=4, padx=10, pady=10)

# deskripsi aplikasi
l_desc = Label(root, text="Berikut format pendaftaran calon anggota baru Palang Merah Remaja Indonesia")
l_desc.grid(row=1, column=8, columnspan=4, padx=10, pady=10)

# form no peserta
l_no = Label(root, text="No Peserta")
l_no.grid(row=0, column=0)
no = Entry(root, width=60)
no.grid(row=0, column=3, columnspan=4, padx=10, pady=10)
no.insert(0, "")

# form nama 
l_nama = Label(root, text="Nama Lengkap")
l_nama.grid(row=1, column=0)
nm = Entry(root, width=60)
nm.grid(row=1, column=3, columnspan=4, padx=10, pady=10)
nm.insert(0, "")

#form tanggal lahir
l_tgllahir = Label(root, text="Tanggal Lahir")
l_tgllahir.grid(row=2, column=0)
tl = Entry(root, width=60)
tl.grid(row=2, column=3, columnspan=4, pady=10)
tl.insert(0, "")

# dropdown jenis kelamin
clicked = StringVar()
clicked.set("Pria")
jk = Label(root, text="Jenis Kelamin")
jk.grid(row=3, column=0)
jk = OptionMenu(root, clicked, "Pria", "Wanita")
jk.grid(row=3, column=3, pady=10)

# Checkbox hobi
hobi = Label(root, text="Hobi")
hobi.grid(row=4, column=0)
var = StringVar()
c1 = Checkbutton(root, text="Menulis")
c1.grid(row=4, column=3)
c2 = Checkbutton(root, text="Membaca")
c2.grid(row=4, column=4)
c3 = Checkbutton(root, text="Lainnya")
c3.grid(row=4, column=5, padx=10, pady=10)

# radiobutton golongan darah
goldar = Label(root, text="Golongan Darah")
goldar.grid(row=5, column=0)
r1 = Radiobutton(root, text="A")
r1.grid(row=5, column=3)
r2 = Radiobutton(root, text="B")
r2.grid(row=5, column=4)
r3 = Radiobutton(root, text="AB")
r3.grid(row=5, column=5)
r4 = Radiobutton(root, text="O")
r4.grid(row=5, column=6, padx=10, pady=10)

# file dialog
b_file= Button(root, text="OPEN PHOTO FILE", command=filedialog, width=50)
b_file.grid(row=6, column=3, columnspan=4, padx=10, pady=10)

# SUBMIT
b_submit= Button(root, text="SUBMIT", command=submit, width=50)
b_submit.grid(row=7, column=3, columnspan=4, padx=10, pady=10)

# melihat data yang sudah disubmit
b_see= Button(root, text="SEE ALL SUBMISSONS", command=query, width=50)
b_see.grid(row=3, column=8, columnspan=4, padx=10, pady=10)

# menghapus data yang sudah disubmit
b_delete= Button(root, text="CLEAR SUBMISSONS", width=50)
b_delete.grid(row=4, column=8, columnspan=4, padx=10, pady=10)

# data tentang organisasi
b_about= Button(root, text="ABOUT", command=desc, width=50)
b_about.grid(row=5, column=8, columnspan=4, padx=10, pady=10)

# menghapus data yang sudah disubmit
b_delete= Button(root, text="EXIT", command=exit, width=50)
b_delete.grid(row=7, column=8, columnspan=4, padx=10, pady=10)

con.commit()

# close connection database
con.close()


root.mainloop()