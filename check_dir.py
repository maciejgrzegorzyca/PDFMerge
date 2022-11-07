import tkinter as tk
window = tk.Tk()
window.title("PDFMerge")
window.geometry("300x200")

inputtxt = tk.Text(window, height=5, width=20)
inputtxt.pack()

# import os
#
# def dir_check_r():                        #funkcja sprawdzajaca poprawnosc wpisanej sciezki do odczytu
#     dir_from = input("Podaj sciezke z plikami pdf do scalenia: ")
#     print(dir_from)
#     isOk = os.path.exists(dir_from)
#     print(isOk)
#     while isOk == False:
#         dir_from = input("Sciezka niewlasciwa. Podaj sciezke z plikami pdf do scalenia: ")
#         print(dir_from)
#         isOk = os.path.exists(dir_from)
#     else:
#         print("Sciezka ok")
#         pass


# def dir_check_w():                        #funkcja sprawdzajaca poprawnosc wpisanej sciezki do zapisu
#     dir_to = input("Podaj sciezke do zapisu: ")
#     print(dir_to)
#     isOk = os.path.exists(dir_to)
#     print(isOk)
#     while isOk == False:
#         dir_to = input("Sciezka niewlasciwa. Podaj sciezke do zapisu: ")
#         print(dir_to)
#         isOk = os.path.exists(dir_to)
#     else:
#         print("Sciezka ok")
#         pass
# dir_check_r()

# dir_check_w()

window.mainloop()