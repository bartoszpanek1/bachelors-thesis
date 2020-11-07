import json
class SemanticMemory:
    def __init__(self, object_names, trait_names):
        self.object_names = object_names
        self.trait_names = trait_names
        self.obj_traits = {}
        for name in object_names:
            self.obj_traits[name] = []
        self.user_requests = []

    def update_from_list(self, input_vector_list):
        for input_vector in input_vector_list:
            self.expand(input_vector.obj_name)
            self.update(input_vector)

    def update(self, input_vector):
        self.obj_traits[input_vector.obj_name].append(input_vector.list)

    def expand(self, new_object_name):
        if new_object_name not in self.object_names:
            self.object_names.append(new_object_name)
            self.obj_traits[new_object_name] = []

    def save_to_file(self, path, name):
        dict_to_save = {}
        dict_to_save["obj_traits"] = dict(self.obj_traits)
        dict_to_save["object_names"] = self.object_names
        dict_to_save["trait_names"] = self.trait_names
        dict_to_save["user_requests"] = self.user_requests
        with open(path + "/" + name, "w") as fp:
            json.dump(dict_to_save, fp)

    def load_from_file(self, path, name):
        data = None
        with open(path + "/" + name, "r") as fp:
            data = json.load(fp)
        self.object_names = data["object_names"]
        self.trait_names = data["trait_names"]
        self.obj_traits = data["obj_traits"]
        self.user_requests = data["user_requests"]

    def save_user_request(self, obj_name, trait_1, trait_2):
        self.user_requests.append([obj_name, trait_1, trait_2])
