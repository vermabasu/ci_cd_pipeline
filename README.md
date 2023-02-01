steps: 
1  Install all the requirements (dvc, dvc[gdrive], sklearn)
```bash
pip install -r requirments.txt
```
2  Create the template.

3  Upload the data 

4  Inititalize git
```bash
git init
```
5  Initialize dvc
```bash
dvc init
```
6  add data to dvc
```bash
dvc add data_given/winequality.csv\
```

7  Push everything to git
```bash
git add .
git commit -m "first commit"
git remote add origin https://github.com/vermabasu/dvc_learning.git
git branch -M main
git push origin main
```
8  Fill the params.yaml file (this contains all the parmaters of training and path for the csv file).
