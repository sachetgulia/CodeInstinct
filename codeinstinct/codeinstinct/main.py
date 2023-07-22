from rest_framework import generics, status
from rest_framework.response import Response


class HealthCheckView(generics.GenericAPIView):
    def get(self, request):
        """
        Health check endpoint to check server health.
        """
        return Response({"status": "Instincts are Healthy"}, status=status.HTTP_200_OK)
