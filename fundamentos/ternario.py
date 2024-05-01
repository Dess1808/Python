esta_chovendo = True

#sera verdade a valor que estiver mais perto da expressao "[esta_chovendo]"
print('Hoje estou com as roupas ' + ('secas.', 'molhadas'[esta_chovendo]))

#ternario em python, mais intuitivo
print('Hoje estou com as roupas ' + ('molhada.' if esta_chovendo else 'secas.'))

