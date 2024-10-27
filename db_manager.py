import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)