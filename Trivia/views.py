from django.shortcuts import get_object_or_404, render
from django.forms import formset_factory
from .models import Game, Question, Round, Team
from .forms import TeamGameForm

def about(request):
    return render(request, 'Trivia/about.html')

def contact(request):
    return render(request, 'Trivia/contact.html')

def game_list(request):
    games = Game.objects.all()
    return render(request, 'Trivia/game_list.html', {'games' : games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    rounds = Round.objects.filter(game=game)

    if request.method == 'POST':
        form = TeamGameForm(request.POST)
    else:
        form = TeamGameForm()

    return render(request, 'Trivia/game_detail.html', {'game': game, 'rounds': rounds, 'form': form, })

def round_detail(request, game_pk, pk):
    round = get_object_or_404(Round, pk=pk)
    game = get_object_or_404(Game, pk=game_pk)
    questions = Question.objects.filter(round=round)
    return render(request, 'Trivia/round_detail.html', {'round': round, 'game': game, 'questions': questions,})
