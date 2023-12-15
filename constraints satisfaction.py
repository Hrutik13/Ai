from __future__ import print_function

from simpleai.search import CspProblem, backtrack, min_conflicts,MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE,LEAST_CONSTRAINING_VALUE

variables = ('Malvan', 'Kudal', 'Vengurla', 'Sawantwadi', 'Kankavli', 'Dodamarg', 'Devgad','Vaibhavwadi')

domains = dict((v, ['red', 'green', 'blue']) for v in variables)

def const_different(variables, values):
    return values[0] != values[1] 
constraints = [
    (('Malvan', 'Kudal'), const_different),
    (('Malvan', 'Devgad'), const_different),
    (('Malvan', 'Kankavli'), const_different),
    (('Malvan', 'Vengurla'), const_different),
    (('Kudal', 'Sawantwadi'), const_different),
    (('Kudal', 'Malvan'), const_different),
    (('Kudal', 'Kankavli'), const_different),
    (('Kudal', 'Vengurla'), const_different),
    (('Sawantwadi', 'Vengurla'), const_different),
    (('Sawantwadi', 'Dodamarg'), const_different),
    (('Sawantwadi', 'Kudal'), const_different),
    (('Kankavli', 'Malvan'), const_different),
    (('Kankavli', 'Devgad'), const_different),
     (('Kankavli', 'Kudal'), const_different),
     (('Kankavli', 'Vaibhavwadi'), const_different),
     (('Vengurla', 'Sawantwadi'), const_different),
     (('Vengurla', 'Kudal'), const_different),
    (('Vengurla', 'Malvan'), const_different),
    (('Vaibhavwadi', 'Kankavli'), const_different),
    (('Dodamarg', 'Sawantwadi'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

print(backtrack(my_problem))
print(backtrack(my_problem,
variable_heuristic=MOST_CONSTRAINED_VARIABLE))
print(backtrack(my_problem,
variable_heuristic=HIGHEST_DEGREE_VARIABLE))
print(backtrack(my_problem,
value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem,
variable_heuristic=MOST_CONSTRAINED_VARIABLE,
value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(my_problem,
variable_heuristic=HIGHEST_DEGREE_VARIABLE,
value_heuristic=LEAST_CONSTRAINING_VALUE))
print(min_conflicts(my_problem))
