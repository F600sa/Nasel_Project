from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer, CommentSerializer,AnimalSerializer
from .models import ProfileModel,CommentModel,Animal


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_profile(request: Request):
    '''
    can only add Admin and Developer
    '''
    if not request.user.is_authenticated:
        return Response({"msg": "Sorry, Not Allowed "}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
    NewProfile = ProfileSerializer(data=request.data)
    if NewProfile.is_valid():
        NewProfile.save()
        dataResponse = {
            "msg": "Thank you for record this Profile...",
            "Certification ": NewProfile.data
        }
        return Response(dataResponse)
    else:
        print(NewProfile.errors)
        dataResponse = {"msg": "Sorry, couldn't add new Profile"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request: Request, profile_id):
    '''
    can only update Admin and Developer
    '''
    if not request.user.is_authenticated :
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    profile = ProfileModel.objects.get(id=profile_id)
    updated_profile = ProfileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_profile(request: Request, profile_id):
    '''
        can only delete Admin and Developer
    '''
    if not request.user.is_authenticated :
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    profile = ProfileModel.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg": "Deleted Successfully"})



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_profile(request: Request):
    profile = ProfileModel.objects.all()
    dataResponse = {
        "msg": "List of All profile",
        "Profile": ProfileSerializer(instance=profile, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_comment(request: Request):
    comment = CommentModel.objects.all()
    dataResponse = {
        "msg": "List of All comment",
        "comment": CommentSerializer(instance=comment, many=True).data
    }
    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, comment_id):
    '''
       all can delete a comment
    '''
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
    comment = CommentModel.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request: Request):
    '''
    all can write a comment
    '''
    if not request.user.is_authenticated:
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    new_comment = CommentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        return Response({"comment": new_comment.data})
    else:
        print(new_comment.errors)
    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_Animal(request: Request):

    if not request.user.is_authenticated:
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    new_animal = AnimalSerializer(data=request.data)
    if new_animal.is_valid():
        new_animal.save()
        return Response({"Animal": new_animal.data})
    else:
        print(new_animal.errors)
    return Response("no", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_Animal(request: Request, Animal_id):

    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
    animal = Animal.objects.get(id=Animal_id)
    animal.delete()
    return Response({"msg": "Deleted Successfully"})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_Animal(request: Request):
    animal = Animal.objects.all()
    dataResponse = {
        "msg": "List of All animal",
        "comment": AnimalSerializer(instance=animal, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_Animal(request: Request, Animal_id):

    if not request.user.is_authenticated :
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    animal = Animal.objects.get(id=Animal_id)
    updated_animal = AnimalSerializer(instance=animal, data=request.data)
    if updated_animal.is_valid():
        updated_animal.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_animal.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


