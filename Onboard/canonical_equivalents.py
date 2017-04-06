# -*- coding: UTF-8 -*-

# Copyright © 2012-2013 marmuta <marmvta@gmail.com>
#
# This file is part of Onboard.
#
# Onboard is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Onboard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import division, print_function, unicode_literals

canonical_equivalents = {
    "all" : {
                'A' : ['Á', 'À', 'Â', 'Ä', 'Ă', 'Ā', 'Ã', 'Å', 'Ą', 'Æ'],
                'B' : ['Ɓ'],
                'C' : ['Ć', 'Ċ', 'Ĉ', 'Č', 'Ç'],
                'D' : ['Ď','Ḍ','Đ', 'Ɗ'],
                'E' : ['É', 'È', 'Ė', 'Ê', 'Ë', 'Ě', 'Ĕ', 'Ē', 'Ę', 'Ẹ', 'Ǝ', 'Ə'],
                'G' : ['Ġ', 'Ĝ', 'Ǧ', 'Ğ', 'Ģ', 'Ɣ'],
                'H' : ['Ĥ', 'Ḥ', 'Ħ'],
                'I' : ['Í', 'Ì', 'İ', 'Î', 'Ï', 'Ǐ', 'Ĭ', 'Ī', 'Ĩ', 'Į', 'Ị', 'Ĳ'],
                'J' : ['Ĵ'],
                'K' : ['Ķ', 'Ƙ'],
                'L' : ['Ĺ', 'Ļ', 'Ł', 'Ľ', 'Ŀ'],
                'N' : ['Ń', 'N̈', 'Ň', 'Ñ', 'Ņ', 'Ŋ'],
                'O' : ['Ó', 'Ò', 'Ô', 'Ö', 'Ǒ', 'Ō', 'Õ', 'Ő', 'Ǫ', 'Ọ', 'Ø', 'Ơ', 'Œ'],
                'R' : ['Ŕ', 'Ř', 'Ŗ'],
                'S' : ['Ś', 'Ŝ', 'Š', 'Ş', 'Ș', 'Ṣ', 'ẞ'],
                'T' : ['Ť', 'Ţ', 'Ṭ', 'Ŧ', 'Þ'],
                'U' : ['Ú', 'Ù', 'Û', 'Ü', 'Ǔ', 'Ŭ', 'Ū', 'Ũ', 'Ű', 'Ů', 'Ų', 'Ụ', 'Ư'],
                'W' : ['Ẃ', 'Ẁ', 'Ŵ', 'Ẅ', 'Ƿ'],
                'Y' : ['Ý', 'Ỳ', 'Ŷ', 'Ÿ', 'Ȳ', 'Ỹ', 'Ƴ'],
                'Z' : ['Ź', 'Ż', 'Ž', 'Ẓ'],

                'a' : ['á', 'à', 'â', 'ä', 'ǎ', 'ă', 'ā', 'ã', 'å', 'ą', 'æ'],
                'b' : ['ɓ'],
                'c' : ['ć', 'ċ', 'ĉ', 'č', 'ç'],
                'd' : ['ď', 'ḍ', 'đ', 'ɗ', 'ð'],
                'e' : ['é', 'è', 'ė', 'ê', 'ë', 'ě', 'ĕ', 'ē', 'ę', 'ẹ', 'ǝ', 'ɛ'],
                'g' : ['ġ', 'ĝ', 'ǧ', 'ğ', 'ģ', 'ɣ'],
                'h' : ['ĥ', 'ḥ', 'ħ'],
                'i' : ['í', 'ì', 'i', 'î', 'ï', 'ǐ', 'ĭ', 'ī', 'ĩ', 'į', 'ị', 'ĳ'],
                'j' : ['ĵ'],
                'k' : ['ƙ', 'ķ', 'ĸ'],
                'l' : ['ĺ', 'ļ', 'ľ', 'ŀ', 'ł'],
                'n' : ['ń', 'ñ', 'n̈', 'ň', 'ŉ', 'ņ', 'ŋ'],
                'o' : ['ó', 'ò', 'ô', 'ö', 'ǒ', 'ō', 'õ', 'ő', 'ǫ', 'ọ', 'ø', 'ơ', 'œ'],
                'r' : ['ŕ', 'ř', 'ŗ', 'ſ'],
                's' : ['ś', 'ŝ', 'š', 'ş', 'ș', 'ṣ', 'ß'],
                't' : ['ť', 'ţ', 'ṭ', 'ŧ', 'þ'],
                'u' : ['ú', 'ù', 'û', 'ü', 'ǔ', 'ŭ', 'ū', 'ũ', 'ű', 'ů', 'ų', 'ụ', 'ư'],
                'w' : ['ẃ', 'ẁ', 'ŵ', 'ẅ', 'ƿ'],
                'y' : ['ý', 'ỳ', 'ŷ', 'ÿ', 'ȳ', 'ỹ', 'ƴ'],
                'z' : ['ź', 'ż', 'ž', 'ẓ'],

                '1' : ['¹', '₁'],
                '2' : ['²', '₂', '½'],
                '3' : ['³', '₃', '⅓','⅔'],
                '4' : ['⁴', '₄', '¼', '¾'],
                '5' : ['⁵', '₅', '⅕', '⅖', '⅗', '⅘'],
                '6' : ['⁶', '₆', '⅙', '⅚'],
                '7' : ['⁷', '₇', '⅐'],
                '8' : ['⁸', '₈', '⅜', '⅝', '⅞'],
                '9' : ['⁹', '₉', '⅑'],
                '0' : ['₀', '⅒'],

                '?' : ['¿', '؟'],
                '!' : ['¡'],

                '"' : ['„', '“', '”', '«', '»', '‹', '›'],
                "'" : ['‘', '’', '`', '´'],

                '(' : ['[', '{'],
                ')' : [']', '}'],
                '[' : ['(', '{'],
                ']' : [')', '}'],
                '{' : ['(', '['],
                '}' : [')', ']'],

                '$' : ['€', '£', '¥', '₽', '₩', '¢'],
                '€' : ['$', '£', '¥', '₽', '₩', '¢'],
                '£' : ['$', '€', '¥', '₽', '₩', '¢'],
                '¥' : ['$', '€', '£', '₽', '₩', '¢'],
                '₽' : ['$', '€', '£', '¥', '₩', '¢'],
                '₩' : ['$', '€', '£', '¥', '₽', '¢'],
                '¢' : ['$', '€', '£', '¥', '₽', '₩'],

                'Æ' : ['Ǣ', 'Ǽ'],
                'Ø' : ['Ǿ'],
                'æ' : ['ǣ', 'ǽ'],
                'ø' : ['ǿ'],
                'ſ' : ['ẛ'],
                'Ʒ' : ['Ǯ'],
                'ʒ' : ['ǯ'],
                'ʹ' : ['ʹ'],
                'Α' : ['Ά', 'Ἀ', 'Ἁ', 'Ἂ', 'Ἃ', 'Ἄ', 'Ἅ', 'Ἆ', 'Ἇ', 'ᾈ', 'ᾉ', 'ᾊ', 'ᾋ', 'ᾌ', 'ᾍ', 'ᾎ', 'ᾏ', 'Ᾰ', 'Ᾱ', 'Ὰ', 'Ά', 'ᾼ'],
                'Ε' : ['Έ', 'Ἐ', 'Ἑ', 'Ἒ', 'Ἓ', 'Ἔ', 'Ἕ', 'Ὲ', 'Έ'],
                'Η' : ['Ή', 'Ἠ', 'Ἡ', 'Ἢ', 'Ἣ', 'Ἤ', 'Ἥ', 'Ἦ', 'Ἧ', 'ᾘ', 'ᾙ', 'ᾚ', 'ᾛ', 'ᾜ', 'ᾝ', 'ᾞ', 'ᾟ', 'Ὴ', 'Ή', 'ῌ'],
                'Ι' : ['Ί', 'Ϊ', 'Ἰ', 'Ἱ', 'Ἲ', 'Ἳ', 'Ἴ', 'Ἵ', 'Ἶ', 'Ἷ', 'Ῐ', 'Ῑ', 'Ὶ', 'Ί'],
                'Ο' : ['Ό', 'Ὀ', 'Ὁ', 'Ὂ', 'Ὃ', 'Ὄ', 'Ὅ', 'Ὸ', 'Ό'],
                'Ρ' : ['Ῥ'],
                'Υ' : ['Ύ', 'Ϋ', 'Ὑ', 'Ὓ', 'Ὕ', 'Ὗ', 'Ῠ', 'Ῡ', 'Ὺ', 'Ύ'],
                'Ω' : ['Ώ', 'Ὠ', 'Ὡ', 'Ὢ', 'Ὣ', 'Ὤ', 'Ὥ', 'Ὦ', 'Ὧ', 'ᾨ', 'ᾩ', 'ᾪ', 'ᾫ', 'ᾬ', 'ᾭ', 'ᾮ', 'ᾯ', 'Ὼ', 'Ώ', 'ῼ', 'Ω'],
                'α' : ['ά', 'ἀ', 'ἁ', 'ἂ', 'ἃ', 'ἄ', 'ἅ', 'ἆ', 'ἇ', 'ὰ', 'ά', 'ᾀ', 'ᾁ', 'ᾂ', 'ᾃ', 'ᾄ', 'ᾅ', 'ᾆ', 'ᾇ', 'ᾰ', 'ᾱ', 'ᾲ', 'ᾳ', 'ᾴ', 'ᾶ', 'ᾷ'],
                'ε' : ['έ', 'ἐ', 'ἑ', 'ἒ', 'ἓ', 'ἔ', 'ἕ', 'ὲ', 'έ'],
                'η' : ['ή', 'ἠ', 'ἡ', 'ἢ', 'ἣ', 'ἤ', 'ἥ', 'ἦ', 'ἧ', 'ὴ', 'ή', 'ᾐ', 'ᾑ', 'ᾒ', 'ᾓ', 'ᾔ', 'ᾕ', 'ᾖ', 'ᾗ', 'ῂ', 'ῃ', 'ῄ', 'ῆ', 'ῇ'],
                'ι' : ['ΐ', 'ί', 'ϊ', 'ἰ', 'ἱ', 'ἲ', 'ἳ', 'ἴ', 'ἵ', 'ἶ', 'ἷ', 'ὶ', 'ί', 'ι', 'ῐ', 'ῑ', 'ῒ', 'ΐ', 'ῖ', 'ῗ'],
                'ο' : ['ό', 'ὀ', 'ὁ', 'ὂ', 'ὃ', 'ὄ', 'ὅ', 'ὸ', 'ό'],
                'ρ' : ['ῤ', 'ῥ'],
                'υ' : ['ΰ', 'ϋ', 'ύ', 'ὐ', 'ὑ', 'ὒ', 'ὓ', 'ὔ', 'ὕ', 'ὖ', 'ὗ', 'ὺ', 'ύ', 'ῠ', 'ῡ', 'ῢ', 'ΰ', 'ῦ', 'ῧ'],
                'ω' : ['ώ', 'ὠ', 'ὡ', 'ὢ', 'ὣ', 'ὤ', 'ὥ', 'ὦ', 'ὧ', 'ὼ', 'ώ', 'ᾠ', 'ᾡ', 'ᾢ', 'ᾣ', 'ᾤ', 'ᾥ', 'ᾦ', 'ᾧ', 'ῲ', 'ῳ', 'ῴ', 'ῶ', 'ῷ'],
                'ϒ' : ['ϓ', 'ϔ'],
                'І' : ['Ї'],
                'А' : ['Ӑ', 'Ӓ'],
                'Г' : ['Ѓ'],
                'Е' : ['Ѐ', 'Ё', 'Ӗ'],
                'Ё' : ['Е', 'Ѐ', 'Ӗ'],              # 'Е' for Mongolian
                'Ж' : ['Ӂ', 'Ӝ'],
                'З' : ['Ӟ'],
                'И' : ['Ѝ', 'Й', 'Ӣ', 'Ӥ'],
                'Ѝ' : ['И', 'Й', 'Ӣ', 'Ӥ'],
                'Й' : ['И', 'Ѝ', 'Ӣ', 'Ӥ'],         # 'Ѝ' for Bulgarian
                'К' : ['Ќ', 'Ҝ'],                   # 'Ҝ' for Azerbaijani(Cyrillic)
                'О' : ['Ӧ'],
                'У' : ['Ў', 'Ӯ', 'Ӱ', 'Ӳ'],
                'Ч' : ['Ӵ', 'Ҹ'],                   # 'Ҹ' for Azerbaijani(Cyrillic)
                'Ш' : ['Щ'],                        # 'Щ' for Mongolian
                'Ь' : ['Ъ'],                        # 'Ъ' for Mongolian
                'Ы' : ['Ӹ'],
                'Э' : ['Ӭ'],
                'а' : ['ӑ', 'ӓ'],
                'г' : ['ѓ'],
                'е' : ['ѐ', 'ё', 'ӗ'],
                'ё' : ['е', 'ѐ', 'ӗ'],              # 'е' for Mongolian
                'ж' : ['ӂ', 'ӝ'],
                'з' : ['ӟ'],
                'и' : ['й', 'ѝ', 'ӣ', 'ӥ'],
                'ѝ' : ['и', 'й', 'ӣ', 'ӥ'],
                'й' : ['и', 'ѝ', 'ӣ', 'ӥ'],         # 'ѝ' for Bulgarian
                'к' : ['ќ', 'ҝ'],                   # 'ҝ' for Azerbaijani(Cyrillic)
                'о' : ['ӧ'],
                'у' : ['ў', 'ӯ', 'ӱ', 'ӳ'],
                'ч' : ['ӵ', 'ҹ'],                   # 'ҹ' for Azerbaijani(Cyrillic)
                'ш' : ['щ'],                        # 'щ' for Mongolian
                'ь' : ['ъ'],                        # 'ъ' for Mongolian
                'ы' : ['ӹ'],
                'э' : ['ӭ'],
                'і' : ['ї'],
                'Ѵ' : ['Ѷ'],
                'ѵ' : ['ѷ'],
                'Ә' : ['Ӛ'],
                'ә' : ['ӛ'],
                'Ө' : ['Ӫ'],
                'ө' : ['ӫ'],
                'ا' : ['آ', 'أ', 'إ'],
                'و' : ['ؤ'],
                'ي' : ['ئ'],
                'ہ' : ['ۂ'],
                'ے' : ['ۓ'],
                'ە' : ['ۀ'],
                'क' : ['क़'],
                'ख' : ['ख़'],
                'ग' : ['ग़'],
                'ज' : ['ज़'],
                'ड' : ['ड़'],
                'ढ' : ['ढ़'],
                'न' : ['ऩ'],
                'फ' : ['फ़'],
                'य' : ['य़'],
                'र' : ['ऱ'],
                'ळ' : ['ऴ'],
                'ড' : ['ড়'],
                'ঢ' : ['ঢ়'],
                'য' : ['য়'],
                'ਖ' : ['ਖ਼'],
                'ਗ' : ['ਗ਼'],
                'ਜ' : ['ਜ਼'],
                'ਫ' : ['ਫ਼'],
                'ਲ' : ['ਲ਼'],
                'ਸ' : ['ਸ਼'],
                'ଡ' : ['ଡ଼'],
                'ଢ' : ['ଢ଼'],
                'େ' : ['ୈ'],
                'ೂ' : ['ೊ'],
                'ೕ' : ['ೀ', 'ೇ'],
                'ೖ' : ['ೈ'],
                'ෙ' : ['ේ'],
                'ො' : ['ෝ'],
                'ཀ' : ['ཀྵ'],
                'ག' : ['གྷ'],
                'ཌ' : ['ཌྷ'],
                'ད' : ['དྷ'],
                'བ' : ['བྷ'],
                'ཛ' : ['ཛྷ'],
                'ဥ' : ['ဦ'],
                'ᬵ' : ['ᬻ', 'ᬽ', 'ᭃ'],
                '᾿' : ['῍', '῎', '῏'],
                '῾' : ['῝', '῞', '῟'],
                '\u2002' : ['\u2000'],
                '\u2003' : ['\u2001'],
                '←' : ['↚'],
                '→' : ['↛'],
                '↔' : ['↮'],
                '⇐' : ['⇍'],
                '⇒' : ['⇏'],
                '⇔' : ['⇎'],
                '∃' : ['∄'],
                '∈' : ['∉'],
                '∋' : ['∌'],
                '∣' : ['∤'],
                '∥' : ['∦'],
                '∼' : ['≁'],
                '≃' : ['≄'],
                '≅' : ['≇'],
                '≈' : ['≉'],
                '≍' : ['≭'],
                '≡' : ['≢'],
                '≤' : ['≰'],
                '≥' : ['≱'],
                '≲' : ['≴'],
                '≳' : ['≵'],
                '≶' : ['≸'],
                '≷' : ['≹'],
                '≺' : ['⊀'],
                '≻' : ['⊁'],
                '≼' : ['⋠'],
                '≽' : ['⋡'],
                '⊂' : ['⊄'],
                '⊃' : ['⊅'],
                '⊆' : ['⊈'],
                '⊇' : ['⊉'],
                '⊑' : ['⋢'],
                '⊒' : ['⋣'],
                '⊢' : ['⊬'],
                '⊨' : ['⊭'],
                '⊩' : ['⊮'],
                '⊫' : ['⊯'],
                '⊲' : ['⋪'],
                '⊳' : ['⋫'],
                '⊴' : ['⋬'],
                '⊵' : ['⋭'],
                '⫝' : ['⫝̸'],
                '〈' : ['〈'],
                '〉' : ['〉'],
                'う' : ['ゔ'],
                'か' : ['が'],
                'き' : ['ぎ'],
                'く' : ['ぐ'],
                'け' : ['げ'],
                'こ' : ['ご'],
                'さ' : ['ざ'],
                'し' : ['じ'],
                'す' : ['ず'],
                'せ' : ['ぜ'],
                'そ' : ['ぞ'],
                'た' : ['だ'],
                'ち' : ['ぢ'],
                'つ' : ['づ'],
                'て' : ['で'],
                'と' : ['ど'],
                'は' : ['ば', 'ぱ'],
                'ひ' : ['び', 'ぴ'],
                'ふ' : ['ぶ', 'ぷ'],
                'へ' : ['べ', 'ぺ'],
                'ほ' : ['ぼ', 'ぽ'],
                'ゝ' : ['ゞ'],
                'ウ' : ['ヴ'],
                'カ' : ['ガ'],
                'キ' : ['ギ'],
                'ク' : ['グ'],
                'ケ' : ['ゲ'],
                'コ' : ['ゴ'],
                'サ' : ['ザ'],
                'シ' : ['ジ'],
                'ス' : ['ズ'],
                'セ' : ['ゼ'],
                'ソ' : ['ゾ'],
                'タ' : ['ダ'],
                'チ' : ['ヂ'],
                'ツ' : ['ヅ'],
                'テ' : ['デ'],
                'ト' : ['ド'],
                'ハ' : ['バ', 'パ'],
                'ヒ' : ['ビ', 'ピ'],
                'フ' : ['ブ', 'プ'],
                'ヘ' : ['ベ', 'ペ'],
                'ホ' : ['ボ', 'ポ'],
                'ワ' : ['ヷ'],
                'ヰ' : ['ヸ'],
                'ヱ' : ['ヹ'],
                'ヲ' : ['ヺ'],
                'ヽ' : ['ヾ'],
           },
}

