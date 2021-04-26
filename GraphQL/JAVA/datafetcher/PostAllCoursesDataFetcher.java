package com.mayukh.graphQL.course.datafetcher;

import com.mayukh.graphQL.course.entity.Course;
import com.mayukh.graphQL.course.entity.CourseID;
import com.mayukh.graphQL.course.repository.CourseRepository;
import graphql.schema.DataFetcher;
import graphql.schema.DataFetchingEnvironment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.LinkedHashMap;
import java.util.List;

@Component
public class PostAllCoursesDataFetcher implements DataFetcher<List<CourseID>>{
    @Autowired
    private CourseRepository courseRepository;

    @Override
    public List<CourseID> get(DataFetchingEnvironment environment) throws Exception {
        List<LinkedHashMap<String, Object>> linkedHashMapList = environment.getArgument("courses");
        return courseRepository.updateAll(linkedHashMapList);
    }
}
