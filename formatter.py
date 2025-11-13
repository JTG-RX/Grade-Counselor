
def CWA_Formater(result):
    if not result:
        result = {}
    most = result.get("most_important")
    below = result.get("below_70", [])

    if most:
        name = most.get("name") if isinstance(most, dict) else str(most)
        
    
    if below:
        names = ", ".join(
            (item.get("name") if isinstance(item, dict) and "name" in item else str(item))
            for item in below
        )
        return f"you need to do {name} Then work on {names}" 
    else:  
         return f"all assignments are above 70% {below}"
