paraBench is a benchmark dataset and script to assess the quality of orthologous groups.

See REFERENCE for more details.

## 1. run your orthology pipeline
You need first to run your orthology pipeline using the 17 proteomes available in the 4 files `proteomes__X-4.zip`located in the `data` folder.

These proteomes files come from the <a href="http://www.ebi.ac.uk/reference_proteomes/">Quest for Orthologs 2019 dataset</a>, with simplified sequence names to ensure that the correct names are present in the output of your orthology pipeline.


## 2. test your orthologous groups
Run the script `paraBench.py` (it only requieres Python 3+) by specifying the file containing the clustering you want to test (`my_clustering.txt` in the example below):
```
python paraBench.py my_clustering.txt
```
**IMPORTANT**: the file `reference_classification.txt` should be in the same directory as the script `paraBench.py`.

The script will output the number of True Positives (TP), False Positives (FP) and False Negatives (FN), as well as the metrics recall, precision and F1-score.

The format of your input clustering should be as follows:
- with or without header lines (lines starting by '#' are considered headers and are ignored)
- each line corresponds to an orthologous group (the lines can start with the name of the orthologous groups, or not), with protein names separated by spaces, tabs, comas or comas + spaces

You can give it a try with any of the precomputed outputs present in the directory `some_results`. For instance:
```
python paraBench.py ./some_results/result_Broccoli_1.0_default.txt
```
The output for this file should be:
```
        -- paraBench --


 read the reference classication
 read the input classication


 RESULTS:

 TP = 18886
 FP = 482
 FN = 3018
 precision = 0.97511
 recall    = 0.86222
 F1-score  = 0.91867
 ```
