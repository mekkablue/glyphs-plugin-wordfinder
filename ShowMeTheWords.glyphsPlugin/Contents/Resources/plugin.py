# encoding: utf-8

###########################################################################################################
#
#
#   Show Me The Words
#
#   Read the docs:
#   https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/SelectTool
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

from words import *

class ShowMeTheWords(GeneralPlugin):
    
    def settings(self):
        self.name = Glyphs.localize({'en': u'Show Me The Words'})

        # self.keyboardShortcut("f")


    def start(self):
        # create a menu item with its name, and a reference to the method it shoud invoke:
        newMenuItem = NSMenuItem(self.name, self.showWords)
        
        # append the menu item to one of the menus:
        Glyphs.menu[GLYPH_MENU].append(newMenuItem)


    def showWords(self, foo):
        print foo
        print Glyphs.font.selectedLayers

        glyphs = []
        for glyph in Glyphs.font.glyphs:
            if glyph.unicode:
                glyphs.append(unichr(int(glyph.unicode, 16)))

        print "available glyphs"
        print glyphs

        selected = []
        for layer in Glyphs.font.selectedLayers:
            glyph = layer.parent
            selected.append( unichr(int(glyph.unicode, 16) ) )

        print "selected glyphs"
        print selected

        words = get_words(amount = 10, letters = selected, availableLetters = glyphs)

        print "words"
        print words
        print " ".join(words)
            
        #Glyphs.font.newTab(unichr(int("0053", 16)))
        Glyphs.font.newTab(" ".join(words))
