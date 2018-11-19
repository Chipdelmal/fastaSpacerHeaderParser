

Creating the environment:

```bash
conda create --name fastaParser
```

Installing the environment as jupyter kernel:

```bash
source activate fastaParser
python -m ipykernel install --user --name fastaParser --display-name "fastaParser"
```

Exporting the environment to YML file:

```bash
conda env create -f fastaParser.yml
```
