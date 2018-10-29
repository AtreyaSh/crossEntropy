# Utility of Cross-Entropy in Fuzzy/Soft Classification

Within the field of deep learning, there exist various cost functions which essentially provide gradients to train deep learning models. Different cost functions are useful for different purposes. Deep learning tasks can typically be classified into classification and regression tasks.

1. Hard classification tasks are expected to output to one-hot vectors such as [0,1,0] or multi-label vectors such as [1,1,0].

2. Regression tasks generally output to continuous values that are not restricted to binary representations.

Here a new concept of soft classification can be introduced. This would be the case where a deep learning model expects an output vector such as [0.3,0.5,0.2] to represent heteregeneity in the output. This would still be considered a classification task since the output represents probabilities which add up to 1. Furthermore, this cannot be considered as a multi-label classification since it is not "hard", in that it does not output clear binary data for classification.

We know very well that we can use aggregated cross-entropy as a cost function for one-hot expected data. We can also use binary cross entropy as a cost function for hard multi-label classification.

The question then arises, can we use either cross-entropy or binary cross-entropy or both for the case of soft classification? With the help of a quick mathematical proof, I would like to provide evidence that we can indeed use both.

## Cross-Entropy

Below is a generic formula for cross-entropy, where `log` assumes base `e`. Assume we are considering the binary cross-entropy (so, i = 1) for one component of the fuzzy classification desired output. Assume the model's output is probability `p` and the desired output is probability `q`. Naturally, p and q will have the range of `[0,1]`. Since cross-entropy is undefined at 0 and 1, we will assume the `p` and `q` have the range of `(0,1)` under the cross-entropy definition. This is just a mathematical trick to avoid singularities.

<p><img src="/svgs/d2a9f9a7e8d39592ff0b795fd716718b.svg" align=middle width=609.6255pt height=84.84168pt/></p>

If we visualize this function in 3 dimensions, we arrive at the following image.

<p align = "center">
<img src = "/crossEntropy.gif" width = 500>
</p>

We want to now calculate the partial derivative of `H(p,q)` with respect to `p`. `q` will remain fixed since it represents a desired output.

<p><img src="/svgs/535e417811d64023c9719eae5e66fd3e.svg" align=middle width=656.3337pt height=342.04994999999997pt/></p>

We want to understand where will `p` progress via gradient descent. We know that for one-hot/binary cases, `p` will tend to `q`, which is 1. However, we want to know if this is also the case if `q` is another number like 0.5.

Now, by minimizing the partial derivative of `H(p,v)`, we arrive at a possible stable state of the cross-entropy function.

<p><img src="/svgs/ecce6cb739501abf291c2a1ed07b5260.svg" align=middle width=448.32809999999995pt height=38.773514999999996pt/></p>

The stable state occurs when `p = q`. This shows that the cross-entropy function will push `p` towards the actual value of `q`. This would therefore imply that we can use cross-entropy for soft/fuzzy classification purposes!
