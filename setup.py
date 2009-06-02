"""

author: Christopher O'Brien  <obriencj@gmail.com>

"""


from distutils.core import setup


setup( name = "javaclass",
       version = "1.0",
       package_dir = {"javaclass": "src"},
       packages = ["javaclass"],
       scripts = ["scripts/classdiff",
                  "scripts/classinfo",
                  "scripts/jardiff",
                  "scripts/jarinfo"])


#
# The end.