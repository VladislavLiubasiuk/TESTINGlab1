
from test_lab1 import Formulas
import unittest

class TestFormulas(unittest.TestCase):

    def test_first_calculation1(self):
        Form = Formulas(1)
        res = Form.result_1()
        self.assertEqual(res, 5.016)

    def test_first_calculation2(self):
        Form = Formulas(1)
        res = Form.result_2()
        self.assertEqual(res, 6.163)

    def test_first_calculation3(self):
        Form = Formulas(1)
        res = Form.result_3()
        self.assertEqual(res, 5.52)

    def test_first_calculation4(self):
        Form = Formulas(1)
        res = Form.result_4()
        self.assertEqual(res, 4.314)

    def test_second_calculation1(self):
        Form = Formulas(0.1)
        res = Form.result_1()
        self.assertEqual(res, 0.16663440000000002)

    def test_second_calculation2(self):
        Form = Formulas(0.1)
        res = Form.result_2()
        self.assertEqual(res, 0.553948)

    def test_second_calculation3(self):
        Form = Formulas(0.1)
        res = Form.result_3()
        self.assertEqual(res, 0.37668)

    def test_second_calculation4(self):
        Form = Formulas(0.1)
        res = Form.result_4()
        self.assertEqual(res, 0.4314)

    def test_third_calculation1(self):
        Form = Formulas(0)
        res = Form.result_1()
        self.assertEqual(res, 0.0)

    def test_third_calculation2(self):
        Form = Formulas(0)
        res = Form.result_2()
        self.assertEqual(res, 0.0)

    def test_third_calculation3(self):
        Form = Formulas(0)
        res = Form.result_3()
        self.assertEqual(res, 0.0)

    def test_third_calculation4(self):
        Form = Formulas(0)
        res = Form.result_4()
        self.assertEqual(res, 0.0)

    def test_fourth_calculation1(self):
        Form = Formulas(-5)
        res = Form.result_1()
        self.assertEqual(res, 423.42)

    def test_fourth_calculation2(self):
        Form = Formulas(-5)
        res = Form.result_2()
        self.assertEqual(res, -392.225)

    def test_fourth_calculation3(self):
        Form = Formulas(-5)
        res = Form.result_3()
        self.assertEqual(res, 30.839999999999996)

    def test_fourth_calculation4(self):
        Form = Formulas(-5)
        res = Form.result_4()
        self.assertEqual(res, -21.57)

    def test_fifth_calculation1(self):
        Form = Formulas(-200)
        res = Form.result_1()
        self.assertEqual(res, 2455437709.8)

    def test_fifth_calculation2(self):
        Form = Formulas(-200)
        res = Form.result_2()
        self.assertEqual(res, -20067344.0)

    def test_fifth_calculation3(self):
        Form = Formulas(-200)
        res = Form.result_3()
        self.assertEqual(res, 77205.6)

    def test_fifth_calculation4(self):
        Form = Formulas(-200)
        res = Form.result_4()
        self.assertEqual(res, -862.8)

    def test_sixth_calculation1(self):
        Form = Formulas(1000)
        res = Form.result_1()
        self.assertEqual(res, 1557856753851.0)

    def test_sixth_calculation2(self):
        Form = Formulas(1000)
        res = Form.result_2()
        self.assertEqual(res, 2495950720.0)

    def test_sixth_calculation3(self):
        Form = Formulas(1000)
        res = Form.result_3()
        self.assertEqual(res, 1951572.0)

    def test_sixth_calculation4(self):
        Form = Formulas(1000)
        res = Form.result_4()
        self.assertEqual(res, 4314.0)

    def test_seventh_calculation1(self):
        Form = Formulas(199)
        res = Form.result_1()
        self.assertEqual(res, 2467366295.196)

    def test_seventh_calculation2(self):
        Form = Formulas(199)
        res = Form.result_2()
        self.assertEqual(res, 19605494.527000003)

    def test_seventh_calculation3(self):
        Form = Formulas(199)
        res = Form.result_3()
        self.assertEqual(res, 77853.57599999999)

    def test_seventh_calculation4(self):
        Form = Formulas(199)
        res = Form.result_4()
        self.assertEqual(res, 858.486)

    def test_eighth_calculation1(self):
        Form = Formulas(192.359)
        res = Form.result_1()
        self.assertEqual(res, 2155038503.593075)

    def test_eighth_calculation2(self):
        Form = Formulas(192.359)
        res = Form.result_2()
        self.assertEqual(res, 17704987.909240797)

    def test_eighth_calculation3(self):
        Form = Formulas(192.359)
        res = Form.result_3()
        self.assertEqual(res, 72766.972896188)

    def test_eighth_calculation4(self):
        Form = Formulas(192.359)
        res = Form.result_4()
        self.assertEqual(res, 829.836726)

    def test_ninth_calculation1(self):
        Form = Formulas(200)
        res = Form.result_1()
        self.assertEqual(res, 2517182450.2)

    def test_ninth_calculation2(self):
        Form = Formulas(200)
        res = Form.result_2()
        self.assertEqual(res, 19902944.0)

    def test_ninth_calculation3(self):
        Form = Formulas(200)
        res = Form.result_3()
        self.assertEqual(res, 78634.4)

    def test_ninth_calculation4(self):
        Form = Formulas(200)
        res = Form.result_4()
        self.assertEqual(res, 862.8)

    def test_tenth_calculation1(self):
        Form = Formulas(300)
        res = Form.result_1()
        self.assertEqual(res, 12691391235.3)

    def test_tenth_calculation2(self):
        Form = Formulas(300)
        res = Form.result_2()
        self.assertEqual(res, 67262766.0)

    def test_tenth_calculation3(self):
        Form = Formulas(300)
        res = Form.result_3()
        self.assertEqual(res, 176391.6)

    def test_tenth_calculation4(self):
        Form = Formulas(300)
        res = Form.result_4()
        self.assertEqual(res, 1294.2)

