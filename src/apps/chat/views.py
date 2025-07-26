from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.chatbot.nlp_engine import OpenRouterEngine

def chat_view(request):
    """
    Renderiza la página de la interfaz de chat.
    """
    return render(request, 'chat/chat.html')


class ChatAPIView(APIView):
    """
    API View to handle chat messages with context.
    """
    def post(self, request, *args, **kwargs):
        user_message = request.data.get('message')

        if not user_message:
            return Response(
                {'error': 'Message not provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        conversation_history = request.session.get('conversation_history', [])

        conversation_history.append({"role": "user", "content": user_message})

        try:
            engine = OpenRouterEngine()
            bot_response = engine.get_response(conversation_history)

            conversation_history.append({"role": "assistant", "content": bot_response})

            request.session['conversation_history'] = conversation_history[-10:]

            return Response(
                {'response': bot_response},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            conversation_history.pop()
            request.session['conversation_history'] = conversation_history

            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
