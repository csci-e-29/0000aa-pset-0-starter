from environs import Env
from canvasapi import Canvas


if __name__ == "__main__":

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

    # Load canvas objects
    canvas = Canvas(env.str("CANVAS_URL"), env.str("CANVAS_TOKEN"))
    course = canvas.get_course(course_id, **masquerade)
    assignment = course.get_assignment(assignment_id, **masquerade)
    quiz = course.get_quiz(quiz_id, **masquerade)

    # Begin submissions
    assignment.submit(
        dict(
            submission_type="online_url",
            url="asdf",
        ),
        **masquerade
    )
    qsubmission = None
    try:
        qsubmission = quiz.create_submission(**masquerade)
        questions = qsubmission.get_submission_questions(**masquerade)
        # pivoted = {q.question_name: q for q in questions}
        # answers = [{"id": pivoted["Question 2"].id, "answer": "111"}]

        responses = qsubmission.answer_submission_questions(
            quiz_questions=answers, **masquerade
        )

    finally:
        if qsubmission is not None:
            qsubmission.complete(**masquerade)

    pass
