from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.chatbot.nlp_engine import OpenRouterEngine

# Create your views here.

class ChatAPIView(APIView):
    """
    API View to handle chat messages.
    """
    def post(self, request, *args, **kwargs):
        user_message = request.data.get('message')

        if not user_message:
            return Response(
                {'error': 'Message not provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Initialize our NLP engine
            engine = OpenRouterEngine()
            # Get the response from the engine
            bot_response = engine.get_response(user_message)

            return Response(
                {'response': bot_response},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
