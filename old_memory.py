class OldMemory:
    def __init__(self, object_names, trait_names):
        self.object_names = object_names
        self.trait_names = trait_names
        self.obj_traits = {}
        for name in object_names:
            self.obj_traits[name] = [0 for i in range(0, len(trait_names) * 3)]

    def update(self, input_vector):
        obj_name = input_vector.obj_name
        zero_indicator = 1
        one_indicator = 0
        two_indicator = 2
        for i in range(len(input_vector.list)):
            val = input_vector.list[i]
            if val == 0:
                self.obj_traits[obj_name][zero_indicator] += 1
            elif val == 1:
                self.obj_traits[obj_name][one_indicator] += 1
            else:
                self.obj_traits[obj_name][two_indicator] += 1
            zero_indicator += 3
            one_indicator += 3
            two_indicator += 3

    def expand(self, new_object_name):
        if new_object_name not in self.object_names:
            self.object_names.append(new_object_name)
            self.obj_traits[new_object_name] = [0 for i in range(0, len(self.trait_names) * 3)]

    def save_to_file(self, path, name):
        f = open(path + "/" + name, "w+")

        for obj_name in self.object_names:
            f.write(obj_name + " ")
        f.write("\n")

        for trait in self.trait_names:
            f.write(trait + " ")
        f.write("\n")

        for obj_name, traits in self.obj_traits.items():
            f.write(obj_name + " ")
            for trait in traits:
                f.write(str(trait) + " ")
            f.write("\n")

    def load_from_file(self, path, name):
        f = open(path + "/" + name, "r+")
        self.object_names = f.readline().rstrip('\n').split(" ")
        self.trait_names = f.readline().rstrip('\n').split(" ")

        new_obj_traits = {}
        for line in f:
            vector = line.split(" ")
            obj = vector.pop(0)
            traits = list(map(int, vector))
            new_obj_traits[obj] = traits

        self.obj_traits = new_obj_traits