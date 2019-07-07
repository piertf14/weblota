from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from local.utils import ReadOnly
from reserve.serializers import ReserveSerializer
from socceruser.utils import get_access_token


class ReserveAPI(APIView):
    permission_classes = (ReadOnly, )

    def post(self, request, format=None):
        request_data = request.data
        user = get_access_token(request).user
        request_data.update({"user": user.id})
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
