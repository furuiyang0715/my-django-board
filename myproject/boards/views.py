from django.http import HttpResponse
from .models import Board


def home(request):
    # 导入 Board 模型并且列出所以的板块
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
