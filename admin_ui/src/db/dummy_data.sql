/*
This script will DELETE all rows from the following entities, 
before inserting the dummy data - Student, Teacher, Assignment,
Category, Quest, Subquest, Npc

For live demo, we assume Assignment, Challenge, Mail will be
created on the spot
 */
DELETE FROM Student;
INSERT INTO Student
VALUES (
        1,
        "B190020@e.ntu.edu.sg",
        "Leong Hao Zhi",
        0,
        2,
        1,
        1
    );
INSERT INTO Student
VALUES (
        2,
        "looy0018@e.ntu.edu.sg",
        "Loo Yi Ying Phoebe",
        0,
        2,
        1,
        2
    );
INSERT INTO Student
VALUES (
        3,
        "ERNE0009@e.ntu.edu.sg",
        "Ernest Ang Cheng Han",
        0,
        2,
        1,
        3
    );
DELETE FROM Teacher;
INSERT INTO Teacher
VALUES (0, "wtan132@e.ntu.edu.sg", "Tan Wei Lun");
DELETE FROM Assignment;
INSERT INTO Assignment
VALUES (
        "CZ3001 Assignment 1",
        "wtan132@e.ntu.edu.sg",
        "ERNE0009@e.ntu.edu.sg",
        "Covering materials from lectures 1 - 3",
        NULL,
        NULL
    );
INSERT INTO Assignment
VALUES (
        "CZ3002 Assignment 1",
        "wtan132@e.ntu.edu.sg",
        "looy0018@e.ntu.edu.sg",
        "Covering materials from lectures 1 - 3",
        NULL,
        NULL
    );
INSERT INTO Assignment
VALUES (
        "CZ3003 Assignment 1",
        "wtan132@e.ntu.edu.sg",
        "B190020@e.ntu.edu.sg",
        "Covering materials from lectures 1 - 3",
        NULL,
        NULL
    );
DELETE FROM Category;
INSERT INTO Category
VALUES (
        "CZ3001 Advanced Computer Organization and Architecture"
    );
INSERT INTO Category
VALUES ("CZ3002 Advanced Software Engineering");
INSERT INTO Category
VALUES ("CZ3003 Software Systems Analysis and Design");
DELETE FROM Quest;
INSERT INTO Quest
VALUES (
        "CZ3001 Quest 1",
        "CZ3001 Advanced Computer Organization and Architecture"
    );
INSERT INTO Quest
VALUES (
        "CZ3002 Quest 1",
        "CZ3002 Advanced Software Engineering"
    );
INSERT INTO Quest
VALUES (
        "CZ3003 Quest 1",
        "CZ3003 Software Systems Analysis and Design"
    );
DELETE FROM Subquest;
INSERT INTO Subquest
VALUES ("CZ3001 Subquest 1", "CZ3001 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 1", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3003 Subquest 1", "CZ3003 Quest 1");
DELETE FROM Npc;
INSERT INTO Npc
VALUES ("Daenerys Targaryen", "CZ3001 Subquest 1");
INSERT INTO Npc
VALUES ("Arya Stark", "CZ3002 Subquest 1");
INSERT INTO Npc
VALUES ("Tyrion Lannister", "CZ3003 Subquest 1");
DELETE FROM Question;
INSERT INTO Question
VALUES (
        0,
        "CZ3001 Subquest 1",
        0,
        5,
        "Which of the following is not a type of cache miss?",
        2,
        "Conflict Miss",
        "Starvation Miss",
        "Capacity Miss",
        "Compulsory Miss"
    );
INSERT INTO Question
VALUES (
        1,
        "CZ3002 Subquest 1",
        0,
        5,
        "Which of the following is not a testing strategy?",
        1,
        "Unit Testing",
        "Integration Testing",
        "Mechanical Testing",
        "Regression Testing"
    );
INSERT INTO Question
VALUES (
        2,
        "CZ3003 Subquest 1",
        0,
        5,
        "Which of the following is not an architectural style?",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );