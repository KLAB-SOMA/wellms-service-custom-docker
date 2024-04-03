from course import Course
from middleware import Middleware

def test_quiz():
    middleware = Middleware("admin")
    course_handler = Course(middleware)
    course_handler.test_list_courses()

if __name__ == "__main__":
    test_quiz()