from rest_framework import serializers
from ..models import SurveyQuestion
from rest_framework.validators import UniqueValidator
import re

"""
    Basicamente aqui se declara y valida el tipo de pregunta que se va a realizar junto con las opciones de
    las preguntas y la forma de calcular el score a partir de las respuestas.
"""

class SelectQuestionSerializer(serializers.Serializer):
    options = serializers.ListField(child=serializers.CharField())
    multiple = serializers.BooleanField(default=False)
    options_score = serializers.DictField(child=serializers.FloatField())

    def validate(self, data):
        for option in data["options_score"]:
            if option not in data["options"]:
                raise serializers.ValidationError("Option score not found in options")
        return data


def validate_select_question(data):
    data = SelectQuestionSerializer(data=data)
    if data.is_valid():
        return data
    else:
        raise serializers.ValidationError(data.errors)


class NumericQuestionSerializer(serializers.Serializer):
    type_score = serializers.ChoiceField(
        choices=["RANGES", "UPPER_THRESHOLDS", "LOWER_THRESHOLDS"]
    )
    scores_schema = serializers.DictField(child=serializers.FloatField())

    def validate(self, data):
        if data["type_score"] == "RANGES":
            for key in data["scores_schema"].keys():
                if not re.match(r"^\[(-?\d+|-inf),(-?\d+|inf)\]$", key):
                    raise serializers.ValidationError("Invalid range")
        elif data["type_score"] == "THRESHOLDS":
            for key in data["scores_schema"].keys():
                if key.isdigit():
                    raise serializers.ValidationError("Invalid threshold")
        return data


def validate_numeric_question(data):
    data = NumericQuestionSerializer(data=data)
    if data.is_valid():
        return data
    else:
        raise serializers.ValidationError(data.errors)


def validate_percentage_question(data):
    data = NumericQuestionSerializer(data=data)
    if data.is_valid():
        return data
    else:
        raise serializers.ValidationError(data.errors)


class TextQuestionSerializer(serializers.Serializer):
    max_length = serializers.IntegerField()
    ai_analysis = serializers.BooleanField(default=False)

    def validate(self, data):
        if data["max_length"] < 0:
            raise serializers.ValidationError("Max length must be greater than 0")
        return data


def validate_text_question(data):
    data = TextQuestionSerializer(data=data)
    if data.is_valid():
        return data
    else:
        raise serializers.ValidationError(data.errors)


class YesNoQuestionSerializer(serializers.Serializer):
    yes_score = serializers.FloatField()
    no_score = serializers.FloatField()


def validate_yes_no_question(data):
    data = YesNoQuestionSerializer(data=data)
    if data.is_valid():
        return data
    else:
        raise serializers.ValidationError(data.errors)


def calculate_score_select(question, answer):
    question_config = question["question_config"]
    if question_config["multiple"]:
        return sum(
            [question_config["options_score"][option] for option in answer.split(",")]
        )
    return question_config["options_score"][answer]


def calculate_score_numeric(question, answer):
    question_config = question["question_config"]
    answer = float(answer)

    if question_config["type_score"] == "RANGES":
        for key in question_config["scores_schema"].keys():
            min_value, max_value = map(float, key[1:-1].split(","))
            if min_value <= answer < max_value:
                return question_config["scores_schema"][key]
        return 0
    elif question_config["type_score"] == "UPPER_THRESHOLDS":
        for key in question_config["scores_schema"].keys():
            if answer <= int(key):
                return question_config["scores_schema"][key]
        return 0
    elif question_config["type_score"] == "LOWER_THRESHOLDS":
        for key in question_config["scores_schema"].keys():
            if answer >= int(key):
                return question_config["scores_schema"][key]

        return 0


def calculate_score_percentage(question, answer):
    return calculate_score_numeric(question, answer)


def calculate_score_text(question, answer):
    # TODO: Implement AI analysis
    return 0


def calculate_score_yes_no(question, answer):
    if answer == "YES":
        return question["question_config"]["yes_score"]
    return question["question_config"]["no_score"]


def calculate_score(question, answer):
    validators = {
        "SELECT": calculate_score_select,
        "NUMERIC": calculate_score_numeric,
        "PERCENTAGE": calculate_score_percentage,
        "TEXT": calculate_score_text,
        "YES_NO": calculate_score_yes_no,
    }

    return validators[question["type_question"]](question, answer)


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = "__all__"

    def validate(self, data):
        validators = {
            "SELECT": validate_select_question,
            "NUMERIC": validate_numeric_question,
            "PERCENTAGE": validate_percentage_question,
            "TEXT": validate_text_question,
            "YES_NO": validate_yes_no_question,
        }
        validation = validators[data["type_question"]](data["question_config"])

        if validation and validation.is_valid():
            return data
        else:
            raise serializers.ValidationError("Invalid question config")
