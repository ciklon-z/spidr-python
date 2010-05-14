"""
A small sample program which shows how to use the SPIDR Python API

spidr-python.py

	required arguments:
		none
		
	optional arguments:
		none
	
	example:
		spidr-python.py
"""


import sys, getopt, spidr_api


def xml_metadata_example():
	
	try:
		xmlmeta = spidr_api.get_metadata('iono.BC840')
		print xmlmeta
	
	except IOError, ioe:
		raise Usage("ERROR")


def csv_data_example():
	
	try:
		csvdata = spidr_api.get_data('iono_fof2.bc840','20100101','20100102')
		
		data = csvdata['data']
		for time, datapnt in data.items():
			print time + ': ' + datapnt
	
	except IOError, ioe:
		raise Usage("ERROR")


def examples():
	csv_data_example()
	xml_metadata_example()


class Usage(Exception): 
	def __init__(self, msg):
		self.msg = msg


def main(argv=None):
	
	if argv is None:
		argv = sys.argv
	
	if len(argv) != 1:
		print >>sys.stderr, "ERROR: arguments given when none were expected"
		print >>sys.stderr, __doc__
		return 2
	
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
			
		except getopt.error, msg:
			 raise Usage(msg)
			
		for o, a in opts:
			if o in ("-h", "--help"):
				print >>sys.stderr, __doc__
				sys.exit(0)

		examples()
			
	except Usage, err:
		print >>sys.stderr, "\n>>> ERROR <<<"
		print >>sys.stderr, err.msg
		print >>sys.stderr, __doc__
		return 2
	
if __name__ == "__main__":
	sys.exit(main())
