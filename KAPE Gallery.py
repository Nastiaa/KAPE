# A program for Task of the "Basics of programming"
# "KAPE Gallery"  v. 1.1.2
# To Open your images you have to change the argument PathGallery and Addres
# which located on the 22 and 23 lines.
# For example: PathGallery='C:\\Users\\1\\Desktop\\фотографии\\'
#              Addres = ' "C:\\Users\\1\\Desktop\\фотографии\\" '
# Programm have been written on the Python 2.7.5 and 2.7.6
# and not tested with the Python 2.7.7 and more newer.
# This program have "Open source softwre" license.
# Thank you for using our project, we wish that you will be pleased.


import os
from Tkinter import *
import tkFileDialog
import subprocess
from PIL import Image
from PIL import ImageTk


# Paths for Gallery
PathGallery='C:\\Users\\user\\Desktop\\Программрование\\Python\\Task2\\arts\\'
Addres=' "C:\\Users\\user\\Desktop\\Программрование\\Python\Task2\\arts\\" '
PathGalleryOpen = Addres


# List of the Paths to images of the gallery
image_list = []
# List with names of images of the gallery
text_list = []
# Reset the counter of the pictures number
Current = 0


# Creating the window "About"
def About():
    """
    Данная функция создаёт новое окно About с определённым текстовым набором

    Возвращаемое значение: None
    """
    AboutWindow = Tk()
    AboutWindow.title('About')
    AboutWindow.maxsize(420,120)
    AboutWindow.minsize(420,120)
    Info = """ "KAPE Gallery"\nСоздатели: Круглова А.В.
                     Привалов Е.В.\nСтуденты группы 1652, СПбНИУ ИТМО\n
                     Программа написана на Языке программирования Python 2.7
                \n\t\t\t\tKAPE Gallery, 2014©All Rights Reserved"""
    lab = Label(AboutWindow,text=Info.decode('cp1251'))
    lab.pack() 


# Looking for images at the Gallery Path and entry their names
# and path into special lists
def OpenPicture():
    """ Данная функция находит всевозможные файлы в папке указанной заранее,
        запоминает полный адрес к найденному файлу, добавляет полные адрес и
        имя файла в соответствующие листы image_list и text_list


        Возвращаемое значение: None
    """
    global FullName
    for root, dirs, files in os.walk(PathGallery): 
        for name in files:
            FullName = os.path.join(root, name)
            image_list.append(FullName)
            text_list.append(name)


# Opening the directory of the gallery
def OpenDirectory():
    """ Данная функция открывает директорию с файлами галереи

        Возвращаемое значение: None
    """
    subprocess.Popen('explorer' + PathGalleryOpen)


# Information about image
def Configuration():
    """ Данная функция создаёт новое окно Configuration, в котором
        указан путь к файлу в текстовой форме и свойства самого файла

        Возвращаемое значение: None
    """
    OpenPicture()
    ConfigurationWindow = Tk()
    Info = 'Расположение изображения: ' + FullName
    ConfigurationWindow.maxsize(760,300)
    ConfigurationWindow.minsize(760,300)
    ConfigurationWindow.title('Configuration')
    lab = Label(ConfigurationWindow, text=Info.decode('cp1251'))
    lab.pack()


# Changing the image(forward/back)
def ChangePicture(Shift):
    """ Данная функция перебирает лист с файлами, добавленными функцией
        OpenPicture, а так же выводит информацию о названии файла на экран

    Аргументы: Shift

    Возвращаемое значение: None
    """
    OpenPicture()
    global Current, image_list
    if not (0 <= Current + Shift < len(image_list)):
        # что тут было? :D
        return
    Current += Shift
    image = Image.open(image_list[Current])
    Photo = ImageTk.PhotoImage(image)
    label['text'] = text_list[Current]
    label['image'] = Photo
    label.Photo = Photo


# Main program's body
root = Tk()
root.title('KAPE Gallery')
root.maxsize(650,560)
root.minsize(650,560)
main_menu = Menu(root)    # Crating menu
root.config(menu=main_menu)    # Add Menu to the Main Window
file_menu = Menu(main_menu)    # Creating submenu
file_menu2 = Menu(main_menu)    # Creating submenu №2
file_menu3 = Menu(main_menu)    # Creating submenu №3
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open Gallery", command=OpenDirectory)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
canvas = Canvas(root, width=600, height=600,bg='green')
main_menu.add_cascade(label="Options", menu=file_menu3)
file_menu3.add_command(label="Configuration", command=Configuration)
main_menu.add_cascade(label="Help", menu=file_menu2)
file_menu2.add_command(label="About", command=About)
label = Label(root, compound=TOP)
label.pack()
# Zone for buttons
frame = Frame(root)
frame.pack()
# Button to change the picture(back)
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Previous picture',
       command=lambda: ChangePicture(-1)).pack(side=LEFT)
# Button to change the picture(forward)
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Next picture',
       command=lambda: ChangePicture(+1)).pack(side=LEFT)
# Button fo closing the program
Button(frame,font=('helvetica', 10, 'underline italic'),bd=8,relief=RAISED,
       cursor='hand2',bg='dark green', fg='white', text='Quit',
       command=root.destroy).pack(side=LEFT)
# Initial сondition of the program 
ChangePicture(0)
root.mainloop()
