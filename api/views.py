
from api.models import (
    fsa_site,
    fsa_user,
    user_daily,
    user_daily_report
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
from dateutil import tz
from cassandra.cqlengine.connection import get_session
import json
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
		# logger.warn("data:"+data)
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
		# serializer = UserDailySerializer(api, many=True)
		return JsonResponse(str(list(api)),safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		utc_zone = tz.gettz('UTC')
		x1_start=datetime.strptime(data['x1_start'][0],'%Y-%m-%d').date()
		x1_end = datetime.strptime(data['x1_end'][0], '%Y-%m-%d').date()
		# x1_start = x1_start.replace(tzinfo=utc_zone)
		# x1_end = x1_end.replace(tzinfo=utc_zone)
		results = (
			user_daily_report
				.objects.filter(m_date__gt=x1_start)
				.filter(m_date__lt=x1_end)
				.allow_filtering()
        )
		# session = get_session()
		# session.set_keyspace('test')
		# tmp=session.execute('select count(*) from user_daily group by userid')
		# # for result in user_daily.objects.filter(m_date__gt=x1_start).filter(m_date__lt=x1_end).allow_filtering():
		# # 	print(result)
		# print(tmp)
		# serializer = UserDailySerializer(results, many=True)
		m_rlst={}
		m_rlst['date']=[]
		m_rlst['value']=[]
		for i in range(0,len(results)):
			result=results[i]
			m_rlst['date'].append(str(result['m_date']))
			m_rlst['value'].append(result['users'])


		return JsonResponse(json.dumps(m_rlst), status=201, safe=False)
		# if serializer.is_valid():
		# # print(json.dumps(serializer.data))
		# 	return JsonResponse(json.dumps(serializer.data), status=201,safe=False)
		# return JsonResponse(serializer.errors, status=400)

		# data['m_date']=datetime.strptime(data['m_date'],"%Y-%m-%d")
		# # logger.warn("date:"+data)
		# serializer = UserDailySerializer(data=data)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	return JsonResponse(serializer.data, status=201)
		# return JsonResponse(serializer.errors, status=400)