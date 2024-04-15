# API by Alicino Moura - April 14th, 2024
from flask import Flask, jsonify
from urllib.parse import unquote
import json
import re

app = Flask(__name__)

# Abre o arquivo JSON e carrega os dados
def load_data():
    with open('Campeonato_Brasileiro.json', 'r') as file:
        return json.load(file)

# Função para verificar se um time corresponde ao nome fornecido
def match_team_name(team_name, name_to_match):
    # Converte ambos os nomes para minúsculas
    team_name = team_name.lower()
    name_to_match = name_to_match.lower()

    # Substitui espaços por hífens para tornar a comparação mais flexível
    team_name = re.sub(r'\s+', '-', team_name)

    # Substitui hífens por espaços para tornar a comparação mais flexível
    name_to_match = re.sub(r'-', ' ', name_to_match)

    # Verifica se o nome do time corresponde ao nome fornecido usando expressões regulares
    if re.search(name_to_match, team_name):
        return True
    else:
        return False

# List ALL
@app.route('/get_data', methods=['GET'])
def get_data():
    # Read data from the JSON file
    data = load_data()

    # Return the data as JSON response
    return jsonify(data)

# List by ID
@app.route('/brasileirao/<int:id>',methods=['GET'])
def obter_campeao_por_id(id):
    data = load_data()

    # Search ID in the file
    for item in data:
        if item['id'] == id:
        #if data.get('id') == id:
            return jsonify(item)
    # If not found, returns a 404 error message
    return jsonify({'error': 'ID not Found'}), 404

# List by YEAR
@app.route('/brasileirao/ano/<int:year>',methods=['GET'])
def obter_campeao_por_ano(year):
    # Check if Year is a valid number
    if year is None:
        return jsonify({'error': 'Ano não fornecido'}), 400
    
    data = load_data()

    # Search YEAR in the file
    for item in data:
        if item['Ano'] == year:
            return jsonify(item)
    else:
        return jsonify({"error": f"Campeao nao encontrado com o ano {year}. Range 2003 to 2023"}), 404


# Route to find the Champion
@app.route('/brasileirao/campeao/<string:time>', methods=['GET'])
def obter_campeao(time):
    # Decodifica o nome do time na rota
    time = unquote(time)

    lista_do_campeao = []

    # Abre o arquivo JSON e carrega os dados
    data = load_data()

    # Itera sobre os dados e adiciona os campeoes à lista
    for item in data:
        campeao = item.get('Campeao')
        # if campeao and time.capitalize() in campeao:
        #     lista_do_campeao.append(item)
        if campeao and match_team_name(campeao, time):
            lista_do_campeao.append(item)

    # Retorna a lista de campeoes encontrados
    if lista_do_campeao:
        return jsonify(lista_do_campeao)
    else:
        return jsonify({"erro": "Nenhum campeao encontrado com o nome fornecido."}), 404

# Rota to finde de "Vice Champion" (Runner-up)
@app.route('/brasileirao/vice/<string:time>', methods=['GET'])
def obter_vices(time):
    # Decodifica o nome do time na rota
    time = unquote(time)

    lista_do_vice = []

    # Abre o arquivo JSON e carrega os dados
    data = load_data()

    # Itera sobre os dados e verifica se o time fornecido está presente na lista de vice-campeões
    for item in data:
        vice = item.get('Vice')
        # Verifica se o nome do time corresponde ao fornecido
        if vice and match_team_name(vice, time):
            lista_do_vice.append(item)

    # Retorna a lista de grupos encontrados
    if lista_do_vice:
        return jsonify(lista_do_vice)
    else:
        return jsonify({"erro": "Nenhum grupo encontrado para o time fornecido"}), 404


# Rota para buscar tanto nos campeões quanto nos vice-campeões
@app.route('/brasileirao/time/<string:time>', methods=['GET'])
def buscar_time(time):
    # Decodifica o nome do time na rota
    time = unquote(time)

    lista_do_time = []

    # Abre o arquivo JSON e carrega os dados
    data = load_data()

    # Itera sobre os dados e verifica se "Sao Paulo" está presente nos campeões ou vice-campeões
    for item in data:
        campeao = item.get('Campeao')
        vice = item.get('Vice')

        # Condição para verificar se "time" está presente no campo 'Campeao' ou 'Vice'
        if campeao and match_team_name(campeao, time):
            lista_do_time.append(item)
        elif vice and match_team_name(vice, time):
            lista_do_time.append(item)

    # Retorna a lista de grupos encontrados
    if lista_do_time:
        return jsonify(lista_do_time)
    else:
        return jsonify({"erro": "Nenhum dado encontrado para o time fornecido"}), 404



# -------------- Main line --------------
if __name__ == '__main__':
    # app.run(debug=True) # Default option
    app.run(port=7865,host='localhost',debug=True)

