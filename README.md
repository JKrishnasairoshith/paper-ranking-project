
#  Paper Review Ranking System — Full Project Report

##  Objective

This project aims to fairly **rank academic paper submissions** based on reviewer scores and confidence using:
- **Simple average** of scores
- **Confidence-weighted average**, giving more weight to reviewers with higher confidence

This helps improve fairness and decision-making in conference paper acceptance processes.

---

##  Input Dataset

File: `all_reviews.xlsx`

| Column               | Description                                      |
|----------------------|--------------------------------------------------|
| Submission ID        | Unique identifier for each paper                |
| Submission Title     | Title of the paper                              |
| Acceptance Status    | (Accept/Reject) ground truth                    |
| Primary Track        | Topic track                                     |
| Reviewer Username    | Reviewer's ID                                   |
| Clarity, Originality, Impact, Overall | Scores per review (1–5)         |
| Confidence           | Confidence level (1–5)                          |

---

##  Methodology

### 1.  Simple Average Method

For each paper:
```
Final Score = Mean of all 'Overall' scores from reviewers
```
Script used: `aggregate_simple.py`  
Output: `simple_average.xlsx`

---

### 2.  Confidence-Weighted Score

For each paper:
```
Weighted Score = (Σ (Confidence × Overall)) / (Σ Confidence)
```
Script used: `confidence_weighted_score.py`  
Output: `confidence_weighted.xlsx`

---

##  Implementation Steps

### 1. Setup Environment

```bash
pip install pandas openpyxl matplotlib
```

### 2. Run Scripts

#### ➤ Simple Score
```bash
python3 aggregate_simple.py all_reviews.xlsx simple_average.xlsx
```

#### ➤ Confidence-Weighted Score
```bash
python3 confidence_weighted_score.py all_reviews.xlsx confidence_weighted.xlsx
```

### 3. Merge & Compare Scores

Jupyter notebook: `top10.ipynb`

Final merged file: `final_ranked_papers.xlsx`  
Comparison logic:
```python
ScoreDiff = Weighted Overall - Average Overall
```

---

##  Results Snapshot

### Top 10 Papers (Most Boost from Confidence Weighting)

| Submission Title | Weighted Score | Simple Score | Score Diff |
|------------------|----------------|--------------|------------|
| jGrlOrjqCzsv      | 3.83           | 3.25         | +0.58      |
| DDxOygmIippV      | 4.33           | 4.00         | +0.33      |
| KvesScxlbYZo      | 4.00           | 3.67         | +0.33      |
| iPVsjISqGYjc      | 2.57           | 2.25         | +0.32      |
| mClUjlPJgeMk      | 3.57           | 3.25         | +0.32      |
| jAvqWIRouqeo      | 3.57           | 3.25         | +0.32      |
| wQoGGNXEwIna      | 3.56           | 3.25         | +0.31      |
| OFildaoRLtWu      | 3.29           | 3.00         | +0.29      |
| GzkbxIfDtyOt      | 2.60           | 2.33         | +0.27      |
| oGnkzKBCNpMX      | 3.25           | 3.00         | +0.25      |

---

##  Visualization

Created in `top10.ipynb`:

-  Bar chart showing top 10 papers ranked by score difference.

-  Insight: Several papers had a **significant positive boost** when confidence was accounted for.

---

##  File Summary

| File Name                  | Description                                    |
|---------------------------|------------------------------------------------|
| `all_reviews.xlsx`        | Raw review data                                |
| `aggregate_simple.py`     | Simple average calculator                      |
| `simple_average.xlsx`     | Simple average results                         |
| `confidence_weighted_score.py` | Confidence-weighted score calculator     |
| `confidence_weighted.xlsx`| Weighted average results                       |
| `final_ranked_papers.xlsx`| Merged comparison of both methods              |
| `top10.ipynb`             | Analysis & charting notebook                   |

---

##  Conclusion

- Confidence-weighted scores offer a **more reliable ranking**, especially when reviewer certainty varies.
- This method ensures **strong, confident reviews have greater influence**, improving the fairness of paper selection.
- Future extensions may include reviewer bias detection or weighting based on historical accuracy.

---

##  Author

**Krishna Sai Roshith Jonnalagadda**  
  

