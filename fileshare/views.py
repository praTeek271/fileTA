# fileshare/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.signing import Signer
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['post'])
    @authentication_classes([TokenAuthentication])  # Use TokenAuthentication
    @permission_classes([IsAuthenticated])  # Require authentication
    def upload_file(self, request):
        # Extract user from the special token obtained during login
        user = self.extract_user_from_token(request.auth.payload.get('special_token', ''))
        
        # Extract file_type from the uploaded file
        file_type = self.extract_file_type(request.FILES.get('file'))

        # If user or file_type extraction fails, return a 400 response
        if not user or not file_type:
            return Response({"message": "Invalid special token or file type"}, status=status.HTTP_400_BAD_REQUEST)

        # Add the extracted information to the request data
        request.data['file_type'] = file_type
        request.data['user'] = user

        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def extract_user_from_token(self, special_token):
        # You need to implement the logic to extract user from the special token
        # For example, you can use Django's Signer for simplicity in this example
        try:
            signer = Signer()
            user = signer.unsign(special_token)
            return user
        except Exception as e:
            # Handle the exception (e.g., invalid token)
            return None

    def extract_file_type(self, uploaded_file):
        # Extract file_type from the uploaded file
        # This is just a basic example, you might need a more robust method
        if uploaded_file:
            return uploaded_file.name.split('.')[-1].lower()  # Get the file extension
        return ''
