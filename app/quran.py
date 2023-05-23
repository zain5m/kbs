from experta import *
import pyarabic.araby as ar
import pyquran.tools.quran as quran

global aya

global Alahkam

aya = quran.get_sura(17,True)  # t = q.quran.get_verse(num_sura, num_aya, True)

Alahkam = {}


class Madd_Tabieiun(Fact):
    pass


class Madd_Motasel(Fact):
    pass


class Madd_Monfasel(Fact):  
    pass


class Madd_Lazem_Kaleme_Mothqal(Fact):
    pass


class Madd_Lazem_Kaleme_Moghafaf(Fact):
    pass


class Madd_Lazem_Harfi(Fact):
    pass


class Madd_Ared_Lsocon(Fact):
    pass


class Madd_Sela(Fact):
    pass


class Madd_Faroq(Fact):
    pass


class Madd_Allayen(Fact):
    pass


class Madd_Albadal(Fact):
    pass


# أحكام النون الساكنة
class Idhar(Fact):
    pass


class Iqlab(Fact):
    pass


class Idgham_Kamel(Fact):
    pass


class Idgham_Nakes(Fact):
    pass


class Ikhfaa(Fact):
    pass


# أحكام الميم الساكنة
class Idhar_Shafawe(Fact):
    pass


class Ikhfaa_Shafawe(Fact):
    pass


class Idgham_Meem(Fact):
    pass


# القلقلة
class Kalkla(Fact):
    pass


# اللام
class Laam(Fact):
    pass


# الراء
class Raa(Fact):
    pass


