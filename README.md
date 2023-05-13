# Code in Place Spring 2023 - Stanford University

Extra suplemental materials dedicated to Code in Place Spring 2023 with Stanford University

Topics to be covered:

## Input Arguments (Week 2: May 05, 2023) ##
<details>
<summary> User Input Prompt: remember all data types are still in string </summary>

```python
def main():
  user_name = input("Enter your name: ")
  print("Good morning " + user_name)
```
</details>  

## Console Programming (Week 3: May 12, 2023) ##

### Conditional Branching ###
<details>
<summary> 1. <b>IF-ELIF-ELSE</b> Statement </summary>

```python
def main():
  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  
  if (planetName == "Mercury"):
    planetWeight = float(earthWeight) * (37.6 / 100)
        
  elif (planetName == "Venus"):
    planetWeight = float(earthWeight) * (88.9 / 100)
        
  elif (planetName == "Mars"):
    planetWeight = float(earthWeight) * (37.8 / 100)    

  elif (planetName == "Jupiter"):
    planetWeight = float(earthWeight) * (236 / 100)
        
  elif (planetName == "Saturn"):
    planetWeight = float(earthWeight) * (108.1 / 100)

  elif (planetName == "Uranus"):
    planetWeight = float(earthWeight) * (81.5 / 100)
        
  elif (planetName == "Neptune"):
    planetWeight = float(earthWeight) * (114 / 100)    
    
  else:
    planetWeight = 0
```
</details>

<details>
<summary> 2. <b>MATCH-CASE</b> Statement (Require Python 3.10 or above) </summary>

```python
def main():
  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  
  match planetName:
    case "Mercury":
      planetWeight = float(earthWeight) * (37.6 / 100)
  
    case "Venus":
      planetWeight = float(earthWeight) * (88.9 / 100)
  
    case "Mars":
      planetWeight = float(earthWeight) * (37.8 / 100)
  
    case "Jupiter":
      planetWeight = float(earthWeight) * (236 / 100)
      
    case "Saturn":
      planetWeight = float(earthWeight) * (108.1 / 100)
  
    case "Uranus":
      planetWeight = float(earthWeight) * (81.5 / 100)
  
    case "Neptune":
      planetWeight = float(earthWeight) * (114 / 100)
  
    case other:
      planetWeight = 0.0
```
</details>

### Printing in Python ###
<b> 1. String Concatenation </b>
- Notice that both "+" and "," can be used interchangably
- Concatenate multiple strings with + (plus) or , (comma)
- All concatenated items have to be converted to the same data type (string)
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on " + planetName + ": " + str(marsWeight))
print("The weight on " , planetName + ": " , str(marsWeight))
```

<b> 2. Reference </b>
- Notice the ```.format(,)``` patten
- Unlike concatenation method, this method requires no string conversion
- Use the {} (curly brackets) to place your variable
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on {}: {}".format(planetName, planetWeight))
```
<b> 3. F-word </b>
- Notice the f letter inside print()
- Similar to method 2 (reference), but now variable name is placed inside the curly brackets 
- Likewise, no variable casting (conversion) is needed
```python
planetName = "Mars"; planetWeight = 175.26
print(f"The weight on {planetName}: {planetWeight}")
```

## Graphics (Week 4: May 19, 2023) ##

### Functions with Parameters ###
<details>
<summary> 1. <b>Single</b> Output Return </summary>

```python
def single_output_function(input_1, input_2, input_3):
  output = input_1 * input_2 * input_3
  return output
```
</details>

<details>
<summary> 2. <b>Multiple</b> Outputs Return </summary>

```python
def multi_output_function(input_1, input_2):
  # Begin by declaring def, brackets, and colon sign (:)
  output_1 = input_1 + input_2
  output_2 = input_1 * input_2
      
  # The correct word is return, NOT result
  return output_1, output_2
```
</details>

## Animation (Week 5: May 26, 2023) ##

  - Coming Soon

## Data Structures: Containers (Week 6: June 02, 2023) ##

  - Coming Soon
