package com.mayukh.rest.services;

import com.mayukh.rest.entity.Course;
import com.mayukh.rest.entity.DateTime;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

//Telling spring boot this is our service implementation
@Service
public class CourseServiceImpl implements CourseService {
    List<Course> list;
    private final int NO_OF_OBJECTS = 100;
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
        return new DateTime((int)(Math.random() * 60),
                            (int)(Math.random() * 60),
                            (int)(Math.random() * 24),
                            (int)((Math.random() * 28) + 1),
                            (int)((Math.random() * 12) + 1),
                            (int)((Math.random() * 23) + 2000));
    }

    public CourseServiceImpl(){
        list = new ArrayList<>();
        for(int i = 0; i<NO_OF_OBJECTS; i++){
            list.add(new Course(i, get_numeric(2), getAlphaNumericString(10), get_date_time()));
        }
    }

    @Override
    public List<Course> getCourses() {
        return list;
    }

    @Override
    public Course getCourse(int CourseID) {
        for(Course course:list){
            if(course.getId() == CourseID){
                return course;
            }
        }
        return null;
    }

    @Override
    public Course addCourse(Course course) {
        list.add(course);
        return course;
    }

    @Override
    public List<Course> addCourses(Map<String, List<Course>> Courses) {
        List<Course> courses = Courses.get("courses");
        for(int i=0; i<NO_OF_OBJECTS; i++){
            list.get(i).setcourse_name(courses.get(i).getcourse_name());
            list.get(i).setavg_marks(courses.get(i).getavg_marks());
        }
        return courses;
    }

    @Override
    public Course updateCourse(int courseId, Course course) {
        for(Course course_unit:list){
            if(course_unit.getId() == courseId){
                course_unit.setcourse_name(course.getcourse_name());
                course_unit.setavg_marks(course.getavg_marks());
                course_unit.setEnd_of_course(course.getEnd_of_course());
                return course_unit;
            }
        }
        list.add(course);
        return course;
    }

    @Override
    public List<Course> updateCourses(List<Course> courses) {
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).getId() == courses.get(i).getId()){
                list.get(i).setId(courses.get(i).getId());
                list.get(i).setcourse_name(courses.get(i).getcourse_name());
                list.get(i).setavg_marks(courses.get(i).getavg_marks());
                list.get(i).setEnd_of_course(courses.get(i).getEnd_of_course());
            }
        }
        return courses;
    }

    @Override
    public Course deleteCourse(int courseId) {
        for(Course course:list){
            if(course.getId() == courseId){
                list.remove(course);
                return course;
            }
        }
        return null;
    }
}
