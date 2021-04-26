package com.mayukh.graphQL.course.entity;

public class CourseID {
    private int id;

    public CourseID(int id) {
        this.id = id;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "CourseID{" +
                "id=" + id +
                '}';
    }
}
