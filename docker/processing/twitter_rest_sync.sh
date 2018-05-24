#!/bin/bash

set -e 
set -o pipefail

echo "Starting export $1 to $2 (`date`)"
cd $2
find_warcs.py $1 | tr ' ' '\n' > source.lst
cat source.lst | xargs basename -a | sed 's/.warc.gz/.json.gz/' > dest_json.lst
cat source.lst | xargs basename -a | sed 's/.warc.gz/.tweet_id.txt/' > dest_txt.lst
export SHELL=/bin/bash
parallel -j $3 -a source.lst -a dest_json.lst -a dest_txt.lst --xapply "[ -f {2} ] || twitter_rest_warc_iter.py {1} | tee >(gzip > {2}) | jq -r '.id_str' > {3}"
echo "Done export $1 to $2 (`date`)"
