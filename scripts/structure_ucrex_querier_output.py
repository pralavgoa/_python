import sys
import re

filename =  sys.argv[1]

with open(filename,"r") as oFile:
   data=oFile.read()

query_result_matcher=re.compile(r"(\.\/.+?\.)\n\n", re.DOTALL)

data

for query_match in query_result_matcher.finditer(data):
   query_result  = query_match.groups()
   query_parts_matcher = re.compile(r"(.+?)\n",re.DOTALL)
   query_result_csv = ""
   comma = ""
   for query_part_match in query_parts_matcher.finditer(query_result[0]):
      query_part = query_part_match.groups()
      query_result_csv +=  comma +  query_part[0]
      comma = ","
   print query_result_csv

