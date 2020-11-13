import json
from response_thresholds import ResponseThresholds
from holon import Holon


class SemanticMemory:
    def __init__(self, object_names, trait_names):
        self.object_names = object_names
        self.trait_names = trait_names
        self.obj_traits = {}
        for name in object_names:
            self.obj_traits[name] = []
        self.last_data_input = []
        self.user_requests = []
        self.response_thresholds = ResponseThresholds()
        self.holons = []

    def update_from_list(self, input_vector_list):
        self.last_data_input = input_vector_list
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
        with open(path + "\\" + name, "w") as fp:
            json.dump(dict_to_save, fp)

    def load_from_file(self, path, name):
        data = None
        with open(path + "\\" + name, "r") as fp:
            data = json.load(fp)
        self.object_names = data["object_names"]
        self.trait_names = data["trait_names"]
        self.obj_traits = data["obj_traits"]
        self.user_requests = data["user_requests"]

    def save_user_request(self, obj_name, trait_1, trait_2):
        self.user_requests.append([obj_name, trait_1, trait_2])

    def handle_user_request(self, obj_name, trait_1, trait_2):
        def search_for_direct_observation():
            for vector in self.last_data_input:
                if vector.obj_name == obj_name:
                    return vector
            return None

        def search_for_holon(memory):
            for existing_holon in memory.holons:
                if existing_holon.obj_name == obj_name and \
                        ((existing_holon.trait_1_name == trait_1 and existing_holon.trait_2_name == trait_2) or
                         (existing_holon.trait_1_name == trait_2 and existing_holon.trait_2_name == trait_1)):
                    return existing_holon
            return None

        def print_response(holon, trait_names, holons):
            def print_for_holon(holon):
                if holon.tt == 1 and holon.analyzed_all_data:
                    print_for_state_of_holon('tt', holon.tt, holon.analyzed_all_data)
                elif holon.tf == 1 and holon.analyzed_all_data:
                    print_for_state_of_holon('tf', holon.tf, holon.analyzed_all_data)
                elif holon.ft == 1 and holon.analyzed_all_data:
                    print_for_state_of_holon('ft', holon.ft, holon.analyzed_all_data)
                elif holon.ff == 1 and holon.analyzed_all_data:
                    print_for_state_of_holon('ff', holon.ff, holon.analyzed_all_data)
                else:
                    print_for_state_of_holon('tt', holon.tt)
                    print_for_state_of_holon('tf', holon.tf)
                    print_for_state_of_holon('ft', holon.ft)
                    print_for_state_of_holon('ff', holon.ff)

            def print_for_state_of_holon(state, probability, all_data_taken=False):
                if state == 'tt':
                    print(
                        f'{self.response_thresholds.get_response(probability, all_data_taken)}({trait_names[trait_1_idx]} <==> {trait_names[trait_2_idx]})')
                elif state == 'tf':
                    print(
                        f'{self.response_thresholds.get_response(probability, all_data_taken)}({trait_names[trait_1_idx]} <==> ¬{trait_names[trait_2_idx]})')
                elif state == 'ft':
                    print(
                        f'{self.response_thresholds.get_response(probability, all_data_taken)}(¬{trait_names[trait_1_idx]} <==> {trait_names[trait_2_idx]})')
                else:
                    print(
                        f'{self.response_thresholds.get_response(probability, all_data_taken)}(¬{trait_names[trait_1_idx]} <==> ¬{trait_names[trait_2_idx]})')

            if holon is None:
                holon = Holon(obj_name, trait_1, trait_2, self)
                holon.update()
                holons.append(holon)
                print_for_holon(holon)

            else:
                holon.update()
                print_for_holon(holon)

        trait_1_idx = self.trait_names.index(trait_1)
        trait_2_idx = self.trait_names.index(trait_2)
        direct_observation = search_for_direct_observation()
        if direct_observation is not None:

            trait_1_value = direct_observation.list[trait_1_idx]
            trait_2_value = direct_observation.list[trait_2_idx]

            if trait_1_value == 1 and trait_2_value == 1:
                print(f'Know({self.trait_names[trait_1_idx]} <==> {self.trait_names[trait_2_idx]})')
            elif trait_1_value == 1 and trait_2_value == 0:
                print(f'Know({self.trait_names[trait_1_idx]} <==> ¬{self.trait_names[trait_2_idx]})')
            elif trait_1_value == 0 and trait_2_value == 1:
                print(f'Know(¬{self.trait_names[trait_1_idx]} <==> {self.trait_names[trait_2_idx]})')
            elif trait_1_value == 0 and trait_2_value == 0:
                print(f'Know(¬{self.trait_names[trait_1_idx]} <==> ¬{self.trait_names[trait_2_idx]})')
            else:
                holon = search_for_holon(self)
                print_response(holon, self.trait_names)
        else:
            holon = search_for_holon(self)
            print_response(holon, self.trait_names, self.holons)
