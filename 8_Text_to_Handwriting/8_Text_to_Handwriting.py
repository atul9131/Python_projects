import pywhatkit as pw

txt = '''Being able to match varying sets of characters is the first thing regular expressions can do that isnt already possible with the methods available on strings.
'''

pw.text_to_handwriting(txt, 'demo1.png')

print('END')
