import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/correlate.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):
        a=[dict(date=str(i),amplitude=i) for i in range(3)];b=[dict(date=str(i),swell=i*2) for i in range(3)]
        self.assertAlmostEqual(m['correlate'](a,b)['pearson_r'],1)
        self.assertEqual(m['correlate'](a,b)['exclusion_log'],[])
        self.assertAlmostEqual(m['correlate'](a,[dict(x,swell=-x['swell']) for x in b])['pearson_r'],-1)
        with self.assertRaises(ValueError):m['correlate'](a+a,b)
        with self.assertRaises(ValueError):m['correlate'](a,[dict(x,swell=1) for x in b])
    def test_exclusion_log_unpaired_days(self):
        a=[dict(date=str(i),amplitude=i) for i in (0,1,2,3,4)]
        b=[dict(date=str(i),swell=i) for i in (0,2,3,5,6)]
        out=m['correlate'](a,b)
        self.assertEqual(out['n'],3);self.assertAlmostEqual(out['pearson_r'],1)
        by_date={e['date']:e for e in out['exclusion_log']}
        self.assertEqual(by_date['1'],dict(date='1',series='amplitude',reason='no swell for day'))
        self.assertEqual(by_date['4'],dict(date='4',series='amplitude',reason='no swell for day'))
        self.assertEqual(by_date['5'],dict(date='5',series='swell',reason='no amplitude for day'))
        self.assertEqual(by_date['6'],dict(date='6',series='swell',reason='no amplitude for day'))

if __name__=="__main__":unittest.main()
