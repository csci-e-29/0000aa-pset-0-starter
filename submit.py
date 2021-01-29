import json
import os
from pprint import pprint
from typing import List, Dict

from canvasapi import Canvas
from canvasapi.quiz import QuizSubmissionQuestion, QuizSubmission
from environs import Env
from git import Repo

import hashlib

from fibonacci import optimized_fibonacci
from fibonacci import SummableSequence
from fibonacci import last_8
from pyramid import print_pyramid
from test_pset import capture_print


def pyramid_extract(rows):
    """Returns string equivalent to what print_pyramid() prints
    Employs capture_print() as provided in test_pset.py
    """
    with capture_print() as std:
        print_pyramid(rows)
    std.seek(0)
    return std.read()


def get_answers(questions: List[QuizSubmissionQuestion]) -> List[Dict]:
    """Creates answers for Canvas quiz questions"""

    answer_0 = {
        "fib_100000": last_8(optimized_fibonacci(100000)),
        "summable_5_7_11_100000": last_8(SummableSequence(5, 7, 11)(100000)),
        "summable_0_1_100000": last_8(SummableSequence(0, 1)(100000)),
        "fib_234202": last_8(optimized_fibonacci(234202)),
        "summable_8_9_99_141515": last_8(SummableSequence(8, 9, 99)(141515)),
        "summable_5_98_7_35_2_603": last_8(SummableSequence(5, 98, 7, 35, 2)(603)),
    }
    answer_1 = {
        "pyramid_24": hashlib.sha256(pyramid_extract(24).encode()).hexdigest()[:8],
        "pyramid_53": hashlib.sha256(pyramid_extract(53).encode()).hexdigest()[:8],
    }
    answer_2 = 8610

    answers = [answer_0, answer_1, answer_2]

    results = []
    for i in range(len(questions)):
        results.append({"id": questions[i].id, "answer": answers[i]})
    return results


def get_submission_comments(repo: Repo, qsubmission: QuizSubmission) -> Dict:
    """Get some info about this submission"""
    return dict(
        hexsha=repo.head.commit.hexsha[:8],
        submitted_from=repo.remotes.origin.url,
        dt=repo.head.commit.committed_datetime.isoformat(),
        branch=os.environ.get("TRAVIS_BRANCH", None),  # repo.active_branch.name,
        is_dirty=repo.is_dirty(),
        quiz_submission_id=qsubmission.id,
        quiz_attempt=qsubmission.attempt,
        travis_url=os.environ.get("TRAVIS_BUILD_WEB_URL", None),
    )


if __name__ == "__main__":

    repo = Repo(".")

    # Load environment
    env = Env()

    course_id = env.int("CANVAS_COURSE_ID")
    assignment_id = env.int("CANVAS_ASSIGNMENT_ID")
    quiz_id = env.int("CANVAS_QUIZ_ID")
    as_user_id = env.int("CANVAS_AS_USER_ID", 0)  # Optional - for test student

    if as_user_id:
        masquerade = dict(as_user_id=as_user_id)
    else:
        masquerade = {}

    if repo.is_dirty() and not env.bool("ALLOW_DIRTY", False):
        raise RuntimeError(
            "Must submit from a clean working directory - commit your code and rerun"
        )

    # Load canvas objects
    canvas = Canvas(env.str("CANVAS_URL"), env.str("CANVAS_TOKEN"))
    course = canvas.get_course(course_id, **masquerade)
    assignment = course.get_assignment(assignment_id, **masquerade)
    quiz = course.get_quiz(quiz_id, **masquerade)

    # Begin submissions
    url = "https://github.com/csci-e-29/2021sp-pset-0-stuartneilson/commit/master".format(
        os.path.basename(repo.working_dir), repo.head.commit.hexsha
    )  # you MUST push to the classroom org, even if CI/CD runs elsewhere (you can push anytime before peer review begins)

    qsubmission = None
    try:
        # Attempt quiz submission first - only submit assignment if successful
        qsubmission = quiz.create_submission(**masquerade)
        questions = qsubmission.get_submission_questions(**masquerade)

        # Get some basic info to help develop
        for q in questions:
            print("{} - {}".format(q.question_name, q.question_text.split("\n", 1)[0]))

            # MC and some q's have 'answers' not 'answer'
            pprint(
                {
                    k: getattr(q, k, None)
                    for k in ["question_type", "id", "answer", "answers"]
                }
            )

            print()

        # Submit your answers
        answers = get_answers(questions)
        pprint(answers)
        responses = qsubmission.answer_submission_questions(
            quiz_questions=answers, **masquerade
        )

    finally:
        if qsubmission is not None:
            completed = qsubmission.complete(**masquerade)

            # Only submit assignment if quiz finished successfully
            submission = assignment.submit(
                dict(
                    submission_type="online_url",
                    url=url,
                ),
                comment=dict(
                    text_comment=json.dumps(get_submission_comments(repo, qsubmission))
                ),
                **masquerade,
            )

    pass
