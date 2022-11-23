import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from base import mods


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

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
