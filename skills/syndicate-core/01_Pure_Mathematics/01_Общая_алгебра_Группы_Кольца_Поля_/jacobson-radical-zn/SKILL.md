---
name: Jacobson Radical of Z/nZ
description: Computes the Jacobson radical, nilradical, and the semisimple quotient of the finite ring Z/nZ for a given positive integer n.
version: 1.0.0
council: SYNDICATE
category: Pure Mathematics
source: pre-generated
---

# Jacobson Radical of Z/nZ

### Preliminary facts

The ring \(\mathbb{Z}/n\mathbb{Z}\) is commutative; therefore its Jacobson radical \(J\) coincides with the nilradical (the set of nilpotent elements).

### Prime factor description

Let \(n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}\) be the prime factorisation. An element \(a \bmod n\) is nilpotent iff for every prime \(p_i\), \(p_i \mid a\). Hence \(J = \mathrm{rad}(n)\,\mathbb{Z} / n\mathbb{Z}\), where \(\mathrm{rad}(n) = p_1 p_2 \cdots p_k\) (the product of distinct primes dividing \(n\)).

### Algorithm

1. **Factor \(n\)** completely (use Pollard’s Rho or trial division; for small \(n\) simple factorisation is fine).
2. **Compute** \(r = \prod_{i=1}^k p_i\).
3. **The Jacobson radical** is the ideal \(J = \{ a \bmod n \mid r \text{ divides } a \}\). It has size \(n/r\).
   - Equivalently, \(J = (r \bmod n)\).
4. **The semisimple quotient** is \(\mathbb{Z}/n\mathbb{Z} / J \cong \mathbb{Z}/r\mathbb{Z} \cong \prod_{i=1}^k \mathbb{F}_{p_i}\).

### Worked example

For \(n = 72 = 2^3 \cdot 3^2\), \(\mathrm{rad}(72) = 6\). Then \(J\) consists of multiples of 6: \(\{0,6,12,\dots,66\}\). The quotient is \(\mathbb{Z}/6\mathbb{Z} \cong \mathbb{F}_2 \times \mathbb{F}_3\), a product of fields.

### Tools
Use any big‑integer factorisation library and modular arithmetic. Decision threshold: output “Jacobson radical is \(\langle r \rangle\)” along with its elements if \(n \le 100\).
