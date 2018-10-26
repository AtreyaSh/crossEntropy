# Exploring Deep Learning with TensorFlow

## Utility of Cross-Entropy for Fuzzy/Soft Classification

Within the field of deep learning, there exist various cost functions which essentially provide a gradient to train a deep learning model. Different cost functions are useful for different purposes. Deep learning tasks can typically be classified into classification and regression tasks.

1. Hard classification tasks are expected to output to one-hot vectors such as [0,1,0] or multi-label vectors such as [1,1,0].

2. Regression tasks generally output to continuous values that are not restricted to binary representations.

Here a new concept of soft classification can be introduced. This would be the case where a deep learning model expects an output vector such as [0.3,0.5,0.2] to represent heteregeneity in the output. This would still be considered a classification task since the output represents probabilities which add up to 1. Furthermore, this cannot be considered as a multi-label classification since it is not "hard", in that it does not output clear binary data for classification.

We know very well that we can use aggregated cross-entropy as a cost function for one-hot expected data. We can also use binary cross entropy as a cost function for hard multi-label classification.

The question then arises, can we use either cross-entropy or binary cross-entropy or both for the case of soft classification? With the help of a quick mathematical proof, I would like to provide evidence that we can indeed use both.

### Cross-Entropy

Below is a generic formula for cross-entropy, where `log` assume base `e`. Assume we are considering the binary cross-entropy (so, i = 1) for one component of the fuzzy classification desired output. Assume the model's output is `p` and the desired output is `q`.

<p align="center"><img src="https://github.com/AtreyaSh/deepUnlearning/blob/master/svgs/56568cdabc887cf1e1be78ecd50508c3.svg" align=middle width=656.3337pt height=580.9682999999999pt/></p>

<p align = "center">
<img src = "/crossEntropy.gif" width = 500>
</p>

