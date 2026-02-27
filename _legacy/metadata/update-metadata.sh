#!/bin/bash

mkdir -p translations

# First we download the current status of languages and the relevant statistics for Scripted Speech
# From there we extract the list of enabled (is_contributable == 1) languages.
pushd scs;
curl https://commonvoice.mozilla.org/api/v1/languages > languages.json;
curl https://commonvoice.mozilla.org/api/v1/stats/languages > statistics.json;
python3 extract-contributable.py languages.json > enabled.tsv;
popd


# Then we download the relevant information for Spontaneous Speech
# We have to download three separate files in order to be able to retrieve information 
# about both total recorded audio, and validated transcriptions.
pushd sps;
# TODO: work out which of those cookie bits are mandatory
curl 'https://commonvoice.mozilla.org/spontaneous-speech/beta/api/v1/statistics/audios'  -H 'Cookie: _ga_B9CY1C9VBC=GS2.1.s1752591552$o3$g0$t1752591555$j57$l0$h0; _ga=GA1.1.2004040008.1750248496; fundraiseup_cid=17504270499412122967; _ga_2VC139B3XV=GS2.1.s1752841046$o1$g0$t1752841046$j60$l0$h0; fundraiseup_stat=1; fundraiseup_func={%22t%22:%22.mozilla.org%22%2C%22s%22:%221755179258159%22%2C%22sp%22:15}; connect.sid=s%3AFF9NIl8Rl-g_i3s9vlcBVIqER6Z66c-3.GYQ%2FD9%2Fq%2BTlLDmm1VGbMcmhw3nhxAyvvJuL%2BpaVX%2FVw; mcv_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2NvbW1vbnZvaWNlLm1vemlsbGEub3JnIiwiYXVkIjoiaHR0cHM6Ly9jb21tb252b2ljZS5tb3ppbGxhLm9yZyIsInN1YiI6IjkxZTJlZWY5LTc3MzYtNDk5ZC1iZmMzLTY3YWJjN2MwNzU0YyIsImFub255bW91cyI6ZmFsc2UsImlhdCI6MTc1NTg3MzAwOH0.TcOCDtzDlmj0aEoqPX50JRjSNe-PIPOfWIB5p8UUXjk' > audios.json

curl 'https://commonvoice.mozilla.org/spontaneous-speech/beta/api/v1/statistics/transcriptions'  -H 'Cookie: _ga_B9CY1C9VBC=GS2.1.s1752591552$o3$g0$t1752591555$j57$l0$h0; _ga=GA1.1.2004040008.1750248496; fundraiseup_cid=17504270499412122967; _ga_2VC139B3XV=GS2.1.s1752841046$o1$g0$t1752841046$j60$l0$h0; fundraiseup_stat=1; fundraiseup_func={%22t%22:%22.mozilla.org%22%2C%22s%22:%221755179258159%22%2C%22sp%22:15}; connect.sid=s%3AFF9NIl8Rl-g_i3s9vlcBVIqER6Z66c-3.GYQ%2FD9%2Fq%2BTlLDmm1VGbMcmhw3nhxAyvvJuL%2BpaVX%2FVw; mcv_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2NvbW1vbnZvaWNlLm1vemlsbGEub3JnIiwiYXVkIjoiaHR0cHM6Ly9jb21tb252b2ljZS5tb3ppbGxhLm9yZyIsInN1YiI6IjkxZTJlZWY5LTc3MzYtNDk5ZC1iZmMzLTY3YWJjN2MwNzU0YyIsImFub255bW91cyI6ZmFsc2UsImlhdCI6MTc1NTg3MzAwOH0.TcOCDtzDlmj0aEoqPX50JRjSNe-PIPOfWIB5p8UUXjk' > transcriptions.json

curl 'https://commonvoice.mozilla.org/spontaneous-speech/beta/api/v1/statistics/validated-transcriptions'  -H 'Cookie: _ga_B9CY1C9VBC=GS2.1.s1752591552$o3$g0$t1752591555$j57$l0$h0; _ga=GA1.1.2004040008.1750248496; fundraiseup_cid=17504270499412122967; _ga_2VC139B3XV=GS2.1.s1752841046$o1$g0$t1752841046$j60$l0$h0; fundraiseup_stat=1; fundraiseup_func={%22t%22:%22.mozilla.org%22%2C%22s%22:%221755179258159%22%2C%22sp%22:15}; connect.sid=s%3AFF9NIl8Rl-g_i3s9vlcBVIqER6Z66c-3.GYQ%2FD9%2Fq%2BTlLDmm1VGbMcmhw3nhxAyvvJuL%2BpaVX%2FVw; mcv_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2NvbW1vbnZvaWNlLm1vemlsbGEub3JnIiwiYXVkIjoiaHR0cHM6Ly9jb21tb252b2ljZS5tb3ppbGxhLm9yZyIsInN1YiI6IjkxZTJlZWY5LTc3MzYtNDk5ZC1iZmMzLTY3YWJjN2MwNzU0YyIsImFub255bW91cyI6ZmFsc2UsImlhdCI6MTc1NTg3MzAwOH0.TcOCDtzDlmj0aEoqPX50JRjSNe-PIPOfWIB5p8UUXjk' > validated-transcriptions.json

python3 extract-contributable.py audios.json > enabled.tsv
popd

# The language names in English and in the language itself are distributed in different places,
# so in order to get the translations, we need to download the localisation files, but we only
# want to do this once, so if we already have a complete set then we skip this step.
# NOTE: These should be redownloaded whenever Pontoon translations are changed.
n_enabled=$(cat sps/enabled.tsv scs/enabled.tsv | cut -f1 | sort -u | wc -l)
n_downloaded_ftl=$(ls translations | wc -l)

if [[ ${n_downloaded_ftl} != ${n_enabled} ]]; then
	for locale in $(cat */enabled.tsv | cut -f1 | sort -u); do 
		curl https://commonvoice.mozilla.org/api/v1/languages/${locale}/translations > translations/${locale}.ftl;
	done
fi

# Finally we generate the final metadata with the following columns:
# modality	code	native_name	english_name	speakers	hours_recorded	hours_validated
# Empty name fields are marked with underscore.

python3 generate-metadata.py > metadata.tsv
