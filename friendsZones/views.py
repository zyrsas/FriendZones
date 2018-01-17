import base64
from rest_framework.response import Response
from rest_framework.decorators import api_view
from friendsZones.models import User, Favorites, Block
import uuid
import random
import json
from FriendZones.settings import MEDIA_URL, MEDIA_ROOT
from django.views.decorators.csrf import csrf_protect


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
                                                                        'latitude',
                                                                        'longitude',
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
                elif i == "latitude":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.facebookToken = body["UserData"]['latitude']
                        j.save()
                        print("Update")
                elif i == "longitude":
                    user = User.objects.filter(id=user_id)
                    for j in user:
                        j.facebookToken = body["UserData"]['longitude']
                        j.save()
                        print("Update")

            users = User.objects.filter(id=user_id).values('id',
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
                                                           'latitude',
                                                           'longitude')


            return Response({"DataUser": list(users)[0]})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def AddRemoveBlock(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            is_new_record = False

            if Block.objects.filter(userID=body['user_id'], otherUser=body['other_user_id']).count() == 0:
                new = Block(userID=body['user_id'], otherUser=body['other_user_id'])
                new.save()
                is_new_record = True
            else:
                Block.objects.filter(userID=body['user_id'], otherUser=body['other_user_id']).delete()
                is_new_record = False

            return Response({"is_new_record": is_new_record})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def SendPushNotification(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            isPushSent = False

            if User.objects.filter(id=body['user_id']).count() > 0:
                isPushSent = True
            else:
                isPushSent = False

            return Response({"isPushSent": isPushSent})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})


@api_view(['POST', ])
def inRadius(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)



            from math import radians, cos, sin, asin, sqrt

            def haversine(lon1, lat1, lon2, lat2):
                """
                Calculate the great circle distance between two points 
                on the earth (specified in decimal degrees)
                """
                # convert decimal degrees to radians
                lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

                # haversine formula
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                r = 6371  # Radius of earth in kilometers. Use 3956 for miles
                return c * r

            center_point = [{'lat': -7.7940023, 'lng': 110.3656535}]
            test_point = [{'lat': -7.79457, 'lng': 110.36563}]

            lat1 = center_point[0]['lat']
            lon1 = center_point[0]['lng']
            lat2 = test_point[0]['lat']
            lon2 = test_point[0]['lng']

            radius = 0.005  # in kilometer

            a = haversine(lon1, lat1, lon2, lat2)

            print('Distance (km) : ', a)
            if a <= radius:
                return Response({"InsideArea": True})
            else:
                return Response({"InsideArea": False})


            return Response({"isPushSent": True})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})

@csrf_protect
@api_view(['POST', ])
def uploadPickture(request):
    if request.method == "POST":
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            print(body["image_data"])
            img_name = "img_" + str(body["user_id"]) + ".png"

            fh = open(MEDIA_ROOT + "/" + img_name, "wb")
            fh.write(base64.b64decode(body["image_data"]))
            fh.close()

            base_url = "{0}://{1}{2}{3}".format(request.scheme, request.get_host(), MEDIA_URL, img_name)

            user = User.objects.filter(id=body["user_id"])
            for j in user:
                j.profilePictureURL = base_url
                j.save()
                print("Update")


            return Response({"profile_picure_URL": base_url})
        except KeyError:
            return Response({"Null": "Null"})
        except ValueError:
            return Response({"Null": "Null"})
        except:
            return Response({"Null": "Null"})
