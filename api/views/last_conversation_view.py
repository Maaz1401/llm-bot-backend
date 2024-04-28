from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Session, Message

class LastConversationView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk=None, format=None):
        session = Session.objects.filter(user=request.user).last()

        messages = list(session.messages.all().values('role','content', 'message_type','document'))
        print(messages)

        response_data = {
            'session': session.id,
            'messages': messages
        }

        return Response(status=status.HTTP_200_OK, data=response_data)
