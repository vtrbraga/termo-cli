# Termo para command line

## Dependências
- Python 3.6+
- bibliotecas nativas (unidecode, colorama, json, random)
- _(apenas windows)_ biblioteca nativa ctypes

## Uso
Navegue até o arquivo em um prompt de comando qualquer e execute com o interpretador Python do seu ambiente:
```
python ./termo.py
```

## Regras do jogo
- São permitidas apenas palavras nas listas `validas` ou `respostas` no arquivo `palavras.json`
- O jogo é feito apenas para palavras com cinco letras
- O jogo escolhe uma palavra aleatória da lista `validas` no início da execução
- São aceitas por padrão apenas 6 palpites
- Acentos e cedilha não interferem no palpite ou na resposta
- Letras na posição correta são pintadas de verde, e letras que aparecem na resposta mas estão na posição incorreta são pintadas de amarelo
- As respostas podem conter mais de uma ocorrência da mesma letra
- Se o palpite tiver mais de uma ocorrência da mesma letra, serão pintadas conforme o número de ocorrências na resposta
- É possível parar a execução do jogo escrevendo **SAIR** ou escapando com ctrl+C 