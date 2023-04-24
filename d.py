# Modulo de transfiguração de cpf, telefone e cep.

import hashlib
import sys
class Programa:
    """
    Método de criptografia de valores com 11 digitos.
        Ex:
            CPF 01234567891
            TEL 21983108439
            CEP 00021640260
            """
    def engrenagemTeste(self, cadastro):
        ab = ["a", "A", "b", "B", "0", "1", "2", "3", "4", "5", "6"]
        cd = ["c", "C", "d", "D", "1", "2", "3", "4", "5", "6", "7"]
        ef = ["e", "E", "f", "F", "2", "3", "4", "5", "6", "7", "8"]
        gh = ["g", "G", "h", "H", "3", "4", "5", "6", "7", "8", "9"]
        ij = ["i", "I", "j", "J", "4", "5", "6", "7", "8", "9", "0"]
        lm = ["l", "L", "m", "M", "5", "6", "7", "8", "9", "0", "1"]
        np = ["n", "N", "p", "P", "6", "7", "8", "9", "0", "1", "2"]
        uv = ["u", "U", "v", "V", "7", "8", "9", "0", "1", "2", "3"]
        wy = ["w", "W", "y", "Y", "8", "9", "0", "1", "2", "3", "4"]
        zq = ["z", "Z", "q", "Q", "9", "0", "1", "2", "3", "4", "5"]
        kx = ["k", "K", "x", "X", "a", "A", "b", "B", "c", "C", "d"]

        escalador = [int(cadastro[0])%3, int(cadastro[1])%2, int(cadastro[2])%3,
                     int(cadastro[3])%3, int(cadastro[4])%2, int(cadastro[5])%3,
                     int(cadastro[6])%3, int(cadastro[7])%2, int(cadastro[8])%3,
                     int(cadastro[9])%3, int(cadastro[10])%2]

        primeiraChamada = f'{ab[int(cadastro[0])]}{cd[int(cadastro[1])]}'
        segundaChamada =  f'{ef[int(cadastro[2])]}{gh[int(cadastro[3])]}'
        terceiraChamada = f'{ij[int(cadastro[4])]}{lm[int(cadastro[5])]}'
        quartaChamada =   f'{np[int(cadastro[6])]}{uv[int(cadastro[7])]}'
        quintaChamada = f'{wy[int(cadastro[8])]}{zq[int(cadastro[9])]}'
        sextaChamada =  f'{kx[int(cadastro[10])]}'

        if cadastro[0] == '0' or cadastro[0] == '1' or cadastro[0] == '2' or cadastro[0] == '3':
            variavelControle1 = f'{sextaChamada}{escalador[4]}{quartaChamada}{escalador[0]}{escalador[2]}'
            variavelControle2 = f'{quintaChamada}{escalador[7]}{escalador[6]}{terceiraChamada}'
            variavelControle3 = f'{primeiraChamada}{segundaChamada}'
            return f'{variavelControle2}{variavelControle3}{variavelControle1}{cadastro[0]}'

        elif cadastro[0] == '4' or cadastro[0] == '5' or cadastro[0] == '6' or cadastro[0] == '7':
            variavelControle1 = f'{sextaChamada}{escalador[4]}{quartaChamada}{escalador[0]}{escalador[2]}'
            variavelControle3 = f'{quintaChamada}{escalador[7]}{escalador[6]}{terceiraChamada}'
            variavelControle2 = f'{primeiraChamada}{segundaChamada}'
            return f'{variavelControle2}{variavelControle3}{variavelControle1}{cadastro[0]}'
        elif cadastro[0] == '8' or cadastro[0] == '9':
            variavelControle3 = f'{sextaChamada}{escalador[4]}{quartaChamada}{escalador[0]}{escalador[2]}'
            variavelControle2 = f'{quintaChamada}{escalador[7]}{escalador[6]}{terceiraChamada}'
            variavelControle1 = f'{primeiraChamada}{segundaChamada}'
            return f'{variavelControle2}{variavelControle3}{variavelControle1}{cadastro[0]}'

