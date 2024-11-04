import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GenerateImageSerializer
from .service import ReplicateService

# Set up logging
logger = logging.getLogger(__name__)

class GenerateImageView(APIView):
    def post(self, request):
        serializer = GenerateImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        prompt = serializer.validated_data["prompt"]
        width = serializer.validated_data["width"]
        height = serializer.validated_data["height"]

        try:
            # Call the synchronous method directly
            image_url = ReplicateService.generate_image(prompt, width, height)
            return Response({"generated_image_url": image_url}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error generating image: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
