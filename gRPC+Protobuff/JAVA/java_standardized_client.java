package java_python_standardized_grpc;

import com.mayukh.grpc_standardized.Jpsmsg;
import com.mayukh.grpc_standardized.MsgGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;

public class java_standardized_client {
    public static String getAlphaNumericString(int n)
    {
        String AlphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvxyz";

        StringBuilder sb = new StringBuilder(n);

        for (int i = 0; i < n; i++) {
            int index = (int)(AlphaNumericString.length() * Math.random());
            sb.append(AlphaNumericString.charAt(index));
        }
        return sb.toString();
    }

    public static float get_numeric(int n)
    {
        return BigDecimal.valueOf(Math.random() * 100)
                .setScale(n, RoundingMode.HALF_UP).floatValue();
    }
    public static void main(String []args){
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", java_standardized_server.PORT).usePlaintext().build();
        MsgGrpc.MsgBlockingStub stub = MsgGrpc.newBlockingStub(channel);
        List<Jpsmsg.Course> courses = new ArrayList<>();
        for(int i = 0; i < java_standardized_server.NO_OF_OBJECTS; i++){
            Jpsmsg.Course.DateTime dateTime = Jpsmsg.Course.DateTime.newBuilder()
                            .setYear((int)((Math.random() * 23) + 2000)).setMonth((int)((Math.random() * 12) + 1))
                            .setDay((int)((Math.random() * 28) + 1)).setHour((int)(Math.random() * 24))
                            .setMinute((int)(Math.random() * 60)).setSecond((int)(Math.random() * 60)).build();
            Jpsmsg.Course course = Jpsmsg.Course.newBuilder().setId(i)
                    .setCourseName(getAlphaNumericString(10)).setAvgMarks(get_numeric(2))
                    .setEndOfCourse(dateTime).build();
            courses.add(course);
        }
        Jpsmsg.Message request = Jpsmsg.Message.newBuilder().addAllMessage(courses).build();
        Jpsmsg.MessageResponse response = stub.getServerResponse(request);
        for(int i = 0; i < java_standardized_server.NO_OF_OBJECTS; i++){
            Jpsmsg.CourseResponse courseResponse = response.getMessageResponse(i);
            Jpsmsg.Course course = request.getMessage(i);
            System.out.println("CourseId: " + courseResponse.getCourseID());
            System.out.println("Course_name: " + course.getCourseName());
            System.out.println("Course_name Response: " + courseResponse.getCourseName());
            System.out.println("Avg_marks: " + course.getAvgMarks());
            System.out.println("Avg_marks Response: " + courseResponse.getAvgMarks());
            System.out.println("End of Course: " + courseResponse.getENDOfCOURSE());
            System.out.println("\n");
        }
    }
}

