import unittest

import knowledge_database as KnowledgeDatabaseClass
import holon as HolonClass

class HolonTest(unittest.TestCase):
    def test_holon_take_part_of_data_0(self):
        trait_names = ['O', 'P', 'Q', 'R']
        object_names = ['o1']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)
        knowledge_database.obj_traits = {'o1': [[0, 0, 1, 1], [1, 1, 1, 1], [2, 1, 1, 2]]}
        
        holon_test = HolonClass.Holon('o1', 'P', 'Q', knowledge_database=knowledge_database)
        self.assertEqual(holon_test.analyzed_vectors, [])
        self.assertEqual(holon_test.analyzed_all_data, False)

        holon_test.take_part_of_data(0.25)
        self.assertEqual(len(holon_test.analyzed_vectors), 1)
        self.assertEqual(holon_test.analyzed_all_data, False)

        holon_test.take_part_of_data(0.25)
        self.assertEqual(len(holon_test.analyzed_vectors), 2)
        self.assertEqual(holon_test.analyzed_all_data, False)

        holon_test.take_part_of_data(0.25)
        self.assertEqual(len(holon_test.analyzed_vectors), 3)
        self.assertEqual(holon_test.analyzed_all_data, True)

    def test_holon_take_part_of_data_1(self):
        trait_names = ['O', 'P', 'Q', 'R']
        object_names = ['o1']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)
        knowledge_database.obj_traits = {'o1': [[0, 0, 1, 1], [1, 1, 1, 1], [2, 1, 1, 2]]}

        holon_test = HolonClass.Holon('o1', 'P', 'Q', knowledge_database=knowledge_database)
        self.assertEqual(holon_test.analyzed_vectors, [])
        self.assertEqual(holon_test.analyzed_all_data, False)

        holon_test.take_part_of_data(1.0)
        self.assertEqual(len(holon_test.analyzed_vectors), 3)
        self.assertEqual(holon_test.analyzed_all_data, True)

    
    def test_holon_update_0(self):
        trait_names = ['O', 'P', 'Q', 'R']
        object_names = ['o1']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)
        knowledge_database.obj_traits = {'o1': [[0, 1, 1, 2], [1, 1, 1, 0], [2, 1, 1, 2]]}

        holon_test = HolonClass.Holon('o1', 'P', 'Q', knowledge_database=knowledge_database)
        self.assertEqual(holon_test.analyzed_vectors, [])
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tt, 0.0)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.0)
        self.assertEqual(holon_test.ff, 0.0)
        
        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 1)
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tt, 1.0)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 2)
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tt, 1.0)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 3)
        self.assertEqual(holon_test.analyzed_all_data, True)
        self.assertEqual(holon_test.tt, 1.0)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

    def test_holon_update_1(self):
        trait_names = ['O', 'P', 'Q', 'R']
        object_names = ['o1']
        knowledge_database = KnowledgeDatabaseClass.KnowledgeDatabase(object_names, trait_names)
        knowledge_database.obj_traits = {'o1': [[0, 1, 1, 2], [1, 1, 1, 0], [2, 1, 1, 2]]}

        holon_test = HolonClass.Holon('o1', 'O', 'Q', knowledge_database=knowledge_database)
        self.assertEqual(holon_test.analyzed_vectors, [])
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tt, 0.0)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 1)
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 2)
        self.assertEqual(holon_test.analyzed_all_data, False)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ff, 0.0)

        holon_test.update()
        self.assertEqual(len(holon_test.analyzed_vectors), 3)
        self.assertEqual(holon_test.analyzed_all_data, True)
        self.assertEqual(holon_test.tt, 0.5)
        self.assertEqual(holon_test.tf, 0.0)
        self.assertEqual(holon_test.ft, 0.5)
        self.assertEqual(holon_test.ff, 0.0)
