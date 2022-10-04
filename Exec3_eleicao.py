candidatos = [
    'nesk',
    'Paluh',
    'Ask',
    'resetz',
    'Lagonis',
    'Nulo',
    'Branco'
]

votos = 0

for i in range(len(candidatos)):
    print(f'Candidato: {i} == {candidatos[i]}')
    

x = [0 for i in range(len(candidatos))]
print(x)


while votos < 5:
    voto = int(input('Em que voce quer votar? '))

    if voto == 0:
        x[0] = x[0] + voto
        votos += 1
    if voto == 1:
        x[1] = x[1] + voto
        votos += 1
    if voto == 2:
        x[2] = x[2] + voto
        votos += 1
    if voto == 3:
        x[3] = x[3] + voto
        votos += 1
    if voto == 4:
        x[4] = x[4] + voto
        votos += 1
    if voto == 5:
        x[5] = x[5] + voto
        votos += 1
    if voto == 6:
        x[6] = x[6] + voto
        votos += 1

print(f"""
Votos candidato {candidatos[0]} {x[0]}
Votos candidato {candidatos[1]} {x[1]}
Votos candidato {candidatos[2]} {x[2]}
Votos candidato {candidatos[3]} {x[3]}
Votos candidato {candidatos[4]} {x[4]}
Votos Nulo {candidatos[5]} {x[5]}
Votos em branco {candidatos[6]} {x[6]}
""")