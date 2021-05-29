from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from .serializers import imagedataserializers
from rest_framework.response import Response
from rest_framework import status
from .models import imagedata
from django.http.response import JsonResponse
from django.conf.urls import url

#
serializer_class = imagedataserializers
@api_view(["GET","POST"])

def show_list(request):
    if request.method=="GET":
         k = len(imagedata.objects.all())
         start = k - 100
         if k < 100:
            start = 0
         data = imagedata.objects.all()[start:k][::-1]
         serializers = imagedataserializers(data,many=True)
         return Response(serializers.data)
    elif request.method=="POST":
        serializers = imagedataserializers(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            k = len(imagedata.objects.all())
            start = k-2
        if k<2:
            start = 0
        returnobject = imagedataserializers(imagedata.objects.all()[start:k][::-1],many = True)
        return Response(returnobject.data,status=status.HTTP_201_CREATED)
    return Response({"msg":"User already present"},status=status.HTTP_400_BAD_REQUEST)




@api_view(["GET", "PATCH"])
def show_id(request, id):
      if request.method == "GET":
        try:
            data = imagedata.objects.get(id=id)
            if request.method == "GET":
                serializers = imagedataserializers(data)
                return JsonResponse(serializers.data)
        except:
            return JsonResponse({'message': 'The Field does not exist'}, status=status.HTTP_404_NOT_FOUND)
      elif request.method == "PATCH":
          if imagedata.objects.filter(id=id).exists():
              if (request.method == "PATCH"):
                  imagedata.objects.filter(id=id).update(caption=request.data['caption'], url=request.data['url'])
                  return Response({'message': 'Updation successful'}, status=status.HTTP_200_OK)
              else:
                  Response({'message': 'Wrong request'}, status=status.HTTP_400_BAD_REQUEST)
          else:
              return Response({'message': 'The Field does not exist'}, status=status.HTTP_400_BAD_REQUEST)
