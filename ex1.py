import nltk

def limpar(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalpha() or char.isspace())
    return texto_limpo

def ocorrencias(texto):
    contar_letras = {}
    for letra in texto:
        if letra.isalpha():
            contar_letras[letra] = contar_letras.get(letra, 0) + 1
    
    letras_ordenadas = sorted(contar_letras.items(), key=lambda item: item[1], reverse=True)
    
    letras_menos_frequentes = sorted(contar_letras.items(), key=lambda item: item[1])
    
    hapax = [letra for letra, frequencia in contar_letras.items() if frequencia == 1]

    return letras_ordenadas, letras_menos_frequentes, hapax

# fim do exercício 1 e continuação para o uso das funções no exercício 2.

def main(texto):
    texto_limpo = limpar(texto)
    letras_ordenadas, _, _ = ocorrencias(texto_limpo)
    return letras_ordenadas

def abrir_ler(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

o_ateneu = abrir_ler('OAteneu.txt')
o_ateneu_limpo = limpar(o_ateneu)
palavras_frequentes_ateneu, _, _ = ocorrencias(o_ateneu_limpo)

primo_basilio = abrir_ler('OPrimoBasilio.txt')
primo_basilio_limpo = limpar(primo_basilio)
palavras_frequentes_primo_basilio, _, _ = ocorrencias(primo_basilio_limpo)

print('Palavras mais frequentes de O Ateneu:', palavras_frequentes_ateneu)
print('Palavras mais frequentes de O Primo Basílio:', palavras_frequentes_primo_basilio)

def letras_comuns(texto1, texto2):
    return list(set(texto1) & set(texto2))

comuns = letras_comuns(palavras_frequentes_ateneu, palavras_frequentes_primo_basilio)
print('Letras comuns aos dois resultados:', comuns)


# Uso das funções para resolução do exercício 3




kommunistischen = abrir_ler('Kommunistischen.txt')
kommunistischen_limpo = limpar(kommunistischen)

NotreDame = abrir_ler('NotreDame.txt')
NotreDame_limpo = limpar(NotreDame)

palavras_frequentes_kommunistischen, menos_frequentes_kommunistischen, hapax_kommunistischen = ocorrencias(kommunistischen_limpo)
palavras_frequentes_NotreDame, menos_frequentes_notredame, hapax_notredame = ocorrencias(NotreDame_limpo)

print('Letras mais frequentes em Kommunistischen:', palavras_frequentes_kommunistischen)
print('Letras mais frequentes em NotreDame:', palavras_frequentes_NotreDame)

print('Letras menos frequentes em Kommunistischen:', menos_frequentes_kommunistischen)
print('Letras menos frequentes em NotreDame:', menos_frequentes_notredame)

print('Hapax legomena em Kommunistischen:', hapax_kommunistischen)
print('Hapax legomena em NotreDame:', hapax_notredame)

alfabeto_kommunistischen = set(letra for letra, _ in palavras_frequentes_kommunistischen)
alfabeto_notredame = set(letra for letra, _ in palavras_frequentes_NotreDame)

diferenca_kommunistischen_notredame = alfabeto_kommunistischen - alfabeto_notredame
diferenca_notredame_kommunistischen = alfabeto_notredame - alfabeto_kommunistischen

print('Letras presentes em Kommunistischen e não em NotreDame:', diferenca_kommunistischen_notredame)
print('Letras presentes em NotreDame e não em Kommunistischen:', diferenca_notredame_kommunistischen)


