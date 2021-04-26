package service;

import io.grpc.stub.StreamObserver;
import com.mayukh.grpc_standardized.Jpsmsg;
import com.mayukh.grpc_standardized.MsgGrpc;
import java_python_standardized_grpc.java_standardized_server;

public class java_python_standardized_service extends MsgGrpc.MsgImplBase{

    @Override
    public void getServerResponse(Jpsmsg.Message request, StreamObserver<Jpsmsg.MessageResponse> responseObserver) {
        Jpsmsg.MessageResponse.Builder response = Jpsmsg.MessageResponse.newBuilder();
        for(int i = 0; i < java_standardized_server.NO_OF_OBJECTS; i++){
            Jpsmsg.Course course = request.getMessage(i);
            Jpsmsg.CourseResponse.DateTime dateTime = Jpsmsg.CourseResponse.DateTime.newBuilder()
                    .setYear(course.getEndOfCourse().getYear()).setMonth(course.getEndOfCourse().getMonth())
                    .setDay(course.getEndOfCourse().getDay()).setHour(course.getEndOfCourse().getHour())
                    .setMinute(course.getEndOfCourse().getMinute()).setSecond(course.getEndOfCourse().getSecond()).build();
            Jpsmsg.CourseResponse courseResponse = Jpsmsg.CourseResponse.newBuilder()
                    .setCourseID(course.getId()).setCourseName(new StringBuilder(course.getCourseName()).reverse().toString())
                    .setAvgMarks(100 - course.getAvgMarks()).setENDOfCOURSE(dateTime).build();
            response.addMessageResponse(courseResponse);
        }
        responseObserver.onNext(response.build());
        responseObserver.onCompleted();
    }
}
