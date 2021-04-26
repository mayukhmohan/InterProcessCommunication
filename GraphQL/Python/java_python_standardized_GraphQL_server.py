from flask import Flask
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, \
    snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from ariadne import convert_kwargs_to_snake_case
import random

app = Flask(__name__)

courseList = []
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
        course = {"id": i, "course_name": get_alpha_numeric_string(10),
                  "avg_marks": get_numeric(2), "end_of_course":get_date_time()}

        courseList.append(course)


@app.route("/courses", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/courses", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

@convert_kwargs_to_snake_case
def resolve_get_courses(obj, info):
    return courseList


@convert_kwargs_to_snake_case
def resolve_get_course(obj, info, id):
    for course in courseList:
        if course["id"] == id:
            return course
    return None

@convert_kwargs_to_snake_case
def resolve_update_course(obj, info, course):
    for course_itr in courseList:
        if course_itr["id"] == course["id"]:
            course_itr["course_name"] = course["course_name"]
            course_itr["avg_marks"] = course["avg_marks"]
            return {"id": course_itr["id"]}
    return None

@convert_kwargs_to_snake_case
def resolve_update_courses(obj, info, courses):
    courseIdList = []
    for i in range(NO_OF_OBJECTS):
        if courseList[i]["id"] == courses[i]["id"]:
            courseList[i]["course_name"] = courses[i]["course_name"]
            courseList[i]["avg_marks"] = courses[i]["avg_marks"]
            courseIdList.append({"id":courseList[i]["id"]})
    return courseIdList

query = ObjectType("Query")

query.set_field("getCourses", resolve_get_courses)
query.set_field("getCourse", resolve_get_course)

mutation = ObjectType("Mutation")
mutation.set_field("updateCourse", resolve_update_course)
mutation.set_field("updateCourses", resolve_update_courses)

type_defs = load_schema_from_path("course.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


if __name__ == "__main__":
    populate()
    app.run(debug=True)


"""
query {
  getCourses {
    id
    course_name
    end_of_course {
      day
      second
    }
  }
}

query {
  getCourse(id: 50) {
    id
    course_name
    end_of_course {
      day
      second
    }
  }
}

mutation {
  updateCourse(course: {
    id:50
    course_name: "graphQL"
    avg_marks: 78.23
  }) {
    id
  }
}
"""