from itertools import product

# Define the colors
colors = ['Blue', 'Red', 'Green']

# Define the regions
regions = ['WA', 'NT', 'QLD', 'SA', 'NSW']

# Define adjacencies (neighbors)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'QLD', 'SA'],
    'QLD': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'QLD', 'NSW'],
    'NSW': ['QLD', 'SA']
}

# Backtracking search for constraint satisfaction
def is_valid(assignment, region, color):
    """Check if assigning color to region violates any constraint"""
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    """Recursive backtracking to find a valid coloring"""
    if len(assignment) == len(regions):
        return assignment
    
    # Select unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]
    
    # Try each color
    for color in colors:
        if is_valid(assignment, region, color):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]
    
    return None

# Solve the problem
solution = backtrack({})
print("Australia 5-Region Coloring Solution:")
print("=" * 40)
if solution:
    for region in regions:
        print(f"{region}: {solution[region]}")
    
    # Verify all constraints
    print("\nVerification (adjacent regions have different colors):")
    for region, neighbors_list in neighbors.items():
        for neighbor in neighbors_list:
            if solution[region] == solution[neighbor]:
                print(f"  ERROR: {region} and {neighbor} both {solution[region]}")
            else:
                print(f"  OK: {region}({solution[region]}) ≠ {neighbor}({solution[neighbor]})")
else:
    print("No solution found!")