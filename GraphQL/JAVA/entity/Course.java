package com.mayukh.graphQL.course.entity;

public class Course {
    private int id;
    private String course_name;
    private float avg_marks;
    private DateTime end_of_course;

    public Course(int id, String course_name, float avg_marks, DateTime end_of_course) {
        this.id = id;
        this.course_name = course_name;
        this.avg_marks = avg_marks;
        this.end_of_course = end_of_course;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCourse_name() {
        return course_name;
    }

    public void setCourse_name(String course_name) {
        this.course_name = course_name;
    }

    public float getAvg_marks() {
        return avg_marks;
    }

    public void setAvg_marks(float avg_marks) {
        this.avg_marks = avg_marks;
    }

    public DateTime getEnd_of_course() {
        return end_of_course;
    }

    public void setEnd_of_course(DateTime end_of_course) {
        this.end_of_course = end_of_course;
    }

    @Override
    public String toString() {
        return "Course{" +
                "id=" + id +
                ", course_name='" + course_name + '\'' +
                ", avg_marks=" + avg_marks +
                ", end_of_course=" + end_of_course +
                '}';
    }
}
