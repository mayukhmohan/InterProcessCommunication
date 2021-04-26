from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask import abort
from flask import make_response
from flask import request
import random
import datetime
import json

app = Flask(__name__)
api = Api(app)

courses = []
NO_OF_OBJECTS = 100

class DateTime:
    def __init__(self, year = 2021, month = 4, day = 8, hour = 19, minute = 5, second = 30):
        self.dict = {}
        self.dict['year'] = year
        self.dict['month'] = month
        self.dict['day'] = day
        self.dict['hour'] = hour
        self.dict['minute'] = minute
        self.dict['second'] = second


def get_alpha_numeric_string(n):
    alpha_numeric_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvxyz"
    sb = ""
    for i in range(n):
        INDEX = int(len(alpha_numeric_string) * random.random())
        sb += alpha_numeric_string[INDEX]
    return sb


def get_numeric(n):
    return round(random.random() * 100, n)


def get_date_time():
    """
    date_time = datetime.datetime.now()
    date_time = date_time.replace(year = int((random.random() * 23) + 2000),
                                  month = int((random.random() * 12) + 1),
                                  day = int((random.random() * 28) + 1),
                                  hour = int(random.random() * 24),
                                  minute = int(random.random() * 60),
                                  second = int(random.random() * 60))
                                  """
    datetime = DateTime(year = int((random.random() * 23) + 2000),
                        month = int((random.random() * 12) + 1),
                        day = int((random.random() * 28) + 1),
                        hour = int(random.random() * 24),
                        minute = int(random.random() * 60),
                        second = int(random.random() * 60))

    datetime = datetime.dict
    return datetime




def populate():
    for i in range(NO_OF_OBJECTS):
        course = {'id': i, 'course_name': get_alpha_numeric_string(10),
                  'avg_marks': get_numeric(2), 'end_of_course':get_date_time()}

        courses.append(course)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify({'courses': courses})


@app.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = [course for course in courses if course['id'] == course_id]
    if len(course) == 0:
        abort(404)
    return jsonify({'course': course[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/course', methods=['POST'])
def create_course():
    if not request.json or not 'course_name' in request.json:
        abort(400)
    course = {
        'id': courses[-1]['id'] + 1,
        'course_name': request.json['course_name'],
        'avg_marks': request.json['avg_marks'],
        'end_of_course': get_date_time()
    }
    courses.append(course)
    return jsonify({'course': course}), 201


@app.route('/courses', methods=['POST'])
def create_courses():
    if not request.json:
        abort(400)
    for i in range(len(courses)):
        courses[i]['course_name'] = request.json['courses'][i]['course_name']
        courses[i]['avg_marks'] = request.json['courses'][i]['avg_marks']
    return jsonify({'courses': courses}), 201


@app.route('/course/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = [course for course in courses if course['id'] == course_id]
    if len(course) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'course_name' in request.json and type(request.json['course_name']) != str:
        abort(400)
    if 'avg_marks' in request.json and type(request.json['avg_marks']) is not float:
        abort(400)
    course[0]['course_name'] = request.json['course_name']
    course[0]['avg_marks'] = request.json['avg_marks']
    return jsonify({'course': course[0]})


@app.route('/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = [course for course in courses if course['id'] == course_id]
    if len(course) == 0:
        abort(404)
    courses.remove(course[0])
    return jsonify({'course': course[0],
                    'result': 'Deleted'})


if __name__ == '__main__':
    populate()
    app.run(debug=True)
