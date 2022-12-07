
import json

from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import telegram


import aspose.words as aw



from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
    
        bot_token = '5868243582:AAFU0ofV56esUNY96DmERyARmld0l-A2ZiA'
        chat_id = '1042938746'
        bot = telegram.Bot(token=bot_token)
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        print(vid)
        try:
            r = mods.get('voting', params={'id': vid})
            
            V=json.dumps(r[0])
            context['voting'] = json.dumps(r[0])
            opciones=[]
            votos=[]
            for v in r[0]["postproc"]:

                opciones.append(v["option"]) 
                votos.append(v["votes"]) 

            fig, ax = plt.subplots()
            ax.set_ylabel('Votos')
            plt.barh(opciones, votos)
            plt.savefig('barras_horizontales.png')

            with open('barras_horizontales.png', 'rb') as photo_file:
                            bot.sendPhoto(chat_id=chat_id,
                                photo=photo_file,
                                caption='Aqui esta una grafica de barras de la votacion')

    
        except:
            raise Http404

        return context
