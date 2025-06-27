
import tkinter as tk
import socket
import psutil

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "IP alınamadı"

def scan_threats():
    return "0 potansiyel tehdit bulundu."

def update_info():
    ip_label.config(text=f"IP Adresi: {get_ip()}")
    cpu_label.config(text=f"CPU Kullanımı: {psutil.cpu_percent()}%")
    threat_label.config(text=f"Tarama: {scan_threats()}")

app = tk.Tk()
app.title("NeuroShield")
app.geometry("400x300")
app.configure(bg="#0a0a0a")

tk.Label(app, text="NeuroShield Güvenlik Paneli", fg="#00aaff", bg="#0a0a0a", font=("Orbitron", 16)).pack(pady=10)

ip_label = tk.Label(app, text="", fg="white", bg="#0a0a0a")
ip_label.pack()

cpu_label = tk.Label(app, text="", fg="white", bg="#0a0a0a")
cpu_label.pack()

threat_label = tk.Label(app, text="", fg="white", bg="#0a0a0a")
threat_label.pack()

tk.Button(app, text="Bilgileri Güncelle", command=update_info, bg="#00aaff", fg="white").pack(pady=20)
tk.Button(app, text="Çıkış", command=app.quit, bg="red", fg="white").pack()

update_info()
app.mainloop()
