# Brasileirão API

### Author
Alicino Moura
Website: (https://alicino.me)

## About
It's a simple API to return information about Brazilian Championship between 2003 and 2023.
Source: [CBF - Confederação Brasileira de Futebol] (https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a).
The data is about the Champion and Runner-up in each Championship played annually and contains the fields:
- id (a sequential number)
- Champion Soccer Team (Campeao)
- Year (Ano) - 2003 to 2023
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

#### 3. By Year
`/brasileirao/ano/<year>`

#### 4. By the Champion
`/brasileirao/campeao/<team_name>`

#### 5. By the Runner-Up
`/brasileirao/vice/<team_name>`

#### 6. By Soccer team name - it returns Champion and Runner-up according the name
`/brasileira/time/<team_name>`

**Note:** Search by the first name soccer name. Ex: Vasco da Gama, type "Vasco" or "Gama".
For "Sao Paulo", you can type only "Sao" or "Paulo"