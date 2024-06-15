import logging
import coloredlogs
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Configure the logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='%(asctime)s %(name)s %(levelname)s %(message)s', level_styles={'info': {'color': 'green'}})

def log_user_info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    remote_addr = request.META.get('REMOTE_ADDR', 'Unknown')
    referer = request.META.get('HTTP_REFERER', 'Unknown')

    logger.info(f"User Agent: {user_agent}")
    logger.info(f"Remote Address: {remote_addr}")
    logger.info(f"Referer: {referer}")

def index(request):
    logger.info(timezone.now())
    log_user_info(request)
    logger.info('Index site')

    return render(request, 'index.html')

def hangout(request):
    logger.info(timezone.now())
    logger.info('Hangout site...')

    return render(request, 'hangout.html')

def thinking(request):
    logger.info(timezone.now())
    logger.info('Thinking site...')

    return render(request, 'firework.html')

def redirect_facebook(request):
    logger.info(timezone.now())
    logger.info('Riderecting to facebook...')

    return HttpResponse('ok')

def confirm(request):
    logger.info(timezone.now())
    logger.info('CONFIRMED !!')

    return HttpResponse('ok')
