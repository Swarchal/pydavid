pydavid
=======

Simple python package to get pandas DataFrames from DAVID queries.

-------------

More info and limitations of the DAVID API see
[here](https://david.ncifcrf.gov/content.jsp?file=DAVID_API.html).


## Example

```python
id_type = "ENTREZ_GENE_ID"
ids = ["2919", "6347", "6348", "6364"]
tool = "chartReport"
annot = ["GOTERM_BP_FAT", "GOTERM_MF_FAT", "INTERPRO"]

get_table(id_type=id_type,
          ids=ids,
          tool=tool,
          annot=annot)
```

```
Category                                             Term  Count  \
0       INTERPRO    IPR001811:Chemokine interleukin-8-like domain      4   
1  GOTERM_MF_FAT                    GO:0008009~chemokine activity      4   
2  GOTERM_MF_FAT            GO:0042379~chemokine receptor binding      4   
3  GOTERM_BP_FAT  GO:0070098~chemokine-mediated signaling pathway      4   
4  GOTERM_BP_FAT                 GO:0030593~neutrophil chemotaxis      4   

       %        PValue                   Genes  List Total  Pop Hits  \
0  100.0  1.425048e-08  6364, 2919, 6347, 6348           4        46   
1  100.0  2.981775e-08  6364, 2919, 6347, 6348           4        49   
2  100.0  6.426903e-08  6364, 2919, 6347, 6348           4        63   
3  100.0  1.151395e-07  6364, 2919, 6347, 6348           4        82   
4  100.0  1.238816e-07  6364, 2919, 6347, 6348           4        84   

   Pop Total  Fold Enrichment    Bonferroni     Benjamini       FDR  
0      18559       403.456522  4.275144e-08  4.275144e-08  0.000004  
1      15478       315.877551  9.541675e-07  9.541675e-07  0.000026  
2      15478       245.682540  2.056607e-06  1.028304e-06  0.000056  
3      16650       203.048780  7.691024e-05  7.691024e-05  0.000173  
4      16650       198.214286  8.274948e-05  4.137560e-05  0.000186  
...
```
