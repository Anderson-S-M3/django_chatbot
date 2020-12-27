from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from chatterbot.response_selection import get_random_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.chatterbot import ChatBot


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
