# Aspect-Based Sentiment Classification 😍

## Abstract
<b>
Aspect-based sentiment classification (ABSC) aims to predict sentiment polarities of
different aspects within sentences or documents. Many previous studies have been conducted
to solve this problem, but previous works fail to notice the correlation between the aspect’s sentiment
polarity and the local context. In this paper, a Local Context Focus (LCF) mechanism is proposed for
aspect-based sentiment classification based on Multi-head Self-Attention (MHSA). This mechanism is
called LCF design, and utilizes the Context features Dynamic Mask (CDM) and Context Features
Dynamic Weighted (CDW) layers to pay more attention to the local context words. Moreover,
a BERT-shared layer is adopted to LCF design to capture internal long-term dependencies of local
context and global context. Experiments are conducted on three common ABSC datasets: the
laptop and restaurant datasets of SemEval-2014 and the ACL twitter dataset. Experimental results
demonstrate that the LCF baseline model achieves considerable performance. In addition, we
conduct ablation experiments to prove the significance and effectiveness of LCF design. Especially,
by incorporating with BERT-shared layer, the LCF-BERT model refreshes state-of-the-art performance
on all three benchmark datasets.
</b><br>
Keywords: aspect-level sentiment classification; local context focus; self-attention; pretrained BERT <br>

## Objectives
The aim of project is to predict polarity of available aspects in text from trained data.<br><br>

## Dataset
We used Public & Community-shared datasets for Aspect-based sentiment analysis and Text Classification.

- [datasets](https://github.com/yangheng95/ABSADatasets)


## Page
<img src = "image\Home.png" width = "700px">

<br><br>

## 🛠️ Requirements
* Python (Programming Language)
* PyABSA (Machine Learning Library)
* gradio (Python Framework)
* pandas (Python Library for Data operations)
<br><br>

#### How to run this code...
- Create virtual environment
```bash
conda create -n myenv python=3.8
```
- Activate the environment
```bash
conda activate myenv
```
- Install the packages
```bash
pip install -r requirements.txt
```
- Run the app
```bash
python app.py
```
- Navigate to URL http://127.0.0.1:5000/
<br>

- Enter valid values in all input boxes and hit Predict.

If everything goes well, you should  be able to see the predcitions on the HTML page!

## Authors
Devansh Mistry - [Linkedin](https://linkedin.com/in/devansh-vinodkumar-mistry-9bb2611aa/)

## If you like this project, please do give the star. If you have any suggestions or issues, please drop me a message.

* All datasets provided are for research only, we do not hold any Copyright of any datasets. These datasets follow their original licenses (if any).