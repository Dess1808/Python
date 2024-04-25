"""
- confirmado os 2: tv 50' + sorvete
- confirmado apenas 1: tv 32' + sorvete
- nenhum trabalho confirmado: Fica em casa
"""
trabalho_terca = True
trabalho_quinta = True

#nao ensinou estruturas de controle

tv50_sorvete = trabalho_terca and trabalho_quinta
tv32_sorvete = trabalho_terca != trabalho_quinta
saude = (trabalho_terca == False) and (trabalho_quinta == False)

print(tv50_sorvete)
print(tv32_sorvete)
print(saude)
