package com.mayukh.graphQL.course.datafetcher;

import com.mayukh.graphQL.course.entity.Course;
import com.mayukh.graphQL.course.repository.CourseRepository;
import graphql.schema.DataFetcher;
import graphql.schema.DataFetchingEnvironment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class AllCoursesDataFetcher implements DataFetcher<List<Course>> {
    @Autowired
    private CourseRepository courseRepository;

    @Override
    public List<Course> get(DataFetchingEnvironment dataFetchingEnvironment) throws Exception {
        return courseRepository.findAll();
    }
}
