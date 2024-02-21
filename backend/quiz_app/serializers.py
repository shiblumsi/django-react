from rest_framework import serializers
from .models import Question, ChoiceOption, AnswerQuestion


class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = ['option']


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = ['answer']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceOptionSerializer(many=True, source='options')
    answer = AnswerQuestionSerializer(source='answer_question')

    class Meta:
        model = Question
        fields = ['id', 'question', 'choices', 'answer']

    def create(self, validated_data):
        choices_data = validated_data.pop('options')
        answer_data = validated_data.pop('answer_question')

        question = Question.objects.create(**validated_data)
        AnswerQuestion.objects.create(answer=answer_data, question=question)

        for choice_data in choices_data:
            ChoiceOption.objects.create(question=question, **choice_data)

        return question
