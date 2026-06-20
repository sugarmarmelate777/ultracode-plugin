---
name: PID Detection for Quadratic Integer Rings
description: Determines whether the ring of integers of a quadratic field Q(√d) (d square‑free) is a principal ideal domain, using norm‑Euclidean checks and class number calculations.
version: 1.0.0
council: SYNDICATE
category: Pure Mathematics
source: pre-generated
---

# PID Detection for Quadratic Integer Rings

### Quadratic rings

For a square‑free integer \(d \neq 0,1\), the ring of integers is \(\mathcal{O}_K = \mathbb{Z}[\sqrt{d}]\) if \(d \equiv 2,3 \pmod 4\), and \(\mathbb{Z}[\frac{1+\sqrt{d}}{2}]\) if \(d \equiv 1 \pmod 4\).

### Detection strategy

1. **Small discriminant list:** If \(d < 0\), the ring is a PID exactly when \(d \in \{-1, -2, -3, -7, -11, -19, -43, -67, -163\}\) (Baker–Heegner–Stark). Return answer immediately.
2. **Norm‑Euclidean test:** Check whether the ring is Euclidean with respect to the norm. A ring is norm‑Euclidean if for all \(a,b \in \mathcal{O}_K, b \neq 0\), there exists \(q \in \mathcal{O}_K\) such that \(|N(a - bq)| < |N(b)|\). For \(d>0\), this holds for a known finite list (e.g., \(d=2,3,5,6,7,11,13,17,19,21,29,33,37,41,57,73\)). If the value of \(d\) appears in the list, output “PID (actually Euclidean)”.
3. **Minkowski bound class number computation:** For other \(d\), compute the class number \(h_K\):
   - Determine the discriminant \(D_K\) ( \(=d\) if \(d \equiv 1 \mod 4\), else \(4d\) ).
   - Minkowski bound \(M = \frac{2}{\pi}\sqrt{|D_K|}\) (imaginary) or \(\frac{1}{2}\sqrt{D_K}\) (real).
   - For each prime \(p \le M\) that ramifies or splits, examine the factorisation of \(p\) and test whether the ideal factors are principal by solving norm equations \(N(x) = p^k\).
   - If every non‑principal ideal in the class group is shown to be principal, then \(h_K=1\) → PID. Otherwise it is not a PID.

### Implementation note

For \(|d| \le 100\), a brute‑force search for counterexamples to the Euclidean condition or direct factorisation of ideals is feasible. Use Python with `sympy` or SageMath for number field operations. Threshold: if \(h_K>1\), output “Not a PID”.
