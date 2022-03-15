import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # lst = [1, [2, [3, [4, [5]]]]]
        lst = [1, 2, 3, 4, 5]
        paket = 0
        # Закупка в магазине
        for i in lst:
            print(i)
            paket = paket + i
        print(paket)

        # self.assertEqual(True, False)  # add assertion here


    def test_something1(self):
        # lst = [1, [2, [3, [4, [5]]]]]
        lst = [1, 2, 3, 4, 5]
        paket = 0
        # Закупка в магазине
        for i in lst:
            #стою на ленте решаю что брать что нет
            print(i)
            if i < 4:
                #ложу в пакет
                paket = paket + i
        print(paket)

        #self.assertEqual(True, False)  # add assertion here

    def test_something2(self):
        # lst = [1, [2, [3, [4, [5]]]]]
        lst = [1, 2, 3, 4, 5]
        paket = 0
        # Закупка в магазине
        for i in lst:
            #стою на ленте решаю что брать что нет
            print(i)
            if i == 3:
                #выход из функции
                break

            #ложу в пакет
            paket = paket + i
        print(paket)

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
