class NeighbourConstraint:
    def __init__(self, region1, region2):
        self.region1 = region1
        self.region2 = region2

    def is_satisfied(self, assignment):
        if self.region1 not in assignment or self.region2 not in assignment:
            return True
        return assignment[self.region1] != assignment[self.region2]


class CSP:
    def __init__(self, regions, colors):
        self.colors = colors
        self.regions = regions
        self.constraints = {region: [] for region in regions}

    def add_constraint(self, constraint):
        self.constraints[constraint.region1].append(constraint)
        self.constraints[constraint.region2].append(constraint)

    def is_consistent(self, region, assignment):
        for constraint in self.constraints[region]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def solve(self, assignment={}):
        if len(assignment) == len(self.regions):
            return assignment

        unassigned_regions = [region for region in self.regions if region not in assignment]
        current_region = unassigned_regions[0]

        for color in self.colors:
            new_assignment = assignment.copy()
            new_assignment[current_region] = color

            if self.is_consistent(current_region, new_assignment):
                result = self.solve(new_assignment)
                if result:
                    return result
        return None


if __name__ == "__main__":
    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]  # Regions of Australia
    colors = ["red", "green", "blue"]

    csp = CSP(regions, colors)

    # Adding constraints
    csp.add_constraint(NeighbourConstraint("WA", "NT"))
    csp.add_constraint(NeighbourConstraint("WA", "SA"))
    csp.add_constraint(NeighbourConstraint("NT", "SA"))
    csp.add_constraint(NeighbourConstraint("NT", "Q"))
    csp.add_constraint(NeighbourConstraint("SA", "Q"))
    csp.add_constraint(NeighbourConstraint("SA", "NSW"))
    csp.add_constraint(NeighbourConstraint("SA", "V"))
    csp.add_constraint(NeighbourConstraint("Q", "NSW"))
    csp.add_constraint(NeighbourConstraint("NSW", "V"))
    csp.add_constraint(NeighbourConstraint("V", "T"))

    solution = csp.solve()
    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution exists!")
