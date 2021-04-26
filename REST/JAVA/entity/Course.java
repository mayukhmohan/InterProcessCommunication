package com.mayukh.rest.entity;

public class Course {
    private int id;
    private float avg_marks;
    private String course_name;
    private DateTime end_of_course;

    public DateTime getEnd_of_course() {
        return end_of_course;
    }

    public void setEnd_of_course(DateTime end_of_course) {
        this.end_of_course = end_of_course;
    }

    public Course() {
    }

    public Course(int id, float avg_marks, String course_name, DateTime end_of_course) {
        this.id = id;
        this.avg_marks = avg_marks;
        this.course_name = course_name;
        this.end_of_course = end_of_course;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getcourse_name() {
        return course_name;
    }

    public void setcourse_name(String course_name) {
        this.course_name = course_name;
    }

    public float getavg_marks() {
        return avg_marks;
    }

    public void setavg_marks(float avg_marks) {
        this.avg_marks = avg_marks;
    }

    public Course(int id, String course_name, float avg_marks) {
        this.id = id;
        this.course_name = course_name;
        this.avg_marks = avg_marks;
    }

    @Override
    public String toString() {
        return "Course{" +
                "id=" + id +
                ", avg_marks=" + avg_marks +
                ", course_name='" + course_name + '\'' +
                ", end_of_course=" + end_of_course +
                '}';
    }
}
