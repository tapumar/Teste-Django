from rest_framework import serializers
from .models import Question, Choice#, Vote, Poll


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question_text',
            'pub_date',
        )
        model = Question

# class VoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vote
#         fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    # votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


# class PollSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True, required=False)
#
#     class Meta:
#         model = Poll
#         fields = '__all__'
