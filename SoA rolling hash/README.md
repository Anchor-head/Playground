# Polynomial rolling hashing using an optimized Sieve of Atkin

## Polynomial rolling hash

A polynomia rolling hash is a hashing method that encodes some string $s$ of length n as:

$$H = \sum_{k=0}^{n-1} s[i]*p^i \mod{m}$$

where $p$ is normally a small prime number just greater than the size of the character set used (p=31 for lowercase letters, p=53 for lowercase and uppercase letters, etc.), and $m$ is a very large prime number (commonly $10^9+7$ or $10^9+9$) that determines the size limit of the hash without while minimizing the probability of collision, the event where different strings map to the same hash.

## Sieve of Atkin

The [Sieve of Atkin](https://en.wikipedia.org/wiki/Sieve_of_Atkin) is an advanced algorithm for finding prime numbers.

## What this project does

The point of this project is to implement an optimized Sieve of Atkin to find a prime number to use as a modulus in a polynomial rolling hash.

old_sieve.py contains the final algorithm.
