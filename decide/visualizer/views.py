import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import telegram

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):

        bot_token = '5920930377:AAHGqZh6OSHtzefvGazRo8JbLwqbbqBTpsw'
        chat_id = '-1005354241660'
        bot = telegram.Bot(token=bot_token)
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        print(vid)
        try:
            r = mods.get('voting', params={'id': vid})

            V=json.dumps(r[0])
            context['voting'] = json.dumps(r[0])
            opci=[]
            votos=[]
            for v in r[0]["postproc"]: 
                opci.append(v["option"]) 
                votos.append(v["votes"]) 
            fig, ax = plt.subplots()
            
            ax.set_ylabel('Votos')
            
            ax.set_title('Número de votos')
            
            plt.bar(opci, votos)
            plt.savefig('grafico_de_barras.png')

             with open('grafico_de_barras.png', 'rb') as photo_file:
                            bot.sendPhoto(chat_id=chat_id,
                                photo=photo_file,
                                caption='Grafica de la votacion:')

        except:
            raise Http404

        return context

# class VisualizerView(TemplateView):
#     template_name = 'visualizer/visualizer.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         vid = kwargs.get('voting_id', 0)

#         try:
#             r = mods.get('voting', params={'id': vid})
#             context['voting'] = json.dumps(r[0])
#         except:
#             raise Http404

#         return context
