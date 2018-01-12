from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from friendsZones.models import User


@api_view(['POST', ])
def SignIn(request):
    if request.method == "POST":
        try:
            if User.objects.filter(name=request.GET.get('user'),
                                   password=request.GET.get('pass')).count() == 0:
                return Response({"Null": "Null"}, )
            else:
                if request.GET.get('regID') != None:
                    reg_ID = User.objects.filter(name=request.GET.get('user'), password=request.GET.get('pass'))
                    print(list(reg_ID))
                    for i in reg_ID:
                        i.regID = request.GET.get('regID')
                        i.save()
                        print("Update")
                data_for_json = User.objects.filter(name=request.GET.get('user')).values('id',
                                                                                         'name',
                                                                                         'departmen_id',
                                                                                         'departmen__name',
                                                                                         'access'
                                                                                         )
                tmp = list(data_for_json)[0]

                return Response(tmp)
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})
