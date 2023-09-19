# Logs

## 19/09

To do :

* [ ] mail to elod to have tuter INSA
* [ ] mail to security team to have info on dataset
* [ ] script to see the corruption of the dataset

Rapport (christopher meeting) to do :

* split backgound into related work and background
* take care to exactly explain the think used
* make a part assumption into background to define concept
* make a ressource section with hardware
* make full question into introduction
* enter more in details into background part

---

* into the statistical embedding, make byte wise and reduce the dimension after
* use under sampling, not over sampling

## 23/08/23

1. **Sutskever, I., Vinyals, O., & Le, Q. V. (2014).** Sequence to sequence learning with neural networks. In Advances in neural information processing systems (pp. 3104-3112).
   * This paper introduces a general end-to-end approach to sequence learning that makes minimal assumptions on the sequence structure, using multilayered Long Short-Term Memory (LSTM) networks.
2. **Chung, J., Gulcehre, C., Cho, K., & Bengio, Y. (2014).** Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555.
   * This paper evaluates the performance of Gated Recurrent Units (GRUs) and their variants on various sequence modeling tasks.
3. **Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017).** Attention is all you need. In Advances in neural information processing systems (pp. 5998-6008).
   * This paper introduces the Transformer model, which solely relies on attention mechanisms to draw global dependencies between input and output, making it suitable for various sequence-to-sequence tasks.
4. **Hochreiter, S., & Schmidhuber, J. (1997).** Long short-term memory. Neural computation, 9(8), 1735-1780.
   * A foundational paper that introduces the LSTM architecture, designed to handle long sequences and their long-range dependencies.
5. **Bai, S., Kolter, J. Z., & Koltun, V. (2018).** An empirical evaluation of generic convolutional and recurrent networks for sequence modeling. arXiv preprint arXiv:1803.01271.
   * This paper provides an empirical evaluation of convolutional networks for sequence modeling and compares them to canonical recurrent networks.
6. **Lai, S., Xu, L., Liu, K., & Zhao, J. (2015).** Recurrent convolutional neural networks for text classification. In Twenty-ninth AAAI conference on artificial intelligence.
   * This paper combines RNNs and CNNs for text classification, which can be seen as a form of sequence embedding.

## 21/08/2023

finish the introduction, beginning of embedding state of the art (chatGpt):

```shell

```

1. **Byte Frequency Distribution (BFD)** : This is the most frequently used feature, which represents the frequency of occurrence of each possible byte value.
2. **Bigram Frequencies** : Some studies have utilized the frequencies of pairs of consecutive bytes.
3. **Trigram Frequencies** : This involves the frequency of occurrences of three consecutive bytes.
4. **Byte Value Statistics** : These include the mean byte value, mean absolute deviation, standard deviation, skewness, and kurtosis.
5. **Complexity and Information Content Metrics** : These include Shannon entropy, compressibility, and Lempel-Ziv complexity.
6. **Other Features** :
   * Hamming weight
   * Difference between consecutive byte values (or “rate of change”)
   * Maximum length of repeated byte values
   * Frequency of occurrence of bytes in the ASCII range
   * Measures computed in a sliding window through the file or fragment.
7. **Less Common Features** :
   * Pairwise differences between frequencies of byte values
   * Distribution of the exclusive-OR of consecutive byte values
   * Chi-square statistics
   * The NIST randomness metrics suite
   * GIST image processing features
   * Least common substring and subsequence measures
   * Sum of the four highest byte frequencies
   * Correlation of values of consecutive bytes
   * Correlation of frequencies of consecutive bytes.
8. **Feature Extraction and Dimensionality Reduction Techniques** : Techniques like Principal Component Analysis and autoencoder networks have been used to extract features with unigram counts as input. Some studies have also used genetic algorithms to evolve a feature extractor from the raw contents of files.

## Tue 8 Aug 2023

Started to create the report template.

