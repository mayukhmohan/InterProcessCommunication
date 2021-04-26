package com.mayukh.rest.controller;

import com.mayukh.rest.entity.Course;
import com.mayukh.rest.services.CourseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class CourseController {

    //Implemented class courServiceImpl will be linked by Spring boot
    @Autowired
    private CourseService courseService;

    //get the courses
    /*@GetMapping("/courses")
    public List<Course> getCourses(){
        return courseService.getCourses();
    }*/
    @GetMapping("/courses")
    public Map<String, List<Course>> getCourses() {
        List<Course> courses = courseService.getCourses();
        Map<String, List<Course>> map = new HashMap<>();
        map.put("courses", courses);
        return map;
    }

    /**@GetMapping("/course/{courseId}")
    public Course getCourse(@PathVariable String courseId){
        return this.courseService.getCourse(Long.parseLong(courseId));
    }
     OR
     */

    @GetMapping("/course/{cId}")
    public ResponseEntity<Course> getCourse(@PathVariable("cId") String courseId){
        Course course = this.courseService.getCourse(Integer.parseInt(courseId));
        if(course == null) return new ResponseEntity<Course>(course, HttpStatus.NOT_FOUND);
        else return new ResponseEntity<Course>(course, HttpStatus.OK);
    }

    //@PostMapping(path = "/course", consumes = "application/json")
    @PostMapping("/course")
    public Course addCourse(@RequestBody Course course){
        return this.courseService.addCourse(course);
    }

    /*@PostMapping("/courses")
    public List<Course> addCourses(@RequestBody List<Course> courses){
        return this.courseService.addCourses(courses);
    }*/
    @PostMapping("/courses")
    public List<Course> addCourses(@RequestBody Map<String, List<Course>> courses) {
        return this.courseService.addCourses(courses);
    }

    @PutMapping("/course/{cId}")
    public Course updateCourse(@PathVariable("cId") String courseId, @RequestBody Course course){
        return this.courseService.updateCourse(Integer.parseInt(courseId), course);
    }

    @PutMapping("/courses")
    public List<Course> updateCourses(@RequestBody List<Course> courses){
        return this.courseService.updateCourses(courses);
    }

    @DeleteMapping("/course/{cId}")
    public Course deleteCourse(@PathVariable("cId") String courseId){
        return this.courseService.deleteCourse(Integer.parseInt(courseId));
    }
}
