def calculate_weighted_average(assignments):
    most_important = None
    assignments_list = []
    for a in assignments:
        if a["score"] / a["max_score"] <= 0.7:
            assignments_list.append(a["name"])
            if most_important is None or a["weight"] > most_important["weight"]:
                most_important = a
                

    return{
        "most_important": most_important,
        "below_70": assignments_list
    }
    