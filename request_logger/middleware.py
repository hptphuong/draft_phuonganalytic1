# -*- coding: utf-8 -*-
# Author: Konstantinos Livieratos <livieratos.konstantinos@gmail.com>

import json
from django.conf import settings
from kafka import KafkaProducer
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

from django.contrib.gis.geoip2 import GeoIP2
import base64



class RequestLoggerMiddleware(MiddlewareMixin):
    """
    Transmits all requests' data to Kafka as a simple string.
    !Attention: Demonstration purpose only!
    """
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        if (request.path!='/a.gif'):
            return None
        info = request.GET
        producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_SERVERS,
            retries=5
        )

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        if (ip == '127.0.0.1'):
            ip = '118.69.213.98'
        g = GeoIP2('geoip2_db')

        producer.send(
            topic='test',
            key=b'request.url',
            value=info['url'].encode()
        )
        # producer.send(
        #     topic='test',
        #     key=b'request.t',
        #     value=info['t'].encode()
        # )
        # producer.send(
        #     topic='test',
        #     key=b'request.country',
        #     value=str(g.country(ip)).encode()
        # )
        #
        # producer.send(
        #     topic='test',
        #     key=b'request.city',
        #     value=str(g.city(ip)).encode()
        # )
        producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('test', {'foo': 'bar'})
        # PIXEL_GIF_DATA = base64.b64decode("")

        return HttpResponse(base64.b64decode(""), content_type='image/gif')
