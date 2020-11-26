import numpy as np

class UnitCell2D:
    def __init__(self, lattice_vectors, verbose=False):
        self.lattice_vectors = lattice_vectors
        self.verbose = verbose

        self.reciprocal_lattice_vectors = self.__get_reciprocal_lattice_vectors()

    def __get_reciprocal_lattice_vectors(self):
        if self.verbose:
            print("Starting to calculate the reciprocal lattice vectors...", end="")

        # TODO 

        if self.verbose:
            print("Done!")

    def get_high_symmetry_points(self):
        


class UnitCell3D:
    def __init__(self, lattice_vectors, verbose=False):
        self.lattice_vectors = lattice_vectors
        self.verbose = verbose

        self.reciprocal_lattice_vectors = self.__get_reciprocal_lattice_vectors()

    def __get_reciprocal_lattice_vectors(self):
        if self.verbose:
            print("Starting to calculate the reciprocal lattice vectors...", end="")

        # TODO 

        if self.verbose:
            print("Done!")

