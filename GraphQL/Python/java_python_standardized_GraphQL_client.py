import requests
import json
from python_graphql_client import GraphqlClient
from java_python_standardized_GraphQL_server import NO_OF_OBJECTS

url = "http://127.0.0.1:5000/courses"
client = GraphqlClient(endpoint= "http://127.0.0.1:5000/courses")


def pythontojava():
    query_post = "{\n" + \
                 "  getCourses{\n" + \
                 "    id\n" + \
                 "    course_name\n" + \
                 "   avg_marks\n" + \
                 "    end_of_course\n" + \
                 "    {\n" + \
                 "     day\n" + \
                 "     year\n" + \
                 "    }\n" + \
                 "   }\n" + \
                 "}"

    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    data = requests.post(url, data = query_post, headers = headers)
    print(data)
    data = data.json()["data"]["getCourses"]
    print(data)

    mutation_post_start = "mutation{\n" \
                          "      updateCourses(courses: [\n"
    mutation_post_end = "         ]){\n" \
                        "        id\n" \
                        "     }\n " \
                        "}"
    mutation_post_itr = ""
    for i in range(NO_OF_OBJECTS):
        temp_string = "{\n"
        id = data[i]["id"]
        course_name = data[i]["course_name"][::-1]
        avg_marks = (100 - data[i]["avg_marks"])
        temp_string += "id: " + str(id) + "\n"
        temp_string += "course_name: \"" + course_name + "\"\n"
        temp_string += "avg_marks: " + str(avg_marks) + "\n"
        temp_string += "}\n"
        mutation_post_itr += temp_string

    mutation_post = mutation_post_start + mutation_post_itr + mutation_post_end
    data = requests.post(url, data = mutation_post, headers = headers)
    print(data, data.json())
    data = requests.post(url, data = query_post, headers = headers)
    print(data, data.json())


def pythontopython():
    query_post = """
    query {
      getCourses {
        id
        course_name
        avg_marks
      }
    }
    """
    query_post_elaborate = """query {
      getCourses {
        id
        course_name
        avg_marks
        end_of_course {
          day
          second
        }
      }
    }"""

    mutation_post_start = "mutation{\n" \
                          "      updateCourses(courses: [\n"
    mutation_post_end = "         ]){\n" \
                        "        id\n" \
                        "     }\n " \
                        "}"
    mutation_post_itr = ""
    data = client.execute(query=query_post)
    data = data["data"]["getCourses"]
    print(data)
    for i in range(NO_OF_OBJECTS):
        temp_string = "{\n"
        id = data[i]["id"]
        course_name = data[i]["course_name"][::-1]
        avg_marks = (100 - data[i]["avg_marks"])
        temp_string += "id: " + str(id) + "\n"
        temp_string += "course_name: \"" + course_name + "\"\n"
        temp_string += "avg_marks: " + str(avg_marks) + "\n"
        temp_string += "}\n"
        mutation_post_itr += temp_string

    mutation_post = mutation_post_start + mutation_post_itr + mutation_post_end
    data = client.execute(query=mutation_post)
    print(data)
    data = client.execute(query=query_post_elaborate)
    print(data["data"]["getCourses"])

if __name__ == "__main__":
    lang = input("whom do u want to communicate to? Python OR JAVA: ")
    if lang.lower() == "python":
        pythontopython()
    if lang.lower() == "java":
        pythontojava()