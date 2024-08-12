PROHIBTID_WORDS = ('futebol', 'religion', 'policy')

phrases = [
    'I like dounts',
    'I like futebol and religion',
    'A new adventure',
    'policy is horribal'
    
]

for phrase in phrases:
    for word in phrase.lower().split(): #separa apartir de um espaco em branco
        if word in PROHIBTID_WORDS:
            print(f'Has at least on prohibtid word - {word}')
            break
    else:
        print('authorized text: ', phrase)
