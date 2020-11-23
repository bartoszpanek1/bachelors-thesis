import random as rnd
import math as math
import json


class Holon:
    def __init__(self, obj_name, trait_1_name, trait_2_name, analyzed_vectors=None, analyzed_all_data=False,
                 tt=0.0, tf=0.0, ft=0.0, ff=0.0, knowledge_database=None):
        if analyzed_vectors is None:
            analyzed_vectors = []
        self.obj_name = obj_name
        self.trait_1_name = trait_1_name
        self.trait_2_name = trait_2_name
        self.knowledge_database = knowledge_database
        self.analyzed_vectors = analyzed_vectors
        self.analyzed_all_data = analyzed_all_data
        self.tt = tt
        self.tf = tf
        self.ft = ft
        self.ff = ff

    def take_part_of_data(self, percentage_of_data):
        obj_memories = self.knowledge_database.obj_traits[self.obj_name]
        data_vectors_to_take = math.ceil(len(obj_memories) * percentage_of_data)

        vectors_taken = 0
        while vectors_taken < data_vectors_to_take:
            rnd.shuffle(obj_memories)
            selected_vector = obj_memories.pop()
            self.analyzed_vectors.append(selected_vector)
            vectors_taken += 1

        if len(obj_memories) == 0:
            self.analyzed_all_data = True
        else:
            self.analyzed_all_data = False

    def update(self):
        self.take_part_of_data(0.25)
        trait_names = self.knowledge_database.trait_names
        trait_1_idx = trait_names.index(self.trait_1_name)
        trait_2_idx = trait_names.index(self.trait_2_name)

        true_true = 0
        true_false = 0
        false_true = 0
        false_false = 0
        for trait_vector in self.analyzed_vectors:
            trait_1 = trait_vector[trait_1_idx]
            trait_2 = trait_vector[trait_2_idx]

            if trait_1 == 1 and trait_2 == 1:
                true_true += 1
            elif trait_1 == 1 and trait_2 == 0:
                true_false += 1
            elif trait_1 == 0 and trait_2 == 1:
                false_true += 1
            elif trait_1 == 0 and trait_2 == 0:
                false_false += 1

        sum = true_true + true_false + false_true + false_false
        if sum == 0:
            sum = 1
        self.tt = true_true / sum
        self.tf = true_false / sum
        self.ft = false_true / sum
        self.ff = false_false / sum

    def toJSON(self):
        self.knowledge_database = None
        return self.__dict__
