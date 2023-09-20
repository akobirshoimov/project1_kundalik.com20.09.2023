from django.shortcuts import render,get_object_or_404
from .serializer import KundalikSerializer
from .models import KundalikModel
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class ListAPIView(APIView):
    def get(self,request):
        if str(request.user) == 'AnonymousUser':
            return Response({'please log in '})

        all = KundalikModel.objects.filter(status = True)
        serializer = KundalikSerializer(all,many = True)
        return Response(serializer.data)
    
class CreateAPIView(APIView):
    def post(self,request,*args,**kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:
                serializer = KundalikSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.sava()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'only director can create this'})
        return Response({'only director can create this'})
    
class UpdateAPIView(APIView):
    def patch(self,request,*args,**kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                info = get_object_or_404(KundalikModel,id = kwargs['kundalik_id'])
                serializer = KundalikSerializer(info,data=request.data,partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            return Response({'only teacher can update this'})
        return Response({'only teacher can update this'})
    
    
    

