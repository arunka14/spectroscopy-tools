def functional_groups(peak):
   
    matches = []
    
    if 3200 < peak < 3600:
        matches.append("Phenol (O-H stretch)")
    if 2500 < peak < 3300:
        matches.append("Carboxylic Acid (O-H stretch)")
    if 3300 < peak < 3500:
        matches.append("Amine (N-H stretch)")
    if 2850 < peak < 2960:
        matches.append("Alkane (C-H stretch)")
    if 3000 < peak < 3100:
        matches.append("Alkene or Aromatic (C-H stretch)")
    if 1650 < peak < 1800:
        matches.append("Carbonyl or Ester (C=O stretch)")
    if 2100 < peak < 2260:
        matches.append("Alkyne (C≡C stretch)")
    if 2220 < peak < 2260:
        matches.append("Nitrile (C≡N stretch)")

    return matches

value = input("Enter your IR peak: ")

try:
    peak = float(value)
    possible_groups = functional_groups(peak)
    
    if possible_groups:
        print("Possible functional groups:")
        for group in possible_groups:
            print(f"- {group}")
    else:
        print("No common functional group found for this peak value.")
        
except ValueError:
    print("Invalid input. Please enter a numerical value.")





