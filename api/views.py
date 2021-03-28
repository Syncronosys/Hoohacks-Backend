from django.shortcuts import render
from django.http import JsonResponse
from . import models
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_join(request):
    sessionId = request.GET.get('sessionid', None)
    name = request.GET.get('name', None)
    if sessionId is not None and name is not None:
        try:
            obj = models.Session.objects.get(uuid=sessionId)
            client = obj.members.create(name=name)
            return JsonResponse({'value': True, 'client': str(client.uuid)})
        except models.Session.DoesNotExist:
            return JsonResponse({'value': False})
    else:
        return JsonResponse({'value': False})


@csrf_exempt
def api_update(request):
    body = json.loads(request.body.decode('utf-8'))
    client = request.GET.get('client', None)
    if client is not None:
        try:
            client = models.Client.objects.get(uuid=client)
            client.anger = round(body['anger'], 5)
            client.contempt = round(body['contempt'], 5)
            client.disgust = round(body['disgust'], 5)
            client.fear = round(body['fear'], 5)
            client.happiness = round(body['happiness'], 5)
            client.neutral = round(body['neutral'], 5)
            client.sadness = round(body['sadness'], 5)
            client.surprise = round(body['surprise'], 5)
            client.save()

            return JsonResponse({'value': True})
        except models.Client.DoesNotExist:
            return JsonResponse({'value': False})
    else:
        return JsonResponse({'value': False})


@csrf_exempt
def api_session(request):
    obj = models.Session.objects.create()
    return JsonResponse({'value': True, 'sessionId': obj.uuid})


@csrf_exempt
def api_poll(request):
    sessionId = request.GET.get('sessionid', None)
    if sessionId is not None:
        try:
            obj = models.Session.objects.get(uuid=sessionId)
            buffer = {}
            for client in obj.members.all():
                buffer[str(client.uuid)] = {
                    'name': client.name,
                    'anger': client.anger,
                    'contempt': client.contempt,
                    'disgust': client.disgust,
                    'fear': client.fear,
                    'happiness': client.happiness,
                    'neutral': client.neutral,
                    'sadness': client.sadness,
                    'surprise': client.surprise,
                }
            return JsonResponse({'value': True, 'composites': buffer})
        except models.Session.DoesNotExist:
            return JsonResponse({'value': False})
    else:
        return JsonResponse({'value': False})
