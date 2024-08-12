PROHIBTID_WORDS = ('futebol', 'religion', 'policy')

phrases = [
    'I like futebol and religion',
    'A new adventure',
    'policy is horribal'
]

for phrase in phrases:
    found = False
    for word in phrase.lower().split(): #separa apartir de um espaco em branco
        if word in PROHIBTID_WORDS:
            print(f'Has at least on prohibtid word - {word}')
            found = True
            break
    
    if not found:
        print(f'authorized text {phrase}')
