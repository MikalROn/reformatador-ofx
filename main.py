import re

# Ecolha o tamaho máximo
tamanho_maximo = 100
nome_arquivo = input()


def reformatar_ofx(nome_do_arquivo):
    with open(f'{nome_do_arquivo}.ofx', 'rb') as ofx:
        ofx_str = ofx.read().decode('utf-8')
        lista_names = re.findall(r'<NAME>.*</NAME>', ofx_str)

        for name in lista_names:

            name_limpo = name.replace('<NAME>', "").replace('</NAME>', '')
            if len(name_limpo) >= tamanho_maximo:
                name_limpo = name_limpo[:tamanho_maximo - 10]
                print(name, "---->", f'<NAME>{name_limpo}</NAME>')
                name_final = f'<NAME>{name_limpo}</NAME>'
                ofx_str_reformatado = ofx_str.replace(name, name_final)
    with open('ofx_reformatado.ofx', 'wb') as ofx:
        try:
            ofx.write(ofx_str_reformatado.encode('utf-8'))
        except:
            raise ValueError('Não existem erros para serem corrigidos')


def main():
    reformatar_ofx(nome_arquivo)


if __name__ == '__main__':
    main()
