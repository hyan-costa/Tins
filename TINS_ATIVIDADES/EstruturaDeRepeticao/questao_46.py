#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos
# de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores
# restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus
# saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
# calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução,
# portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta.

atletas = []
while 1:
    nome = input("nome do atleta: ")
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhorSalto": 0,
        "piorSalto": 0,
    }
    #adiciona valores na lista saltos
    for item in range(5):
        atleta.get("saltos").append(float(input(f"Distância do {item+1}º salto: ")))
    #ordena a lista para apagar a posiçao inicial e final
    atleta.get("saltos").sort()
    atleta["piorSalto"] = atleta.get("saltos").pop(0)
    atleta["melhorSalto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3
    print(f"\nMelhor salto: {atleta.get('melhorSalto'):.1f} m")
    print(f"\nPior salto: {atleta.get('piorSalto'):.1f} m")
    print(f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n")
    atletas.append(atleta)
    
print("------------------------\nResultado final")
for atleta in atletas:
    if nome == "":
        break
    continue
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")
        