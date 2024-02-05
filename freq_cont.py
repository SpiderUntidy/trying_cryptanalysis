import argparse
from string import ascii_uppercase
from collections import Counter
from functools import partial


def format_dict(dic):
    """Recebe um dict e formata sequencialmente seus elementos."""
    f_dic = []
    for k, v in dic.items():
        f_dic.append(f"\n{k}: {v}")

    return f_dic


def ler(paths):
    """Recebe uma lista de arquivos e retorna seu texto numa única string."""
    texto = []
    for path in paths:
        with open(path) as file:
            t_file = file.read().replace(' ', '')
            texto.append(t_file)

    return ''.join(texto)


def _base_contar(texto, tam_grupo):
    """Recebe string e tamanho e retorna um dict associando os grupos contidos na string às suas quantidades de ocorrência."""
    alf = list(ascii_uppercase)
    grupos = []
    for n in range(len(texto) - tam_grupo + 1):
        grupo = texto[n:n+tam_grupo]
        if all([letter in alf for letter in grupo]):
            grupos.append(grupo)
    
    return dict(Counter(grupos))


# --- Funções de contagem ---
contar_letras = partial(_base_contar, tam_grupo=1)
contar_pares = partial(_base_contar, tam_grupo=2)

if __name__ == "__main__":
    # Interpretação dos argumentos dados ao programa
    parser = argparse.ArgumentParser()
    parser.add_argument("paths")  # "paths" deve ser uma string em que cada path é separado do seguinte por um espaço
    arg = parser.parse_args()
    paths = arg.paths.split()
    
    # Leitura dos arquivos inseridos como argumento
    ciphertext = ler(paths)

    # Contagem de ocorrência de letras
    contagem_letras = contar_letras(ciphertext)
    contagem_letras = dict(reversed(sorted(contagem_letras.items(), key=lambda item: item[1])))  # Ordenando o dict

    # Contagem de ocorrência de pares de letras
    contagem_pares = contar_pares(ciphertext)
    contagem_pares = dict(reversed(sorted(contagem_pares.items(), key=lambda item: item[1])))  # Ordenando o dict

    # Printa a contagem de letras e pares
    print("\n--- Letras ---\n", *format_dict(contagem_letras))
    print("\n--- Pares ---\n", *format_dict(contagem_pares))
