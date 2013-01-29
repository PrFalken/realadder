from django.shortcuts import render_to_response
from ligue1.models import Club

def index(request):
    real_ranking = Club.objects.all().order_by('real_points').reverse()
    ranking = Club.objects.all().order_by('points').reverse()
    context = { 'ranking' : ranking,
            'real_ranking': real_ranking,
            }
    return render_to_response('ligue1/index.html', context)
