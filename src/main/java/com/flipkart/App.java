package com.flipkart;

public class App {

    public String getMessage() {
        return "Flipkart CI/CD Automation";
    }

    public static void main(String[] args) {
        System.out.println(new App().getMessage());
    }
}
