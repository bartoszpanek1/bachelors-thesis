class Holon:
    def __init__(self, obj_name, trait_1, trait_2, semantic_memory):
        self.obj_name = obj_name
        self.trait_1_name = trait_1
        self.trait_2_name = trait_2
        self.tt = 0.0
        self.tf = 0.0
        self.ft = 0.0
        self.ff = 0.0
        self.semantic_memory = semantic_memory
        self.last_vector = semantic_memory.obj_traits[self.obj_name][-1]

    def update(self):
        obj_memories = self.semantic_memory.obj_traits[self.obj_name]
        trait_names = self.semantic_memory.trait_names
        trait_1_idx = trait_names.index(self.trait_1_name)
        trait_2_idx = trait_names.index(self.trait_2_name)

        true_true = 0
        true_false = 0
        false_true = 0
        false_false = 0
        for trait_vector in obj_memories:
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
        self.tt = true_true / sum
        self.tf = true_false / sum
        self.ft = false_true / sum
        self.ff = false_false / sum