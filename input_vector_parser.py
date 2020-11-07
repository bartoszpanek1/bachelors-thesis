from input_vector import InputVector

class InputVectorParser:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.is_running = False
        self.input_vectors_list = []

    def read(self):
        full_path = self.path + '/' + self.name
        file = open(full_path)

        obj_list = file.readline().rstrip('\n').split(" ")
        traits_list = file.readline().rstrip('\n').split(" ")

        print("Object list ", obj_list)
        print("Traits names", traits_list)

        for i, line in enumerate(file):
            vector = line.split(" ")
            obj = vector.pop(0)

            assert (obj in obj_list)
            assert (len(traits_list) == len(vector))

            traits = list(map(int, vector))
            input_vec = InputVector(obj, len(traits_list), traits, i)
            self.input_vectors_list.append(input_vec)

    def return_vec_list(self):
        return self.input_vectors_list