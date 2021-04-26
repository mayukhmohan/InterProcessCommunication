package com.mayukh.graphQL.course;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class courseGraphQLApplication {

    public static void main(String[] args) {
        SpringApplication.run(courseGraphQLApplication.class, args);
    }
}


/**
 * {
 *     getCourses {
 *         id
 *         course_name
 *         avg_marks
 *         end_of_course{
 *             day
 *         }
 *     }
 *     getCourse(id: 99){
 *         id
 *         course_name
 *         avg_marks
 *         end_of_course{
 *             day
 *         }
 *     }
 * }
 *
 * mutation{
 *     updateCourse(course: {
 *         id: 99
 *         course_name: "graphQL"
 *         avg_marks: 90.54
 *         }){
 *         id
 *     }
 * }
 * */