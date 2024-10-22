from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.models import Notes
from .serializers import NotesSerializer
from rest_framework import status



from django.contrib.auth import authenticate
from rest_framework import status










@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/note_title',
        'GET /api/names/:id'

    ]
    return Response(routes)

@api_view(['GET'])
def getNames(request):
    notes=Notes.objects.all()
    serializer=NotesSerializer(notes,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    serializer = NotesSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    


@api_view(['GET', 'PUT', 'DELETE'])
def detailData(request, id, format=None):
    try:
        note = Notes.objects.get(pk=id)
    except Notes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotesSerializer(note)
        return Response(serializer.data)

    
    elif request.method == 'PUT':
        serializer = NotesSerializer(data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
