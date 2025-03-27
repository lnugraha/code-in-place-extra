# Code in Place Spring 2025 - Stanford University

Extra suplemental materials dedicated to Code in Place Spring 2025 with Stanford University

Topics to be covered:

## Input Arguments (Week 2: May 02, 2025) ##
<details>
<summary> User Input Prompt: remember all data types are still in string </summary>

```python
def main():
  user_name = input("Enter your name: ")
  print("Good morning " + user_name)
```
</details>  

## Console Programming (Week 3: May 09, 2025) ##

### Conditional Branching ###
<details>
<summary> 1. <b>IF-ELIF-ELSE</b> Statement </summary>

```python
def main():
  MERCURY_GRAVITY = (37.6 / 100)
  VENUS_GRAVITY = (88.9 / 100)
  MARS_GRAVITY = (37.8 / 100)
  JUPITER_GRAVITY = (236 / 100)
  SATURN_GRAVITY = (108.1 / 100)
  URANUS_GRAVITY = (81.5 / 100)
  NEPTUNE_GRAVITY = (114 / 100)    

  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  
  if (planetName == "Mercury"):
    planetWeight = float(earthWeight) * MERCURY_GRAVITY
        
  elif (planetName == "Venus"):
    planetWeight = float(earthWeight) * VENUS_GRAVITY
        
  elif (planetName == "Mars"):
    planetWeight = float(earthWeight) * MARS_GRAVITY

  elif (planetName == "Jupiter"):
    planetWeight = float(earthWeight) * JUPITER_GRAVITY
        
  elif (planetName == "Saturn"):
    planetWeight = float(earthWeight) * SATURN_GRAVITY

  elif (planetName == "Uranus"):
    planetWeight = float(earthWeight) * URANUS_GRAVITY
        
  elif (planetName == "Neptune"):
    planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
    
  else:
    planetWeight = -1.0 # Why put a negative value here?
```
</details>

<details>
<summary> 2. <b>IF</b> Statement</summary>

```python
def main():
  MERCURY_GRAVITY = (37.6 / 100)
  VENUS_GRAVITY = (88.9 / 100)
  MARS_GRAVITY = (37.8 / 100)
  JUPITER_GRAVITY = (236 / 100)
  SATURN_GRAVITY = (108.1 / 100)
  URANUS_GRAVITY = (81.5 / 100)
  NEPTUNE_GRAVITY = (114 / 100)    

  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  planetWeight = -1 # Why put a negative value here?

  if (planetName == "Mercury"):
    planetWeight = float(earthWeight) * MERCURY_GRAVITY
        
  if (planetName == "Venus"):
    planetWeight = float(earthWeight) * VENUS_GRAVITY
        
  if (planetName == "Mars"):
    planetWeight = float(earthWeight) * MARS_GRAVITY

  if (planetName == "Jupiter"):
    planetWeight = float(earthWeight) * JUPITER_GRAVITY
        
  if (planetName == "Saturn"):
    planetWeight = float(earthWeight) * SATURN_GRAVITY

  if (planetName == "Uranus"):
    planetWeight = float(earthWeight) * URANUS_GRAVITY
        
  if (planetName == "Neptune"):
    planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
```
</details>

<details>
<summary> 3. <b>MATCH-CASE</b> Statement (Require Python 3.10 or above) </summary>

```python
def main():
  MERCURY_GRAVITY = (37.6 / 100)
  VENUS_GRAVITY = (88.9 / 100)
  MARS_GRAVITY = (37.8 / 100)
  JUPITER_GRAVITY = (236 / 100)
  SATURN_GRAVITY = (108.1 / 100)
  URANUS_GRAVITY = (81.5 / 100)
  NEPTUNE_GRAVITY = (114 / 100)    

  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  
  match planetName:
    case "Mercury":
      planetWeight = float(earthWeight) * MERCURY_GRAVITY
  
    case "Venus":
      planetWeight = float(earthWeight) * VENUS_GRAVITY
  
    case "Mars":
      planetWeight = float(earthWeight) * MARS_GRAVITY
  
    case "Jupiter":
      planetWeight = float(earthWeight) * JUPITER_GRAVITY
      
    case "Saturn":
      planetWeight = float(earthWeight) * SATURN_GRAVITY
  
    case "Uranus":
      planetWeight = float(earthWeight) * URANUS_GRAVITY
  
    case "Neptune":
      planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
  
    case other:
      planetWeight = -1.0 # Why put a negative value here?
```
</details>

