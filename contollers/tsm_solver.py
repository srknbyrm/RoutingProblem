import pulp

from contollers.database_operations.problem_record import record_problem

"""
Travelling Sales Man Mathematical Representation
obj:
    min sum Ci*Xi
st:
    sum sign with index i  Nij * Xi >= Rj
    all var >= 0
    
DV : Xij --> 1: if driver travels from location i to location j, o.w. : 0
obj:
    min z = sum i,j Dij*Xij
st:
    sum i Xi,j = 1
    sum j Xi,j = 1
    sum i, j Xi,j <= |S|-1 S C V, 2<=|S|<=n-2
    All var. >= 0
    
Parameters
Dij: Distance btw locations 
"""

from contollers.distance_calculator import DistanceCalculator


class TSM:
    def __init__(self, locations, name):
        self.locations = locations
        self.name = name

    def solve_tsm(self):
        distance_calculator = DistanceCalculator()
        coordinates = distance_calculator.create_coordinate_list(self.locations)
        distance = distance_calculator.create_distance_matrix(coordinates)
        I = [i for i in range(1, len(self.locations) + 1)]
        J = [j for j in range(1, len(self.locations) + 1)]
        x = pulp.LpVariable.dicts('x', [(i, j) for i in I for j in J], 0, 1, pulp.LpBinary)
        u = pulp.LpVariable.dicts('u', (i for i in I), lowBound=1, upBound=len(I), cat='Integer')
        objective = pulp.LpAffineExpression(e=[(x[i, j], distance[i, j]) for i in I for j in J],
                                            name='Objective function')
        model = pulp.LpProblem('TSP', pulp.LpMinimize)
        model += pulp.lpSum(objective)

        for i in I:
            model += x[i, i] == 0
        for i in I:
            tmp_expression = pulp.LpAffineExpression(e=[(x[i, j], 1) for j in J if j != i])
            tmp_constraint = pulp.LpConstraint(e=pulp.lpSum(tmp_expression),
                                               sense=pulp.LpConstraintEQ,
                                               rhs=1)
            model.addConstraint(tmp_constraint)

        for j in J:
            tmp_expression = pulp.LpAffineExpression(e=[(x[i, j], 1) for i in I if j != i])
            tmp_constraint = pulp.LpConstraint(e=pulp.lpSum(tmp_expression),
                                               sense=pulp.LpConstraintEQ,
                                               rhs=1)
            model.addConstraint(tmp_constraint)

        for i in range(len(I)):
            for j in range(len(I)):
                if i != j and (i != 0 and j != 0):
                    model += u[i] - u[j] <= 4 * (1 - x[i, j]) - 1

        status = model.solve()

        direction = dict()
        for i in I:
            for j in J:
                if x[i, j].varValue == 1.0:
                    direction[i] = j
        list_of_direction = list()
        list_of_direction.append(direction[1])
        for i in range(2, len(I) + 1):
            list_of_direction.append(direction[list_of_direction[-1]])
        output = list()
        output.append(self.locations[0]["name"])
        for index in list_of_direction:
            output.append(self.locations[index - 1]["name"])
        record_problem(name=self.name, locations=self.locations, objective=pulp.value(model.objective), output=output)
        return status, output, pulp.value(model.objective)


# Test

# locations = [{"name": "Ankara", "latitude": "32144", "longitude": "35090"},
#              {"name": "Izmir", "latitude": "32144", "longitude": "35090"},
#              {"name": "Adana", "latitude": "32144", "longitude": "35090"},
#              {"name": "Istanbul", "latitude": "45554", "longitude": "54222"}]
#
# tsm = TSM(locations, "Deneme")
# tsm.solve_tsm()
