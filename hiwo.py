import os
import re
import time
from collections import defaultdict
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import subprocess
import sys
import io

class SimpleChatbot:
    def __init__(self):
        self.patterns = defaultdict(list)
        self.add_patterns()

    def add_patterns(self):
        self.patterns['saudacao'].extend([r'oi', r'olá', r'e aí'])
        self.patterns['despedida'].extend([r'tchau', r'até logo', r'adeus'])
        self.patterns['hiwo'].extend([r'o que é hiwo', r'me fale sobre hiwo'])
        self.patterns['ajuda'].extend([r'ajuda', r'preciso de ajuda', r'como usar'])
        self.patterns['variaveis'].extend([r'variáveis', r'variaveis', r'como criar variável'])
        self.patterns['print'].extend([r'print', r'como imprimir', r'exibir na tela'])
        self.patterns['input'].extend([r'input', r'como receber entrada', r'ler do usuário'])

    def responder(self, mensagem):
        mensagem = mensagem.lower()
        for intencao, padroes in self.patterns.items():
            for padrao in padroes:
                if re.search(padrao, mensagem):
                    return self.gerar_resposta(intencao)
        return "Desculpe, não entendi. Pode reformular?"

    def gerar_resposta(self, intencao):
        if intencao == 'saudacao':
            return "Olá! Como posso ajudar você hoje?"
        elif intencao == 'despedida':
            return "Até logo! Foi um prazer conversar com você."
        elif intencao == 'hiwo':
            return "Hiwo é um assistente/mini sistema operacional desenvolvido em Python para o Visual Studio."
        elif intencao == 'ajuda':
            return "Estou aqui para ajudar! Você pode me perguntar sobre o Hiwo, ou pedir ajuda com comandos específicos."
        elif intencao == 'variaveis':
            return ("Variáveis são espaços na memória do computador que podem armazenar dados. "
                    "Para criar uma variável, use: nome_variavel = valor. Exemplo: idade = 25")
        elif intencao == 'print':
            return ("A função print() é usada para mostrar informações na tela. "
                    "Exemplo: print('Olá, mundo!')")
        elif intencao == 'input':
            return ("A função input() é usada para receber dados do usuário. "
                    "Exemplo: nome = input('Digite seu nome: ')")

def chatbot_ia():
    bot = SimpleChatbot()
    print("Bem-vindo ao Chatbot IA do Hiwo! Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Até logo!")
            break
        resposta = bot.responder(user_input)
        print("Chatbot:", resposta)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
