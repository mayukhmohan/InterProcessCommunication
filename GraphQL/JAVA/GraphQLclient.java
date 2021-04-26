package com.mayukh.graphQL.course;

import com.fasterxml.jackson.databind.SerializationFeature;
import com.google.gson.*;
import com.mayukh.graphQL.course.entity.Course;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.*;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import java.util.*;

public class GraphQLclient {
    private static final String URI = "http://127.0.0.1:5000/courses";

    static RestTemplate restTemplate = new RestTemplate();

    private static final String QUERY_GET = "{\n" +
            "  getCourses{\n" +
            "    id\n" +
            "    course_name\n" +
            "    avg_marks\n" +
            "    end_of_course\n" +
            "    {\n" +
            "     day\n" +
            "     year\n" +
            "    }\n" +
            "   }\n" +
            "}";

    private static String QUERY_POST = "";

    public static String makePostQueryPython(JsonArray jsonArray){
        String result = "";
        String result_start = "\n    mutation {\n      updateCourses (courses: [\n";
        String result_end = "         ]){\n" +
                "        id\n" +
                "     }\n" +
                " }";
        for(int i = 0; i < jsonArray.size(); i++){
            String temp_string = "{\n";
            JsonObject jsonObject_ = jsonArray.get(i).getAsJsonObject();
            int id = jsonObject_.get("id").getAsInt();
            String course_name = jsonObject_.get("course_name").getAsString();
            float avg_marks = jsonObject_.get("avg_marks").getAsFloat();
            avg_marks = (100 - avg_marks);
            course_name = new StringBuilder(course_name).reverse().toString();
            temp_string += "id: " + id + "\n";
            temp_string += "course_name: \"" + course_name + "\"\n";
            temp_string += "avg_marks: " + avg_marks + "\n";
            temp_string += "}\n";
            result += temp_string;
        }
        result = result_start + result + result_end;
        return result;
    }

    public static void makePostQuery(JsonArray jsonArray){
        String temp_query_post_start = "mutation{\n" +
                "      updateCourses(courses: [\n";
        String temp_query_post_itr = "";
        String temp_query_post_end = "         ]){\n" +
                "        id\n" +
                "     }\n" +
                " }";
        for(int i = 0; i < jsonArray.size(); i++){
            String temp_string = "{\n";
            JsonObject jsonObject_ = jsonArray.get(i).getAsJsonObject();
            int id = jsonObject_.get("id").getAsInt();
            String course_name = jsonObject_.get("course_name").getAsString();
            float avg_marks = jsonObject_.get("avg_marks").getAsFloat();
            avg_marks = (100 - avg_marks);
            course_name = new StringBuilder(course_name).reverse().toString();
            temp_string += "id: " + id + "\n";
            temp_string += "course_name: \"" + course_name + "\"\n";
            temp_string += "avg_marks: " + avg_marks + "\n";
            temp_string += "}\n";
            temp_query_post_itr += temp_string;
        }

        QUERY_POST = temp_query_post_start + temp_query_post_itr + temp_query_post_end;
    }

    public static void main(String[] args) throws JSONException {
        Scanner in = new Scanner(System.in);
        System.out.print("whom do u want to communicate to? Python OR JAVA: ");
        String input = in.nextLine();
        if(input.equalsIgnoreCase("java")){
            postAllUsersAPIJAVA(callPostAllUsersAPIJAVA());
            callPostAllUsersAPIJAVA();
        }
        else if(input.equalsIgnoreCase("python")){
            postAllUsersAPIPython(callPostAllUsersAPIPython());
            callPostAllUsersAPIPython();
        }
    }

    private static JsonArray callPostAllUsersAPIJAVA() throws JSONException {
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Arrays.asList(MediaType.APPLICATION_JSON));

        HttpEntity<String> entity = new HttpEntity<>(QUERY_GET, headers);
        ResponseEntity<String> result = restTemplate.exchange(URI,
                HttpMethod.POST, entity, String.class);
        //System.out.println(result.getBody());

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonParser jp = new JsonParser();
        JsonElement je = jp.parse(result.getBody());
        //System.out.println(gson.toJson(je));
        JsonObject jsonObject = je.getAsJsonObject();
        System.out.println(jsonObject.get("data"));
        JsonElement jsonElement= jsonObject.get("data");
        return (JsonArray) ((JsonObject) jsonElement).get("getCourses");
    }

    private static void postAllUsersAPIJAVA(JsonArray jsonArray) {
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Arrays.asList(MediaType.APPLICATION_JSON));

        makePostQuery(jsonArray);

        HttpEntity<String> entity = new HttpEntity<>(QUERY_POST, headers);
        ResponseEntity<String> result = restTemplate.exchange(URI,
                HttpMethod.POST, entity, String.class);

        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonParser jp = new JsonParser();
        JsonElement je = jp.parse(result.getBody());
        System.out.println(gson.toJson(je));
    }

    private static JsonArray callPostAllUsersAPIPython() throws JSONException {
        Map<String, String> param = new HashMap<>();
        param.put("query", "\n    query {\n      getCourses {\n        id\n        course_name\n        avg_marks\n      }\n    }\n    ");
        ResponseEntity<String> result = restTemplate.postForEntity(URI, param, String.class);
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonParser jp = new JsonParser();
        JsonElement je = jp.parse(result.getBody());
        System.out.println(gson.toJson(je));
        JsonObject jsonObject = je.getAsJsonObject();
        JsonElement jsonElement= jsonObject.get("data");
        return (JsonArray) ((JsonObject) jsonElement).get("getCourses");
    }

    private static void postAllUsersAPIPython(JsonArray jsonArray) {
        String QUERY_POST_PYTHON = makePostQueryPython(jsonArray);
        Map<String, String> param = new HashMap<>();
        param.put("query", QUERY_POST_PYTHON);
        ResponseEntity<String> result = restTemplate.postForEntity(URI, param, String.class);
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        JsonParser jp = new JsonParser();
        JsonElement je = jp.parse(result.getBody());
        System.out.println(gson.toJson(je));
    }
}