import pandas as pd
 

my_dataset = {
    "cars" : ["BMW", "Volvo", "Ford"],
    "passing" : [3,7,2]
}

myvar = pd.DataFrame(my_dataset)

print(myvar)
print(pd.__version__)