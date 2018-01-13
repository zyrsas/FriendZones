from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from friendsZones.models import User, Favorites
import uuid
import random
import json


@api_view(['POST', ])
def SignIn(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            if User.objects.filter(facebookToken=body['FacebookToken']).count() == 0:
                token = str(uuid.uuid1(random.randint(0, 281474976710655)))

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


@api_view(['POST', ])
def AddRemoveFavorites(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            is_new_record = False

            if Favorites.objects.filter(userID=body['user_id'], otherUser=body['other_user_id']).count() == 0:
                new = Favorites(userID=body['user_id'], otherUser=body['other_user_id'])
                new.save()
                is_new_record = True
            else :
                Favorites.objects.filter(userID=body['user_id'], otherUser=body['other_user_id']).delete()
                is_new_record = False

            return Response({"is_new_record": is_new_record})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def GetAllFavorites(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            response = Favorites.objects.filter(userID=body['user_id']).values('otherUser')

            response_users = []
            for item in response:
                users = User.objects.filter(id=item['otherUser']).values(
                                                                        'id',
                                                                        'name',
                                                                        'gender',
                                                                        'lookingFor',
                                                                        'radius',
                                                                        'isNotification',
                                                                        'isBeacon',
                                                                        'subscriptionDate',
                                                                        'biography',
                                                                        'profilePictureURL',
                                                                        'AuthenticationToken',
                                                                        'facebookToken',
                                                                        )
                response_users.append(list(users))

            return Response({"User": response_users})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def UpdateUser(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user_id = body['user_id']

            for i in body["UserData"]:
                if i == "name":
                    print(body["UserData"]['name'])
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.name = body["UserData"]['name']
                        j.save()
                        print("Update")
                elif i == "biography":
                    print(body["UserData"]['biography'])
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.biography = body["UserData"]['biography']
                        j.save()
                        print("Update")
                elif i == "gender":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.gender = body["UserData"]['gender']
                        j.save()
                        print("Update")
                elif i == "lookingFor":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.lookingFor = body["UserData"]['lookingFor']
                        j.save()
                        print("Update")
                elif i == "isNotification":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.isNotification = body["UserData"]['isNotification']
                        j.save()
                        print("Update")
                elif i == "subscriptionDate":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.subscriptionDate = body["UserData"]['subscriptionDate']
                        j.save()
                        print("Update")
                elif i == "profilePictureURL":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.profilePictureURL = body["UserData"]['profilePictureURL']
                        j.save()
                        print("Update")
                elif i == "isBeacon":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.isBeacon = body["UserData"]['isBeacon']
                        j.save()
                        print("Update")
                elif i == "AuthenticationToken":
                    print(body["UserData"]['AuthenticationToken'])
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.AuthenticationToken = body["UserData"]['AuthenticationToken']
                        j.save()
                        print("Update")
                elif i == "radius":
                    print(body["UserData"]['AuthenticationToken'])
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.AuthenticationToken = body["UserData"]['AuthenticationToken']
                        j.save()
                        print("Update")
                elif i == "facebookToken":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.facebookToken = body["UserData"]['facebookToken']
                        j.save()
                        print("Update")

            users = User.objects.filter(id=user_id).values('id', 'name', 'gender', 'lookingFor', 'radius',
                'isNotification', 'isBeacon', 'subscriptionDate', 'biography', 'profilePictureURL',
                'AuthenticationToken', 'facebookToken', )


            return Response({"DataUser": list(users)[0]})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})