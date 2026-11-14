symptom(fever, flu).
symptom(cough, flu).

symptom(sneezing, allergy).
symptom(itchy_eyes, allergy).

symptom(headache, general_symptom).

diagnose(Person, Condition) :-
    has_symptom(Person, Symptom),
    symptom(Symptom, Condition).

has_symptom(ravi, fever).
has_symptom(ravi, cough).

has_symptom(priya, sneezing).
has_symptom(priya, itchy_eyes).