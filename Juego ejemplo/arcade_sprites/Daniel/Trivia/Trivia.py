from pathlib import Path
import random as rdm

QUESTIONS_FILE = "questions.txt"
QUESTIONS_DIR = "questions"

DEFAULT_QUESTION = "Is this a default question?"
DEFAULT_ANSWERS = ("Yes", "No")

SEPARATOR = "|"
ENCODING = "utf-8"

question_list = []

def write_default_questions_file(file):

    string_buffer = DEFAULT_QUESTION

    for answer in DEFAULT_ANSWERS:
        string_buffer += SEPARATOR + answer

    file.write_text(string_buffer, encoding = ENCODING)

def read_questions_file(file: Path):

    with file.open("r", encoding = ENCODING) as f:

        for line in f:

            line.strip()
            if not line:
                continue

            question_list.append(get_question(line))

def get_question(question_line: str) -> dict:

    question_data = question_line.split(SEPARATOR)

    if len(question_data) < 3:
        raise ValueError("Questions file is not valid!")

    question = question_data[0]
    answers = question_data[1:]

    return {
        "question": question,
        "correct": answers[0],
        "answers": answers
    }

def shuffle_questions() -> list:

    question_list_buffer = question_list

    rdm.shuffle(question_list_buffer)

    for question in question_list_buffer:
        rdm.shuffle(question["answers"])

    return question_list_buffer

def show_answers(question: dict) -> int:

    letters_min = 97
    letters_max = 122

    answers = question["answers"]
    correct = question["correct"]

    current_letter = letters_min

    current_answer_id = 0
    correct_letter = -1

    while current_letter < (letters_max + 1) and current_answer_id < len(answers):

        current_answer = str(answers[current_answer_id]).strip()

        print(f"{chr(current_letter)}) {current_answer}")

        if current_answer == correct:
            correct_letter = current_letter

        current_answer_id += 1
        current_letter += 1

    return correct_letter

def init_game() -> None:

    path = Path(QUESTIONS_DIR)
    path.mkdir(parents = True, exist_ok = True)

    file_path = path / QUESTIONS_FILE

    if not file_path.exists():
        write_default_questions_file(file_path)

    read_questions_file(file_path)
    shuffle_questions()

def start_game() -> None:

    init_game()
    question_pool = shuffle_questions()

    score = 0

    print("Welcome to the Trivia Game!\n")

    for i in range(0, len(question_pool)):

        score += start_round(question_pool, i)
        print()

    print(f"Your final score is: {score}")

def start_round(question_pool: list, current: int) -> int:

    current_question = question_pool[current]["question"]

    print(f"Question {current + 1}: {current_question}")
    print("Choose an answer by typing its letter:")

    correct_letter = show_answers(question_pool[current])
    user_answer = input("> ")

    return 5 if user_answer.lower() == chr(correct_letter) else 0

start_game()