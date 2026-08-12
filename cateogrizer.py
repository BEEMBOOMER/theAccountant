def categorizer(row):
    description=row[1].lower()
    categoryKeyword={
        "Grocery":["woolworths","coles","golgappa"],
        "EatingOut":["kfc","maccas","hungry jacks","dominoes","pizza hut","bombay dhaba","south seoul"],
        "Transport":["translink","didi","uber"],
        "Subscription":["lebara","vodafone","telstra","openai","claude"],
        "Health":["chemist warehouse","clinic","hospital","dental"],
        "Education":["qut","uq"],
        "Social":["birthday","club"],
        "Roomate Settlement":["dhanuk","malik","mahith"]}
    for category,keywords in categoryKeyword.items():
        for keyword in keywords:
            if keyword in description:
                return (category,keyword)
    print(description)
    return ("misc",'unknown')
