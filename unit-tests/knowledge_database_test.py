import io
import os
import sys
import unittest

import knowledge_database as KnowledgeDatabaseClass
import input_vector as InputVectorClass


class KnowledgeDatabaseTest(unittest.TestCase):
    def test_knowledge_database_creation_0(self):
        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.object_names, ['o1', 'o2', 'o3', 'o4'])
        self.assertEqual(knowledge_database.trait_names, ['O', 'P', 'Q', 'R'])

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})
        self.assertEqual(knowledge_database.last_data_input, [])
        self.assertEqual(knowledge_database.holons, [])
        self.assertEqual(knowledge_database.response_thresholds.min_pos, 0)
        self.assertEqual(knowledge_database.response_thresholds.max_pos, 0.66)
        self.assertEqual(knowledge_database.response_thresholds.min_bel, 0.66)
        self.assertEqual(knowledge_database.response_thresholds.max_bel, 1)
        self.assertEqual(knowledge_database.response_thresholds.min_know, 1)
        self.assertEqual(knowledge_database.response_thresholds.max_know, 1)

    def test_expand_object_list_0(self):
        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        knowledge_database.expand('o5')

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': [],
                                                         'o5': []})

    def test_expand_object_list_1(self):
        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        knowledge_database.expand('o5')
        knowledge_database.expand('o5')
        knowledge_database.expand('o5')
        knowledge_database.expand('o6')

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': [],
                                                         'o5': [],
                                                         'o6': []})

    def test_update_object_traits_list_0(self):
        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        input_vector = InputVectorClass.InputVector('o1', 4, [1, 2, 1, 1])
        knowledge_database.update(input_vector)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1]],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        input_vector = InputVectorClass.InputVector('o3', 4, [2, 2, 2, 1])
        knowledge_database.update(input_vector)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1]],
                                                         'o2': [],
                                                         'o3': [[2, 2, 2, 1]],
                                                         'o4': []})

        input_vector = InputVectorClass.InputVector('o2', 4, [0, 0, 1, 0])
        knowledge_database.update(input_vector)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [[2, 2, 2, 1]],
                                                         'o4': []})

        input_vector = InputVectorClass.InputVector('o1', 4, [0, 0, 1, 0])
        knowledge_database.update(input_vector)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1], [0, 0, 1, 0]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [[2, 2, 2, 1]],
                                                         'o4': []})

    def test_update_from_list_0(self):
        input_vector_list = [InputVectorClass.InputVector('o1', 4, [1, 2, 1, 1]),
                             InputVectorClass.InputVector('o2', 4, [0, 0, 1, 0]),
                             InputVectorClass.InputVector('o1', 4, [0, 0, 1, 0])]

        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        knowledge_database.update_from_list(input_vector_list)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1], [0, 0, 1, 0]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [],
                                                         'o4': []})

    def test_save_to_file_0(self):
        input_vector_list = [InputVectorClass.InputVector('o1', 4, [1, 2, 1, 1]),
                             InputVectorClass.InputVector('o2', 4, [0, 0, 1, 0]),
                             InputVectorClass.InputVector('o1', 4, [0, 0, 1, 0])]

        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        knowledge_database.update_from_list(input_vector_list)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1], [0, 0, 1, 0]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [],
                                                         'o4': []})

        path = 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests'
        filename = 'test_memory_file'
        knowledge_database.save_to_file(path, filename)

        self.assertTrue(os.path.exists('D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests\\test_memory_file'))

    def test_load_from_file_0(self):
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase([], trait_names)

        self.assertEqual(knowledge_database.object_names, [])
        self.assertEqual(knowledge_database.trait_names, ['O', 'P', 'Q', 'R'])

        self.assertEqual(knowledge_database.obj_traits, {})
        self.assertEqual(knowledge_database.last_data_input, [])
        self.assertEqual(knowledge_database.holons, [])
        self.assertEqual(knowledge_database.response_thresholds.min_pos, 0)
        self.assertEqual(knowledge_database.response_thresholds.max_pos, 0.66)
        self.assertEqual(knowledge_database.response_thresholds.min_bel, 0.66)
        self.assertEqual(knowledge_database.response_thresholds.max_bel, 1)
        self.assertEqual(knowledge_database.response_thresholds.min_know, 1)
        self.assertEqual(knowledge_database.response_thresholds.max_know, 1)

        path = 'D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests'
        filename = 'test_memory_file'

        self.assertTrue(os.path.exists('D:\\PyCharm\\PyCharm Projects\\bachelors-thesis\\unit-tests\\test_memory_file'))

        knowledge_database.load_from_file(path, filename)

        self.assertEqual(knowledge_database.object_names, ['o1', 'o2', 'o3', 'o4'])
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1], [0, 0, 1, 0]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [],
                                                         'o4': []})

    def test_handle_user_request(self):
        input_vector_list = [InputVectorClass.InputVector('o1', 4, [1, 2, 1, 1]),
                             InputVectorClass.InputVector('o2', 4, [0, 0, 1, 0]),
                             InputVectorClass.InputVector('o1', 4, [0, 0, 1, 0]),
                             InputVectorClass.InputVector('o4', 4, [1, 1, 2, 1])]

        object_names = ['o1', 'o2', 'o3', 'o4']
        trait_names = ['O', 'P', 'Q', 'R']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)

        self.assertEqual(knowledge_database.obj_traits, {'o1': [],
                                                         'o2': [],
                                                         'o3': [],
                                                         'o4': []})

        knowledge_database.update_from_list(input_vector_list)
        self.assertEqual(knowledge_database.obj_traits, {'o1': [[1, 2, 1, 1], [0, 0, 1, 0]],
                                                         'o2': [[0, 0, 1, 0]],
                                                         'o3': [],
                                                         'o4': [[1, 1, 2, 1]]})

        self.assertEqual(knowledge_database.holons, [])

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        request = ['o1', 'O', 'R']
        knowledge_database.handle_user_request(request[0], request[1], request[2])

        self.assertNotEqual(knowledge_database.holons, [])
        self.assertEqual(len(knowledge_database.holons), 1)
        self.assertTrue((capturedOutput.getvalue() == 'Pos(O <==> R)(o1)\n') or (
                    capturedOutput.getvalue() == 'Bel(O <==> R)(o1)\n'))
        sys.stdout = sys.__stdout__

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        request = ['o2', 'O', 'Q']
        knowledge_database.handle_user_request(request[0], request[1], request[2])

        self.assertNotEqual(knowledge_database.holons, [])
        self.assertEqual(len(knowledge_database.holons), 2)
        self.assertEqual(capturedOutput.getvalue(), 'Know(¬(O <==> Q)(o2))\n')

        sys.stdout = sys.__stdout__

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        request = ['o4', 'O', 'P']
        knowledge_database.handle_user_request(request[0], request[1], request[2])

        self.assertNotEqual(knowledge_database.holons, [])
        self.assertEqual(len(knowledge_database.holons), 3)
        self.assertEqual(capturedOutput.getvalue(), 'Know(O <==> P)(o4)\n')

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput