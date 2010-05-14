"""
spidr_api.py

The core SPIDR Python API module
"""


import csv
from urllib import urlopen

_SPIDR = 'http://spidr.ngdc.noaa.gov'
_SPIDR_DATA_PREFIX     = _SPIDR + '/spidr/servlet/GetData?format=csv&'
_SPIDR_METADATA_PREFIX = _SPIDR + '/spidr/servlet/GetMetadata?'


#------------------------------------------------------------------------
# 
# Get CSV data from SPIDR, return a dict with header and data separated
#
#------------------------------------------------------------------------
def get_data(param,begin,end):
	
	try:
		url = _SPIDR_DATA_PREFIX + 'param=' + param + '&dateFrom=' + begin + '&dateTo=' + end
		csvdata = urlopen(url)
		
		header = []
		data = {}
		for row in csv.reader(csvdata):
			if ('#' in row):
				header.append(row)
			else:
				if (len(row) == 4):
					data[row[0]] = row[1]
	
		result = {}
		result['header'] = header
		result['data'] = data
		return result
	
	except IOError, ioe:
		raise Usage("ERROR")


#------------------------------------------------------------------------
# 
# Get XML metadata from SPIDR, return a single string for the doc obtained
#
#------------------------------------------------------------------------
def get_metadata(param):
	
	try:
		url = _SPIDR_METADATA_PREFIX + 'param=' + param
		xmldata = urlopen(url)
		
		xml = ''
		for row in xmldata:
			xml += row
		return xml

	except IOError, ioe:
		raise Usage("ERROR")
		
class Usage(Exception): 
	def __init__(self, msg):
		self.msg = msg