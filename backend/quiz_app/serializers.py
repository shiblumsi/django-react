from rest_framework import serializers
from .models import Question, ChoiceOption


class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = ['option']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceOptionSerializer(many=True, source='choiceoption_set')

    class Meta:
        model = Question
        fields = ['id', 'question', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choiceoption_set')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            ChoiceOption.objects.create(question=question, **choice_data)
        return question
