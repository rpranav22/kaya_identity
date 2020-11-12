import unittest

def compute_score(pop, gdp, enInt, carbInt, output_type='co2'):
    '''

    :param pop: Population
    :param gdp: Gross Domestic Product
    :param enInt: Energy Intensity
    :param carbInt: Carbon Intensity
    :return: CO2 emmissions
    '''
    print(output_type.lower())
    if pop < 0 or gdp < 0:
        raise ValueError("Population and GDP cannot be less than 0")
    elif output_type.lower() not in ["co2","c"]:
        raise ValueError("Invalid output type")
    emission = pop * gdp * enInt * carbInt
    if output_type.lower() == "c":
        return emission/3.67
    return emission

class TestKayaCompute(unittest.TestCase):

    def test_accuracy(self):
        self.assertEqual(round(compute_score(82.4, 44, 5, 0.05),1), 906.4)

    def test_value_exception(self):
        with self.assertRaises(ValueError) as context:
            compute_score(-82.4, 44, 5, 0.05, 'c')
        self.assertEqual(str(context.exception),"Population and GDP cannot be less than 0" )
    def test_outputtype(self):
        with self.assertRaises(ValueError) as context:
            compute_score(-82.4, 44, 5, 0.05, 'd')
        self.assertEqual(str(context.exception), "Invalid output type")
        # self.assertTrue('Population and GDP cannot be less than 0' in context.exception)


if __name__ == '__main__':
    unittest.main()