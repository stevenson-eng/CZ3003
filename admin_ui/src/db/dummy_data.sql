/*
 This script will DELETE all rows from the following entities, 
 before inserting the dummy data - Student, Teacher, Assignment,
 Category, Quest, Subquest, Npc, Attempt
 
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
INSERT INTO Student
VALUES (
        4,
        "student4@gmail.com",
        "student 4",
        0,
        2,
        1,
        4
    );
INSERT INTO Student
VALUES (
        5,
        "student5@gmail.com",
        "student 5",
        0,
        2,
        1,
        5
    );
INSERT INTO Student
VALUES (
        6,
        "student6@gmail.com",
        "student 6",
        0,
        2,
        1,
        6
    );
INSERT INTO Student
VALUES (
        11,
        "student11@gmail.com",
        "student 11",
        0,
        2,
        1,
        4
    );
INSERT INTO Student
VALUES (
        10,
        "student10@gmail.com",
        "student 10",
        0,
        2,
        1,
        5
    );
INSERT INTO Student
VALUES (
        12,
        "student12@gmail.com",
        "student 12",
        0,
        2,
        1,
        6
    );
INSERT INTO Student
VALUES (
        7,
        "student7@gmail.com",
        "student 7",
        0,
        2,
        1,
        7
    );
INSERT INTO Student
VALUES (
        8,
        "student8@gmail.com",
        "student 8",
        0,
        2,
        1,
        8
    );
INSERT INTO Student
VALUES (
        9,
        "student9@gmail.com",
        "student 9",
        0,
        2,
        1,
        8
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
INSERT INTO Category
VALUES ("CZ2006 Software Engineering");
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
INSERT INTO Quest
VALUES (
        "CZ2006 Quest 1",
        "CZ2006 Software Engineering"
    );
INSERT INTO Quest
VALUES (
        "CZ2006 Quest 2",
        "CZ2006 Software Engineering"
    );
INSERT INTO Quest
VALUES (
        "CZ2006 Quest 3",
        "CZ2006 Software Engineering"
    );
INSERT INTO Quest
VALUES (
        "CZ2006 Quest 4",
        "CZ2006 Software Engineering"
    );
INSERT INTO Quest
VALUES (
        "CZ2006 Quest 5",
        "CZ2006 Software Engineering"
    );
DELETE FROM Subquest;
INSERT INTO Subquest
VALUES ("CZ3001 Subquest 1", "CZ3001 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 1", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 2", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 3", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 4", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3002 Subquest 5", "CZ3002 Quest 1");
INSERT INTO Subquest
VALUES ("CZ3003 Subquest 1", "CZ3003 Quest 1");




INSERT INTO Subquest
VALUES ("CZ2006 Subquest 1", "CZ2006 Quest 1");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 2", "CZ2006 Quest 1");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 3", "CZ2006 Quest 1");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 4", "CZ2006 Quest 1");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 5", "CZ2006 Quest 1");

INSERT INTO Subquest
VALUES ("CZ2006 Subquest 6", "CZ2006 Quest 2");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 7", "CZ2006 Quest 2");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 8", "CZ2006 Quest 2");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 9", "CZ2006 Quest 2");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 10", "CZ2006 Quest 2");

INSERT INTO Subquest
VALUES ("CZ2006 Subquest 11", "CZ2006 Quest 3");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 12", "CZ2006 Quest 3");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 13", "CZ2006 Quest 3");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 14", "CZ2006 Quest 3");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 15", "CZ2006 Quest 3");

INSERT INTO Subquest
VALUES ("CZ2006 Subquest 16", "CZ2006 Quest 4");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 17", "CZ2006 Quest 4");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 18", "CZ2006 Quest 4");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 19", "CZ2006 Quest 4");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 20", "CZ2006 Quest 4");

INSERT INTO Subquest
VALUES ("CZ2006 Subquest 21", "CZ2006 Quest 5");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 22", "CZ2006 Quest 5");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 23", "CZ2006 Quest 5");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 24", "CZ2006 Quest 5");
INSERT INTO Subquest
VALUES ("CZ2006 Subquest 25", "CZ2006 Quest 5");


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
        "0",
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
        "1",
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
        "2",
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
















/* CZ2006 Subquest 1, 5 questions, 3 difficulty each */
INSERT INTO Question
VALUES (
        "3",
        "CZ2006 Subquest 1",
        0,
        5,
        "CZ2006 Subquest 1, Easy Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "4",
        "CZ2006 Subquest 1",
        0,
        5,
        "CZ2006 Subquest 1, Easy Question.Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "5",
        "CZ2006 Subquest 1",
        0,
        5,
        "CZ2006 Subquest 1, Easy Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "6",
        "CZ2006 Subquest 1",
        0,
        5,
        "CZ2006 Subquest 1, Easy Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );

INSERT INTO Question
VALUES (
        "7",
        "CZ2006 Subquest 1",
        1,
        5,
        "CZ2006 Subquest 1, Medium Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "8",
        "CZ2006 Subquest 1",
        1,
        5,
        "CZ2006 Subquest 1, Medium Question. Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "9",
        "CZ2006 Subquest 1",
        1,
        5,
        "CZ2006 Subquest 1, Medium Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "10",
        "CZ2006 Subquest 1",
        1,
        5,
        "CZ2006 Subquest 1, Medium Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "11",
        "CZ2006 Subquest 1",
        2,
        5,
        "CZ2006 Subquest 1, Hard Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "12",
        "CZ2006 Subquest 1",
        2,
        5,
        "CZ2006 Subquest 1, Hard Question. Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "13",
        "CZ2006 Subquest 1",
        2,
        5,
        "CZ2006 Subquest 1, Hard Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "14",
        "CZ2006 Subquest 1",
        2,
        5,
        "CZ2006 Subquest 1, Hard Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "15",
        "CZ2006 Subquest 1",
        0,
        5,
        "CZ2006 Subquest 1, Easy Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );
INSERT INTO Question
VALUES (
        "16",
        "CZ2006 Subquest 1",
        1,
        5,
        "CZ2006 Subquest 1, Medium Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );
INSERT INTO Question
VALUES (
        "17",
        "CZ2006 Subquest 1",
        2,
        5,
        "CZ2006 Subquest 1, Hard Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );
















INSERT INTO Question
VALUES (
        "1113",
        "CZ2006 Subquest 2",
        0,
        5,
        "CZ2006 Subquest 2, Easy Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "1114",
        "CZ2006 Subquest 2",
        0,
        5,
        "CZ2006 Subquest 2, Easy Question.Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "1115",
        "CZ2006 Subquest 2",
        0,
        5,
        "CZ2006 Subquest 2, Easy Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "1116",
        "CZ2006 Subquest 2",
        0,
        5,
        "CZ2006 Subquest 2, Easy Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );

INSERT INTO Question
VALUES (
        "1117",
        "CZ2006 Subquest 2",
        1,
        5,
        "CZ2006 Subquest 2, Medium Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "1118",
        "CZ2006 Subquest 2",
        1,
        5,
        "CZ2006 Subquest 2, Medium Question. Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "1119",
        "CZ2006 Subquest 2",
        1,
        5,
        "CZ2006 Subquest 2, Medium Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "110",
        "CZ2006 Subquest 2",
        1,
        5,
        "CZ2006 Subquest 2, Medium Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "111",
        "CZ2006 Subquest 2",
        2,
        5,
        "CZ2006 Subquest 2, Hard Question. Answer is 1",
        1,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "112",
        "CZ2006 Subquest 2",
        2,
        5,
        "CZ2006 Subquest 2, Hard Question. Answer is 2",
        2,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "113",
        "CZ2006 Subquest 2",
        2,
        5,
        "CZ2006 Subquest 2, Hard Question. Answer is 3",
        3,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "114",
        "CZ2006 Subquest 2",
        2,
        5,
        "CZ2006 Subquest 2, Hard Question. Answer is 4",
        4,
        "Pipe-and-filter",
        "Layered",
        "Client-Server",
        "Message Stacks"
    );
INSERT INTO Question
VALUES (
        "115",
        "CZ2006 Subquest 2",
        0,
        5,
        "CZ2006 Subquest 2, Easy Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );
INSERT INTO Question
VALUES (
        "116",
        "CZ2006 Subquest 2",
        1,
        5,
        "CZ2006 Subquest 2, Medium Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );
INSERT INTO Question
VALUES (
        "117",
        "CZ2006 Subquest 2",
        2,
        5,
        "CZ2006 Subquest 2, Hard Question. Answer is 4",
        4,
        "Lorem Ipsum",
        "expedita distinctio",
        "maiores alias consequatur",
        "tenetur a sapiente"
    );



























DELETE FROM Attempt;
INSERT INTO Attempt
VALUES (
        "CZ3001 Quest 1",
        "B190020@e.ntu.edu.sg",
        50,
        100,
        3600,
        "2021-10-18 16:53:31.498332"
    );
INSERT INTO Attempt
VALUES (
        "CZ3002 Quest 1",
        "B190020@e.ntu.edu.sg",
        85,
        120,
        1800,
        "2021-10-18 18:10:31.498332"
    );
INSERT INTO Attempt
VALUES (
        "CZ3003 Quest 1",
        "B190020@e.ntu.edu.sg",
        50,
        150,
        600,
        "2021-10-18 20:23:31.498332"
    );