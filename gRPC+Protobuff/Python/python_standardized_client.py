import grpc
import msg_pb2_grpc as pb2_grpc
import msg_pb2 as pb2
from python_standardized_server import MsgService
import random
# from memory_profiler import profile

# mprof run python_standardized_client.py
# mprof plot
# python -m memory_profiler python_standardized_client.py

NO_OF_OBJECTS = 100

class MsgClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.ms = MsgService()
        self.server_port = self.ms.PORT

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.MsgStub(self.channel)


    def get_url(self, message):
        message = pb2.Message(message=message.message)
        return self.stub.getServerResponse(message)


class DateTime:
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second


class Course:
    def __init__(self, id, course_name, avg_marks, year, month,
                 day, hour, minute, second):
        self.id = id
        self.course_name = course_name
        self.avg_marks = avg_marks
        self.end_of_course = DateTime(year, month, day, hour, minute, second)


def AddCourse(message, course):
    message.id = course.id
    message.course_name = course.course_name
    message.avg_marks = course.avg_marks
    end_of_course = message.end_of_course
    end_of_course.year = course.end_of_course.year
    end_of_course.month = course.end_of_course.month
    end_of_course.day = course.end_of_course.day
    end_of_course.hour = course.end_of_course.hour
    end_of_course.minute = course.end_of_course.minute
    end_of_course.second = course.end_of_course.second


def get_alpha_numeric_string(n):
    alpha_numeric_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvxyz"
    sb = ""
    for i in range(n):
        INDEX = int(len(alpha_numeric_string) * random.random())
        sb += alpha_numeric_string[INDEX]
    return sb


def get_numeric(n):
    return round(random.random() * 100, n)


if __name__ == '__main__':
    client = MsgClient()
    courses = []
    messageRequest = pb2.Message()
    for i in range(NO_OF_OBJECTS):
        course = Course(id = i,
                        course_name = get_alpha_numeric_string(10),
                        avg_marks = get_numeric(2),
                        year = int((random.random() * 23) + 2000),
                        month = int((random.random() * 12) + 1),
                        day = int((random.random() * 28) + 1),
                        hour = int(random.random() * 24),
                        minute = int(random.random() * 60),
                        second = int(random.random() * 60))
        courses.append(course)
        AddCourse(messageRequest.message.add(), course)
    results = client.get_url(message=messageRequest)
    for (result, message) in zip(results.messageResponse, messageRequest.message):
        print("{")
        print(result.Course_ID, message.course_name, result.Course_Name, message.avg_marks, result.Avg_Marks, sep="\n")
        print("{")
        print(result.END_of_COURSE.Year, result.END_of_COURSE.Month,
              result.END_of_COURSE.Day, result.END_of_COURSE.Hour,
              result.END_of_COURSE.Minute, result.END_of_COURSE.Second)
        print("}")
        print("}\n")
    # print("In Client: {}".format(result))