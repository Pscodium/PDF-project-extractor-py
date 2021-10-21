#_______________________________________________________________________IMPORTANDO BIBLIOTÉCAS_______________________________________________________________________

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


#___________________________________________________________________CRIANDO MAIN FRAME DO PROGRAMA__________________________________________________________________
root = tk.Tk()

root.title('Extrator de Texto PDF')

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(column=1, rowspan=3)


#_____________________________________________________________________________LOGO_________________________________________________________________________________


logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#______________________________________________________________________TEXTO DE INSTRUÇÃO__________________________________________________________________________

instructs = tk.Label(root, text="Selecione um arquivo PDF do seu computador para extrair todo o seu texto", font='Raleway')
instructs.grid(columnspan=3, column=1, row=1)



#________________________________________________________________FUNÇÃO DE EXTRAÇÃO DE TEXTO PDF___________________________________________________________________

def open_file():
    browse_text.set("Carregando...")
    file = askopenfile(parent=root, mode='rb', title='Escolha o arquivo', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Procurar")
        


#_______________________________________________________________________BOTÃO DE PROCURA___________________________________________________________________________

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#5ce1e6", fg="white", height=2, width=15, border=0)
browse_text.set("Procurar")
browse_btn.grid(column=1, row=2)

#_____________________________________________________________________ALINHAMENTO DE ITENS_________________________________________________________________________


canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(column=1)


#__________________________________________________________________LOOP DE INICIALIZAÇÃO DA JANELA_________________________________________________________________

root.mainloop()

