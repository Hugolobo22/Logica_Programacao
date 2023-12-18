# Dicionário de tradução do idioma Plus2 para o português
plus2_to_portuguese = {
    'jqlg': 'hoje',
    'xqw': 'vou',
    'rtqitcoct': 'programar',
    # Adicione mais palavras conforme necessário
}

# Função para traduzir uma palavra do Plus2 para o português
def translate_word(word):
    return plus2_to_portuguese.get(word, word)

# Função para traduzir uma frase do Plus2 para o português
def translate_plus2_to_portuguese(plus2_text):
    words = plus2_text.split()
    translated_words = [translate_word(word) for word in words]
    translated_text = ' '.join(translated_words)
    return translated_text

# Comando Plus2 fornecido
plus2_command = 'rtkpv("jvvru://ujqtvwtn.cv/eDIPX")'

# Extrair a parte entre parênteses
url_part = plus2_command.split('"')[1]

# Traduzir a parte da URL do Plus2 para o português
translated_url_part = translate_plus2_to_portuguese(url_part)

# Recriar o comando com a parte traduzida
translated_command = f'rtkpv("{translated_url_part}")'

# Exibir o resultado
print(translated_command)

# Não entendi muito bom como fazer essa questão, tentei com auxílio de sites externos