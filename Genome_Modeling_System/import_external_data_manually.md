### Importing External Data with or without Analysis Project

*If you only have a few samples for import, you can use this protocol to manually import your samples. If you have over 3 samples, we recommend using the automated protocol found here: [Import External Data - Automated](./import_external_data_automated)*

First, you will need to create an individual:

```
genome individual create --taxon "human" --name=$NAME
```

Next, you will need to create samples:

```
genome sample create --description=DESC --name=NAME --source=INDIVIDUAL_ID
```

You can verify that the sample was linked correctly with:

```
genome sample list --filter individual.id=INDIVIDUAL_ID

or

genome sample list --filter individual.name=INDIVIDUAL_NAME
```

Next, you will will need to create libraries for each sample:

```
genome library create --sample=SAMPLE_NAME --name=LIBRARY_NAME
```
***IF YOU HAVE MORE THAN 2 FASTQ.GZ Files, you will need to consolidate them into two final fastq.gz files. GMS looks for 2 fastq files, forward (R1) and Reverse (R2). If you ingest more, your pipeline will fail!!!***

```cat *R1* > Sample_HG001_all_R1.fastq.gz``` and ```cat *R2* > Sample_HG001_all_R2.fastq.gz```

Finally, you can import your data:

*If you want your data added to your analysis-project, you will need to use the `--analysis-project` parameter shown below. If you want to import without an attached analysis-project, omit the `--analysis-project` parameter.
```
genome instrument-data import trusted-data --analysis-project=PROJECT_NAME --import-source-name=SOURCE_NAME --library=LIBRARY_NAME --source-directory=PATH --import-format=FORMAT --read-count=COUNT
```

Specific Example:

```
genome instrument-data import trusted-data --analysis-project=chiari_GATK4_exome_test import-source-name=https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data_indexes/NA12878/sequence.index.NA12878_Illumina_HiSeq_Exome_Garvan_fastq_09252015 --library=NA12878-HG001-extlibs --source-directory=/gscmnt/gc2698/jin810/fastq/benchmark/NA12878 —import-format=fastq —read-count=20203002
```

The read-count can be determined by running 

```
zcat reads.fastq.gz | wc -l
```

for each read, dividing the outputs by 4, and then summing.

The source-directory should only contain your read files. The import will copy all data in the source directory, even if there are unrelated files in the directory.
