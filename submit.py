import json
import os
from datetime import timezone, timedelta, datetime
from pprint import pprint
from typing import List, Dict

from canvasapi import Canvas
from canvasapi.quiz import QuizSubmissionQuestion, QuizSubmission
from environs import Env
from git import Repo


def get_answers(questions: List[QuizSubmissionQuestion]) -> List[Dict]:
    """Creates answers for Canvas quiz questions"""
    # Formulate your answers - see docs for QuizSubmission.answer_submission_questions below
    # It should be a list of dicts, one per q, each with an 'id' and 'answer' field
    # The format of the 'answer' field depends on the question type
    # You are responsible for collating questions with the functions to call - do not hard code
    raise NotImplementedError()
    # eg {"id": questions[0].id, "answer": {key: some_func(key) for key in questions[0].answer.keys()}}


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
    as_test_student = env.bool(
        "CANVAS_AS_TEST_STUDENT", False
    )  # Ignore - for faculty testing

    late_days = env.int(
        "LATE_SUBMISSION_DAYS", 0
    )  # Prevents builds after the submission deadline

    if repo.is_dirty() and not env.bool("ALLOW_DIRTY", False):
        raise RuntimeError(
            "Must submit from a clean working directory - commit your code and rerun"
        )

    # Load canvas objects
    canvas = Canvas(env.str("CANVAS_URL"), env.str("CANVAS_TOKEN"))
    course = canvas.get_course(course_id)

    # Masquerade as a student (for faculty testing)
    if as_test_student:
        test_student = course.get_users(enrollment_type=["student_view"])[0]
        masquerade = dict(as_user_id=test_student.id)
    else:
        masquerade = {}

    assignment = course.get_assignment(assignment_id, **masquerade)
    quiz = course.get_quiz(quiz_id, **masquerade)

    # Begin submissions
    url = "https://github.com/csci-e-29/{}/commit/{}".format(
        os.path.basename(repo.working_dir), repo.head.commit.hexsha
    )  # you MUST push to the classroom org, even if CI/CD runs elsewhere (you can push anytime before peer review begins)

    qsubmission = None

    if datetime.now(timezone.utc) > (
        assignment.due_at_date + timedelta(days=late_days, minutes=30)
    ):
        # If you accidentally trigger a build after the deadline, this
        # code will rerun - and mark your submissions late!  Therefore it
        # is best to error out unless you intend to submit late
        raise RuntimeError(
            "Assignment past due, will not submit. Set LATE_SUBMISSION_DAYS if you want to submit late"
        )

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
