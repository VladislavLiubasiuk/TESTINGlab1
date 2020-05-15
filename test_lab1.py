class Formulas():
    def __init__(self, x):
        self.x = x

    def variantN4(self):
        try:
            if self.x <= 1.707 or self.x >= 106.33:
                result_1 = self.x**4 * 4.968 + self.x**3 * 2.271 - self.x**2 * 3.589 + self.x * 3.317
                result_2 = self.x**3 * 3.774 - self.x**2 * 2.298 + self.x * 3.873
                result_3 = self.x**2 * 4.165 + self.x * 3.363
                result_4 = self.x*6.363
                return result_1, result_2, result_3, result_4
        except TypeError:
            return "Error"
if __name__ == '__main__':
    Form = Formulas(6)
    print(Form.variantN4())