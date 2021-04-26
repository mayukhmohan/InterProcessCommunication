package java_python_standardized_grpc;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import service.java_python_standardized_service;
import java.io.IOException;

public class java_standardized_server {
    public static int PORT = 50000;
    public static int NO_OF_OBJECTS = 100;
    public static void main(String []args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(PORT).addService(new java_python_standardized_service()).build();
        server.start();
        System.out.println("Server started on: " + PORT);
        server.awaitTermination();
    }
}

