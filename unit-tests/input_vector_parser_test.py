import unittest

import input_vector_parser as InputVectorParserClass

class InputVectorParserTest(unittest.TestCase):
    def test_read_data_0(self):
        path = 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests'
        filename = 'test_data_1'
        input_vector_parser = InputVectorParserClass.InputVectorParser(path, filename)

        self.assertEqual(input_vector_parser.path, 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests')
        self.assertEqual(input_vector_parser.name, 'test_data_1')
        self.assertEqual(input_vector_parser.input_vectors_list, [])

        input_vector_parser.read()

        self.assertEqual(len(input_vector_parser.input_vectors_list), 4)

        self.assertEqual(input_vector_parser.input_vectors_list[0].obj_name, 'o1')
        self.assertEqual(input_vector_parser.input_vectors_list[0].traits_list, [1, 1, 1])

        self.assertEqual(input_vector_parser.input_vectors_list[2].obj_name, 'o3')
        self.assertEqual(input_vector_parser.input_vectors_list[2].traits_list, [0, 1, 0])

    def test_return_data_0(self):
        path = 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests'
        filename = 'test_data_2'
        input_vector_parser = InputVectorParserClass.InputVectorParser(path, filename)

        self.assertEqual(input_vector_parser.path, 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests')
        self.assertEqual(input_vector_parser.name, 'test_data_2')
        self.assertEqual(input_vector_parser.input_vectors_list, [])

        input_vector_parser.read()

        self.assertEqual(len(input_vector_parser.input_vectors_list), 3)

        self.assertEqual(input_vector_parser.input_vectors_list[0].obj_name, 'o2')
        self.assertEqual(input_vector_parser.input_vectors_list[0].traits_list, [0, 0, 0])

        self.assertEqual(input_vector_parser.input_vectors_list[2].obj_name, 'o4')
        self.assertEqual(input_vector_parser.input_vectors_list[2].traits_list, [0, 2, 0])

        returned_value = input_vector_parser.return_vec_list()

        self.assertEqual(len(returned_value), 3)
        self.assertEqual(returned_value[0].obj_name, 'o2')
        self.assertEqual(returned_value[0].traits_list, [0, 0, 0])

        self.assertEqual(returned_value[1].obj_name, 'o3')
        self.assertEqual(returned_value[1].traits_list, [2, 1, 1])