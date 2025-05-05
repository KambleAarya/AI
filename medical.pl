% Symptoms for illnesses
disease(flu) :- has_symptom(fever), has_symptom(cough), has_symptom(body_ache).
disease(covid) :- has_symptom(fever), has_symptom(cough), has_symptom(loss_of_taste), has_symptom(breathing_difficulty).
disease(malaria) :- has_symptom(fever), has_symptom(chills), has_symptom(sweating), has_symptom(nausea).
disease(dengue) :- has_symptom(fever), has_symptom(headache), has_symptom(rash), has_symptom(joint_pain).
disease(common_cold) :- has_symptom(runny_nose), has_symptom(cough), has_symptom(sore_throat).

% Interface rule
diagnose :- 
    write('Enter symptom names one by one followed by a period (.)'), nl,
    repeat,
    read(S),
    (S == done -> true; assertz(has_symptom(S)), fail),
    disease(D), write('Diagnosis: '), write(D), nl,
    retractall(has_symptom(_)).

?- diagnose.
Enter symptom names one by one followed by a period (.)
|: fever.
|: cough.
|: loss_of_taste.
|: breathing_difficulty.
|: done.
Diagnosis: covid