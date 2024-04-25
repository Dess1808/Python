"""
- confirmado os 2: tv 50' + sorvete
- confirmado apenas 1: tv 32' + sorvete
- nenhum trabalho confirmado: Fica em casa
"""
trabalho_terca = True
trabalho_quinta = True

#nao ensinou estruturas de controle

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saude = not sorvete

#utilizar o format para mostrar output com string e valores
print("tv50={}, tv32={}, sorvete={}, saudavel={}".format(tv_50, tv_32, sorvete, mais_saude))