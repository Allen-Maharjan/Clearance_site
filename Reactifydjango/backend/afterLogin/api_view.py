# from rest_framework import serializers
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .serializer import InfoModelSerializer
# from accounts.models import Clearance


# class InfoClassBasedView(APIView):

#     def get(self, request, *args, **kwargs):
#         qs = Clearance.objects.all()
#         serializer = InfoModelSerializer(instance=qs, many=True)
#         return Response(serializer.data)
from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView)

from .serializer import InfoModelSerializer
from accounts.models import Clearance


class ClearanceModelCreateApiView(CreateAPIView):
    serializer_class = InfoModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        print('serializer is save')


class ClearanceModelListApiView(ListAPIView):
    queryset = Clearance.objects.all()
    serializer_class = InfoModelSerializer


class ClearanceModelDestroyApiView(DestroyAPIView):
    queryset = Clearance.objects.all()


class ClearanceModelUpdateAPIView(UpdateAPIView):
    queryset = Clearance.objects.all()
    serializer_class = InfoModelSerializer


class ClearanceModelRetrieveAPIView(RetrieveAPIView):
    queryset = Clearance.objects.all()
    serializer_class = InfoModelSerializer
