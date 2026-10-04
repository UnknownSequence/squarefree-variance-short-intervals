# The variance of squarefree integers in short intervals of length up to X^{4/7}

**Status: AI-generated research draft, not refereed. No human has checked it; treat every claim as unverified.**

## Claim

Gorodetsky, Matomäki, Radziwiłł and Rodgers
([On the variance of squarefree integers in short intervals and arithmetic progressions](https://arxiv.org/abs/2006.04060),
Geom. Funct. Anal. 2021, Theorem 1) proved that the number of squarefree integers in (x, x + H], for x chosen at
random in [X, 2X], has variance C√H + O(H^{1/2−ε/16}) when H ≤ X^{6/11−ε}. The note
(`squarefree_variance_4_7.pdf`) claims the same asymptotic, with error O(H^{1/2−ε/64}), for **H ≤ X^{4/7−ε}**.

- **Method.** Only one step changes. In the contribution of integers with a large square divisor, the large value
  estimate of Guth and Maynard ([Ann. of Math. 2026](https://doi.org/10.4007/annals.2026.203.2.6)) replaces
  Huxley's, which relaxes the condition z ≥ H^{4/3} to z ≥ H^{5/4}.
- **Limit of the method.** 4/7. At H = X^{4/7} several constraints become sharp at once. With the large value and
  moment estimates tried, going further needs a larger range for the estimate on small square divisors, which
  produces the main term.
- **Arithmetic progressions.** The analogue for progressions to a prime modulus q ≥ x^{3/7+ε} is sketched in a
  remark but has not been checked.

## Contents

| Path | What it is |
|---|---|
| `squarefree_variance_4_7.tex`, `.pdf` | the note, 7 pages |
| `numerics/opt2.py` | the exponent model (large value estimates, moments of ζ) |
| `numerics/limits.py`, `limits.out` | the optimisation behind the table in "Why the method stops at 4/7" |

## Provenance

Produced with Claude (Anthropic) at the request of Siddharth Iyer, as part of a search for problems from the work of
Matomäki. The literature search behind it (October 2026) found no earlier claim of this range, but it was not
exhaustive.

Related: [exact-semiprimes-lean](https://github.com/UnknownSequence/exact-semiprimes-lean), a companion project on
products of two primes in almost all short intervals.
