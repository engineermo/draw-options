class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    urls = ['https://www.google.com/search?q=python+class+challenges+and+solutions&rlz=1C1SQJL_enUS818US818&oq=python'
            '+class+challenges+and+solutions&aqs=chrome..69i57.10308j0j7&sourceid=chrome&ie=UTF-8',
            'https://www.w3resource.com/python-exercises/class-exercises/', 'https://www.practicepython.org/', 'https'
            '://www.techbeamers.com/python-tutorial-step-by-step/']


print(py_solution().int_to_Roman(1))