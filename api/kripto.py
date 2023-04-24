import hashlib
import sys
from cryptography.fernet import Fernet


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

        escalador = [int(cadastro[0]) % 3, int(cadastro[1]) % 2, int(cadastro[2]) % 3,
                     int(cadastro[3]) % 3, int(
                         cadastro[4]) % 2, int(cadastro[5]) % 3,
                     int(cadastro[6]) % 3, int(
                         cadastro[7]) % 2, int(cadastro[8]) % 3,
                     int(cadastro[9]) % 3, int(cadastro[10]) % 2]

        primeiraChamada = f'{ab[int(cadastro[0])]}{cd[int(cadastro[1])]}'
        segundaChamada = f'{ef[int(cadastro[2])]}{gh[int(cadastro[3])]}'
        terceiraChamada = f'{ij[int(cadastro[4])]}{lm[int(cadastro[5])]}'
        quartaChamada = f'{np[int(cadastro[6])]}{uv[int(cadastro[7])]}'
        quintaChamada = f'{wy[int(cadastro[8])]}{zq[int(cadastro[9])]}'
        sextaChamada = f'{kx[int(cadastro[10])]}'

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


text1 = 'Modulo de Criptografia. Aqui você pode gerar os passes secretos!'
text2 = 'Modulo de Instrução'


def md5_gerador(string):
    "Retorna a string convertido em md5."
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def dchavakey_gerador(md1, md2):
    "Pega os resultados de usuario 'md1' e senha 'md2' simplificando para junção dos hashs em 16 dígitos."
    usuario = str(md1).lower()
    senha = str(md2)
    usuario_encry = str(md5_gerador(usuario)).lower()
    senha_encry = str(md5_gerador(senha)).upper()
    passe_secreto = str(f'{senha_encry[0]}'
                        f'{usuario_encry[2]}'
                        f'{usuario_encry[0]}'
                        f'{senha_encry[2]}'
                        f'{senha_encry[3]}'
                        f'{senha_encry[5]}'
                        f'{senha_encry[7]}'
                        f'{senha_encry[11]}'
                        f'{senha_encry[13]}'
                        f'{senha_encry[17]}'
                        f'{usuario_encry[3]}'
                        f'{usuario_encry[5]}'
                        f'{usuario_encry[7]}'
                        f'{usuario_encry[11]}'
                        f'{usuario_encry[13]}'
                        f'{usuario_encry[17]}')
    return passe_secreto


def cadastropessoa(CPF):
    senha_encry = str(md5_gerador(str(CPF))).upper()
    cadastro_cript = str(f'{senha_encry[11]}'
                         f'{senha_encry[7]}'
                         f'{senha_encry[17]}'
                         f'{senha_encry[5]}'
                         f'{senha_encry[21]}'
                         f'{senha_encry[2]}'
                         f'{senha_encry[27]}'
                         f'{senha_encry[0]}'
                         f'{senha_encry[31]}')
    return cadastro_cript


def criptografaTexto(textos):
    # gera uma chave de criptografia
    key = Fernet.generate_key()

    # cria um objeto Fernet com a chave gerada
    fernet = Fernet(key)

    # texto a ser criptografado
    texto = textos

    # criptografa o texto
    texto_criptografado = fernet.encrypt(texto.encode())

    # descriptografa o texto
    texto_descriptografado = fernet.decrypt(texto_criptografado).decode()

    # imprime o texto original, o texto criptografado e o texto descriptografado
    if __name__ == '__main__':
        print("Texto original:", texto)
        print("Texto criptografado:", texto_criptografado)
        print("Texto descriptografado:", texto_descriptografado)
    else:
        return texto_criptografado.decode()


if __name__ == '__main__':
    import sys
    # Para o gerador funcionar no console.
    # deve ser digitado: código usuario cpf
    # Exemplo;
    # ---      passe diogo 12345678910

    if sys.argv[1] == 'd-usuario-senha':
        print('Teste para:', sys.argv[2], sys.argv[3])
        if len(sys.argv) != 3:
            print('Chave gerada:', dchavakey_gerador(sys.argv[2], sys.argv[3]))
            sys.exit(1)
    elif sys.argv[1] == 'd-pessoa-numero':
        print('Teste para :', sys.argv[2])
        if len(sys.argv) == 3:
            print('Dado criptografado:',
                  Programa().engrenagemTeste(sys.argv[2]))
            print('Dado descriptografado:', desengrenagem(
                Programa().engrenagemTeste(sys.argv[2])))

            sys.exit(1)
    elif sys.argv[1] == 'd-texto-numero':
        print('Teste para :', sys.argv[2])
        if len(sys.argv) == 3:
            criptografaTexto(sys.argv[2])
            sys.exit(1)
