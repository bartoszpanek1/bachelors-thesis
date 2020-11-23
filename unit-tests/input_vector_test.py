import unittest

import input_vector as InputVectorClass


class InputVectorTest(unittest.TestCase):
    def test_create_input_vector_0(self):
        obj_name = 'o1'
        size = 3
        list = ['O', 'P', 'Q']
        input_vector = InputVectorClass.InputVector(obj_name, size, list)

        self.assertEqual(input_vector.obj_name, 'o1')
        self.assertEqual(len(input_vector.traits_list), 3)
        self.assertEqual(input_vector.traits_list, ['O', 'P', 'Q'])

    def test_create_input_vector_1(self):
        obj_name = 'Object 1'
        size = 4
        list = ['Name', 'Size', 'Color', 'Age']
        input_vector = InputVectorClass.InputVector(obj_name, size, list)

        self.assertEqual(input_vector.obj_name, 'Object 1')
        self.assertEqual(len(input_vector.traits_list), 4)
        self.assertEqual(input_vector.traits_list, ['Name', 'Size', 'Color', 'Age'])

    def test_create_input_vector_2(self):
        obj_name = 'Object 1'
        size = 3
        list = ['Name', 'Size', 'Color', 'Age']
        self.assertRaises(AssertionError, lambda: InputVectorClass.InputVector(obj_name, size, list))
