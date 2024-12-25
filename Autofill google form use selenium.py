from selenium import webdriver
import time
import tkinter as tk
import threading
from selenium.webdriver.common.by import By

def isi_form(nama, nim, recycle):
    for x in range(int(recycle)):  
        print(f"Mengisi form ke-{x + 1}")
        
        web = webdriver.Chrome()  
        web.get('https://docs.google.com/forms/d/e/1FAIpQLSdVf6DHW92lAzgTboffTNg43VLcbTKah46iafNfiXML46sfRw/viewform')
        time.sleep(0.3)

        dropdown = web.find_element(By.XPATH, '//div[@role="listbox"]')  
        dropdown.click()
        time.sleep(0.1)

        option = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/span')  
        option.click()
        time.sleep(0.1)

        inputnama = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputnama.send_keys(nama)
        time.sleep(0.1)

        inputNIM = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        inputNIM.send_keys(nim)
        time.sleep(0.1)

        skor = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[1]')
        skor.click()
        time.sleep(0.1)

        submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()
        time.sleep(0.1)

        print("Tanggapan anda telah direkam, Berhasil mengirim")    

        web.quit()

def start_thread():
    nama = entry_nama.get()  
    nim = entry_nim.get()    
    recycle = entry_recycle.get()  
    thread = threading.Thread(target=isi_form, args=(nama, nim, recycle))
    thread.start()

window = tk.Tk()
window.geometry('400x200')
window.configure(background='red')
window.title('Praktikum UTS ALPRO')

label = tk.Label(window, text='Praktikum UTS ALPRO', bg='red', fg='white')
label.pack()

label_nama = tk.Label(window, text="Nama:", bg='red', fg='white')
label_nama.pack()
entry_nama = tk.Entry(window)
entry_nama.pack()

label_nim = tk.Label(window, text="NIM:", bg='red', fg='white')
label_nim.pack()
entry_nim = tk.Entry(window)
entry_nim.pack()

label_recycle = tk.Label(window, text="Jumlah Perulangan:", bg='red', fg='white')
label_recycle.pack()
entry_recycle = tk.Entry(window)
entry_recycle.pack()

button_start = tk.Button(window, text='Start', command=start_thread)
button_start.pack(padx=100, pady=1, fill='x', expand=True)

button_exit = tk.Button(window, text='Exit', command=window.quit)
button_exit.pack(padx=100, pady=1, fill='x', expand=True)

window.mainloop()