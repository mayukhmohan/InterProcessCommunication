package com.mayukh.graphQL.course.datafetcher;

import com.mayukh.graphQL.course.entity.CourseID;
import com.mayukh.graphQL.course.repository.CourseRepository;
import graphql.schema.DataFetcher;
import graphql.schema.DataFetchingEnvironment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.LinkedHashMap;

@Component
public class PostCourseDataFetcher implements DataFetcher<CourseID> {
    @Autowired
    private CourseRepository courseRepository;

    @Override
    public CourseID get(DataFetchingEnvironment environment) throws Exception {
        LinkedHashMap<String, Object> linkedHashMap= environment.getArgument("course");
        return courseRepository.updateOne(linkedHashMap);
    }
}
