from tqdm import tqdm
import time
import os
import subprocess
import sys
import random
from datetime import datetime
import locale

def show_date_time():
    # Configurar o locale para português brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    # Obter a data e hora atuais
    now = datetime.now()

    # Formatar a saída
    formatted_date = now.strftime("%A, %d de %B de %Y")
    formatted_time = now.strftime("%H:%M:%S")

    print(f"Data: {formatted_date}")
    print(f"Hora: {formatted_time}")

class SimpleTerminalIDE:
    def __init__(self):
        self.code = ""

    def run(self):
        while True:
            command = input("HiwoPocket IDE > ").strip().lower()
            if command == "exit":
                break
            elif command == "write":
                self.write_code()
            elif command == "run":
                self.run_code()
            elif command == "show":
                self.show_code()
            elif command == "clear":
                self.clear_code()
            elif command == "help":
                self.show_help()
            else:
                print("Comando desconhecido. Digite 'help' para ver os comandos disponíveis.")

    def write_code(self):
        print("Digite seu código Python. Digite 'END' em uma nova linha para finalizar.")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        self.code = "\n".join(lines)

    def run_code(self):
        if not self.code:
            print("Nenhum código para executar. Use 'write' para adicionar código.")
            return
        try:
            result = subprocess.run([sys.executable, "-c", self.code], capture_output=True, text=True, timeout=5)
            print("Saída:")
            print(result.stdout)
            if result.stderr:
                print("Erros:")
                print(result.stderr)
        except subprocess.TimeoutExpired:
            print("Erro: Tempo de execução excedido (limite de 5 segundos)")
        except Exception as e:
            print(f"Erro ao executar o código: {str(e)}")

    def show_code(self):
        print("Código atual:")
        print(self.code if self.code else "Nenhum código escrito ainda.")

    def clear_code(self):
        self.code = ""
        print("Código limpo.")

    def show_help(self):
        print("""
        Comandos disponíveis:
        write - Escrever ou editar código
        run - Executar o código atual
        show - Mostrar o código atual
        clear - Limpar o código atual
        help - Mostrar esta mensagem de ajuda
        exit - Sair da IDE
        """)

os.system('cls')
total_items = 100

print("Samsung A32")
print("Powered By Hiwo Pocket")

for _ in tqdm(range(total_items)):
    time.sleep(0.1)

while True:
    time.sleep(0.1)
    act = input("HiwoPocket >>")
    if act == "pyhelp":
        print("""
        pyhelp - Mostra a lista de comandos
        exit - Sai do Hiwo Pocket
        pylist - Mostra a lista de programas
        pyzero - apaga a tela
        
        """)
    elif act == "exit":
        print("Saindo...")
    elif act == "pylist":
        print("""
        Notas 'pyhp sticky'
        PocketIDE 'pyhp nano'
        Calendario Pocket  'pyhp calendar'
        """)
    elif act == "pyhp sticky":
       nota = input('> ')
       print(nota)
    elif act == "pyhp nano":
       if __name__ == "__main__":
        ide = SimpleTerminalIDE()
        ide.run()
    elif act == "pyzero":
      os.system('cls')
    elif act == "pyhp calendar":
        show_date_time()
    