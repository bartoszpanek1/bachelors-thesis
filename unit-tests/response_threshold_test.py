import unittest

import response_thresholds as ResponseThresholdsClass


class ResponseThresholdsTest(unittest.TestCase):
    def test_get_response_0(self):
        response_thresholds = ResponseThresholdsClass.ResponseThresholds(0, 0.66, 0.66, 1, 1, 1)

        self.assertEqual(response_thresholds.min_pos, 0)
        self.assertEqual(response_thresholds.max_pos, 0.66)
        self.assertEqual(response_thresholds.min_bel, 0.66)
        self.assertEqual(response_thresholds.max_bel, 1)
        self.assertEqual(response_thresholds.min_know, 1)
        self.assertEqual(response_thresholds.max_know, 1)

        taken_all_data = False
        probability_1 = 0.25
        probability_2 = 0.66
        probability_3 = 0.75
        probability_4 = 1

        response = response_thresholds.get_response(probability_1, taken_all_data)
        self.assertEqual(response, 'Pos')

        response = response_thresholds.get_response(probability_2, taken_all_data)
        self.assertEqual(response, 'Pos')

        response = response_thresholds.get_response(probability_3, taken_all_data)
        self.assertEqual(response, 'Bel')

        response = response_thresholds.get_response(probability_4, taken_all_data)
        self.assertEqual(response, 'Bel')

        taken_all_data = True
        response = response_thresholds.get_response(probability_4, taken_all_data)
        self.assertEqual(response, 'Know')

    def test_get_response_1(self):
        response_thresholds = ResponseThresholdsClass.ResponseThresholds(0, 0.33, 0.33, 0.66, 0.66, 1)

        self.assertEqual(response_thresholds.min_pos, 0)
        self.assertEqual(response_thresholds.max_pos, 0.33)
        self.assertEqual(response_thresholds.min_bel, 0.33)
        self.assertEqual(response_thresholds.max_bel, 0.66)
        self.assertEqual(response_thresholds.min_know, 0.66)
        self.assertEqual(response_thresholds.max_know, 1)

        taken_all_data = False
        probability_1 = 0.25
        probability_2 = 0.66
        probability_3 = 0.75
        probability_4 = 1

        response = response_thresholds.get_response(probability_1, taken_all_data)
        self.assertEqual(response, 'Pos')

        response = response_thresholds.get_response(probability_2, taken_all_data)
        self.assertEqual(response, 'Bel')

        response = response_thresholds.get_response(probability_3, taken_all_data)
        self.assertEqual(response, 'Bel')

        response = response_thresholds.get_response(probability_4, taken_all_data)
        self.assertEqual(response, 'Bel')

        taken_all_data = True
        response = response_thresholds.get_response(probability_4, taken_all_data)
        self.assertEqual(response, 'Know')