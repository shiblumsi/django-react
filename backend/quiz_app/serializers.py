from rest_framework import serializers
from .models import Question, ChoiceOption, AnswerQuestion, ResultQuiz


class ChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOption
        fields = ['id', 'option']


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


class QuestionSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ResultSerializer(serializers.Serializer):
    question_options = serializers.DictField(
        child=serializers.IntegerField(),
        allow_empty=True
    )


class ResultQuizSerializer(serializers.ModelSerializer):
    selected_option = serializers.StringRelatedField()

    class Meta:
        model = ResultQuiz
        fields = ['selected_option', 'is_currect']


class ResultQuizSerializer2(serializers.ModelSerializer):
    choices = ChoiceOptionSerializer(many=True, source='options')
    answer = AnswerQuestionSerializer(source='answer_question')
    rqs = ResultQuizSerializer(many=True,source='result_quizzes')

    class Meta:
        model = Question
        fields = ['id', 'question', 'choices', 'answer','rqs']