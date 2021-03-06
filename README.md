# GAN Model Training

A repository to train TensorFlow GAN models and generate images.

## Dependencies

* Python==3.8.10

## Install

### Windows

```
python -m venv env

.\env\Scripts\activate

pip install -r requirements.txt
```

## View Architecture

```
python main.py --summary
```

## Train

```
python main.py --train
```

## Generate Images

```
python main.py --inference --modelPath <path-to-model>
```
