from rest_framework import status as statuses
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SumEndpointSerializer


class SumView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SumEndpointSerializer

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content, status=statuses.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Endpoint that find all of the numbers throughout the given body and add them together.
        """
        serializer = SumEndpointSerializer(data=request.body)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=statuses.HTTP_200_OK)
