disease(diabetes).
disease(blood_pressure).
disease(obesity).

advice(diabetes,
       'Consult a qualified healthcare professional for dietary guidance').

advice(blood_pressure,
       'Consult a qualified healthcare professional for dietary guidance').

advice(obesity,
       'Consult a qualified healthcare professional for dietary guidance').

check_diet(Disease) :-
    disease(Disease),
    advice(Disease, Advice),
    write(Advice).