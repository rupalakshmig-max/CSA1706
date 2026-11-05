student(101, 'Ravi').
student(102, 'Priya').
student(103, 'Arun').

teacher(201, 'Kumar').
teacher(202, 'Meena').

subject(301, 'Mathematics').
subject(302, 'Computer Science').

student_teacher(101, 201, 301).
student_teacher(102, 202, 302).
student_teacher(103, 201, 302).

details(S, T, Sub) :-
    student(S, Student),
    teacher(T, Teacher),
    subject(Sub, Subject),
    student_teacher(S, T, Sub),
    write(Student), write(' - '),
    write(Teacher), write(' - '),
    write(Subject).