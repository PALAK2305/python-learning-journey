# write a program to fill in a letter template given below with name & date

letter = '''dear <|name|>, 
        you are selected! 
        <|date|>'''

print(letter.replace("<|name|>","Palak").replace("<|date|>","24 sept 2025")) 