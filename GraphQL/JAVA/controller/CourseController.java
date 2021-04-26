package com.mayukh.graphQL.course.controller;

import com.mayukh.graphQL.course.service.CourseService;
import graphql.ExecutionResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/courses")
@RestController
public class CourseController {
    @Autowired
    CourseService courseService;

    @GetMapping
    public ResponseEntity<Object> getCourses(){ return
            new ResponseEntity<Object>(courseService.findAllCourses(), HttpStatus.OK);}

    @PostMapping
    public ResponseEntity<Object> getAllCourses(@RequestBody String query) {
        ExecutionResult execute = courseService.getGraphQL().execute(query);

        return new ResponseEntity<>(execute, HttpStatus.OK);
    }
}
