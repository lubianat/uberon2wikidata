# Workflow for connecting GAZ to Wikidata


1 - Load UBERON ontology and clean it up with the `get_obo_entities.sh` script

Notice that UBERON ids on Wikidata are numerical only. (https://www.wikidata.org/wiki/Property:P1554)

2 - Select a term present on description to subset the table, to limit curation to a subset of interest

3 - Run `extract_and_parse_subset.py`. 

The script will subset the table and find Wikidata matches. You can improve the matches found automatically by excluding types (P31 values of wrong matches) or fixing a type (P31 value mandatory for all matches).

4 - Check the generated curation_sheet.csv on a spreadsheet editor (e.g. Excel, LibreOffice Calc, Google Sheets). 

If the automatic results are worse then expected, run `extract_and_parse_subset.py` with different parameters.

Do this until you are satisfied with the result.

Change the `wikidata_id` value of the wrong matches either to the right id or to "NONE" to skip the field.

Watchout when opening/saving the spreadsheet! Leading 0s might be eliminated, causing issues later, as they are part of the id. In Libre Office Calc, for example, you have to change the column type from "Standard" to "Text". 


5 - Run `generate_quickstatements.py` to go to Quickstatements and add the matched ids to Wikidata. 