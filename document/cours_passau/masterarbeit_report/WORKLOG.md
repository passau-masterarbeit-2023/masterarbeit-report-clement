# Logs

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
