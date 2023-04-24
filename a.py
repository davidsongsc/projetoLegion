import hashlib

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


if __name__ == '__main__':
    import sys
    # Para o gerador funcionar no console.
    # deve ser digitado: código usuario cpf
    # Exemplo;
    # ---      passe diogo 12345678910

    if sys.argv[1] == 'passe':
        print(sys.argv[2], sys.argv[3])
        if len (sys.argv) != 3:
            print(dchavakey_gerador(sys.argv[2], sys.argv[3]))
            sys.exit(1)

