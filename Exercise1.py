survey_results = [
    ["Python", "Java", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python","Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

survey_sets = [set(language) for language in survey_results]
print(survey_sets)

most_popular_language = set.intersection(*survey_sets)
print("Most popular language:", most_popular_language)

unique_languages_count = len(set.union(*survey_sets))
print("Number of unique languages:", unique_languages_count)