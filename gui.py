import tkinter as tk
from tkinter import ttk, messagebox

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
    harf = combo_not.get()

    if not ad or not kredi or not harf:
        messagebox.showerror("Hata", "Tüm alanları doldur")
        return

    if not kredi.isdigit():
        messagebox.showerror("Hata", "Kredi sayı olmalı")
        return

    puan = harf_notu_to_puan(harf)

    dersler.append({
        "ad": ad,
        "kredi": int(kredi),
        "puan": puan
    })

    listbox.insert("", tk.END, values=(ad, kredi, harf))

    entry_ad.delete(0, tk.END)
    entry_kredi.delete(0, tk.END)
    combo_not.set("")


def ders_sil():
    selected = listbox.selection()
    if selected:
        index = listbox.index(selected)
        listbox.delete(selected)
        dersler.pop(index)


def gpa_hesapla():
    if not dersler:
        messagebox.showerror("Hata", "Ders ekle")
        return

    toplam_puan = sum(d["kredi"] * d["puan"] for d in dersler)
    toplam_kredi = sum(d["kredi"] for d in dersler)

    gpa = toplam_puan / toplam_kredi
    label_gpa.config(text=f"GPA: {gpa:.2f}")


def hedef_hesapla():
    if not dersler:
        messagebox.showerror("Hata", "Önce ders ekle")
        return

    hedef = entry_hedef.get()
    kalan = entry_kalan.get()

    if not hedef or not kalan:
        messagebox.showerror("Hata", "Hedef ve kredi gir")
        return

    try:
        hedef = float(hedef)
        kalan = int(kalan)
    except:
        messagebox.showerror("Hata", "Geçersiz değer")
        return

    mevcut_puan = sum(d["kredi"] * d["puan"] for d in dersler)
    mevcut_kredi = sum(d["kredi"] for d in dersler)

    gerekli_toplam = hedef * (mevcut_kredi + kalan)
    gereken = gerekli_toplam - mevcut_puan

    gerekli_ortalama = gereken / kalan

    label_hedef.config(text=f"Gerekli Ortalama: {gerekli_ortalama:.2f}")


# GUI
root = tk.Tk()
root.title("GPA Calculator")
root.geometry("500x550")

style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

# Giriş alanları
ttk.Label(frame, text="Ders Adı").pack()
entry_ad = ttk.Entry(frame)
entry_ad.pack(pady=5)

ttk.Label(frame, text="Kredi").pack()
entry_kredi = ttk.Entry(frame)
entry_kredi.pack(pady=5)

ttk.Label(frame, text="Harf Notu").pack()
combo_not = ttk.Combobox(frame, values=["AA","BA","BB","CB","CC","DC","DD","FD","FF"])
combo_not.pack(pady=5)

ttk.Button(frame, text="Ders Ekle", command=ders_ekle).pack(pady=5)

# Liste (tablo gibi)
columns = ("Ders", "Kredi", "Not")
listbox = ttk.Treeview(frame, columns=columns, show="headings", height=6)
for col in columns:
    listbox.heading(col, text=col)
listbox.pack(pady=10)

ttk.Button(frame, text="Seçili Dersi Sil", command=ders_sil).pack(pady=5)

# GPA
ttk.Button(frame, text="GPA Hesapla", command=gpa_hesapla).pack(pady=5)
label_gpa = ttk.Label(frame, text="GPA: ")
label_gpa.pack(pady=5)

# Hedef GPA
ttk.Label(frame, text="Hedef GPA").pack()
entry_hedef = ttk.Entry(frame)
entry_hedef.pack(pady=5)

ttk.Label(frame, text="Kalan Kredi").pack()
entry_kalan = ttk.Entry(frame)
entry_kalan.pack(pady=5)

ttk.Button(frame, text="Hedef Hesapla", command=hedef_hesapla).pack(pady=5)
label_hedef = ttk.Label(frame, text="Gerekli Ortalama: ")
label_hedef.pack(pady=10)

root.mainloop()
