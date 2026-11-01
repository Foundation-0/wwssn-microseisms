import unittest,runpy,pathlib,tempfile,datetime,csv,json
ROOT=pathlib.Path(__file__).resolve().parents[1]
m=runpy.run_path(str(ROOT/'tools/inventory.py'))
class OfflineTests(unittest.TestCase):
    def test_behaviour(self):
        a=dict(station='ALQ',date='1964-02-29',scan_id='one')
        rows,q=m['inventory']([a,a,dict(a,scan_id='two')])
        self.assertEqual(q,[]);self.assertEqual(rows[0]['scan_count'],2);self.assertEqual(rows[0]['days_with_records'],1)
        with self.assertRaises(ValueError):m['inventory']([a,dict(a,date='1964-02-28')])
    def test_quarantine_bad_rows(self):
        good=dict(station='ALQ',date='1964-02-29',scan_id='one')
        rows,q=m['inventory']([good,dict(wrong='header'),dict(good,date='not-a-date'),dict(good,station='')])
        self.assertEqual(len(rows),1);self.assertEqual(rows[0]['scan_count'],1)
        self.assertEqual(len(q),3)
        self.assertIn('missing field',q[0]['reason']);self.assertIn('date',q[0]['reason'])
        self.assertIn('invalid date',q[1]['reason'])
        self.assertEqual(q[2]['reason'],'empty station or scan_id')
    def test_cli_quarantine_in_output(self):
        with tempfile.TemporaryDirectory() as d:
            listing=pathlib.Path(d)/'listing.csv';out=pathlib.Path(d)/'out.json'
            listing.write_text('station,date,scan_id\nALQ,1964-02-29,one\n,bad\n')
            import subprocess,sys
            subprocess.check_call([sys.executable,str(ROOT/'tools/inventory.py'),str(listing),str(out)])
            payload=json.loads(out.read_text())
            self.assertEqual(len(payload['station_months']),1)
            self.assertEqual(len(payload['quarantine']),1)
            self.assertIn('invalid date',payload['quarantine'][0]['reason'])

if __name__=="__main__":unittest.main()
