#!/usr/local/bin/python3
def note_conferece(note):
    if note > 10:
        return 'invalid note'
    elif note >= 9.1:
        return 'A'
    elif note >= 8.1:
        return 'A-'
    elif note >= 7.1:
        return 'B'
    elif note >= 6.1:
        return 'B-'
    elif note >= 5.1:
        return 'C'
    elif note >= 4.1:
        return 'C-'
    elif note >= 3.1:
        return 'D'
    elif note >= 2.1:
        return 'D-'
    elif note >= 1.1:
        return 'E'
    elif note >= 0:
        return 'E-'
    else:
        return 'invalid note'

#main
if __name__ == '__main__':
    note = float(input("note: "))
    print(note_conferece(note))   
