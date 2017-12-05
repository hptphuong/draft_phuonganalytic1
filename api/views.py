
from api.models import (
    fsa_site,
    fsa_user,
    user_daily
)
from api.serializers import (
	FsaSiteModelSerializer,
	FsaUserSerializer,
	UserDailySerializer
)

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import logging
from datetime import datetime
logger = logging.getLogger(__name__)
#curl http://localhost:8000/user/ -X POST 
# -H "Content-Type: application/json" 
# -d '{"idx":"1002","user_id":"fsoft1002",
# "email":"huynhthang@gmail.com","password":"123456",
# "first_name":"thang","last_name":"huynh","url":"123434"}'

# curl http://localhost:8000/user/fsoft1001/ -X PUT 
# -H "Content-Type: application/json" 
# -d '{"idx":"1003","user_id":"fsoft1003",
# "email":"trantu.uit@gmail.com","password":"tu",
# "first_name":"tu","last_name":"tran"}'

@csrf_exempt
def fsaSiteList(request):
    """
    List all code apis, or create a new snippet.
    """
    if request.method == 'GET':
        api = fsa_site.objects.all()
        serializer = FsaSiteModelSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
    	logger.warn("parse data>>>>>>>>>>>>>>>>>>>")
    	data = JSONParser().parse(request)
    	logger.warn("passed >>>>>>>>>>>>>>>>>>>")
    	logger.warn("data:"+data['idsite'])
    	serializer = FsaSiteModelSerializer(data=data)
    	if serializer.is_valid():
    		serializer.save()
    		return JsonResponse(serializer.data, status=201)
    	return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def fsaUserList(request):
	if request.method == 'GET':
		api = fsa_user.objects.all()
		serializer = FsaUserSerializer(api, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		logger.warn("parse data>>>>>>>>>>>>>>>>>>>")
		data = JSONParser().parse(request)
		logger.warn("passed >>>>>>>>>>>>>>>>>>>")
		logger.warn("data:"+data)
		serializer = FsaUserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def userDailyList(request):
	logger.warn(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	logger.warn(">>>>>>>>>>>> userDailyList<<<<<<<<<")
	if request.method == 'GET':
		api = user_daily.objects.all()
		serializer = UserDailySerializer(api, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		logger.warn("parse data>>>>>>>>>>>>>>>>>>>")
		data = JSONParser().parse(request)
		logger.warn("passed >>>>>>>>>>>>>>>>>>>")
		logger.warn("data:"+data['m_date'])
		data['m_date']=datetime.strptime(data['m_date'],"%Y-%m-%d")
		# logger.warn("date:"+data)
		serializer = UserDailySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)