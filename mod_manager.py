import os
import shutil
import subprocess
import sys
from tkinter import Tk, filedialog, Button, Listbox, END, messagebox, Checkbutton, IntVar

arquivos_selecionados = set()

def atualizar_textos():
    if usar_ingles.get():
        btn_selecionar.config(text="Select .pak Files")
        btn_criar.config(text="Create Folders and Copy Files")
        btn_abrir.config(text="Open Destination Folder")
        chk_ingles.config(text="English")
        root.title("Mod Manager for Hogwarts Legacy")
    else:
        btn_selecionar.config(text="Selecionar Arquivos .pak")
        btn_criar.config(text="Criar Pastas e Copiar Arquivos")
        btn_abrir.config(text="Abrir Pasta de Destino")
        chk_ingles.config(text="English")
        root.title("Gerenciador de Mods para Hogwarts Legacy")

def selecionar_arquivos():
    novos_arquivos = filedialog.askopenfilenames(
        title="Selecione os arquivos .pak" if not usar_ingles.get() else "Select .pak files",
        filetypes=[("Arquivos .pak", "*.pak")]
    )
    for arquivo in novos_arquivos:
        if arquivo not in arquivos_selecionados:
            arquivos_selecionados.add(arquivo)
            listbox.insert(END, arquivo)

def criar_pastas_e_copiar():
    documentos_path = os.path.expanduser("~/Documents")
    pasta_base = os.path.join(documentos_path, "mod_manager")
    pasta_hogwarts = os.path.join(pasta_base, "hogwarts_legacy")
    pasta_destino = os.path.join(pasta_hogwarts, "atmosphere", "Contents", "0100F7E00C70E000", "Romfs", "Phoenix", "Content", "Paks", "~mods")
    os.makedirs(pasta_destino, exist_ok=True)
    for arquivo in arquivos_selecionados:
        try:
            shutil.copy(arquivo, pasta_destino)
        except Exception as e:
            messagebox.showerror(
                "Error" if usar_ingles.get() else "Erro",
                f"Error copying {arquivo}: {e}" if usar_ingles.get() else f"Erro ao copiar o arquivo {arquivo}: {e}"
            )
            return
    msg = (
        f"The 'hogwarts_legacy' folder was created at:\n{pasta_hogwarts}\nCopy its contents to your SD card."
        if usar_ingles.get() else
        f"A pasta 'hogwarts_legacy' foi criada em:\n{pasta_hogwarts}\nCopie seu conteúdo para o cartão SD."
    )
    title = "Success" if usar_ingles.get() else "Sucesso"
    messagebox.showinfo(title, msg)

def abrir_pasta():
    documentos_path = os.path.expanduser("~/Documents/mod_manager/hogwarts_legacy")
    if os.name == 'nt':
        subprocess.Popen(f'explorer "{documentos_path}"')
    elif os.name == 'posix':
        subprocess.Popen(["xdg-open", documentos_path])

def carregar_arquivos_linha_de_comando():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.isfile(arg) and arg.endswith(".pak"):
                arquivos_selecionados.add(arg)
                listbox.insert(END, arg)

root = Tk()
root.geometry("700x500")
usar_ingles = IntVar()

chk_ingles = Checkbutton(root, text="English", variable=usar_ingles, command=atualizar_textos)
chk_ingles.pack(pady=5)

btn_selecionar = Button(root, command=selecionar_arquivos)
btn_selecionar.pack(pady=10)

listbox = Listbox(root, width=100, height=12)
listbox.pack(pady=10)

btn_criar = Button(root, command=criar_pastas_e_copiar)
btn_criar.pack(pady=10)

btn_abrir = Button(root, command=abrir_pasta)
btn_abrir.pack(pady=10)

atualizar_textos()
carregar_arquivos_linha_de_comando()
root.mainloop()
