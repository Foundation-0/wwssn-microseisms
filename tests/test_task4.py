import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/correlate.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):

        a=[dict(date=str(i),amplitude=i) for i in range(3)];b=[dict(date=str(i),swell=i*2) for i in range(3)]
        self.assertAlmostEqual(m['correlate'](a,b)['pearson_r'],1)
        self.assertAlmostEqual(m['correlate'](a,[dict(x,swell=-x['swell']) for x in b])['pearson_r'],-1)
        with self.assertRaises(ValueError):m['correlate'](a+a,b)
        with self.assertRaises(ValueError):m['correlate'](a,[dict(x,swell=1) for x in b])

if __name__=="__main__":unittest.main()
