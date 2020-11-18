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
        self.holons = []
        self.response_thresholds = ResponseThresholds(0, 0.66, 0.66, 1, 1, 1)

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
        dict_to_save['obj_traits'] = dict(self.obj_traits)
        dict_to_save['object_names'] = self.object_names
        dict_to_save['trait_names'] = self.trait_names
        dict_holons = []
        for holon in self.holons:
            dict_holons.append(holon.toJSON())
        dict_to_save['holons'] = dict_holons
        dict_to_save['response_thresholds'] = self.response_thresholds.__dict__
        with open(path + '\\' + name, 'w') as fp:
            json.dump(dict_to_save, fp)

    def load_from_file(self, path, name):
        data = None
        with open(path + '\\' + name, 'r') as fp:
            data = json.load(fp)
        self.object_names = data['object_names']
        self.trait_names = data['trait_names']
        self.obj_traits = data['obj_traits']
        holons = []
        for dict_holon in data['holons']:
            holon = Holon(**dict_holon)
            holon.semantic_memory = self
            holons.append(holon)

        self.holons = holons
        self.response_thresholds = ResponseThresholds(**data['response_thresholds'])

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
                if holon.tf != 0 or holon.ft != 0:
                    print_for_state_of_holon('tfft')
                else:
                    print_for_state_of_holon('ttff', holon.tt, holon.analyzed_all_data)

            def print_for_state_of_holon(state, probability=0.0, all_data_taken=False):
                if state == 'ttff':
                    print(
                        f'{self.response_thresholds.get_response(probability, all_data_taken)}({trait_names[trait_1_idx]} <==> {trait_names[trait_2_idx]})({holon.obj_name})')
                elif state == 'tfft':
                    print(
                        f'Know(¬({self.trait_names[trait_1_idx]} <==> {self.trait_names[trait_2_idx]})({holon.obj_name})')

            holon.update()
            print_for_holon(holon)

        holon = search_for_holon(self)

        trait_1_idx = self.trait_names.index(trait_1)
        trait_2_idx = self.trait_names.index(trait_2)

        if holon is None:
            holon = Holon(obj_name, trait_1, trait_2, semantic_memory=self)
            self.holons.append(holon)
            print(self.holons)

        if holon.tf != 0 or holon.ft != 0:
            print(f'Know(¬({self.trait_names[trait_1_idx]} <==> {self.trait_names[trait_2_idx]})({obj_name})')
        else:
            direct_observation = search_for_direct_observation()

            if direct_observation is not None:
                trait_1_value = direct_observation.list[trait_1_idx]
                trait_2_value = direct_observation.list[trait_2_idx]
                if (trait_1_value == 1 and trait_2_value == 0) or \
                        (trait_1_value == 0 and trait_2_value == 1):
                    print(
                        f'Know(¬({self.trait_names[trait_1_idx]} <==> {self.trait_names[trait_2_idx]})({obj_name})')
                else:
                    print_response(holon, self.trait_names, self.holons)
            else:
                print_response(holon, self.trait_names, self.holons)
