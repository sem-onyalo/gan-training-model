import argparse

from data import Data
from inference import Inference
from model import AuxiliaryClassifierGAN, Discriminator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--summary', '-s', action='store_true', help='Output model summary only.')
    parser.add_argument('--inference', '-s', action='store_true', help='Run inference using an existing model. Model path must be supplied.')
    parser.add_argument('--train', '-s', action='store_true', help='Train the model.')
    
    parser.add_argument('--modelType', '-m', type=str, default='aux', help='The type of model to load')
    parser.add_argument('--latentDim', '-d', type=int, default=100, help='Latent space dimension')
    parser.add_argument('--labelDim', '-l', type=int, default=50, help='Label space dimension')
    parser.add_argument('--epochs', '-e', type=int, default=100, help='Number of training epochs')
    parser.add_argument('--batchsize', '-b', type=int, default=128, help='The training batch size')
    parser.add_argument('--evalfreq', '-v', type=int, default=10, help='Frequency to run model evaluations')
    parser.add_argument('--modelPath', '-p', type=str, default=None, help='Path to model to load. If this is set script will run inference instead of training.')
    
    parser.add_argument('--batchNorm', type=bool, default=True, help='')
    parser.add_argument('--convFilters', type=str, default='128,128', help='')
    parser.add_argument('--convTransposeFilters', type=str, default='128,128', help='')
    parser.add_argument('--generatorInputFilters', type=int, default=128, help='')
    parser.add_argument('--adamLearningRate', type=float, default=0.0002, help='')
    parser.add_argument('--adamBeta1', type=float, default=0.5, help='')
    parser.add_argument('--kernelInitStdDev', type=float, default=0.02, help='')
    parser.add_argument('--leakyReluAlpha', type=float, default=0.2, help='')
    parser.add_argument('--dropoutRate', type=float, default=0.4, help='')
    parser.add_argument('--evalDirLocal', type=str, default='eval', help='')

    args = parser.parse_args()

    data = Data()

    if args.inference:
        inference = Inference(data, args.modelPath, args.latentDim)
        inference.run()
    else:
        model = None
        if args.modelType == "aux":
            model = AuxiliaryClassifierGAN(data, args)
        elif args.modelType == "discriminator":
            model = Discriminator(data, args)

        if model != None:
            if args.summary:
                model.summary()
            
            if args.train:
                model.train(args.epochs, args.batchsize, args.evalfreq)
        else:
            raise Exception(f'Invalid model type {args.modelType}')