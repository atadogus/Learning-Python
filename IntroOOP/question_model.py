from data import question_data


class Question:
    def __init__(self, question_index):
        self.question = question_data[question_index]["text"]  # first index is to select the dictionary in the list and the second index is to find the specific value stored in the dic. by entering the key
        self.answer = question_data[question_index]["answer"]
