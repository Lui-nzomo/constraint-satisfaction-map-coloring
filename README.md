# constraint-satisfaction-map-coloring
Constraint Satisfaction Problem (CSP) solver for coloring Australia's regions and Nairobi's sub-counties with minimum colors
# Map Coloring using Constraint Satisfaction Problem (CSP)

## Overview
This repository implements **Constraint Satisfaction Problem (CSP)** solutions for two real-world map coloring challenges:
1. **Australia's 5 regions** - Colored using exactly 3 colors (Blue, Red, Green)
2. **Nairobi's 17 sub-counties** - Colored using the minimum possible number of colors

## Problem Statement
Given a map divided into regions (nodes) with adjacency constraints (edges), assign colors to each region such that:
- No two adjacent regions share the same color
- Minimize the number of colors used (for Nairobi)
- Use exactly 3 colors (for Australia)

## Algorithms Implemented
- **Backtracking Search** - For systematic constraint satisfaction
- **Forward Checking** - Prunes invalid assignments early
- **Welsh-Powell Algorithm** - Greedy coloring with degree-based ordering
- **Graph Coloring Heuristics** - Largest-first vertex ordering

## Features
✅ Australia map coloring with 5 regions and 3 colors  
✅ Nairobi simulative map with 17 sub-counties  
✅ Constraint validation for all adjacencies  
✅ Minimum color optimization (Four Color Theorem compliant)  
✅ Easy to adapt for any map by modifying adjacency data  
✅ Visualization-ready output (color assignments mapped to region names)

## Technologies Used
- Python 3.8+
- Standard libraries only (no external dependencies)
- Optional: NetworkX for advanced graph operations

