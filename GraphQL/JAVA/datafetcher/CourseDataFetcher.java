package com.mayukh.graphQL.course.datafetcher;

import com.mayukh.graphQL.course.entity.Course;
import com.mayukh.graphQL.course.repository.CourseRepository;
import graphql.schema.DataFetcher;
import graphql.schema.DataFetchingEnvironment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class CourseDataFetcher implements DataFetcher<Course> {
    @Autowired
    private CourseRepository courseRepository;


    @Override
    public Course get(DataFetchingEnvironment dataFetchingEnvironment) throws Exception {
        int id = dataFetchingEnvironment.getArgument("id");
        return courseRepository.findOne(id);
    }
}
