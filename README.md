# Avalanche_PBKDF1
Avalanche effect analysis on PBKDF1 algorithm with Python and Matlab

# Analysis
To perform these tests I have used a key derivation function with a sliding computational cost, aimed to reduce the vulnerability of encrypted keys to brute force attacks, known as PBKDF1. The function parameters are a function
Hash, a password, a salt, an iteration counter and the size of the
key already derived. This function is based on calculating the hash of the
password concatenated with the salt, and then calculate the hash of the hash
which it had been calculated, as many times as the iteration counter estipulates:

>K=H(H(...H(P||S)...))

The hash function to use, which can be an MD2, an MD5 or a
SHA-1, affect the size of the output of the algorithm in 16
Octets for MD2 and MD5, and 20 for SHA-1. The tests that use the hash
SHA-1 since the output is larger and is the default option of the
algorithm.

The rest of the parameters that are maintained in all the tests, will be the
iterations counter value to 1000, recommended by the
Documentation of the algorithm and default option.

The programming language chosen is Python and the function has been obtained thanks to the pyCrypto package. We can see in the file 'test\KDF.py' as it solves the
test vector correctly.

The data of the first test (PB.py), a fixed and random password of 4 bytes size and what it varies is the random and different salt of 8 bytes size with one bit changed in each one of the iterations of the test loop. Calculate the Hamming distance between the derived keys and dump the result in the file 'hamming'.

For the second test (PBv2.py) a random password, which variates and keep the salt. Maintaining the same sizes of the previous test and calculating the Hamming distance overturning the result on the file 'hammingv2'.

In the third test. It maintains the same structure as the first, but as password is used the string 'password' to be able to check how it affects whether the password to be encrypted is random or not. This test (PBv3.py) returns the data in 'hammingv3'.

All tests of the charts in the calculation of  HAmming distances of pseudo-random functions, generated in the file 'ran.py' and Dump in 'ran'.

The sample size is 10, which cover a small part of the whole possible, and have enough data to be reliable.

The statistical measures to be calculated include:

The Skewness value that measures the asymmetry of the distribution. The value of the asymmetry can be positive or negative, or even indefinite. For a value close to zero is the case of a symmetric distribution.

Kurtosis is a descriptor of the shape of a distribution of probability, and the kurtosis of any normal univariate distribution is 3.

The Pearson χ² test is used to measure the discrepancy between an observed distribution and a theoretical distribution, indicating the extent to which the differences exist between the two, and to test for independence between the two variables.

The higher the chi square value, the lower the probability that the hypothesis is correct.

Statistical measures and histograms obtained with Matlab and available in 'crypto.m', 'cryptov2.m', 'cryptov3.m'.

|                         | **PBDKF1 Test1** | **PBDKF1 Test2** | **PBDKF1 Test3** | **Ramdon Func.** |
| :---------------------- | ---------------: | ---------------: | ---------------: | ---------------: |
| **Average**             | 80.0080          | 79.9939          | 80.0034          | 80.0002          |
| **Median**              | 80               | 80               | 80               | 80               |
| **Mode**                | 80               | 80               | 80               | 80               |
| **Variance**            | 40.0587          | 40.0855          | 39.9810          | 40.0535          |
| **Standard Desviation** | 6.3292           | 6.3313           | 6.3231           | 6.3288           |
| **Standard Error**      | 0.0063           | 0.0063           | 0.0063           | 0.0063           |
| **Skewness**            | -7.2674e-04      | 0.0012           | -0.0048          | 0.0030           |
| **Kurtosis**            | 2.9872           | 2.9869           | 2.9864           | 2.9896           |
| **Range**               | 59               | 58               | 66               | 59               |
| **Max**                 | 111              | 109              | 114              | 110              |     
| **Min**                 | 52               | 51               | 51               | 51               |
| **Sum**                 | 80007962         | 79993924         | 80003366         | 80000159         |
| **χ²**                  | 0.3334           | 0.3335           | 0.3333            
 

As we can see once obtained all the data we have distributions symmetrical, normal and univariate in all cases.

In the histograms the difference between the algorithm and a random function is minimal and with chi square results we can certify that the three tests do not differ from a uniform and random distribution with a degree of significance of 0.5%.

#References

- Cryptographic API. [*https://www.dlitz.net/software/pycrypto/*](https://www.dlitz.net/software/pycrypto/)

- Documentation of the algorithm and its parameters within the Api. 
[*https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html*](https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html)

- Example Vectors. [*http://www.di-mgt.com.au/cryptoKDFs.html\#examplespbkdf*](http://www.di-mgt.com.au/cryptoKDFs.html\#examplespbkdf) - Vectores de
ejemplo

- PBKDF1 on RFC 2898 (Specification of PKCS \#5 v2.0.)[*https://tools.ietf.org/html/rfc2898\#section-5.1*](https://tools.ietf.org/html/rfc2898\#section-5.1) 

- Skewness [*https://en.wikipedia.org/wiki/Skewness*](https://en.wikipedia.org/wiki/Skewness)

- Kurtosis [*https://en.wikipedia.org/wiki/Kurtosis*](https://en.wikipedia.org/wiki/Kurtosis)

- χ² [*https://es.wikipedia.org/wiki/Prueba\_%CF%87%C2%B2\_de\_Pearson*](https://es.wikipedia.org/wiki/Prueba_χ²_de_Pearson)

- Statistical significance for χ² [*https://es.wikipedia.org/wiki/Significaci%C3%B3n\_estad%C3%ADstica*](https://es.wikipedia.org/wiki/Significación_estadística)