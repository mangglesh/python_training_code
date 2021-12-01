#A package contains a group of usually related code files (modules)
import package_training
print(package_training.version)
# The package_training/__init__.py file assigns 1.03 to the variable version. version is in
# the scope of the pachage_training package namespace

#print(package_training.package_training_level_2.c1)
# loading the top-level module of a package isn’t enough to load all the
# submodules

import  package_training.package_training_level_2.c1
package_training.package_training_level_2.c1.func()

#other package in the path are also imported 
package_training.package_training_level_2



# Relative imports can be handy and quick to type, but be aware that they’re relative to
# the module’s __name__property
import package_training
package_training.__name__
import package_training.package_training_level_2
package_training.package_training_level_2.__name__


# option 1 -----> going below the folder structure use package and module name
# look a2 for example
# option 2 -----> going above the current diretory use ..... one dot for each level 
# look c2 for example
# option 3 -----> using relative path from parent package in this case its packageleve1
# look c1 for example


#__init__ file should always be their for python te recognise folder as package



##################### __all__ ###########################33
# This has to do with execution of
# statements of the form from ... import * it tell what * should import 

import package_training
package_training_level_2.c1.c1_var  # wont work
# in the above example it tells us that we cant access packages just by using import alone (beacuse its a package :D)

# makes my code simple
from package_training import *
a = 78
package_training_level_2.c2.c2_var #will work
print(package_training.a1.a)
#uncomment __all__ in package_training.__init__.py




