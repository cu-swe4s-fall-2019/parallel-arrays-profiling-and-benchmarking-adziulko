# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

## File Instruction

To run linear search follow the example below in command line:
```
$ python plot_gtex.linear py --fngr GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --fna GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --t SMTS --tg ACTA2 --bfn test2.png
```
to run binary search follow the example below in command line:
```
$ python plot_gtex_binary.py --fngr GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --fna GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --t SMTS --tg ACTA2 --bfn test2.png
```

--fngr = Input RNA Seq gene read file (gziped)

--fna = file_name_annotations

--t = Input either tissue group (SMTS) or tissue type (SMTSD)

--tg = Input target gene

--bfn = Name of output boxplot file
