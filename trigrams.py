#!/usr/bin/env python

key_table = {
    'a': 'blbobrbsccchcrctdddmdverfffrftgagegoheirlilllmlolrlsltlwm memondngninonsnypappprrergrmrrrtsisksltetmttudugutvevowa',
    'b': 'abacadagalanasate eaecedeeefegeheleseteyicigikiliritlaleloluoaodonooorotouoxoyrarerirouiurusutuyy ',
    'c': 'akalamanaparasatauenerhahehihohihuiritlalelilooaofoiolomonoooporosouovowreriroryupurusut',
    'd': 'adaiamanaratauayeaeceeefegelemenepesetevicidieifiginirisivo ocoeogolonooouowozrareriroruryueurusut',
    'e': 'acarasatduffggigitlelsmpndnengnjnontqurrspurvexaxcxexpye',
    'f': 'acaialamarasateaebedeeelewieifigilinirisivixlalelilolyolooorourareriroruulunut',
    'g': 'aiamarasataveneretirivlao odoionoootovrarerouaueuiun',
    'h': 'abadaialanaparasatave eaeieleri idigilimirisitolomonoporosotouowumunurus',
    'i': '  cedef mammmpn ncndnfnsntnvros slt ts',
    'j': 'anapoboiudulumunus',
    'k': "eeepeyicilinitneninoabadaiakanarasatauawayazeaedefegenesetevibieifigikiminisitivoconooosotouovowunyiacadagaiajakanaparataye eaedeeemenesetidigilinisodomonooorosotouovucumusy ysamarateaeceeeievewexicigino oboionooorosotovowumbj'cctf fffth ilkaldn ncnenlpepippr rardthurutvewn",
    'p': 'acagaiaparasatayeaeneoerhoicieiniplaleocoioloooposotouowrareriroubulupurusut',
    'q': 'uaueui',
    'r': 'acadaianapateaecedefegelemepeqeseticidiginisivoaocodolooosouowulunus',
    's': 'adafaialamanatavawaycechcicoeaeceeeleneperetevexhahehihohuicidigiliminisitixizkikylelilomamemimonoo oaocofoiolomonoooroupapepipoprqutatetitotrtutyubucudufugumunupurwawewiwuys',
    't': 'abakalasauaxeaeeelemenereshahehihohrhuicieilimirito odogolomonoooporotouowrareriroruryueurv wewiwoyiyp',
    'u': 'nancndninlntp pos sesu',
    'v': 'alaregerieilisoiolotaiakalanarasatavaye eaedeeeieleneresethahehihohyidifilinirisitivokomonooorouriroma',
    'y': 'areaelenesetou',
    'z': 'er'
}


def main():
    for letter in key_table:
        keys = key_table[letter]

        print '=' * 20
        print 'trigram table for %s' % (letter)
        print '=' * 20

        for i in range(0, len(keys), 2):
            key = keys[i:i+2]
            print '%s%s' % (letter, key)

        print ''


if __name__ == '__main__':
    main()
