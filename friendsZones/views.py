from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from friendsZones.models import User
import uuid
import random
import json


@api_view(['POST', ])
def SignIn(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print(body['FacebookToken'])
            if User.objects.filter(facebookToken=body['FacebookToken']).count() == 0:

                token = str(uuid.uuid1(random.randint(0, 281474976710655)))
                print(token)

                new = User(facebookToken=str(body['FacebookToken']), AuthenticationToken=token)
                new.save()

            user = User.objects.filter(facebookToken=body['FacebookToken']).values(
                                                                                    'AuthenticationToken',
                                                                                    'id'
                                                                                   )
            return Response(list(user)[0])
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})
