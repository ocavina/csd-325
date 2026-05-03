# Oscar Avina
# 05/2/2026
# Module 7.2 Assignment
# This program returns the name of a city and its country, with optional language and population information.

def city_country(city, country, population="", language=""):
  if population and language: # returns the following info if both population and language are provided
    return f"{city}, {country} - population: {population}, {language}"
  elif population: # returns the following info if only population is provided
    return f"{city}, {country} - population: {population}"
  elif language: # returns the following info if only language is provided
    return f"{city}, {country}, {language}"
  else:
    return f"{city}, {country}"

if __name__ == "__main__":
  print(city_country("Santiago", "Chile"))
  print(city_country("Paris", "France", "2,000,000"))
  print(city_country("London", "England", "9,000,000", "English"))