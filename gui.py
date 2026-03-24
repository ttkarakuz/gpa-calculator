import tkinter as tk
from tkinter import messagebox

dersler = []

def harf_notu_to_puan(harf):
    mapping = {
        "AA": 4.0, "BA": 3.5, "BB": 3.0,
        "CB": 2.5, "CC": 2.0, "DC": 1.5,
        "DD": 1.0, "FD": 0.5, "FF": 0.0
    }
    return mapping.get(harf.upper(), -1)


def ders_ekle():
    ad = entry_ad.get()
    kredi = entry_kredi.get()
    harf = entry_harf.get()

    if not ad or not kredi or not harf:
        messagebox.showerror("Hata", "Tüm alanları doldur")
        return

    puan = harf_notu_to_puan(harf)

    if puan == -1:
        messagebox.showerror("Hata", "Geçersiz harf notu")
        return

    dersler.append({
        "ad": ad,
        "kredi": int(kredi),
        "puan": puan
    })

    listbox.insert(tk.END, f"{ad} - {kredi} kredi - {harf}")

    entry_ad.delete(0, tk.END)
    entry_kredi.delete(0, tk.END)
    entry_harf.delete(0, tk.END)


def gpa_hesapla():
    if not dersler:
        messagebox.showerror("Hata", "Ders ekle")
        return

    toplam_puan = sum(d["kredi"] * d["puan"] for d in dersler)
    toplam_kredi = sum(d["kredi"] for d in dersler)

    gpa = toplam_puan / toplam_kredi
    label_sonuc.config(text=f"GPA: {gpa:.2f}")


# GUI
root = tk.Tk()
root.title("GPA Calculator")

tk.Label(root, text="Ders Adı").pack()
entry_ad = tk.Entry(root)
entry_ad.pack()

tk.Label(root, text="Kredi").pack()
entry_kredi = tk.Entry(root)
entry_kredi.pack()

tk.Label(root, text="Harf Notu (AA, BB...)").pack()
entry_harf = tk.Entry(root)
entry_harf.pack()

tk.Button(root, text="Ders Ekle", command=ders_ekle).pack(pady=5)
tk.Button(root, text="GPA Hesapla", command=gpa_hesapla).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack()

label_sonuc = tk.Label(root, text="GPA: ")
label_sonuc.pack(pady=10)

root.mainloop()
