package com.mayukh.rest.services;

import com.mayukh.rest.entity.Course;

import java.util.List;
import java.util.Map;

public interface CourseService {
    public List<Course> getCourses();
    public Course getCourse(int ID);
    public Course addCourse(Course course);
    public List<Course> addCourses(Map<String, List<Course>> courses);
    public Course updateCourse(int ID, Course course);
    public List<Course> updateCourses(List<Course> courses);
    public Course deleteCourse(int ID);
}