# /////////////////////////////////////////////////////////////////////////////////////////////////

    def test_eleventh_calculation1(self):
        Form = Formulas(999)
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation2(self):
        Form = Formulas(999)
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation3(self):
        Form = Formulas(999)
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_eleventh_calculation4(self):
        Form = Formulas(999)
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation1(self):
        Form = Formulas("minrugh")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation2(self):
        Form = Formulas("minrugh")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation3(self):
        Form = Formulas("minrugh")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twelfth_calculation4(self):
        Form = Formulas("minrugh")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation1(self):
        Form = Formulas("ewryt")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation2(self):
        Form = Formulas("ewryt")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation3(self):
        Form = Formulas("ewryt")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_thirteenth_calculation4(self):
        Form = Formulas("ewryt")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation1(self):
        Form = Formulas(-5487)
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation2(self):
        Form = Formulas(-5487)
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation3(self):
        Form = Formulas(-5487)
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_fourteenth_calculation4(self):
        Form = Formulas(-5487)
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation1(self):
        Form = Formulas("randirandom")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation2(self):
        Form = Formulas("randirandom")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation3(self):
        Form = Formulas("randirandom")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_fifteenth_calculation4(self):
        Form = Formulas("randirandom")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation1(self):
        Form = Formulas("hygn")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation2(self):
        Form = Formulas("hygn")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation3(self):
        Form = Formulas("hygn")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_sixteenth_calculation4(self):
        Form = Formulas("hygn")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation1(self):
        Form = Formulas(-10)
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation2(self):
        Form = Formulas(-10)
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation3(self):
        Form = Formulas(-10)
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_seventeenth_calculation4(self):
        Form = Formulas(-10)
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation1(self):
        Form = Formulas("98u")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation2(self):
        Form = Formulas("98u")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation3(self):
        Form = Formulas("98u")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_eighteenth_calculation4(self):
        Form = Formulas("98u")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation1(self):
        Form = Formulas("  `")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation2(self):
        Form = Formulas("  `")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation3(self):
        Form = Formulas("  `")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_nineteenth_calculation4(self):
        Form = Formulas("  `")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation1(self):
        Form = Formulas(765)
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation_2(self):
        Form = Formulas(765)
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation3(self):
        Form = Formulas(765)
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twentieth_calculation4(self):
        Form = Formulas(765)
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation1(self):
        Form = Formulas("frd")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation2(self):
        Form = Formulas("frd")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation3(self):
        Form = Formulas("frd")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_first_calculation4(self):
        Form = Formulas("frd")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation1(self):
        Form = Formulas("sd484")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation2(self):
        Form = Formulas("sd484")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation3(self):
        Form = Formulas("sd484")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_second_calculation4(self):
        Form = Formulas("sd484")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation1(self):
        Form = Formulas("kimhj")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation2(self):
        Form = Formulas("kimhj")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation3(self):
        Form = Formulas("kimhj")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_third_calculation4(self):
        Form = Formulas("kimhj")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation1(self):
        Form = Formulas("adw98")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation2(self):
        Form = Formulas("adw98")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation3(self):
        Form = Formulas("adw98")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_fourth_calculation4(self):
        Form = Formulas("adw98")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation1(self):
        Form = Formulas("4cd4")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation2(self):
        Form = Formulas("4cd4")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation3(self):
        Form = Formulas("4cd4")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_fifth_calculation4(self):
        Form = Formulas("4cd4")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation1(self):
        Form = Formulas("lka462")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation2(self):
        Form = Formulas("lka462")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation3(self):
        Form = Formulas("lka462")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_sixth_calculation4(self):
        Form = Formulas("lka462")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation1(self):
        Form = Formulas("*5w2w2")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation2(self):
        Form = Formulas("*5w2w2")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation3(self):
        Form = Formulas("*5w2w2")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_seventh_calculation4(self):
        Form = Formulas("*5w2w2")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation1(self):
        Form = Formulas("9ad8u")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation2(self):
        Form = Formulas("9ad8u")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation3(self):
        Form = Formulas("9ad8u")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_eighth_calculation4(self):
        Form = Formulas("9ad8u")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation1(self):
        Form = Formulas("51")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation2(self):
        Form = Formulas("51")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation3(self):
        Form = Formulas("51")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_twenty_ninth_calculation4(self):
        Form = Formulas("51")
        res = Form.result_4()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation1(self):
        Form = Formulas("4c86k")
        res = Form.result_1()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation2(self):
        Form = Formulas("4c86k")
        res = Form.result_2()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation3(self):
        Form = Formulas("4c86k")
        res = Form.result_3()
        self.assertEqual(res, "Error")

    def test_thirtieth_calculation4(self):
        Form = Formulas("4c86k")
        res = Form.result_4()
        self.assertEqual(res, "Error")


if __name__ == '__main__':
    unittest.main()
