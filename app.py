import os
import subprocess
import urllib.request
import time
import sys
import platform
import ctypes
import tkinter as tk
from tkinter import messagebox

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def reset_hosts_file():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    
    with open(hosts_path, 'w') as hosts_file:
        hosts_file.write("""
# Copyright (c) 1993-2009 Microsoft Corp.
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.

127.0.0.1       localhost
::1             localhost
""")
    print("Le fichier hosts a été réinitialisé avec succès.")

def download_and_run_antivirus():
    url = "https://download.bitdefender.com/windows/installer/en-us/bitdefender_avfree.exe"
    filename = "bitdefender_avfree.exe"
    
    print("Téléchargement de Bitdefender...")
    urllib.request.urlretrieve(url, filename)
    
    if os.path.exists(filename):
        print(f"Lancement de l'installeur Bitdefender : {filename}")
        
        subprocess.Popen([filename], shell=True)  
        print("L'installeur de Bitdefender a été lancé.")
    else:
        print("Le fichier d'installation n'a pas pu être téléchargé correctement.")

def disable_wifi():
    print("Désactivation du Wi-Fi...")
    if platform.system() == 'Windows':
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'disable'], check=True)
        print("Le Wi-Fi a été désactivé.")
    else:
        print("Cette fonctionnalité n'est pas supportée sur ce système.")

def enable_wifi():
    print("Réactivation du Wi-Fi...")
    if platform.system() == 'Windows':
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'enable'], check=True)
        print("Le Wi-Fi a été réactivé.")
    else:
        print("Cette fonctionnalité n'est pas supportée sur ce système.")

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  
    messagebox.showinfo(title, message)

def show_instructions():
    instructions = """
    Instructions :
1. Lancez "bitdefender_avfree.exe" puis effectuez l'installation. Effectuez une analyse complète du système, pas une analyse rapide.
2. Si vous avez d'autres problèmes, veuillez contacter un expert en sécurité ou vous pouvez me contacter.
3. Si votre Wi-Fi ne s'est pas réactivé automatiquement, réactivez-le en suivant ces étapes :
   - Ouvrez une invite de commandes en tant qu'administrateur.
   - Tapez : netsh interface set interface 'Wi-Fi' enable
4. Je vous conseille également de changer vos mots de passe après l'analyse, car ils pourraient être compromis.
"""
    show_message("Instructions", instructions)

def main():
    if not is_admin():
        show_message("Erreur", "Ce script doit être exécuté en tant qu'administrateur.")
        sys.exit()

    show_message("Bienvenue", "Bienvenue dans le nettoyeur d'infections.")

    reset_hosts_file()
    time.sleep(2)
    
    download_and_run_antivirus()
    
    disable_wifi()

    time.sleep(5) 
    enable_wifi()

    show_instructions()

    show_message("Opération terminée", "Votre appareil devrait être plus sécurisé maintenant.")

if __name__ == "__main__":
    main()
