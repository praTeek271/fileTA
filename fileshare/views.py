# fileshare/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['post'])
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def upload_file(self, request):
        serializer = FileSerializer(data={'file': request.FILES.get('file')})

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def download_file(self, request, pk=None):
        file_instance = self.get_object()

        if request.user != file_instance.user:
            return Response({"message": "Access denied"}, status=status.HTTP_403_FORBIDDEN)

        special_url = file_instance.generate_special_url()

        return Response({"download_link": special_url, "message": "success"})

    def extract_user_from_token(self, special_token):
        try:
            from django.core.signing import Signer
            signer = Signer()
            user = signer.unsign(special_token)
            return user
        except Exception as e:
            return None

    def extract_file_type(self, uploaded_file):
        return uploaded_file.name.split('.')[-1].lower() if uploaded_file else ''
