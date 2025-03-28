import hashlib

# S-box de l'AES
S_BOX = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
]


""" les 4 fonctions principales """


#def AddRoundKey128(): 


calcul de la clé de tour
cle en 4 col
pour obtenir la col1 de la clé2 on fait un RotWord sur la col4
(la case du haut vas en bas et toutes les autre remonte de 1)
ensuite on fait un Subytes sur toute la col4
ensuite on fait un xor entre la col4 la col1 et Rcon(*le nb de tour)
cela donne la col5 (ou future col1)

pour obtenir la col2 de la clé2 on fait un xor entre col2 et col5 (ou future col1)
pour obtenir la col3 de la clé2 on fait un xor entre col3 et col6 (ou future col2)
pour obtenir la col4 de la clé2 on fait un xor entre col4 et col7 (ou future col3)



d'un point de vu de la matrice ça donne
rotword sur col4
subbytes sur col4
xor entre col1 col4 et Rcon
le resultat deviens col4, mes autres avance de 1 et col1 disparrait
puis
xor entre col1 et col4
le resultat deviens col4, mes autres avance de 1 et col1 disparrait
xor entre col1 et col4
le resultat deviens col4, mes autres avance de 1 et col1 disparrait
xor entre col1 et col4
le resultat deviens col4, mes autres avance de 1 et col1 disparrait
on a la nouvelle clé






def SubBytes(state):
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            row = int(byte[0], 16)
            col = int(byte[1], 16) 
            print( byte , row , col)
            state[i][j] = format(S_BOX[row][col], '02x')
    return state


def ShiftRows(state):
    for i in range(1, 4): 
        print( state[i][i:])
        print(state[i][:i])
        state[i] = state[i][i:] + state[i][:i]
    return state

#def MixColumns():




"""
cette fonction découpe le message en matrice de taille 4x4. 
Chaque case correspond à un caractère. Si il manque des caractère dans la dernière matrice, on ajoute des espaces, 20 en hexadécimal.
la fonction retourne une liste de matrices
"""
def texte_en_matrice(phrase, taille_bloc=16):

    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    liste_matrices = []
    for bloc in blocs:
        matrice = [[bloc[i + j*4] for i in range(4)] for j in range(4)]
        liste_matrices.append(matrice)
    return liste_matrices


""" pareil mais pour la clé """
def cle_en_matrice(phrase, taille_bloc=32):

    if len(phrase) % taille_bloc != 0:
        phrase = phrase.ljust((len(phrase) // taille_bloc + 1) * taille_bloc)
    blocs = [phrase[i:i+taille_bloc] for i in range(0, len(phrase), taille_bloc)]
    liste_matrices = []
    for bloc in blocs:
        matrice = [[bloc[(i*8) + (j*2):(i*8) + (j*2) + 2] for j in range(4)] for i in range(4)]
        liste_matrices.append(matrice)
    return liste_matrices





""" cette fonction transforme chaque caractere d'une matrice en hexadécimal. """
def text_en_hexa(text):
    hex_matrice = [[format(ord(char), '02x') for char in row] for row in text]
    return hex_matrice




""" cette fonction applique l'opération xor entre 2 caractère en hexadécimal """
def xor(phrase, cle):
    resultat = int(phrase, 16) ^ int(cle, 16) # Convertie les caractere hexadécimals en entiers et effectue le XOR
    return format(resultat, f'0{len(phrase)}x') # Formate le résultat en hexadécimal



""" cette fonction retourne le hash de 128 bits pour la clé en utilisant MD5 """
def hash_128bit(cle):
    hash_object = hashlib.md5(cle.encode()) # on met dans 'hash_object' le hash en MD5 de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal



""" cette fonction retourne le hash de 192 bits pour la clé en tronquant SHA-384 """
def hash_192bit(password):
    hash_object = hashlib.sha384(password.encode()) # on met dans 'hash_object' le hash en SHA-384 de la clé
    return hash_object.hexdigest()[:48]  # on retourne le résultat en hexadécimal en enlevant 48 caractères 



""" cette fonction retourne le hash de 256 bits pour la clé en utilisant SHA-256 """
def hash_256bit(password):
    hash_object = hashlib.sha256(password.encode()) # on met dans 'hash_object' le hash en SHA-256 de la clé
    return hash_object.hexdigest() # on retourne le résultat en hexadécimal 



"""
#fonction de chiffrement, c'est la fonction principale 
- on commence par prendre le hash de la clé en fonction de la taille demandé
- ensuite on le met en matrice (1 matrice 4x4 pour une clé 128bits)
- on met le texte en matrice
- ensuite on le transforme en hexadécimal
- on peut appliquer l'algorithme c'est à dite
    - addRoundKey(cle)
    - pendant x tour:
        - subBytes
        - shiftRows
        - mixColumns
        - addRoundKey(roundKey)
    - puis dernier tous sans mixColumns
-on affiche le texte chiffré
 """
def chiffrement(texte_en_clair, cle, taille_cle):
    """ on hash la clé en fonction de la taille souhaité """
    """ pour la clé il faut d'abord la transformer en hexa avec la fonction de hash puis la mettre en matrice avec cle_en_matrice() """
    if taille_cle == 128:
        cle_hash = hash_128bit(cle)
    elif taille_cle == 192:
        cle_hash = hash_192bit(cle)
    elif taille_cle == 256:
        cle_hash = hash_256bit(cle)
    else:
        print("pas la bonne taille pour la clé")
        return 0
   
    print("Clé hasher:\n",cle_hash)
    cle_hash = cle_en_matrice(cle_hash)
    print("Clé en matrice:\n",cle_hash)
 


    """ pour le texte il faut d'abord le mettre en matrice avec texte_en_matrice() puis le transformer en hexa avec texte_en_hexa()"""
    print("Texte normal:\n",texte_en_clair)
    msg = texte_en_matrice(texte_en_clair) 
    print("Texte en matrice:\n",msg)
    hexadecimal = [] 
    for matrice in msg:
        hexadecimal.append(text_en_hexa(matrice)) 
    print("Texte en hexadécimal:\n",hexadecimal)



    """ application de l'algorithme 
        - AddRoundKey
        - boucle:
            - SubBytes
            - ShiftRows
            - MixColumns
            - AddRoundKey
        - SubBytes
        - ShiftRows
        - AddRoundKey
        """



    AddRoundKey()


    # return text_chiffre




#fonction de déchiffrement
def déchiffrement(text_chiffré, clé,taille):
    # return text_dechiffre   
    return 0


def main():
    texte_a_chiffrer = "Voici un exemeple de texte à chiffrer."
    cle_secrete = "Ceci est ma clé secrète."
    chiffrement(texte_a_chiffrer, cle_secrete, 128)


if __name__ == "__main__":
    main()





test_state = [
    ['19', 'a0', '9a', 'e9'],
    ['3d', 'f4', 'c6', 'f8'],
    ['e3', 'e2', '8d', '48'],
    ['be', '2b', '2a', '08']
]

print("\nÉtat avant SubBytes:")
for row in test_state:
    print(row)

test_state = SubBytes(test_state)

print("\nÉtat après SubBytes:")
for row in test_state:
    print(row)

test_state = ShiftRows(test_state)

print("\nÉtat après ShiftRows:")
for row in test_state:
    print(row)