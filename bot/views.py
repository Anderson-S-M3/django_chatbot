from django.views.generic.base import TemplateView
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .chatbot import chatbot
import json


class BotIndex(TemplateView):
    template_name = 'index.html'


class BotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = chatbot

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """

        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'Atributo Texto é obrigatorio.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)
        
        #  Adicionar Frase Não encontrada ao txt
        if str(response) == 'Desculpa, Ainda estou aprendendo, qual a resposta ?':
            f = open("./training_data/semresposta.txt", 'a+', encoding='utf8')
            descompactar = list(input_data.values())
            f.write(f'{str(descompactar[0])} \n')
            f.close() 

        return HttpResponse(response)


    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
