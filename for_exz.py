from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
from tkinter import messagebox


root = Tk()




# Загрузите изображение для анализа  28
#



# ТУТ Я ПРОБУЮ ВЫВЕСТИ СООБЩЕНИЕ О СРАВНЕВАНИИ СООБЩЕНИЙ


def open_img():
    x = openfilename()



def openfilename():
    filename = filedialog.askopenfilename(title='Выбор изображения')
    return filename



# def save_canny():
#     # file = filedialog.asksaveasfilename(title = u'save file ', filetypes = files, defaultextension=files)
#     if img_canny != '':
#         files = [('JPEG files', '*.jpeg'),
#                  ('PNG Files', '*.png'),
#                  ('Python Files', '*.py')]
#         cv2.imwrite(filedialog.asksaveasfilename(title=u'save file ', filetypes=files, defaultextension=files),
#                     img_canny)
#         messagebox.showinfo(title="Информация", message="Изображение сохранено")
#
#     else:
#         messagebox.showerror(title="Ошибка", message="Необходимо выбрать изображение")
#


root.title("Contour search")
root.geometry("1000x750")
root.resizable()
root.resizable(width=True, height=True)
root.option_add("*tearOff", FALSE)

main_menu = Menu()
file_menu = Menu()
setings_menu = Menu()





root.config(menu=main_menu)


root.mainloop()

