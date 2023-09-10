# Odd One Out

## Overview
In this project, we implement an Odd One Out videogame.
The project's backend is made in Python with the Flask micro web framework, and for the frontend we use HTML and CSS.

The game contains multiple game modes, so the player can choose their favourite ones in the GUI.
After the player has chosen their game mode, their purpose is to find the inappropriate word in the word set.
The purpose of each game mode is different. (see Functional Specification)

You play this game just for the sheer fun of it. This game provides pure enjoyment for individuals aged 2 to 99.
Plus thanks to more game modes, you can choose what is the most suitable for you.
The first game mode would be a base game, where you just select the Odd One Out.
In the next game mode race against time.
In the third game mode you decide how many rounds youu wanna play.
The fourth game mode would be a hardcore game mode.

## Current state
The first and most important purpose of our application is entertainment and spending valuable time. The Odd One Out games are intuitive and
challenging. As scientific publications state, the game helps young children to improve the way of their thinking.
The game is also good for ability testing such as linguistic and analytic skills measuring.

## Developers purpose
Our purpose is to create an open source, free application which helps the education of the young generation.
We also want the game to be available in digital format.

We are planning to create four game modes:
- Base game
- Time race
- Input based
- Hardcore

## Functional requirements
In the main menu we can choose between different game modes.
In each game mode the player choose between given words with their mice in the GUI window.

## System License
It's an open source project, no licence is used.

## Why would I use this project?
Nowadays the young generation have access to digital devices, thus our objective is to have this game available also digitally, not only as a card game.

This provides more flexibility.

## Applied business processes
In contrast to accessable websites, our application requires no registration.
We don't keep any of your data, so you can play safely with our game.

## List of Requirements

| Modul   | ID   | Name       | Description |
| ------- | ---- | ---------- | ----------- |
| Surface | N1   | Main menu  |  The player can choose between different game modes.  |
| Surface | N2   | Base game  | Displays the base game mode |
| Surface | N3   | Time race  |  Displays the Time race mode |
| Surface | N4   | Input based| Displays the Input based mode  |
| Surface | N5   | Hardcore   |   Displays the Hardcore mode  |

## Functional specification of requirement list

| Modul   | ID   | Name       | Description |
| ------- | ---- | ---------- | ----------- |
| Surface | N1   | Main menu  |  The user encounters this screen when they start the program. The main function of the interface is to allow the player to navigate between game modes. A crucial requirement is a clean and clear design.  |
| Surface | N2   | Base game  | The most basic game mode. The user is provided with word quadruples, from which they can choose which one does not belong to the group. The program provides feedback on the success of the guess. |
| Surface | N3   | Time race  |  On the screen, the player can test their speed. The basic game loop remains, but the goal here is to provide as many correct answers as possible within a given time frame. |
| Surface | N4   | Input based| he interface also includes an input field in this screen. The user can decide how many rounds they want to start consecutively. The goal is to make as few mistakes as possible.  |
| Surface | N5   | Hardcore   |   Hardcore mode. The user receives tasks one after another consecutively. However, they cannot make a single mistake. If they provide a wrong answer, the game is over.  |


## Use cases

The software does not handle user profiles. There is no authentication, and there are no user roles. As soon as the program starts, the user appears as a player. In this capacity, they have access to all of the program's game modes. They have unlimited attempts, and they can restart the game as many times as they want. However, there are no admin privileges, and users cannot modify the software's properties.

## Model of required business processes

The Odd One Out game is a versatile and valuable educational tool that promotes critical thinking, creativity, and cognitive skills while also making learning enjoyable. It can be employed in various contexts to engage participants, reinforce learning, and foster a deeper understanding of concepts and relationships. Whether in a classroom, a team-building session, or a family gathering, this game has enduring appeal and usefulness.