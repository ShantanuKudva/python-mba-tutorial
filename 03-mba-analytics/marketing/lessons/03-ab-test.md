# Lesson 3 — A/B Test with a t-test

## The question

"Variant B converted at 12%, A at 10%. Is that a real lift or random noise?"

## The test

For continuous metrics (revenue per user, time on page) use Welch's t-test:

```python
from scipy import stats

a = [...revenue per user in group A...]
b = [...revenue per user in group B...]

result = stats.ttest_ind(a, b, equal_var=False)
print(result.statistic, result.pvalue)
```

If `p < 0.05`, treat the difference as statistically significant at the 95% level.

## Wrap it

```python
def ab_test(a, b, alpha=0.05):
    res = stats.ttest_ind(a, b, equal_var=False)
    return {
        "mean_a": float(sum(a) / len(a)),
        "mean_b": float(sum(b) / len(b)),
        "lift_pct": (sum(b) / len(b) - sum(a) / len(a)) / (sum(a) / len(a)) * 100,
        "p_value": float(res.pvalue),
        "significant": bool(res.pvalue < alpha),
    }
```

## Caveats (real ones, not exam ones)

- **Sample size matters.** A 2% lift on n=50 is noise.
- **Don't peek mid-experiment.** Decide sample size before starting.
- **Practical significance ≠ statistical significance.** p<0.05 doesn't mean the lift matters to the business.

For a binary conversion metric (clicked vs not), prefer a chi-square or proportion test — but a t-test on the binary 0/1 vector is "close enough" for our purposes.

---

Done with marketing lessons. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).

---

## 📚 Resources

**Official docs**
- [`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
- [`scipy.stats.chi2_contingency`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)

**Deep dives**
- [HBR — the surprising power of online experiments](https://hbr.org/2017/09/the-surprising-power-of-online-experiments)
- [Investopedia — A/B testing](https://www.investopedia.com/terms/a/ab-split.asp)

**Video tutorials**
- [YouTube — A/B testing in Python](https://www.youtube.com/results?search_query=a%2Fb+testing+python+scipy+tutorial)

