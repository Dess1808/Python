#utilizando set() e intersetion() do mundo do conjuntos!!!

PROHIBTID_WORDS = {'futebol', 'religion', 'policy'}

phrases = [
    'I like futebol and religion',
    'A new adventure',
    'policy is horribal'
]

for phrase in phrases:
    intersetion = PROHIBTID_WORDS.intersection(set(phrase.lower().split()))
    if intersetion:
        print('Prohibtid word: ', intersetion)
    else:
        print('authorized text: ', phrase)