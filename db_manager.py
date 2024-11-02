#serve somente pra facilitar o processo de salvar os arquivos para mim
import json

#Carrega arquivo
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

#Salva arquivo    
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)