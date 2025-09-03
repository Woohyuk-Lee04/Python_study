import converters
from converters import kg_to_lbs

from utils import find_max

from package import packages
from package.packages import shipping

print(kg_to_lbs(100))

print(converters.kg_to_lbs(70))
print(converters.lbs_to_kg(200))

numbers = [2,6,10,5,3,7,2,1]
print(find_max(numbers))
print(max(numbers))


packages.shipping()
shipping()