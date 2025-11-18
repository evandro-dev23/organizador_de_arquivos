import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory

def organizador_de_arquivos():
    caminho = askdirectory(title="Selecione uma pasta para organizar")
    if caminho == '':
        messagebox.showinfo(
            'Mensagem do Sistema',
            'Nenhuma pasta foi selecionada!'
        )
        
    else:
        confirmacao = messagebox.askyesno(
            "Mensagem do Sistema",
            f"Deseja organizar os arquivos na pasta:\n{caminho}?\n\n"
            f"Os arquivos serão movidos para pastas organizadas por tipo."
        )
        
        if not confirmacao:
            messagebox.showinfo(
                "Mensagem do Sistema",
                "Operação cancelada pelo usuário."
            )
            return
        
        lista_arquivos = os.listdir(caminho)
        locais = {
            "→ Banco de Dados": [".dbf", ".mdb", ".accdb", ".fb"],
            "→ Certificados": [".crt", ".key"],
            "→ Códigos Python": [".py"],
            "→ Códigos JavaScript": [".js", ".mjs", ".cjs"],  #  e 
            "→ Códigos HTML": [".html"],
            "→ Imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
            "→ Ícones": [".ico"],
            "→ ISO's": [".iso", ".deb", ".img"],
            "→ Json": [".json"],
            "→ Músicas": [".mp3", ".wav"],
            "→ Pdfs": [".pdf"],
            "→ Planilhas": [".xls", ".xlsx", ".csv"],
            "→ Powers MS": [".pbix", ".ppt"],
            "→ Programas Windows": [".exe", ".msi", ".rdp"],
            "→ Programas Android": [".apk"],
            "→ Textos": [".doc", ".txt", ".docx"],
            "→ VPNs": [".ovpn"],
            "→ Vídeos": [".mp4", ".avi", ".mpeg", ".mov", ".rmvb", ".mkv"],
            "→ XML": [".xml"],
            "→ Zipados": [".zip", ".rar", ".7z"],
        }

        for arquivo in lista_arquivos:
            # Dividindo o caminho em duas partes: Pasta raiz e arquivo + extensão
            nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
            for pasta in locais:
                if extensao in locais[pasta]:
                    # Se a pasta não existir, a mesma será criada
                    if not os.path.exists(f"{caminho}/{pasta}"):
                        # Criando a pasta
                        os.mkdir(f"{caminho}/{pasta}")
                    # Renomeando o novo caminho dos arquivos
                    os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

        messagebox.showinfo(
            'Mensagem do Sistema',
            'Procedimento finalizado!'
        )

def main():
    # Tenta executar o Organizador de Arquivos
    try:
        organizador_de_arquivos()
    # Se houver(em) erro(s), uma a mensagem será apresentada com o(s) erro(s)
    except Exception as e:
        messagebox.showerror(
            'Aviso',
            f'Erro(s) Encontrado(s): {e}'
        )

if __name__ == '__main__':
    # Construtor
    main()
