import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from gtts import gTTS
import speech_recognition as sr


def newFile():
    textBox.delete(1.0, tk.END)


def openFile():
    new_file = askopenfilename(defaultextension=".txt",
                               filetypes=[("Text Documents", "*.txt")])
    if new_file != "":
        textBox.delete(1.0, tk.END)
        file = open(new_file, 'r')
        textBox.insert(1.0, file.read())
        file.close()


def saveFile():
    new_file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
    if new_file != "":
        file = open(new_file, 'w')
        file.write(textBox.get(1.0, tk.END))
        file.close()


def updateWord(event):
    st1 = str(textBox.get(1.0, tk.END))
    arr1 = st1.split()
    num1 = len(arr1)
    label_word.configure(text='Words : ' + str(num1))


def cut():
    textBox.event_generate("<<Cut>>")


def copy():
    textBox.event_generate("<<Copy>>")


def paste():
    textBox.event_generate("<<Paste>>")


def text2audio():
    text = str(textBox.get(1.0, tk.END))
    language = 'en'
    obj = gTTS(text=text, lang=language, slow=False)
    new_file = asksaveasfilename(initialfile='Untitled.wav',
                                 defaultextension=".wav",
                                 filetypes=[("wav file", "*.wav")])
    if new_file != "":
        obj.save(new_file)


def audio2text():
    new_file = askopenfilename(defaultextension=".flac",
                               filetypes=[("Flac Files", "*.flac")])
    if new_file != "":
        r = sr.Recognizer()

        with sr.AudioFile(new_file) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            textBox.insert(1.0, text)


def pic2Text():
    from PIL import Image
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    new_file = askopenfilename(defaultextension=".png",
                               filetypes=[("All Files", "*.*"),
                                          ("PNG Files", "*.png")])
    if new_file != "":
        img = Image.open(new_file)
        result = pytesseract.image_to_string(img)
        result = result[:len(result)-1]
        textBox.insert(1.0, result)


mainWindow = tk.Tk()
mainWindow.title('NotePad')
mainWindow.geometry('820x620')
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=4)
mainWindow.rowconfigure(2, weight=1)
menuBar = tk.Menu(mainWindow)
fileMenu = tk.Menu(menuBar, tearoff=0)
editMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.quit)

editMenu.add_cascade(label='Cut', command=cut)
editMenu.add_cascade(label='Copy', command=copy)
editMenu.add_cascade(label='Paste', command=paste)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Edit", menu=editMenu)

top_frame = tk.Frame(mainWindow, bd=3, relief=tk.GROOVE)
mid_frame = tk.Frame(mainWindow, bd=3, relief=tk.GROOVE)
bot_frame = tk.Frame(mainWindow, bd=3, relief=tk.GROOVE)
top_frame.grid(row=0, sticky=tk.NSEW)
mid_frame.grid(row=1, sticky=tk.NSEW)
bot_frame.grid(row=2, sticky=tk.NSEW)

textBox = tk.Text(mid_frame, bd=2, relief=tk.GROOVE)
mid_frame.rowconfigure(0, weight=1)
mid_frame.columnconfigure(0, weight=1)
textBox.grid(row=0, sticky=tk.NSEW)

sBar = tk.Scrollbar(mid_frame)

sBar.config(command=textBox.yview)
textBox.config(yscrollcommand=sBar.set)

textBox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
sBar.pack(side='right', fill='y')
st = str(textBox.get(1.0, tk.END))
arr = st.split()
num = len(arr)
label_word = tk.Label(bot_frame, text='Words : ' + str(num))
label_word.pack(side=tk.RIGHT, padx=50)
textBox.bind('<Key>', updateWord)

open_img = tk.PhotoImage(file=r'open1.png')

open_Button = tk.Button(top_frame, text='Open', image=open_img, compound=tk.TOP, width=50, height=70, padx=3, pady=3,
                        command=openFile, relief=tk.GROOVE, activebackground='#4444ff')
open_Button.pack(side=tk.LEFT, padx=5, pady=5)

save_img = tk.PhotoImage(file=r'save1.png')
save_Button = tk.Button(top_frame, text='Save', image=save_img, compound=tk.TOP, width=50, height=70, padx=3, pady=3,
                        command=saveFile, relief=tk.GROOVE, activebackground='#4444ff')
save_Button.pack(side=tk.LEFT, padx=5, pady=5)

audio_img = tk.PhotoImage(file='audio1.png')
text2audio_Button = tk.Button(top_frame, text='Text to Audio', image=audio_img, compound=tk.TOP, width=50, height=70,
                              padx=3, pady=3, relief=tk.GROOVE, activebackground='#4444ff', wraplength=70,
                              command=text2audio)
text2audio_Button.pack(side=tk.LEFT, padx=5, pady=5)

audio2text_Button = tk.Button(top_frame, text='Audio to Text', image=audio_img, compound=tk.TOP, width=50, height=70,
                              padx=3, pady=3, relief=tk.GROOVE, activebackground='#4444ff', wraplength=70,
                              command=audio2text)
audio2text_Button.pack(side=tk.LEFT, padx=5, pady=5)

pic1 = tk.PhotoImage(file='pic1.png')
pic2text_Button = tk.Button(top_frame, text='Pic to Text', image=pic1, compound=tk.TOP, width=50, height=70,
                            padx=3, pady=3, relief=tk.GROOVE, activebackground='#4444ff', wraplength=70,
                            command=pic2Text)
pic2text_Button.pack(side=tk.LEFT, padx=5, pady=5)

mainWindow.config(menu=menuBar)
mainWindow.mainloop()
