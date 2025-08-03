from django.http import HttpResponse
from utils import chat_room

# Create your views here.


def index(request):
    return HttpResponse("hello bitches from the other side")


def create_room(request):
    chat_room = utils.ChatRoom()
    raise NotImplementedError()