### Printing in Python ###
<b> 1. String Concatenation </b>
- Notice that both "+" and "," can be used interchangably
- Concatenate multiple strings with + (plus) or , (comma)
- All concatenated items have to be converted to the same data type (string)
<details>
<summary> Examples </summary>
  
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on " + planetName + ": " + str(marsWeight))
print("The weight on " , planetName + ": " , str(marsWeight))
```

</details>

<b> 2. Reference </b>
- Notice the ```.format(,)``` patten
- Unlike concatenation method, this method requires no string conversion
- Use the {} (curly brackets) to place your variable
<details>
<summary> Examples </summary>
 
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on {}: {}".format(planetName, planetWeight))
```
</details>

<b> 3. F-word </b>
- Notice the f letter inside print()
- Similar to method 2 (reference), but now variable name is placed inside the curly brackets 
- Likewise, no variable casting (conversion) is needed
<details>
<summary> Examples </summary>
  
```python
planetName = "Mars"; planetWeight = 175.26
print(f"The weight on {planetName}: {planetWeight}")
```
</details>

## Control Flow (Week 4: May 16, 2025) ##

### Writing Functions ###
<b> 1. Returning a Single Output </b>

<details>
<summary> Example: </summary>
  
```python
def calculate_mars_weight(earth_weight):
  MARS_GRAVITY = 0.376
  mars_weight = float(earth_weight) * MARS_GRAVITY
  return round(mars_weight, 2)
  
def main():
  earth_test = float(input("Enter the object weight on Earth: "))
  mars_test = calculate_mars_weight(earth_test)
```
</details>

<b> 2. Returning More than One Output </b>

<details>
<summary> Example: </summary>
  
```python
def calculate_planet_weights(earth_weight):
  MERCURY_GRAVITY = 0.376
  VENUS_GRAVITY = 0.889
  MARS_GRAVITY = 0.378

  mercury_weight = earth_weight * MERCURY_GRAVITY
  venus_weight = earth_weight * VENUS_GRAVITY
  mars_weight = earth_weight * MARS_GRAVITY

  return round(mercury_weight, 2), round(venus_weight, 2), round(mars_weight, 2)
  
def main():
  earth_test = float(input("Enter the object weight on Earth: "))
  mercury_test, venus_test, mars_test = calculate_planet_weights(earth_test)
```
</details>

## Canvas, Graphics, and Animation (Week 5: May 23, 2025) ##

