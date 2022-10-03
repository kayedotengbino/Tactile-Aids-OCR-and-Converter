from pyexpat import model
from django.db import models

class toBraille(models.Model):
    def translateToBraille(text):
        alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇',
        '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
        numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        puntuation = [',',';',':','.','?','!', ';','(',')', '/', '-']
        puntuationBraille = ['⠂','⠆','⠒','⠲','⠦','⠖','⠐⠣','⠐⠜','⠸⠌','⠤']
        character = ['&','*','@','©','®','™','°',]
        characterBraille = ['⠈⠯','⠐⠔','⠈⠁','⠘⠉','⠘⠗','⠘⠞','⠘⠚',]

        inputString = ' '

        if len(text) > 0 : 
            for n in text.lower():
                if n in alphabet:
                    inputString += alphaBraille[alphabet.index(n)]
                elif n in nums:
                    inputString += numBraille[nums.index(n)]
                elif n in puntuation:
                    inputString += puntuationBraille[puntuation.index(n)]
                elif n in character:
                    inputString += characterBraille[character.index(n)]
            
            return inputString

class textTo(models.Model):
    input = models.CharField(max_length = 200)

    def __str__(self):
        return self.input + ' is' + toBraille.translateToBraille(self.input)