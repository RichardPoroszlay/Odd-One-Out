## Purpose of the system

Introduction:
The purpose of the Odd-One-Out game is to create an interactive and entertaining Python-based application that challenges players' observation and analytical skills. The game is designed to present a series of words to the player, with the objective of identifying the item that does not belong to the group based on a predefined rule or pattern.

Game Objective:
The primary goal of the Odd-One-Out game is to engage players in a fun and intellectually stimulating activity.
Within each set, there will be one item that does not conform to the underlying rule or pattern, making it the "odd one out." Players must identify and select this item to advance to the next level or earn points.

Key Features:
- User-Friendly Interface: A clean and intuitive graphical user interface (GUI) will be provided to enhance the overall gaming experience.
- Varied Content: The game will support multiple modes, ensuring a diverse and engaging experience for players.

Target Audience:
The Odd-One-Out game is designed for individuals of all ages who enjoy puzzle-solving and cognitive challenges. It can be a valuable educational tool for enhancing logical reasoning and pattern recognition skills in children and adults alike.

Conclusion:
The Odd-One-Out game aims to provide an engaging and intellectually stimulating gaming experience, fostering cognitive skills and logical reasoning in players. By offering varied content, it seeks to entertain and educate players of all ages.

## Project plan

The first and most important issue is to clarify responsibilites to our project.

In our project there are two roles: Scrum master and Developer.

### What does a Scrum master do?

Scrum master: A Scrum Master is a professional who leads a team using Agile project management through the course of a project. A Scrum Master facilitates all the communication and collaboration between leadership and team players to ensure a successful outcome.

### What does a Developer do?

Software developers design, program, build, deploy and maintain software using many different skills and tools. They also help build software systems that power networks and devices and ensure that those systems remain functional.

### Members in our team

- Richárd Poroszlay: Scrum master, Developer
- Balázs Ádám Sidlóczki: Developer
- Lambert Attila Lipők: Developer
- Zoltán Tar: Developer

### Schedule

We make this project within 3 weeks.

- First week: Declaring functional and requirement specification.
- Second week: Declaring system-plan.
- Third week: Coding the project.

### Achievements

Our goal is to create the application by the end of September. We want it to be presentable to public audience.

## Model of business processes

The project has basically two participants: players and developers.
The players can access and play all the available game modes, whereas the developers can also change the sourcecode and they have access to the database.
The players can not see the database itself nor can not change the code.

We've created a diagram of this process, see it below.

![model of business processes](../res/model-of-business-processes.png)

## Requirements

### Functional requirements

- operation in a web environment
- Database management. Storing puzzles in a database.
- Navigation between game modes
- Base game mode
- Time race mode
- Input based mode
- Hardcore mode

### Non-functional requirements

- Clean design
- User-friendly software

## Physical environment

Development Platform: Our program will be implemented in Python using the Flask web framework. Furthermore we will use MySQL database to store the data.

Development tools:
- Python
- Flask
- MySQL
- Visual Studio Code

Operating System: Since our program will be hosted as a web page, the only requirement is to use a web browser with stable internet.

## Installation plan

It's a web application, thus you only need to download a web browser.

This web browser can be:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Opera
- Safari

In order to play with the game, you need to have internet connection, because the client connects directly to the webserver via internet connection.

## Test plan

The purpose of testing is to fully examine and verify the functionality of the system and its components,
as well as to verify the business services implemented by the system.

### Testing Procedures

Unit Test:
Wherever possible, it is necessary to test during the development phase to ensure that the methods are functioning correctly. 
Therefore, Unit tests should be written for each method, keeping in mind the goal of achieving maximum code coverage. 
The methods are considered ready when the test cases run without errors on each method.

Alpha Test:
The primary goal of this test is to test the compatibility of existing features with different browsers. 
The test is performed by the developers themselves.
The procedure is considered successful if the various features work correctly in different browsers.

### Functions to be Tested

Backend Service:
- It should be able to connect to web clients.
- It should be capable of serving multiple clients simultaneously.
- It should be able to upload and query data from the database.
- It should be capable of providing all the functionalities available on all interfaces.

### Registration interface

The program will not have a registration interface, so it cannot and will not be tested.


## Implementation plan

### WEB

HTML - serves as a fundamental language in a web project, aiding in the structuring of web content.
It enables web developers to design the layout, style, and interactivity of web pages, thereby enhancing the user experience.
Its defines the elements and tags used to arrange text, images, links, and multimedia on web pages.
HTML files form the foundation of web pages, and browsers use them to display content, allowing users to access it over the internet.

CSS - In a web project, CSS is responsible for controlling the visual appearance and style.
It defines attributes like colors, fonts, sizes, and layouts for web pages.
CSS enables web developers to create a consistent look and feel across all webpages.
CSS facilitates improving user experience and effortlessly formatting content on webpages.

### Backend

Python - Python is a commonly used programming language in web projects, known for its versatility and ease of learning.
With Python, you can develop web applications, websites, and server-side scripts.
Popular frameworks like Flask make it easy to build web applications using Python.
Its simplicity and versatility make Python a powerful tool for developing and maintaining web projects.

Flask - Flask is a lightweight and micro web framework for building web applications in Python.
It provides essential tools and libraries to create web-based projects quickly and efficiently.
Flask is ideal for prototyping, building small to medium-sized web applications, and can be extended with various extensions and libraries as needed.

MySQL - MySQL is an open-source relational database management system that plays a crucial role in web projects.
It aids in efficiently storing, querying, and managing data for web applications and websites.
MySQL offers a reliable and efficient database system, making it indispensable for modern web development.