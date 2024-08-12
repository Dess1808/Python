PROHIBTID_WORDS = ('futebol', 'religion', 'policy')

phrases = [
    'I like futebol and religion',
    'A new adventure',
    'policy is horrible'
]

for phrase in phrases:
    for word in phrase.lower().split():
        print(word)