package com.example.QLTV;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class QltvApplication {

	public static void main(String[] args) {
		SpringApplication.run(QltvApplication.class, args);
	}

}
