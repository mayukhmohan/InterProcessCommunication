import grpc
from concurrent import futures
import time
import msg_pb2_grpc as pb2_grpc
import msg_pb2 as pb2
from memory_profiler import profile


def ListStringCourses(messageRequest):
    result = ""
    for course in messageRequest.message:
        result += "[Course ID:" + str(course.id)
        result += "\nCourse Name:" + str(course.course_name)
        result += "\nAvg Marks: " + str(course.avg_marks)
        result += "\nEND of COURSE: "
        result += "\n Year: " + str(course.end_of_course.year)
        result += "\n Month: " + str(course.end_of_course.month)
        result += "\n Day: " + str(course.end_of_course.day)
        result += "\n Hour: " + str(course.end_of_course.hour)
        result += "\n Minute: " + str(course.end_of_course.minute)
        result += "\n Second: " + str(course.end_of_course.second) + "]\n"
    return result


def ListCourses(messageRequest):
    results = []
    for course in messageRequest.message:
        result = {"Course_ID": course.id, "Course_Name": course.course_name[::-1],
                  "Avg_Marks": (100 - course.avg_marks),
                  "END_of_COURSE": {}}
        result["END_of_COURSE"]["Year"] = course.end_of_course.year
        result["END_of_COURSE"]["Month"] = course.end_of_course.month
        result["END_of_COURSE"]["Day"] = course.end_of_course.day
        result["END_of_COURSE"]["Hour"] = course.end_of_course.hour
        result["END_of_COURSE"]["Minute"] = course.end_of_course.minute
        result["END_of_COURSE"]["Second"] = course.end_of_course.second
        results.append(result)
    return results



class MsgService(pb2_grpc.MsgServicer):

    def __init__(self, *args, **kwargs):
        self.PORT = 50000
        pass

    def getServerResponse(self, request, context):
        message = ListCourses(request)
        # result = "From Python Server: \n{} Got this :)!!".format(message)
        result = {"messageResponse": message}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MsgServicer_to_server(MsgService(), server)
    ms = MsgService()
    server.add_insecure_port('[::]:'+str(ms.PORT))
    print("Up and Running at "+ str(ms.PORT))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()