def desengrenagem(engrenado):
    ab = ["a", "A", "b", "B", "0", "1", "2", "3", "4", "5", "6"]
    cd = ["c", "C", "d", "D", "1", "2", "3", "4", "5", "6", "7"]
    ef = ["e", "E", "f", "F", "2", "3", "4", "5", "6", "7", "8"]
    gh = ["g", "G", "h", "H", "3", "4", "5", "6", "7", "8", "9"]
    ij = ["i", "I", "j", "J", "4", "5", "6", "7", "8", "9", "0"]
    lm = ["l", "L", "m", "M", "5", "6", "7", "8", "9", "0", "1"]
    np = ["n", "N", "p", "P", "6", "7", "8", "9", "0", "1", "2"]
    uv = ["u", "U", "v", "V", "7", "8", "9", "0", "1", "2", "3"]
    wy = ["w", "W", "y", "Y", "8", "9", "0", "1", "2", "3", "4"]
    zq = ["z", "Z", "q", "Q", "9", "0", "1", "2", "3", "4", "5"]
    kx = ["k", "K", "x", "X", "a", "A", "b", "B", "c", "C", "d"]
    
    p = len(engrenado)-1
    if engrenado[p] == '0' or engrenado[p] == '1' or engrenado[p] == '2' or engrenado[p] == '3':
        try:
            recipiente1 = f'{engrenado[10]}{engrenado[11]}{engrenado[12]}{engrenado[13]}{engrenado[14]}{engrenado[15]}'
            recipiente2 = f'{engrenado[0]}{engrenado[1]}{engrenado[2]}{engrenado[3]}{engrenado[4]}{engrenado[5]}'
            recipiente3 = f'{engrenado[6]}{engrenado[7]}{engrenado[8]}{engrenado[9]}'
            ordenador = f'{ab.index(recipiente3[0])}{cd.index(recipiente3[1])}{ef.index(recipiente3[2])}{gh.index(recipiente3[3])}' \
                        f'{ij.index(recipiente2[4])}{lm.index(recipiente2[5])}{np.index(recipiente1[2])}{uv.index(recipiente1[3])}' \
                        f'{wy.index(recipiente2[0])}{zq.index(recipiente2[1])}{kx.index(recipiente1[0])}'
            return ordenador
        except ValueError:
            print('Erro na leitura, falta um digito!')
    elif engrenado[p] == '4' or engrenado[p] == '5' or engrenado[p] == '6' or engrenado[p] == '7':
        try:
            recipiente1 = f'{engrenado[10]}{engrenado[11]}{engrenado[12]}{engrenado[13]}{engrenado[14]}{engrenado[15]}'
            recipiente3 = f'{engrenado[0]}{engrenado[1]}{engrenado[2]}{engrenado[3]}{engrenado[4]}{engrenado[5]}'
            recipiente2 = f'{engrenado[6]}{engrenado[7]}{engrenado[8]}{engrenado[9]}'
            ordenador = f'{ab.index(recipiente3[0])}{cd.index(recipiente3[1])}{ef.index(recipiente3[2])}{gh.index(recipiente3[3])}' \
                        f'{ij.index(recipiente2[4])}{lm.index(recipiente2[5])}{np.index(recipiente1[2])}{uv.index(recipiente1[3])}' \
                        f'{wy.index(recipiente2[0])}{zq.index(recipiente2[1])}{kx.index(recipiente1[0])}'
            return ordenador
        except ValueError:
            print('Erro na leitura, falta um digito!')
    elif engrenado[p] == '8' or engrenado[p] == '9':
        try:
            recipiente3 = f'{engrenado[10]}{engrenado[11]}{engrenado[12]}{engrenado[13]}{engrenado[14]}{engrenado[15]}'
            recipiente2 = f'{engrenado[0]}{engrenado[1]}{engrenado[2]}{engrenado[3]}{engrenado[4]}{engrenado[5]}'
            recipiente1 = f'{engrenado[6]}{engrenado[7]}{engrenado[8]}{engrenado[9]}'
            ordenador = f'{ab.index(recipiente3[0])}{cd.index(recipiente3[1])}{ef.index(recipiente3[2])}{gh.index(recipiente3[3])}' \
                        f'{ij.index(recipiente2[4])}{lm.index(recipiente2[5])}{np.index(recipiente1[2])}{uv.index(recipiente1[3])}' \
                        f'{wy.index(recipiente2[0])}{zq.index(recipiente2[1])}{kx.index(recipiente1[0])}'
            return ordenador
        except ValueError:
            print('Erro na leitura, falta um digito!')
if __name__ == '__main__':
    if len (sys.argv) == 2:
        print(desengrenagem(Programa().engrenagemTeste(sys.argv[1])))
        print(Programa().engrenagemTeste(sys.argv[1]))
        sys.exit(1)
        