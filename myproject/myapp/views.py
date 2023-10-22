from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def data(request):
    return HttpResponse("<h1>Родился в 31 мая 1979 года<br>"                        
                        "В городе Нижний Новгород</h1>")


def about(request):
    return HttpResponse("<h2>Александр Загайнов <br/><br>"
                        "В данный момент учусь в Geek Brain <br/>"
                        "и осваиваю новый framefork Django <br>"
                        "Удачи в Django чайник!)"
                        "</h2>")


def index_(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about_(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")
