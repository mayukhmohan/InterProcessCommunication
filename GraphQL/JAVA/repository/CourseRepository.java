package com.mayukh.graphQL.course.repository;

import com.mayukh.graphQL.course.entity.Course;
import com.mayukh.graphQL.course.entity.CourseID;
import com.mayukh.graphQL.course.entity.DateTime;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

@Repository
public class CourseRepository {
    List<Course> courseList;
    public static final int NO_OF_OBJECTS = 100;

    public String getAlphaNumericString(int n)
    {
        String AlphaNumericString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvxyz";

        StringBuilder sb = new StringBuilder(n);

        for (int i = 0; i < n; i++) {
            int index = (int)(AlphaNumericString.length() * Math.random());
            sb.append(AlphaNumericString.charAt(index));
        }
        return sb.toString();
    }

    public float get_numeric(int n)
    {
        return BigDecimal.valueOf(Math.random() * 100)
                .setScale(n, RoundingMode.HALF_UP).floatValue();
    }

    public DateTime get_date_time()
    {
        return new DateTime((int)((Math.random() * 23) + 2000),
                (int)((Math.random() * 12) + 1),
                (int)((Math.random() * 28) + 1),
                (int)(Math.random() * 24),
                (int)(Math.random() * 60),
                (int)(Math.random() * 60));
    }

    public CourseRepository() {
        courseList = new ArrayList<>();
        for(int i=0; i<NO_OF_OBJECTS; i++){
            courseList.add(new Course(i, getAlphaNumericString(10)
                    , get_numeric(2), get_date_time()));
        }
    }

    public List<Course> findAll(){
        return courseList;
    }

    public Course findOne(int id){
        for(Course course:courseList){
            if(course.getId() == id) return course;
        }
        return null;
    }

    public CourseID updateOne(LinkedHashMap<String, Object> linkedHashMap){
        for(Course course:courseList){
            if(course.getId() == ((Integer) linkedHashMap.get("id")).intValue()) {
                course.setCourse_name((String) linkedHashMap.get("course_name"));
                course.setAvg_marks(((Double) linkedHashMap.get("avg_marks")).floatValue());
                return new CourseID(course.getId());
            }
        }
        return null;
    }

    public List<CourseID> updateAll(List<LinkedHashMap<String, Object>> linkedHashMapList){
        List<CourseID> courseIDList = new ArrayList<>();
        for(int i = 0; i < courseList.size(); i++){
            if(courseList.get(i).getId() == ((Integer) linkedHashMapList.get(i).get("id")).intValue()) {
                courseList.get(i).setCourse_name((String) linkedHashMapList.get(i).get("course_name"));
                courseList.get(i).setAvg_marks(((Double) linkedHashMapList.get(i).get("avg_marks")).floatValue());
                courseIDList.add(new CourseID(courseList.get(i).getId()));
            }
        }
        return courseIDList;
    }
}
