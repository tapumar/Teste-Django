from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import  Choice, Question, Vote
from .serializers import ChoiceSerializer, QuestionSerializer

# ...
# PollList and PollDetail views

class ChoiceList(generics.ListCreateAPIView):
    """
    Retorna a lista de escolhas da questão.
    """
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

class VoteView(generics.ListCreateAPIView):
    """
    get retorna a lista com todos os votos.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'question_detail.html'


    def post(self, request, pk, choice_pk):
        #voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk,
                'poll': pk,
                #'voted_by': voted_by,
                'question': question_pk}
        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class CreateQuestion(generics.ListCreateAPIView):
    """
    get retorna a lista com todas as questões.
    """
    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')
        
    def post(self, request, pk, choice_pk):
        #voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk,
                'poll': pk,
                #'voted_by': voted_by,
                'question': question_pk}
        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
