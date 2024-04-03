import requests
from icecream import ic
import json as j
import datetime
import logging
import os


API_URL = "http://api.localhost:1001/api/"

ADMIN_PREFIX = "admin/"
AUTH_PREFIX = "auth/"
COURSE_PREFIX = "courses/"
LESSON_PREFIX = "lessons/"
TOPIC_PREFIX = "topics/"
QUIZ_PREFIX = "gift-quizes/"
QUIZ_QUESTIONS_PREFIX = "quiz-questions/"
QUIZ_ANSWERS_PREFIX = "quiz-answers/"
QUIZ_ATTEMPTS_PREFIX = "quiz-attempts/"


authentication = None


logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


# Build the authentication headers with JWT's token
def build_authentication_headers():
    global authentication
    return {
        "Authorization": "Bearer "+authentication
    }

# Athentication in the API
def authenticate():
    global authentication
    credentials_data = j.load(open("mockdata/" + "admin" + "_credentials.json"))
    print()
    LOGIN_ENDPOINT = API_URL+AUTH_PREFIX+"login"
    response = requests.post(LOGIN_ENDPOINT, data=credentials_data)
    assert response.status_code == 200
    data = response.json()
    logging.debug("Response data: %s", data)
    assert data["data"]["token"] is not None
    authentication = data["data"]["token"]

# ??????? What is enquires?? Just ignore it for now !
def course_access_enquires():
    COURSE_ACCESS_ENQUIRES = API_URL+ADMIN_PREFIX+"course-access-enquires"
    headers = build_authentication_headers()
    response = requests.get(COURSE_ACCESS_ENQUIRES, headers=headers)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)

# List all courses
def list_courses():
    COURSES = API_URL+ADMIN_PREFIX+COURSE_PREFIX
    headers = build_authentication_headers()
    print(COURSES, headers)
    response = requests.get(COURSES, headers=headers)
    print(response)
    assert response.status_code == 200
    data = response.json()
    logging.debug("Response data: %s", data)
    assert (len(data['data']) > 0)
    ic(len(data['data']))
    #ic(data['data'])

def create_course():
    global course_creation_data
    COURSES = API_URL+ADMIN_PREFIX+COURSE_PREFIX
    headers = build_authentication_headers()
    ic(course_creation_data)
    response = requests.post(COURSES, headers=headers, json=course_creation_data)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    #ic(data)
    logging.debug("Response data: %s", data)

def delete_course(course_id):
    COURSES = API_URL+ADMIN_PREFIX+COURSE_PREFIX+str(course_id)
    headers = build_authentication_headers()
    response = requests.delete(COURSES, headers=headers)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)

def create_lesson(course_id):
    global lesson_creation_data
    LESSONS = API_URL+ADMIN_PREFIX+LESSON_PREFIX
    headers = build_authentication_headers()
    lesson_creation_data['course_id'] = course_id
    ic(lesson_creation_data)
    response = requests.post(LESSONS, headers=headers, json=lesson_creation_data)
    #assert response.status_code == 200
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)

def create_topic(topic_creation_data): # gift quiz is a implementation of a topic
    TOPICS = API_URL+ADMIN_PREFIX+TOPIC_PREFIX
    headers = build_authentication_headers()
    ic(topic_creation_data)
    response = requests.post(TOPICS, headers=headers, json=topic_creation_data)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)
    pass

def create_quiz_question():
    global gift_quiz_creation_data
    QUIZ_QUESTIONS = API_URL+ADMIN_PREFIX+QUIZ_QUESTIONS_PREFIX
    headers = build_authentication_headers()
    ic(gift_quiz_creation_data)
    response =  requests.get(QUIZ_QUESTIONS, headers=headers, json=gift_quiz_creation_data)
    data = response.json()
    ic(data)

def list_topics():
    TOPICS = API_URL+ADMIN_PREFIX+TOPIC_PREFIX
    headers = build_authentication_headers()
    response = requests.get(TOPICS, headers=headers)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)
    # save the response json to a json file
    with open('topics.json', 'w') as f:
        f.write(str(data))

def see_course(course_id):
    COURSES = API_URL+ADMIN_PREFIX+COURSE_PREFIX+str(course_id)
    headers = build_authentication_headers()
    response = requests.get(COURSES, headers=headers)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)

def see_gift_quiz(quiz_id):
    QUIZ = API_URL+ADMIN_PREFIX+QUIZ_PREFIX+str(quiz_id)
    headers = build_authentication_headers()
    response = requests.get(QUIZ, headers=headers)
    data = response.json()
    ic(data)
    logging.debug("Response data: %s", data)


def test_automated_quiz_creation():
    authenticate()
    list_courses()
    return
    #list_topics()
    #create_course()
    #list_courses()
    #create_lesson(13)
    #create_topic(topic_gift_quiz_creation_data)
    create_quiz_question()
    #see_course(13)
    see_gift_quiz(1)

if __name__ == "__main__":
    test_automated_quiz_creation()