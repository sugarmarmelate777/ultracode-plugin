---
name: Classification of Groups of Order p³ for Odd Primes
description: Classifies all isomorphism classes of groups of order p³ (p odd prime) and provides explicit presentations for each class.
version: 1.0.0
council: SYNDICATE
category: Pure Mathematics
source: pre-generated
---

# Classification of Groups of Order p³ for Odd Primes

### Context

For an odd prime \(p\), there are exactly five isomorphism types of groups of order \(p^3\). This skill lists them with standard presentations and can verify the classification for a given \(p\).

### The five groups

1. **Cyclic** \(C_{p^3}\): \(\langle a \mid a^{p^3}=1 \rangle\).
2. **Abelian type \((p^2, p)\)**: \(C_{p^2} \times C_p\), presentation \(\langle a,b \mid a^{p^2}=b^p=1,\; ab=ba \rangle\).
3. **Elementary abelian** \(C_p^3\): \(\langle a,b,c \mid a^p=b^p=c^p=1,\; \text{all commute} \rangle\).
4. **Non‑abelian of exponent \(p\)** (Heisenberg group mod \(p\)): \(\langle a,b,c \mid a^p=b^p=c^p=1,\; [a,b]=c,\; [a,c]=[b,c]=1 \rangle\).
5. **Non‑abelian of exponent \(p^2\)**: \(\langle a,b \mid a^{p^2}=b^p=1,\; b a b^{-1} = a^{1+p} \rangle\).

### Verification procedure

- For a given odd prime \(p\), check that each presentation indeed yields a group of order \(p^3\).
- Distinguish them by computing the exponent, centre, and derived subgroup: 
  - Cyclic: centre = whole group, exponent \(p^3\).
  - Abelian type (p²,p): exponent \(p^2\), centre = whole group.
  - Elementary abelian: exponent \(p\), centre = whole group.
  - Non‑abelian exp p: centre \(\cong C_p\), exponent \(p\), derived subgroup of order \(p\).
  - Non‑abelian exp p²: centre \(\cong C_p\), exponent \(p^2\), derived subgroup of order \(p\).

### Tools

Use a computer algebra system to confirm orders and standard invariants. The classification is rigorous and needs no heavy computation beyond verifying isomorphisms.
