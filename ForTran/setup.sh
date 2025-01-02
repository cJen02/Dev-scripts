# Ref:- https://laptops.eng.uci.edu/engineering-software/programming-basics/gfortran-hello-world
sudo apt-get install gfortran  # Linux
which gfortran
which pico


## "Hello World" Program
pico helloworld.f90
"""
program helloworld
      print *, "Hello World"
end program helloworld
"""
gfortran helloworld.f90 -o hello