time.sleep(2)
print("Iniciando Sistema")
time.sleep(5)
print("Verificando Hardware atual...")
time.sleep(1)
print("Sucesso!(Seu dispositivo atual é compativél com o Hiwo!)")
time.sleep(0.50)
os.system('cls')
print('''
             __  
|__| | |  | /  \ 
|  | | |/\| \__/ 
      
Feito por Benjamin Krik
Programado em Python                
Não Distribuir                                            
''')
while True:
    acao = input("\nUSER/BenjaminKrik $ > ")

    if acao == 'oi':
        print('Olá, eu sou o terminal Hiwo, e estou aqui para te ajudar.')
    elif acao == 'help':
        print('''
        Comandos:
        oi -> ver se o Hiwo está funcionando.
        help -> Mostra os comandos disponíveis.
        clear -> Limpa a tela.
        exit -> Sai do Hiwo.
        open(launcher) -> Abre o lançador de programas.
        about -> Mostra informações sobre o Hiwo.
        cd -> Abre um arquivo ou pasta.
        install(pro) -> instala o Hiwo Pro.

        ''')
    elif acao == 'clear':
        clear_screen()
    elif acao == 'exit':
        print('Obrigado por usar o Hiwo. Até logo!')
        break
    elif acao == 'open(launcher)':
        print('''
        LAUNCHER --------------------------------------------------------------------------------
        Anotar no terminal do Hiwo 'open(notepad)'
        Executar um projeto no Hiwo 'open(python)'
        Versão do Hiwo!!! 'open(version)'
        Sorte 'open(givemeluck)'
        Email do Hiwo 'open(email)'
        Chatbot IA do Hiwo 'open(chatbot_ia)
        Executar a calculadora do Hiwo 'open(calculator)'
        Mensagens do Hiwo 'open(main)'
        Explorador de arquivos 'open(explorer)'
        Hiwo Studio 'open(studio)'
        Usar o potencial completo do python (so use em caso de emergencia) 'open(pot)'

        ------------------------------------------------------------------------------------------

        11 programas disponiveis no Hiwo.
        
        ''')
    elif acao == 'open(notepad)':
        print("Abrindo o bloco de notas...")
        notas = input("Digite uma nota para gravar no terminal do Hiwo: ")
        print(notas)
    elif acao == 'open(python)':
        print("digite 'python (nome do arquivo.py)' para executar o arquivo.")
        print("digite 'python hiwo.py' para voltar ao Hiwo")
        print("(main.py abre um app de mensagens)")
        break 
    elif acao == 'open(version)':
        print('''
        Hiwo 5.3
        Versão Open Source
        ''')
    elif acao == 'open(email)':
        print("Bem vindo ao email do Hiwo, para começar, insira seu email .hiwo")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if senha == 'python':
            print("Login realizado com sucesso.")
            print("Bem vindo ao Hiwo Email Express, benjamin.krik")
            print("Login realizado no Hiwo (dell)")
            print("Hiwo baixado com sucesso no seu computador.")
        else:
            print('Senha incorreta.')
    elif acao == 'open(givemeluck)':
        print('''
        Olá mundo!!!!!!!!!!!!!!!!
        ''')
    elif acao == 'open(calculator)':
        from Calculator import calculator 
        calculator()
    elif acao == 'open(chatbot_ia)':
        chatbot_ia()
    elif acao == 'open(main)':
        from main import main 
        main()
    elif acao == 'open(explorer)':
        print('''
        Explorador de arquivos do Hiwo-----------------------------------------------
        Assistente do explorador de arquivos do Hiwo
        Conhecimento basico do explorador de arquivos do Hiwo
            Cd -> Abre uma pasta/arquivo.
            Py -> Abre um arquivo.py.
            HiwoSSD -> Abre os arquivos do sistema
            codecheck -> Abre verifica o codigo do Hiwo. (só funciona na pasta do Hiwo)
            puppy -> Abre o PuppyIDE
        Com esse conhecimento, agora vamos explorar esse Mundo de pastas e arquivos!
        ___________________________________________________________________________________
            Arquivos:
            Pasta do Hiwo (hiwossd)
            Arquivos do Visual Studio Code (cd(vscode))
            Diretorios do Hiwo (dir)
            Sobre o Hiwo (about)
            Arquivos Python (cd(python))
            Arquivos do Windows (cd(windows))
        5 Pastas e 1 executavel.
        Hiwo
        ''') 
    elif acao == 'cd(python)':
        print('''
        Pasta do Visual Studio Code
        Hiwo.py
        main.py
        Calculator.py
        New.py
        Para executar esse arquivos acima, use Open(python) ou Py.
        ''')
    elif acao == 'cd(vscode)':
        print('''
        Pasta do Visual Studio Code
        Hiwo.py
        main.py
        Calculator.py
        New.py
        Para executar esse arquivos acima, use Open(python) ou Py.
        Extenções do Visual Studio Code (pasta) 🠗
        >   Cody
        >   GitHub Copilot (desativado)
        *esta pasta é uma pasta de leitura, para executar esses arquivos, use a barra no esquerda do Visual Studio Code.
        ''')
    elif acao == 'cd(windows)':
        print('''
        Windows:
        Apps
        Arquivos de programas
        Arquivos de programas(x86)
        dell
        Drivers
        e-logo
        Intel
        langpacks
        PerfLogs
        ProgramData
        Usuarios
        Windows
        XboxData
        ^ Essa pasta é uma pasta de leitura. não é possivel editar, apagar, criar ou abrir pastas ou arquivos nela.
        ''')
    elif acao == 'hiwossd':
        print('''
        comandos
        codigo
        arquivos
        diretorios
        ''')
    elif acao == 'codecheck':
        print('''
        :(
        Ocorreu um erro e o Hiwo está reiniciando
        ''')
        time.sleep(10)
        os.system('cls')
        print("O HIWO FALHOU PARA INICIAR, ABRINDO POWERSHELL")
        time.sleep(3)
        break

    elif acao == 'about':
        print('''
        Hiwo é um sistema operacional baseado em texto desenvolvido em Python.
        Codenome:Blue_Bytes

        ''')
    elif acao == 'py':
        print("digite 'python (nome do arquivo.py)' para executar o arquivo.py")
        print("digite 'python hiwo.py' para voltar ao Hiwo")
        print("(main.py abre um app de mensagens)")
        break
    elif acao == 'open(puppy)':
        print("Digite '/about(pup)' para saber mais sobre o PuppyIDE")
        time.sleep(3)
        from HiwoStudio import HiwoStudio
        HiwoStudio()  
    elif acao == 'install(pro)':
        print('''
        instalando o Hiwo Pro...
         ''')
        time.sleep(3)
        print("Olá!")
        time.sleep(3)
        print("Você está instalando o Hiwo Pro")
        time.sleep(3)
        print("Por favor insira sua Chave de ativação")
        chave = input("Chave de ativação §-> ")
        print("Verificando chave de ativação...")
        time.sleep(3)
        print("Chave de ativação válida.")
        print("Instalando...")
        time.sleep(3)
        print("Instalado com sucesso!")
        print("desligando...")
        break
    elif acao == 'open(pot)':
        from pyhton import python
    else:
        print("O Hiwo não consegue encontrar o comando especificado,digite help para obter ajuda")
