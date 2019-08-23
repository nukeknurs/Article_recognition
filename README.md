# QARwD - Quick Article Recognition with DOI
Can find anything about any given article in PDF format **if only** it has DOI inside. How it works?

This particular script:
1. Changes names of PDF files in the folder.
2. Creates:
    - `Archive` folder with original-name-files.
    - `Dictionary.txt` file.
    - `PeDeFy.log` wchich is just output-log-file.

Usage
====
Allrighty, first of all **remove `Archive` folder as well as `*.log` and `*.txt` files.**

Then rename all PDF-files in the folder to `test`. Select them, press `F2`, type `test` and press `Enter`. 

Here, I got you homie.

![img](https://i.imgur.com/y9ggmdw.gif)

Everything is setup now so...It's Python3, just run it! ~~I have to get some life, gosh~~.

If sth is missing use `pip` or `conda` to install missing packages (depends on what you use) and you should be just fine. For example:

```python
pip install pdfminder.six
```
or
```python
conda install -c conda-forge pdfminer.six
```

Oh yeah, that was made with use of `pdfminder.six`. Any other PDFminer probably won't work.

How it should look like when you use it on `test` files 💻
====

![img](https://i.imgur.com/9GW71qh.gif)

If everything is fine `Dictionary.txt` should look like this:
```
test (1).pdf 	 =-> 	 Sophia E. Whitlock - Environmentally relevant exposure to an antidepressant alters courtship behaviours in a songbird, Elsevier BV, 11_2018.pdf  10.1016/j.chemosphere.2018.07.074
test (2).pdf 	 =-> 	 A. Al-Mohamadi - Dispensing medications without prescription at Saudi community pharmacy: Extent and perception, Elsevier BV, 1_2013.pdf  10.1016/j.jsps.2011.11.003
test (3).pdf 	 =-> 	 Ahmed Alahmari - Colonic atresia associated with imperforate anus in a patient with down syndrome, expect the unexpected, Elsevier BV, 8_2018.pdf  10.1016/j.epsc.2018.06.002 
test (4).pdf 	 =-> 	 Edna Nahon - Fluoxetine (Prozac) interaction with the mitochondrial voltage-dependent anion channel and protection against apoptotic cell death, Wiley, 9_2005.pdf  10.1016/j.febslet.2005.08.020
test (5).pdf 	 =-> 	 Francesco Buda - Introduction to theory/modeling methods in photosynthesis, Springer Nature, 12_2009.pdf  10.1007/s11120-009-9476-5
test (6).pdf 	 =-> 	 Hsiang-Ling Huang - Antidepressant-like effects of Gan-Mai-Dazao-Tang via monoamine regulatory pathways on forced swimming test in rats, Elsevier BV, 1_2018.pdf  10.1016/j.jtcme.2017.01.007
test (7).pdf 	 =-> 	 Sophia E. Whitlock - Detecting fluoxetine and norfluoxetine in wild bird tissues and feathers, Elsevier BV, 5_2019.pdf  10.1016/j.envint.2019.01.083
```
and `PeDeFy.log` exactly like things on the gif above.
