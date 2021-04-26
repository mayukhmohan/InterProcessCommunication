package com.mayukh.rest;

import com.google.gson.*;
import com.mayukh.rest.entity.Course;
import com.mayukh.rest.entity.DateTime;
import com.mayukh.rest.services.CourseServiceImpl;
import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;

import java.util.*;

public class RestClient {
    private static final String GET_ALL_COURSES_API = "http://127.0.0.1:5000/courses";
    private static final String GET_COURSE_BY_ID_API = "http://127.0.0.1:5000/course/{cId}";
    private static final String POST_CREATE_COURSE_API = "http://127.0.0.1:5000/course";
    private static final String POST_CREATE_COURSES_API = "http://127.0.0.1:5000/courses";
    private static final String PUT_UPDATE_COURSE_API = "http://127.0.0.1:5000/course/{cId}";
    private static final String DELETE_COURSE_API = "http://127.0.0.1:5000/course/{cId}";
    private static final String PUT_UPDATE_COURSES_API = "http://127.0.0.1:5000/courses";

    static RestTemplate restTemplate = new RestTemplate();

    public static List<Long> timeList = new ArrayList<>();
    public static void main(String []args){
        callUpdateUsers(callGetAllUsersAPI());
        callGetAllUsersAPI();
        Scanner in = new Scanner(System.in);
        int i = in.nextInt();
        System.out.println(timeList);
    }

    private static JsonArray callGetAllUsersAPI(){
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Arrays.asList(MediaType.APPLICATION_JSON));

        HttpEntity<String> entity = new HttpEntity<>("parameters", headers);
        long start = System.nanoTime();
        ResponseEntity<String> result = restTemplate.exchange(GET_ALL_COURSES_API, HttpMethod.GET, entity, String.class);
        long end = System.nanoTime();
        //System.out.println(result.getBody());

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonParser jp = new JsonParser();
        JsonElement je = jp.parse(result.getBody());
        System.out.println(gson.toJson(je));
        //Scanner in = new Scanner(System.in);
        //Integer i = in.nextInt();
        timeList.add(end - start);
        return (JsonArray) ((JsonObject) je).get("courses");
    }

    private static void callGetUserByIdAPI(){
        Map<String, Integer> param = new HashMap<>();
        param.put("cId", 50);

        Course course = restTemplate.getForObject(GET_COURSE_BY_ID_API, Course.class, param);
        System.out.println(course);
    }

    private static void callCreateUserAPI(){
        Course course = new Course(100, (float) 92.86, "JAVA", new DateTime(30, 30, 20, 15, 4, 2021));
        ResponseEntity<Course> course_unit = restTemplate.postForEntity(POST_CREATE_COURSE_API, course, Course.class);
        System.out.println(course_unit.getBody());
    }

    private static void callUpdateUserAPI(){
        Map<String, Integer> param = new HashMap<>();
        param.put("cId", 99);
        Course course = new Course(99, (float) 92.86, "JAVA", new DateTime(30, 30, 20, 15, 4, 2021));
        restTemplate.put(PUT_UPDATE_COURSE_API, course, param);
    }

    private static void callUpdateUsers(JsonArray jsonArray){
        List<Course> courseList = new ArrayList<>();
        for(int i = 0; i < CourseServiceImpl.NO_OF_OBJECTS; i++){
            JsonObject jsonObject = jsonArray.get(i).getAsJsonObject();
            int id = jsonObject.get("id").getAsInt();
            float avg_marks = jsonObject.get("avg_marks").getAsFloat();
            String course_name = jsonObject.get("course_name").getAsString();
            JsonObject dateTimeJsonObject = jsonObject.get("end_of_course").getAsJsonObject();
            int day = dateTimeJsonObject.get("day").getAsInt();
            int month = dateTimeJsonObject.get("month").getAsInt();
            int year = dateTimeJsonObject.get("year").getAsInt();
            int second = dateTimeJsonObject.get("second").getAsInt();
            int minute = dateTimeJsonObject.get("minute").getAsInt();
            int hour = dateTimeJsonObject.get("hour").getAsInt();
            avg_marks = (100 - avg_marks);
            course_name = new StringBuilder(course_name).reverse().toString();
            Course course = new Course(id, avg_marks, course_name, new DateTime(second, minute, hour, day, month, year));
            courseList.add(course);
        }
        Long start = System.nanoTime();
        restTemplate.put(PUT_UPDATE_COURSES_API, courseList);
        Long end = System.nanoTime();
        timeList.add(end - start);
    }

    private static void callDeleteUserAPI(){
        Map<String, Integer> param = new HashMap<>();
        param.put("cId", 99);
        restTemplate.delete(DELETE_COURSE_API, param);
    }
}
