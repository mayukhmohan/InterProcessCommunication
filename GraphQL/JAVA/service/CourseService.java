package com.mayukh.graphQL.course.service;

import com.mayukh.graphQL.course.datafetcher.AllCoursesDataFetcher;
import com.mayukh.graphQL.course.datafetcher.CourseDataFetcher;
import com.mayukh.graphQL.course.datafetcher.PostAllCoursesDataFetcher;
import com.mayukh.graphQL.course.datafetcher.PostCourseDataFetcher;
import com.mayukh.graphQL.course.entity.Course;
import com.mayukh.graphQL.course.repository.CourseRepository;
import graphql.GraphQL;
import graphql.Scalars;
import graphql.schema.GraphQLSchema;
import graphql.schema.idl.RuntimeWiring;
import graphql.schema.idl.SchemaGenerator;
import graphql.schema.idl.SchemaParser;
import graphql.schema.idl.TypeDefinitionRegistry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.io.File;
import java.io.IOException;
import java.util.List;

@Service
public class CourseService {
    @Autowired
    CourseRepository courseRepository;

    @Value("classpath:course.graphql")
    Resource resource;

    private GraphQL graphQL;

    @Autowired
    private AllCoursesDataFetcher allCoursesDataFetcher;

    @Autowired
    private CourseDataFetcher courseDataFetcher;

    @Autowired
    private PostCourseDataFetcher postCourseDataFetcher;

    @Autowired
    private PostAllCoursesDataFetcher postAllCoursesDataFetcher;

    @PostConstruct
    private void loadSchema() throws IOException {
        courseRepository = new CourseRepository();
        File schema = resource.getFile();
        TypeDefinitionRegistry typeDefinitionRegistry = new SchemaParser().parse(schema);
        RuntimeWiring runtimeWiring = buildRuntimeWiring();
        GraphQLSchema graphQLSchema = new SchemaGenerator()
                .makeExecutableSchema(typeDefinitionRegistry, runtimeWiring);
        graphQL = GraphQL.newGraphQL(graphQLSchema).build();
    }

    private RuntimeWiring buildRuntimeWiring() {
        return RuntimeWiring.newRuntimeWiring()
                .type("Query", typeWiring -> typeWiring
                        .dataFetcher("getCourses", allCoursesDataFetcher)
                        .dataFetcher("getCourse", courseDataFetcher))
                .type("Mutation", typeWiring -> typeWiring
                        .dataFetcher("updateCourse", postCourseDataFetcher)
                        .dataFetcher("updateCourses", postAllCoursesDataFetcher))
                .build();
    }


    public GraphQL getGraphQL() {
        return graphQL;
    }

    // For simple GETs in REST way
    public List<Course> findAllCourses() {
        return courseRepository.findAll();
    }
    // For simple GETs in REST way
    public Course findCourseById(int courseId) {
        return courseRepository.findOne(courseId);
    }
}
