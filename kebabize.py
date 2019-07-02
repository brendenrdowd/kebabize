def kebabize(string):
    result = ''
    for index, letter in enumerate(string):
        if letter.islower() == True or (index == 0 and letter.isalpha() == True):
            result += letter
        elif letter.isupper() == True:
            result += '-' + letter
        else:
            continue
    return result.lower()

Test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
Test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
Test.assert_equals(kebabize('SOS'), 's-o-s')
Test.assert_equals(kebabize('42'), '')
``