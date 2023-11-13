from dataclasses import dataclass


@dataclass
class Question:
    """Question dataclass"""

    question_text: str
    question_answer: str