## Data Structures (Week 6: May 30, 2025) ##
Visit: [2024_05_31_DataStructures](https://github.com/lnugraha/code-in-place-extra/tree/2024-edition/2024_05_31_DataStructures)

<b> 1. Calculating Factorial </b>
<details>
<summary> Using Recursion </summary>
  
```python
def factorial_recursion(n):
  if (n==0 or n==1):
    return 1

  return n * factorial_recursion(n-1)
```

</details>

<details>
<summary> Using Iteration </summary>
  
```python
def factorial_iteration(n):
  result = 1;
  for i in range(n, 1, -1):
    result = i*result

  return result
```

</details>

<details>
<summary> Using Dynamic Programming (List) </summary>
  
```python
def factorial_dynamic_programming(n):
  factorial_list = [-1] * (n+1)
  factorial_list[0] = 1

  for i in range(1, n+1, 1):
    factorial_list[i] = factorial_list[i-1] * i

  return factorial_list[n]
```

</details>

<b> 2. Revisiting Planetary Weight </b>
- Becoming familiar with JSON file format
- Storing, hashing, and accessing dictionary value elements using its key
- List of dictionary vs Dictionary

<details>
<summary> Using <b>Conditionals</b> (planet_conditional.py) </summary>

```python
MERCURY_GRAVITY = (37.6 / 100)
VENUS_GRAVITY = (88.9 / 100)
MARS_GRAVITY = (37.8 / 100)
JUPITER_GRAVITY = (236 / 100)
SATURN_GRAVITY = (108.1 / 100)
URANUS_GRAVITY = (81.5 / 100)
NEPTUNE_GRAVITY = (114 / 100)    

def calculate_weight(planetName, earthWeight):
  
  match planetName:
    case "Mercury":
        planetWeight = earthWeight * MERCURY_GRAVITY
  
    case "Venus":
        planetWeight = earthWeight * VENUS_GRAVITY
  
    case "Mars":
        planetWeight = earthWeight * MARS_GRAVITY
  
    case "Jupiter":
        planetWeight = earthWeight * JUPITER_GRAVITY
      
    case "Saturn":
        planetWeight = earthWeight * SATURN_GRAVITY
  
    case "Uranus":
        planetWeight = earthWeight * URANUS_GRAVITY
  
    case "Neptune":
        planetWeight = earthWeight * NEPTUNE_GRAVITY
  
    case "Earth":
        planetWeight = earthWeight

    case other:
        planetWeight = -1.0 # Why put a negative value here?

return planetWeight
  
def main():
  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  planetWeight = calculate_weight(planetName, earthWeight)
  
  print("The name of the planet: " + planetName + " with weight: " + str(planetWeight))

```

</details>

<details>
  
<summary> Using <b>List of Dictionary</b> (planet_dictionary.py) </summary>
  
```python
planet_dict = [
  {"mercury": 0.376}, 
  {"venus": 0.889},
  {"earth": 1.0},  
  {"mars": 0.378},
  {"jupiter": 2.36}, 
  {"saturn": 1.081}, 
  {"uranus": 0.815}, 
  {"neptune": 1.14}
]

def calculate_weight(target_planet, earth_weight):
    # TODO: Check the earth weight, make sure >= 0 and numbers only
    # TODO: Check that the target planet name is listed in the dictionary, otherwise return an error

    planet_name = target_planet.lower()
    planet_constant = -1.0
    for i in range( len(planet_dict) ):
        for name, gravity in planet_dict[i].items():
            if (planet_name == name):
                planet_constant = gravity

    planet_weight = planet_constant * earth_weight

    return planet_weight

def main():
  earth_weight = float(input("Enter the object weight: "))
  planet_name = input("Enter a planet name: ")
  
  planet_weight = calculate_weight(planet_name, earth_weight)

  print("The name of the planet: " + planet_name + " with weight: " + str(planet_weight))

```

</details>

<details>
  
<summary> Using <b>Dictionary</b> (planet_dictionary.py) </summary>
  
```python
planet_dict = {
  "mercury": 0.376, 
  "venus": 0.889,
  "earth": 1.0,  
  "mars": 0.378,
  "jupiter": 2.36, 
  "saturn": 1.081, 
  "uranus": 0.815, 
  "neptune": 1.14
  }

def calculate_weight_alternative(target_planet, earth_weight):
    planet_name = target_planet.lower()
    planet_constant = -1.0

    if planet_dict[ planet_name ] is not None:
        planet_constant = planet_dict[planet_name]
    
    planet_weight = planet_constant * earth_weight

    return planet_weight

def main():
  earth_weight = float(input("Enter the object weight: "))
  planet_name = input("Enter a planet name: ")
  
  planet_weight = calculate_weight_alternative(planet_name, earth_weight)

  print("The name of the planet: " + planet_name + " with weight: " + str(planet_weight))

```

</details>

<b> 3. Plotting Regression Line </b>
<details>
  
<summary> Using <b>List of Dictionary</b> (snow_plot.py) </summary>
  
```python
from matplotlib import pyplot as plt

snow_yield_dictionary =
[{"Snow": 
[23.1, 32.8, 31.8, 32.0, 30.4, 24.0, 39.5, 24.2, 52.5, 37.9, 30.5, 25.1, 12.4, 35.1, 31.5, 21.1, 27.6]
},
{"Yield": 
[10.5, 16.7, 18.2, 17.0, 16.3, 10.5, 23.1, 12.4, 24.9, 22.8, 14.1, 12.9, 8.8, 17.4, 14.9, 10.5, 16.1]
}]

def plot_the_curve():
    snow_dictionary = snow_yield_dictionary[0]
    yield_dictionary = snow_yield_dictionary[1]

    snow_list = snow_dictionary["Snow"]
    yield_list = yield_dictionary["Yield"]

    plt.title("Plot of Snow vs Yield"); plt.xlabel("Snow"); plt.ylabel("Yield")
    plt.scatter(snow_list, yield_list, c='blue', marker='H')
    plt.show()
    plt.savefig('plot_of_snow_vs_yield.png')

def main():
    plot_the_curve()

```

</details>
