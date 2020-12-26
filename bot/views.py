from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse
from .chatbot import chatbot


class BotIndex(TemplateView):
    template_name = 'index.html'


class BotApiView(View):

    def get(self, request):
        userText = request.GET.get('msg')

        print(userText)

        resposta = chatbot.get_response(userText)
        resposta = str(resposta)

        if 'The current time' in resposta:
            return HttpResponse('Desculpe, ainda estou aprendendo sobre isso...')    
        
        return HttpResponse(chatbot.get_response(userText))