class ES(KnowledgeEngine):


    @Rule()
    def Find_Madd_Tabieiun(self):
        Madd = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                Madd.append(i)
        for f in Madd:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):
                self.declare(Madd_Tabieiun(a='True'))
                ahkam.append(aya[f - 2:f + 1])
        if (len(ahkam) > 0):
            Alahkam['حكم مد طبيعي في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Motasel(self):
        MaddMotasel = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                MaddMotasel.append(i)
        for f in MaddMotasel:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA) and \
                    f + 1 <= len(aya) and ar.is_hamza(aya[f + 1]):
                self.declare(Madd_Motasel(a='True'))
                ahkam.append(f' {aya[f - 1:f + 2]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد متصل في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Monfasel(self):
        MaddMotasel = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                MaddMotasel.append(i)
        for f in MaddMotasel:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):
                if f + 1 <= len(aya) and aya[f + 1] == ' ':
                    if f + 2 < len(aya) and (ar.is_hamza(aya[f + 2]) or ar.is_alef_above_hamza(aya[f + 2])):
                        self.declare(Madd_Motasel(a='True'))
                        ahkam.append(f' {aya[f - 2:f + 3]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد منفصل في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Lazem_Kaleme_Moghafaf(self):
        MaddLazem_Kaleme_Moghafaf = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                MaddLazem_Kaleme_Moghafaf.append(i)

        for f in MaddLazem_Kaleme_Moghafaf:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):

                if f + 1 < len(aya) and not ar.is_shadda(aya[f + 2]):
                    self.declare(Madd_Lazem_Kaleme_Moghafaf(a='True'))
                    ahkam.append(f' {aya[f - 3:f + 3]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد لازم كلمي مخفف في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Lazem_Kaleme_Mothqal(self):
        MaddLazem_Kaleme_Mothqal = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                MaddLazem_Kaleme_Mothqal.append(i)

        for f in MaddLazem_Kaleme_Mothqal:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):

                if f + 1 < len(aya) and ar.is_shadda(aya[f + 2]):
                    self.declare(Madd_Lazem_Kaleme_Mothqal(a='True'))
                    ahkam.append(f' {aya[f - 3:f + 3]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد لازم كلمي مثقل في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Ared_Lsocon(self):
        ahkam = []
        list = aya.split(" ")

        for val in list:
            for i, char in enumerate(val):
                if (char == ar.ALEF and i - 1 >= 0 and val[i - 1] == ar.FATHA) or (
                        char == ar.WAW and i - 1 >= 0 and val[i - 1] == ar.DAMMA) or \
                        (char == ar.YEH and i - 1 >= 0 and val[i - 1] == ar.KASRA):

                    if val[len(val) - 3] == ar.ALEF or val[len(val) - 3] == ar.WAW or val[
                        len(val) - 3] == ar.YEH:  # الحرف قبل الاخير
                        self.declare(Madd_Ared_Lsocon(a='True'))
                        ahkam.append(f' {val[len(val) - 5:]}')

        if (len(ahkam) > 0):
            Alahkam['حكم مد عارض للسكون في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Sela(self):
        Madd_Sela_Kobra = []
        Madd_Sela_Soghra = []

        for i, char in enumerate(aya):
            if char == ar.HEH and ar.is_haraka(aya[i - 1]) and ar.is_haraka(aya[i + 1]):

                if i + 2 < len(aya) and aya[i + 2] == ' ':  # مفخمة
                    if ar.is_hamza(aya[i + 3]):
                        self.declare(Madd_Sela(a='True'))
                        Madd_Sela_Kobra.append(f'{aya[i - 2:i + 3]}')

                if i + 2 < len(aya) and aya[i + 2] == ' ':  # مفخمة
                    if not ar.is_hamza(aya[i + 3]):
                        self.declare(Madd_Sela(a='True'))
                        Madd_Sela_Soghra.append(f'{aya[i - 2:i + 3]}')

        if len(Madd_Sela_Kobra) > 0:
            Alahkam['حكم مد صلة كبرى في المواضع'] = Madd_Sela_Kobra

        if len(Madd_Sela_Soghra) > 0:
            Alahkam['حكم مد صلة صغرى في المواضع'] = Madd_Sela_Soghra

    @Rule()
    def Find_Madd_Faroq(self):
        FindMadd_Faroq = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.MADDA_ABOVE or char == ar.WAW or char == ar.YEH:
                FindMadd_Faroq.append(i)

        for f in FindMadd_Faroq:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):

                if f + 1 < len(aya) and ar.is_shadda(aya[f + 2]):
                    self.declare(Madd_Lazem_Kaleme_Mothqal(a='True'))
                    ahkam.append(f' {aya[f - 3:f + 3]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد لازم كلمي مثقل في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Allayen(self):
        FindMadd_Allayen = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.WAW or char == ar.YEH:
                FindMadd_Allayen.append(i)

        for f in FindMadd_Allayen:
            if f - 1 >= 0 and aya[f - 1] == ar.FATHA and f + 1 < len(aya) and not ar.is_haraka(aya[f + 1]) and not ar.is_shadda(aya[f + 1]):
                self.declare(Madd_Allayen(a='True'))
                ahkam.append(f' {aya[f - 2:f + 1]}')
        if (len(ahkam) > 0):
            Alahkam['حكم مد اللين في المواضع'] = ahkam

    @Rule()
    def Find_Madd_Albadal(self):
        FindMadd_Albadal = []
        ahkam = []
        for i, char in enumerate(aya):
            if char == ar.ALEF or char == ar.WAW or char == ar.YEH:
                FindMadd_Albadal.append(i)
        for f in FindMadd_Albadal:
            if f - 1 >= 0 and (aya[f - 1] == ar.FATHA or aya[f - 1] == ar.KASRA or aya[f - 1] == ar.DAMMA):
                if f - 2 >= 0 and ar.is_hamza(aya[f - 2]):
                    self.declare(Madd_Albadal(a='True'))
                    ahkam.append(aya[f - 2:f + 1])

        if (len(ahkam) > 0):
            Alahkam['حكم مد بدل في المواضع'] = ahkam

    # أحكام النون الساكنة
    @Rule()
    def Find_Idhar(self):
        FindIdhar = []
        ahkam_noon = []
        ahkam_tanwen = []
        for i, char in enumerate(aya):
            if char == ar.TANWIN or (char == ar.NOON and aya[i+1]==ar.SUKUN ):
                FindIdhar.append(i)

        for f in FindIdhar:
            if (f + 1 < len(aya) and (
                    aya[f + 1] == ar.HAMZA or aya[f + 1] == ar.HAH or aya[f + 1] == ar.AIN or aya[f + 1] == ar.HEH or
                    aya[f + 1] == ar.KHAH or aya[f + 1] == ar.GHAIN)) or \
                    (f + 2 < len(aya) and (
                            aya[f + 2] == ar.HAMZA or aya[f + 2] == ar.HAH or aya[f + 2] == ar.AIN or aya[f + 2] == ar.HEH or
                            aya[f + 2] == ar.KHAH or aya[f + 2] == ar.GHAIN)):

                if aya[f] == ar.TANWIN:
                    self.declare(Idhar(a='True'))
                    ahkam_tanwen.append(f' {aya[f - 2:f + 2]}')
                else:
                    self.declare(Idhar(a='True'))
                    ahkam_noon.append(f' {aya[f - 3:f + 3]}')

        if (len(ahkam_noon) > 0):
            Alahkam['حكم النون الساكنة(الاظهار) في المواضع'] = ahkam_noon

        if (len(ahkam_tanwen) > 0):
            Alahkam['حكم التنوين الساكن(الاظهار) في المواضع'] = ahkam_tanwen

    @Rule()
    def Find_Iqlap(self):
        FindIqlap = []
        ahkam_noon = []
        ahkam_tanwen = []
        for i, char in enumerate(aya):
            if char == ar.TANWIN or (char == ar.NOON and not ar.is_haraka(aya[i + 1]) and not ar.is_shadda(aya[i + 1])):
                FindIqlap.append(i)

        for f in FindIqlap:
            if f + 1 < len(aya) and aya[f + 1] == ar.BEH:
                if aya[f] == ar.TANWIN:
                    self.declare(Iqlab(a='True'))
                    ahkam_tanwen.append(f' {aya[f - 2:f + 2]}')
                else:
                    self.declare(Idhar(a='True'))
                    ahkam_noon.append(f' {aya[f - 3:f + 3]}')

        if (len(ahkam_noon) > 0):
            Alahkam['حكم النون الساكنة(الاقلاب) في المواضع'] = ahkam_noon

        if (len(ahkam_tanwen) > 0):
            Alahkam['حكم التنوين الساكن(الاقلاب) في المواضع'] = ahkam_tanwen

    @Rule()
    def Find_Idgham_Kamel(self):
        FindIdgham_Kamel = []
        ahkam_noon = []
        ahkam_tanwen = []
        for i, char in enumerate(aya):
            if char == ar.TANWIN or (char == ar.NOON and not ar.is_haraka(aya[i + 1])and not ar.is_shadda(aya[i + 1])):
                FindIdgham_Kamel.append(i)

        for f in FindIdgham_Kamel:
            if f + 1 < len(aya) and aya[f + 1] == ' ':
                if f + 2 < len(aya) and (aya[f + 2] == ar.LAM or aya[f + 2] == ar.REH):
                    if aya[f] == ar.TANWIN:
                        self.declare(Idgham_Kamel(a='True'))
                        ahkam_tanwen.append(f' {aya[f - 2:f + 2]}')
                    else:
                        self.declare(Idgham_Kamel(a='True'))
                        ahkam_noon.append(f' {aya[f - 3:f + 3]}')

        if (len(ahkam_noon) > 0):
            Alahkam['حكم النون الساكنة(ادغام كامل بدون غنة) في المواضع'] = ahkam_noon

        if (len(ahkam_tanwen) > 0):
            Alahkam['حكم التنوين الساكن(ادغام كامل بدون غنة) في المواضع'] = ahkam_tanwen

    @Rule()
    def Find_Idgham_Nakes(self):
        FindIdgham_Nakes = []
        ahkam_noon = []
        ahkam_tanwen = []
        for i, char in enumerate(aya):
            if char == ar.TANWIN or (char == ar.NOON and not ar.is_haraka(aya[i + 1]) and not ar.is_shadda(aya[i + 1])):
                FindIdgham_Nakes.append(i)

        for f in FindIdgham_Nakes:
            if f + 1 < len(aya) and aya[f + 1] == ' ':
                if f + 2 < len(aya) and (
                        aya[f + 2] == ar.YEH or aya[f + 2] == ar.WAW or aya[f + 2] == ar.MEEM or aya[f + 2] == ar.NOON):
                    if aya[f] == ar.TANWIN:
                        self.declare(Idgham_Nakes(a='True'))
                        ahkam_tanwen.append(f' {aya[f - 2:f + 2]}')
                    else:
                        self.declare(Idgham_Nakes(a='True'))
                        ahkam_noon.append(f' {aya[f - 3:f + 3]}')

        if (len(ahkam_noon) > 0):
            Alahkam['حكم النون الساكنة(ادغام ناقص مع غنة) في المواضع'] = ahkam_noon

        if (len(ahkam_tanwen) > 0):
            Alahkam['حكم التنوين الساكن(ادغام ناقص مع غنة) في المواضع'] = ahkam_tanwen

    @Rule()
    def Find_Ikhfaa(self):
        FindIkhfaa = []
        ahkam_noon = []
        ahkam_tanwen = []
        for i, char in enumerate(aya):
            if char == ar.TANWIN or (char == ar.NOON and not ar.is_haraka(aya[i + 1]) and not ar.is_shadda(aya[i + 1])):
                FindIkhfaa.append(i)

        for f in FindIkhfaa:
            if ((f + 1 < len(aya) and aya[f + 1] != ar.YEH and aya[f + 1] != ar.WAW and aya[f + 1] != ar.MEEM and aya[
                f + 1] != ar.NOON and aya[f + 1] != ar.LAM and aya[f + 1] != ar.REH and aya[f + 1] != ar.HAMZA or aya[
                     f + 1] != ar.HAH or aya[f + 1] != ar.AIN or aya[f + 1] != ar.HEH and
                 aya[f + 1] != ar.KHAH or aya[f + 1] != ar.GHAIN) or (aya[f + 1] == ' ' and f + 2 < len(aya) and (
                    aya[f + 2] != ar.YEH and aya[f + 2] != ar.WAW and aya[f + 2] != ar.MEEM and aya[f + 2] != ar.NOON and aya[
                f + 2] != ar.LAM and aya[f + 2] != ar.REH and aya[f + 2] != ar.HAMZA or aya[f + 2] != ar.HAH or aya[
                        f + 2] != ar.AIN or aya[f + 2] != ar.HEH and
                    aya[f + 2] != ar.KHAH or aya[f + 2] != ar.GHAIN))):

                if aya[f] == ar.TANWIN:
                    self.declare(Ikhfaa(a='True'))
                    ahkam_tanwen.append(f' {aya[f - 2:f + 4]} ')
                else:
                    self.declare(Ikhfaa(a='True'))
                    ahkam_noon.append(f' {aya[f - 2:f + 4]} ')

        if (len(ahkam_noon) > 0):
            Alahkam['حكم النون الساكنة(اخفاء) في المواضع'] = ahkam_noon

        if (len(ahkam_tanwen) > 0):
            Alahkam['حكم التنوين الساكن(اخفاء) في المواضع'] = ahkam_tanwen

    # أحكام الميم الساكنة:
    @Rule()
    def Find_Idhar_Shafawe(self):
        FindIdhar_Shafawe = []
        ahkam_meem = []
        for i, char in enumerate(aya):
            if char == ar.MEEM and i + 1 < len(aya) and aya[i + 1] == ar.SUKUN:
                FindIdhar_Shafawe.append(i)

        for f in FindIdhar_Shafawe:
            if ((f + 1 < len(aya) and aya[f + 1] != ' ' and aya[f + 1] != ar.MEEM and aya[f + 1] != ar.BEH) or
                    (f + 1 < len(aya) and aya[f + 1] == ' ' and f + 2 < len(aya) and aya[f + 2] != ar.MEEM and aya[
                        f + 1] != ar.BEH)):
                self.declare(Idhar_Shafawe(a='True'))
                ahkam_meem.append(f' {aya[f - 2:f + 2]}')

        if (len(ahkam_meem) > 0):
            Alahkam['حكم الميم الساكنة(الاظهار الشفوي) في المواضع'] = ahkam_meem

    @Rule()
    def Find_Ikhfaa_Shafawe(self):
        FindIkhfaa_Shafawe = []
        ahkam_meem = []
        for i, char in enumerate(aya):
            if (char == ar.MEEM and not ar.is_haraka(aya[i + 1]) and not ar.is_shadda(aya[i + 1])):
                FindIkhfaa_Shafawe.append(i)

        for f in FindIkhfaa_Shafawe:
            if ((f + 1 < len(aya) and aya[f + 1] == ar.BEH) or (f + 1 < len(aya) and aya[f + 1] == ' ' and aya[f + 2] == ar.BEH)):
                self.declare(Ikhfaa_Shafawe(a='True'))
                ahkam_meem.append(f'{aya[f:f + 3]}')

        if (len(ahkam_meem) > 0):
            Alahkam['حكم الميم الساكنة(الاخفاء الشفوي) في المواضع'] = ahkam_meem

    @Rule()
    def Find_Idgham_Meem(self):
        FindIdgham_Meem = []
        ahkam_meem = []
        for i, char in enumerate(aya):
            if (char == ar.MEEM and not ar.is_haraka(aya[i + 1]) and not ar.is_shadda(aya[i + 1])):
                FindIdgham_Meem.append(i)

        for f in FindIdgham_Meem:
            if f + 1 < len(aya) and aya[f + 1] == ' ' and aya[f + 2] == ar.MEEM and aya[f + 3] == ar.SHADDA:
                self.declare(Idgham_Meem(a='True'))
                ahkam_meem.append(f'{aya[f:f + 4]}')

        if (len(ahkam_meem) > 0):
            Alahkam['حكم الميم الساكنة(الادغام) في المواضع'] = ahkam_meem

    # أحكام القلقة الصغرى والوسطى والكبرى:
    @Rule()
    def Find_Kalkla(self):
        list = aya.split(' ')
        Kalkla_Kobra = []
        Kalkla_Wosta = []
        Kalkla_Soghra = []

        for i, char in enumerate(aya):
            if ((char == ar.QAF or char == ar.TAH or char == ar.BEH or char == ar.JEEM or char == ar.DAL) and
                    aya[i + 1] == ar.SUKUN):
                self.declare(Kalkla(a='True'))
                Kalkla_Soghra.append(f'{aya[i - 3:i + 2]}')

        for val in list:
            if len(val) - 3 >=0:
                if ((val[len(val) - 3] == ar.QAF or val[len(val) - 3] == ar.TAH or val[len(val) - 3] == ar.BEH or val[
                    len(val) - 3] == ar.JEEM or val[len(val) - 3] == ar.DAL) and val[len(val) - 2] == ar.SHADDA):

                    if val[len(val) - 2] == ar.SHADDA:
                        self.declare(Kalkla(a='True'))
                        Kalkla_Kobra.append(f'{val[len(val) - 5:]}')

                if ((val[len(val) - 2] == ar.QAF or val[len(val) - 2] == ar.TAH or val[len(val) - 2] == ar.BEH or val[
                    len(val) - 2] == ar.JEEM or val[len(val) - 2] == ar.DAL) and val[len(val) - 1] != ar.SHADDA):
                    self.declare(Kalkla(a='True'))
                    Kalkla_Wosta.append(f'{val[len(val) - 3:]}')



        if len(Kalkla_Kobra) > 0:
            Alahkam['حكم قلقلة كبرى في المواضع'] = Kalkla_Kobra

        if len(Kalkla_Wosta) > 0:
            Alahkam['حكم قلقلة وسطى في المواضع'] = Kalkla_Wosta

        if len(Kalkla_Soghra) > 0:
            Alahkam['حكم قلقلة صغرى في المواضع'] = Kalkla_Soghra

    # أحكام اللام المفخمة والمرققة:
    @Rule()
    def Find_Laam_Mofaghama_and_Moraqqa(self):
        list = aya.split(' ')
        Laam_Mofaghama = []
        Laam_Moraqaqa = []

        for i, char in enumerate(list):  # اللام المفخمة
            if char == 'اللَّهِ' or char == 'اللَّهَ' or char == 'اللَّهُ':  # لفظ الجلالة
                if i - 1 >= 0:
                    word = list[i - 1]
                    if word[len(word) - 1] == ar.FATHA or word[len(word) - 1] == ar.DAMMA:
                        self.declare(Laam(a='True'))
                        Laam_Mofaghama.append(f'{aya[i - 3:i + 11]}')
            else:

                if ar.LAM in char:
                    self.declare(Laam(a='True'))
                    Laam_Moraqaqa.append(char)

        if len(Laam_Mofaghama) > 0:
            Alahkam['حكم لام مفخمة في المواضع'] = Laam_Mofaghama

        # if len(Laam_Moraqaqa) > 0:
        #     Alahkam['حكم لام مرققة في المواضع'] = Laam_Moraqaqa

    # أحكام الراء المفخمة والمرققة:
    @Rule()
    def Find_Raa_Mofaghama_and_Moraqqa(self):
        Raa_Mofaghama = []
        Raa_Moraqaqa = []

        for i, char in enumerate(aya):
            if char == ar.REH:

                if i + 1 < len(aya) and ((aya[i + 1] == ar.FATHA and aya[i + 1] == ar.DAMMA) or (
                        aya[i + 1] == ar.SUKUN and (aya[i - 1] == ar.FATHA or aya[i - 1] == ar.DAMMA))):  # مفخمة

                    self.declare(Raa(a='True'))
                    Raa_Mofaghama.append(f'{aya[i - 2:i + 2]}')

                if i + 1 < len(aya) and ((aya[i + 1] == ar.KASRA) or (
                        aya[i + 1] == ar.SUKUN and aya[i - 1] == ar.KASRA or aya[i - 1] == ar.YEH)):  # مرققة

                    self.declare(Raa(a='True'))
                    Raa_Moraqaqa.append(f'{aya[i - 3:i + 3]}')

        if len(Raa_Mofaghama) > 0:
            Alahkam['حكم راء مفخمة في المواضع'] = Raa_Mofaghama

        if len(Raa_Moraqaqa) > 0:
            Alahkam['حكم راء مرققة في المواضع'] = Raa_Moraqaqa




