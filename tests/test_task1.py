import unittest,runpy,pathlib,tempfile,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/inventory.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):

        a=dict(station='ALQ',date='1964-02-29',scan_id='one')
        r=m['inventory']([a,a,dict(a,scan_id='two')])
        self.assertEqual(r[0]['scan_count'],2);self.assertEqual(r[0]['days_with_records'],1)
        with self.assertRaises(ValueError):m['inventory']([a,dict(a,date='1964-02-28')])

if __name__=="__main__":unittest.main()
