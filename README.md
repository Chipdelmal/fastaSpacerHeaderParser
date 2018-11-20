# Fasta "Spacer" Parser


## Instructions

Having python 3.7 installed, move to the folder containing the scripts definition.
Once there, the code can be run either with the "main.py" routine by changing the work paths, or it can be called directly from the terminal with the following command:

```bash
python fastaParser.py "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Data/" "/Users/sanchez.hmsc/Documents/GitHub/fastaSpacerHeaderParser/Out/"
```

Where the first argument is the folder where the data is stored, and the second folder is the path where the concatenated files will be saved.

## Specifications

Merge:
* __MN184_CRISPR3spacer.fa__
* __MN184_CRISPR4spacer.fa__

into __MN184_CRISPRspacer.fa__
with sequence names changed from:

```
\>spacer1
\>spacer2
......
```

into:

```
\>spacer1_MN184CRISPR3
\>spacer2_MN184CRISPR4
```

for the __MN184___ example.

## Author

[PhD Héctor Manuel Sánchez Castellanos](http://chipdelmal.github.io)
