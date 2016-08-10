import csv
import pprint

from django.db import IntegrityError

from .codes import CODES
from .models import RHC


def import_codes_from_csv(path):
    codes = []
    with open(path, 'rU') as f:
        reader = csv.reader(f)
        township_code = 0
        for row in reader:
            i = 0
            for code, title in zip(row[0::2], row[1::2]):
                i += 1
                if code and title:
                    code = int(code)
                    if i == 1:
                        codes.append([(code, title), []])
                    elif i == 2:
                        codes[-1][-1].append([(code, title), []])
                    elif i == 3:
                        township_code += 1
                        codes[-1][-1][-1][-1].append((township_code, code, title))
    pprint.pprint(codes)

def import_RHC_from_csv(path):

    RHC.objects.all().delete()
    with open(path, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            (ST_DV, DIS, TWN, RHC_code, Village) = row
            if int(RHC_code)*int(ST_DV)*int(TWN)*int(DIS) > 0:
                try:
                    ST_DV_index = int(ST_DV)-1
                    diss = map(lambda a: a[0][0], CODES[ST_DV_index][1])
                    DIS_index = diss.index(int(DIS))
                    twn = dict((number, code) for code,number,name in CODES[ST_DV_index][1][DIS_index][1])
                    TWN = twn[int(TWN)]
                    rhc = RHC.objects.create(ST_DV=ST_DV, DIS=DIS, TWN=TWN, RHC=RHC_code, Village=Village)
                    rhc.save()
                except IndexError:
                    print twn
                    print (ST_DV, DIS, TWN, RHC_code, "Index!")
                    pass
                except IntegrityError:
                    print (ST_DV, DIS, TWN, RHC_code, "Duplicate!")
                    pass


