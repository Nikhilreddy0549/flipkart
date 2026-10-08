package com.flipkart;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AppTest {

    @Test
    void shouldReturnCorrectMessage() {
        App app = new App();

        assertEquals(
                "Flipkart CI/CD Automation",
                app.getMessage()
        );
    }
}
