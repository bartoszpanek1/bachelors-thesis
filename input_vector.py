class InputVector:
    def __init__(self, obj_name, size, traits_list):
        assert (size == len(traits_list))
        self.obj_name = obj_name
        self.traits_list = traits_list
