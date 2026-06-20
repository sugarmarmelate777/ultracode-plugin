---
name: Determination of Galois Group of Irreducible Quartic Polynomials over Q
description: Determines the Galois group of an irreducible quartic polynomial f(x) over Q using the resolvent cubic and discriminant, and outputs the isomorphism class as a transitive subgroup of S4.
version: 1.0.0
council: SYNDICATE
category: Pure Mathematics
source: pre-generated
---

# Determination of Galois Group of Irreducible Quartic Polynomials over Q

### Input

An irreducible separable quartic polynomial \(f(x) \in \mathbb{Q}[x]\). (If the polynomial is reducible, this skill does not apply.)

### Step‑by‑step method

1. **Resolvent cubic:** Transform \(f\) to the depressed quartic \(x^4 + px^2 + qx + r\) via a linear shift, then form the resolvent cubic
   \[g(x) = x^3 - p x^2 - 4r x + (4pr - q^2).\]
   (Equivalently, use the formula \(x^3 - a_2 x^2 + (a_1 a_3 - 4 a_0) x - (a_1^2 a_0 + a_3^2 - 4 a_0 a_2)\) where \(f = x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0\).)
2. **Discriminant:** Compute \(\Delta = \operatorname{Disc}(f)\). Check whether \(\Delta\) is a perfect square in \(\mathbb{Q}\).
3. **Galois group decision tree:**
   - If \(g(x)\) is irreducible over \(\mathbb{Q}\):
     - If \(\Delta\) is a square → \(\operatorname{Gal}(f) \cong A_4\).
     - If \(\Delta\) is not a square → \(\operatorname{Gal}(f) \cong S_4\).
   - If \(g(x)\) has exactly one rational root (partially reducible):
     - If \(\Delta\) is a square → \(\operatorname{Gal}(f) \cong V_4\) (Klein four‑group).
     - If \(\Delta\) is not a square → \(\operatorname{Gal}(f) \cong D_4\) (dihedral of order 8).
   - If \(g(x)\) splits completely (three rational roots) → \(\operatorname{Gal}(f) \cong V_4\).

### Implementation details

- Use exact rational factorisation of the cubic, e.g., via `sympy.factor` or by checking rational roots via the Rational Root Theorem.
- Compute the discriminant exactly. For a quartic \(a_4 x^4 + \dots + a_0\), use the standard formula or \(\operatorname{Disc}(f) = \operatorname{Resultant}(f,f')\).
- Threshold: if \(\Delta = 0\) the polynomial is not separable – reject input.

### Example

\(f(x) = x^4 + x + 1\). Resolvent \(g(x)=x^3 + 4x - 1\), irreducible. \(\Delta = 229\), not a square. → \(S_4\).
