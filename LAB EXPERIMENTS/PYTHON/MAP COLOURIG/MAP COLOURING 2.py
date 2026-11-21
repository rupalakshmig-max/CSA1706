
# Map Colouring using Graph Colouring

# Countries and their neighbouring countries
graph = {
    'Germany': ['Poland', 'Austria', 'Czech Republic', 'Switzerland'],
    'Poland': ['Germany', 'Czech Republic', 'Slovakia'],
    'Austria': ['Germany', 'Czech Republic', 'Switzerland',
                'Italy', 'Slovenia', 'Hungary', 'Slovakia'],
    'Czech Republic': ['Poland', 'Germany', 'Austria', 'Slovakia'],
    'Switzerland': ['Germany', 'Austria', 'Italy'],
    'Slovakia': ['Poland', 'Czech Republic', 'Austria', 'Hungary'],
    'Italy': ['Switzerland', 'Austria', 'Slovenia'],
    'Slovenia': ['Italy', 'Austria', 'Hungary'],
    'Hungary': ['Slovenia', 'Austria', 'Slovakia']
}

colors = ['Red', 'Green', 'Blue','YELLLOW']
result = {}

def is_safe(country, color):
    for neighbor in graph[country]:
        if result.get(neighbor) == color:
            return False
    return True

def solve(index=0):
    countries = list(graph.keys())

    if index == len(countries):
        return True

    country = countries[index]

    for color in colors:
        if is_safe(country, color):
            result[country] = color

            if solve(index + 1):
                return True

            del result[country]

    return False

# Display the solution
if solve():
    print("Map Colouring Solution:")
    for country, color in result.items():
        print(country, ":", color)
else:
    print("No solution exists")
