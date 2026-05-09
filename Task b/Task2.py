from itertools import combinations

def color_nairobi_subcounties_simulative():
    """
    Simulative coloring of Nairobi's 17 sub-counties
    Using graph coloring with minimum colors
    """
    
    # Define sub-counties
    sub_counties = [
        'Westlands', 'Dagoretti_North', 'Dagoretti_South', 'Langata', 'Kibra',
        'Roysambu', 'Kasarani', 'Ruaraka', 'Embakasi_North', 'Embakasi_East',
        'Embakasi_West', 'Embakasi_South', 'Makadara', 'Kamukunji', 'Starehe',
        'Mathare', 'Njiru'
    ]
    
    # Approximated adjacency based on Nairobi's geography
    # (For real application, you'd need actual map data)
    adjacency = {
        'Westlands': ['Dagoretti_North', 'Starehe', 'Roysambu'],
        'Dagoretti_North': ['Westlands', 'Dagoretti_South', 'Kibra'],
        'Dagoretti_South': ['Dagoretti_North', 'Langata', 'Kibra'],
        'Langata': ['Dagoretti_South', 'Kibra', 'Makadara'],
        'Kibra': ['Dagoretti_North', 'Dagoretti_South', 'Langata', 'Makadara'],
        'Roysambu': ['Westlands', 'Kasarani', 'Ruaraka', 'Starehe'],
        'Kasarani': ['Roysambu', 'Ruaraka', 'Embakasi_North'],
        'Ruaraka': ['Roysambu', 'Kasarani', 'Embakasi_North', 'Mathare'],
        'Embakasi_North': ['Kasarani', 'Ruaraka', 'Embakasi_East', 'Embakasi_West'],
        'Embakasi_East': ['Embakasi_North', 'Embakasi_West', 'Embakasi_South', 'Makadara'],
        'Embakasi_West': ['Embakasi_North', 'Embakasi_East', 'Embakasi_South', 'Makadara', 'Njiru'],
        'Embakasi_South': ['Embakasi_East', 'Embakasi_West', 'Makadara', 'Njiru'],
        'Makadara': ['Langata', 'Kibra', 'Embakasi_East', 'Embakasi_West', 'Embakasi_South', 'Kamukunji', 'Starehe'],
        'Kamukunji': ['Makadara', 'Starehe', 'Mathare'],
        'Starehe': ['Westlands', 'Roysambu', 'Makadara', 'Kamukunji', 'Mathare'],
        'Mathare': ['Ruaraka', 'Kamukunji', 'Starehe', 'Njiru'],
        'Njiru': ['Embakasi_West', 'Embakasi_South', 'Mathare']
    }
    
    # Use Welsh-Powell algorithm (greedy coloring with degree ordering)
    # Sort sub-counties by degree (number of neighbors) in descending order
    degrees = {sc: len(adjacency[sc]) for sc in sub_counties}
    sorted_sc = sorted(sub_counties, key=lambda x: degrees[x], reverse=True)
    
    # Greedy coloring
    color_map = {}
    available_colors = list(range(1, 5))  # Start with up to 4 colors
    
    for sc in sorted_sc:
        # Find colors used by neighbors
        used_colors = set()
        for neighbor in adjacency[sc]:
            if neighbor in color_map:
                used_colors.add(color_map[neighbor])
        
        # Assign smallest available color
        for color in available_colors:
            if color not in used_colors:
                color_map[sc] = color
                break
        else:
            # Need more colors
            color_map[sc] = len(color_map) + 1
            available_colors.append(len(color_map) + 1)
    
    # Number the colors
    color_names = {1: 'Red', 2: 'Green', 3: 'Blue', 4: 'Yellow', 5: 'Purple'}
    
    print("Nairobi Sub-Counties Map Coloring (Simulative)")
    print("=" * 50)
    print(f"\nTotal colors used: {max(color_map.values())}")
    print("\nColoring Assignment:")
    print("-" * 40)
    
    for sc in sub_counties:
        print(f"{sc:20} : {color_names[color_map[sc]]}")
    
    # Verify constraints
    print("\n" + "=" * 50)
    print("Constraint Verification (sample of 10 random adjacencies):")
    import random
    verified = 0
    all_edges = [(sc, nb) for sc in sub_counties for nb in adjacency[sc] if sc < nb]
    random_sample = random.sample(all_edges, min(10, len(all_edges)))
    
    for sc, nb in random_sample:
        if color_map[sc] != color_map[nb]:
            print(f"✓ {sc}({color_names[color_map[sc]]}) ≠ {nb}({color_names[color_map[nb]]})")
            verified += 1
        else:
            print(f"✗ ERROR: {sc} and {nb} both {color_names[color_map[sc]]}")
    
    print(f"\nPassed {verified}/{len(random_sample)} random checks")
    
    # Calculate chromatic number lower bound
    max_clique = max(len([n for n in adjacency[sc] if n in adjacency.get(nb, [])]) for sc in sub_counties)
    print(f"\nGraph properties:")
    print(f"  - Number of regions: {len(sub_counties)}")
    print(f"  - Chromatic number lower bound (clique size): ≥ {max_clique + 1}")
    print(f"  - Colors used: {max(color_map.values())}")
    
    return color_map

# Run the simulative solution
solution_map = color_nairobi_subcounties_simulative()