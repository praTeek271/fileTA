# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=True, methods=['get'])
    def download_file(self, request, pk=None):
        file_instance = self.get_object()
        if request.user != file_instance.user:
            return Response({"message": "Access denied"}, status=403)

        # Logic to generate and encrypt download link
        download_link = "generate_secure_download_link_here"

        return Response({"download-link": download_link, "message": "success"})
