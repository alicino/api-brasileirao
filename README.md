# Brasileirão API

### Author
Alicino Moura
[https://alicino.me](https://alicino.me)

Last update: _January 19th, 2025_ 

## About
It's a simple API in Python to return information about Brazilian Championship (aka Brasileirão) between 2003 and 2024.

Source: [CBF - Confederação Brasileira de Futebol](https://www.cbf.com.br/futebol-brasileiro/tabelas/campeonato-brasileiro/serie-a/2024).

The data is about the Champion and Runner-up in each Championship played annually and contains the fields:

- id (a sequential number)
- Champion Soccer Team (Campeao)
- Year (Ano) - 2003 to 2024
- Champion points - total (Pontos Campeao)
- Champion's victories - total (Vitoria Campeao)
- Champion draws - total (Empate Campeao)
- Champion defeats - total (Derrotas Campeao)
- Runner-Up Soccer Team (Vice)
- Runner-up points (Pontos Vice)
- Runner-up victories - total (Vitoria Vice)
- Total of matches played (Rodadas)
- Percentage of Victories (% Vitorias)
- Difference between the number of wins between the champion and the runner-up (Dif. Vit p/ Vice)

## Endpopints
#### 1. All data
`/get_data`

#### 2. By ID
`/brasileirao/<id>`

#### 3. By Year (2003 to 2024)
`/brasileirao/ano/<year>`

#### 4. By the Champion
`/brasileirao/campeao/<team_name>`

#### 5. By the Runner-Up
`/brasileirao/vice/<team_name>`

#### 6. By the Soccer team name - it returns Champion and Runner-up according to the name
`/brasileirao/time/<team_name>`

**Note:** 
1. Search for the first name of the football team and without grammatical accent Ex: Vasco da Gama, type "Vasco" or "Gama". For "São Paulo", you can type only "Sao" (no accent), or just "Paulo".

2. GET method only

## Aditional Information

The port is 5867. Change according to your needs.

The code has several comments. I believe they are self-explanatory and helpful for beginners. So enjoy it.

To run this API locally, clone this repository. Then install all dependencies using pip:

- Flask
- json
- re (regex)

> pip install Flask

**Note:** It is not necessary to install the *json* and *re* libraries. These are already found in Python in the most recent versions.

