<h1 align="center">
<a href="https://github.com/Anderson-S-M3/django_chatbot">:robot: Chat Bot :robot:</a>
</h1>

<p align="center">Esse Chatbot foi desenvolvido para responder perguntas correspondente ao coronavirus:mask:.</p>

<p align="center">
<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen"> <img alt="PyPI - Django Version badge" src="https://img.shields.io/badge/django-2.2.17-blue"> <img alt="PyPI - Chatterbot Version badge" src="https://img.shields.io/badge/chatterbot-1.0.4-blue">
</p>

<h5 align="center">:rotating_light: Chatbot :snake: Finalizado... :rotating_light:</h5>

<p align="center"><a href="#instalacao">Instalação</a> • <a href="#rodando">Rodando o Bot</a> • <a href="#tecnologias">Tecnologias</a> • <a href="#demonstracao">Código</a></p>

<img src="https://user-images.githubusercontent.com/65872811/103164911-f2ba8d00-47ef-11eb-85c4-03929da9d6ee.gif">

<h2 id="instalacao">Instalação:</h2>
<h4>Pré-requisito:</h4>

Antes de começar, você vai precisar ter em sua máquina o [Git](https://git-scm.com) instalado.
Além disto é bom ter um editor para trabalhar com o código como por exemplo o [VSCode](https://code.visualstudio.com/)

No windows é necessário  o download do [Microsoft C++](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/)

Caso surja problemas na instalação dos pacotes, pode-se optar pela instalação de pacotes [Binários](https://www.lfd.uci.edu/~gohlke/pythonlibs/) não oficial.

<h5 id="rodando">:ticket: Fazendo o Bot funcionar:</h5>

```
# Clone este repositório
git clone https://github.com/Anderson-S-M3/django_chatbot

# Acesse a pasta do projeto no terminal/cmd
cd django_chatbot

# crie uma Venv
python -m venv <nome_da_venv>

#Ative a Venv
cmd: "<nome_da_venv>/Scripts/activate"
terminal: source <nome_da_venv>/bin/activate

# Instale o Django e o Chatterbot
pip install Django==2.2.16
pip install chatterbot==1.0.4

# Execute a aplicação
manage.py runserver

# O servidor inciará na porta:8000 - acesse < http://localhost:8000 >
```

<h2 id="tecnologias">🛠 Tecnologias</h2>
<p>As seguintes ferramentas foram usadas na construção do projeto:</p>

- [Chatterbot](https://chatterbot.readthedocs.io/en/stable/)
- [Django](https://www.djangoproject.com/)

<h2 id="demonstracao">:eyes: Código :eyes:</h2>

```
// index.html - Request Bot Response
$.post("{% url 'chatterbot'%}", JSON.stringify({'text': rawText}), {csrfmiddlewaretoken:'{{csrf_token}}'}).done(function(data){
    console.log(rawText);
    console.log(data);
    const msgText = data;
    appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
});

// chatbot.py - Get Bot Response
# Creating ChatBot Instance
chatbot = ChatBot(
    name = 'Lee',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    response_selection_method = get_random_response,
    statement_comparison_function = levenshtein_distance,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'empty',
            'output_text': ''
        },
        {   
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpa, Ainda estou aprendendo, qual a resposta ?',
            'maximum_similarity_threshold': 0.9
        }
    ],
    database="botData.sqlite3",
    database_uri="sqlite:///botData.sqlite3"
)

# Treino baseado no corpus 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    "chatterbot.corpus.portuguese",
    "training_data",
)
```

<br>
<br>

## 📝 Licença
---

Este projeto esta sobe a licença [MIT](./LICENSE.md).

<br>
<br>

### Autor
---

Feito com :blue_heart: por Anderson S. 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/Anderson_S-0077B5?style=for-the-badge&logo=linkedin&logoColor=white/)](https://www.linkedin.com/in/anderson-s-antunes-b879251b9/) <br>
[![Email](https://img.shields.io/badge/Anderson__S__Antunes@hotmail.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:anderson_s_antunes@hotmail.com)
