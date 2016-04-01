from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging
import logging.handlers


# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from urllib import unquote
logger = logging.getLogger("django")

@csrf_exempt
def doPost(request):
	#print "doPost is working"

	request.encoding = "utf-8"
	remote_addr = request.META['REMOTE_ADDR']
	if request.method == 'POST':
		mouse_message = request.POST.get('mouse_message')
		if (mouse_message != None):
			message = unquote(mouse_message)
			ms = message.split("\n")
			for m in ms:
				logger.info("IP:" + remote_addr + "\t" + m)
	return HttpResponse("success!")

