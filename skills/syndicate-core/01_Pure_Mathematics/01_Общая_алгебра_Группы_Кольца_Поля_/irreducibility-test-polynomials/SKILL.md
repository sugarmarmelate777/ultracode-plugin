---
name: Irreducibility Test for Polynomials over Q and Finite Fields
description: Determines if a given polynomial over Q or F_p is irreducible using combination of Eisenstein's criterion, modular reduction, and rational root test, with fallback to factorization algorithms.
version: 1.0.0
council: SYNDICATE
category: Pure Mathematics
source: pre-generated
---

# Irreducibility Test for Polynomials over Q and Finite Fields

### Scope

This skill handles univariate polynomials with rational coefficients (convert to primitive integer polynomials) or with coefficients in \(\mathbb{F}_p\).

### Over Q: Algorithm

1. **Primitive cleaning:** Multiply by the lcm of denominators to obtain a polynomial \(f(x) \in \mathbb{Z}[x]\) whose coefficients have gcd 1.
2. **Degree ≤ 3:** Apply the Rational Root Theorem. If no rational root exists, the polynomial is irreducible (except for possible quadratic factors when degree 3, but over Q degree 3 irreducibility ⇔ no rational root). For degree 2, check discriminant is not a square.
3. **Eisenstein’s criterion:** Try the original polynomial and translations \(x \leftarrow x + k\) for small \(k \in \mathbb{Z}\). If any translated polynomial satisfies Eisenstein for some prime, it is irreducible.
4. **Modular reduction:** Choose a prime \(p\) that does not divide the leading coefficient. Reduce modulo \(p\) and factor the resulting polynomial over \(\mathbb{F}_p\). If it is irreducible over \(\mathbb{F}_p\), then \(f\) is irreducible over \(\mathbb{Q}\).
5. **Further prime checks:** If reduction modulo one prime yields a factorisation pattern that forces a possible factorisation over \(\mathbb{Z}\) (e.g., factors of degree 2 and 2 for a quartic), test additional primes to build constraints (Dedekind’s theorem). If after testing primes up to some bound (say 20) no irreducibility is proved, proceed to full factorisation.
6. **Full factorisation:** Use a polynomial factorisation algorithm (Zassenhaus, van Hoeij) via a computer algebra system.

### Over F_p: Algorithm

1. Eliminate repeated factors (square‑free part).
2. Apply Berlekamp’s algorithm or Cantor–Zassenhaus to obtain irreducible factors.
3. Output “irreducible” if there is only one factor.

### Tools

- Symbolic Python with `sympy.factor` for small degrees; for large degrees, rely on `sympy.factor` with modulus.
- Threshold: if degree > 100 and prime > 1000, rely exclusively on built‑in factorisation.
