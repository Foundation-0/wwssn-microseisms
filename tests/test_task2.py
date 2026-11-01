import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/coverage.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):

        start=datetime.date(1963,1,1);days=[str(start+datetime.timedelta(days=i)) for i in range(1096)]
        self.assertTrue(m['assess'](days,1963)['eligible'])
        self.assertEqual(m['assess'](days,1963)['days_expected'],1096)
        self.assertFalse(m['assess'](days[8:],1963)['eligible'])

if __name__=="__main__":unittest.main()
