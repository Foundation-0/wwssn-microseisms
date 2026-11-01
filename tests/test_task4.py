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

    def test_missing_values_are_logged(self):
        a=[dict(date=str(i),amplitude=i) for i in range(4)]+[dict(date='4',amplitude=None),dict(date='5',amplitude='')]
        b=[dict(date=str(i),swell=i) for i in range(6)];b[2]=dict(date='2',swell=None)
        out=m['correlate'](a,b)
        self.assertEqual(out['n'],3)
        reasons={(e['date'],e['series']):e['reason'] for e in out['exclusion_log']}
        self.assertEqual(reasons[('4','amplitude')],'non-finite amplitude')
        self.assertEqual(reasons[('5','amplitude')],'non-finite amplitude')
        self.assertEqual(reasons[('2','swell')],'non-finite swell')
    def test_errors_carry_exclusion_log(self):
        a=[dict(date=str(i),amplitude=i) for i in range(3)];b=[dict(date=str(i),swell=i) for i in (0,1,7)]
        with self.assertRaises(ValueError) as c:m['correlate'](a,b)
        self.assertIn(dict(date='2',series='amplitude',reason='no swell for day'),c.exception.exclusion_log)
        self.assertIn(dict(date='7',series='swell',reason='no amplitude for day'),c.exception.exclusion_log)
        with self.assertRaises(ValueError) as c:m['correlate'](a+a[:1],[dict(x,swell=x['amplitude']) for x in a])
        self.assertEqual(c.exception.exclusion_log,[dict(date='0',series='amplitude',reason='duplicate day')])

if __name__=="__main__":unittest.main()
