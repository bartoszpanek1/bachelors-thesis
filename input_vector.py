class InputVector:
    def __init__(self, obj_name, size, list, line_num):
        assert (size == len(list))
        self.obj_name = obj_name
        self.list = list
        self.line_num = line_num