<div align="center">

# editdrift

**Notice when an edited cell line has moved, before the experiment is read as biology.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Status:** problem brief. The question and the measurement are written here. An implementation is not in this repository yet.

</div>

---

## The problem

An edited line is not a stable reagent. Passage number, guide batch, reagent lot, confluence, and who thawed the vial all move, and the paper still cites the line as if it were the same object as last quarter.

The failure mode is quiet. A phenotype shifts. The write-up treats the shift as an editing result. The shift was the cells.

Data teams already watch pipelines for this: a distribution moved, a null rate jumped, a fresh batch does not match the last good one. Edited lines deserve the same habit. Most lab records still keep it in a notebook, or not at all.

## The measurement I would trust

Compare a line to its own recent history, not to a universal "healthy cells" template.

| Signal | Why it matters |
| --- | --- |
| Passage and thaw | The line's age, stated |
| Guide and reagent lot | A new bottle is a new condition |
| A small panel of stable readouts | Growth, marker, or karyotype-style checks the lab already runs |
| Drift vs baseline | A distance from this line's last accepted window, with the window shown |

An alert with no baseline window is a mood. A baseline with no lot or passage is a chart that cannot be audited.

## What this repository is

The observability question for edited lines, beside the lineage question in [editledger](https://github.com/TechieGoku2623/editledger) and the methods-audit work in [methods-audit](https://github.com/TechieGoku2623/methods-audit). It does not ship a model, and it does not claim a biological result.

## Author

**Choppa Devasai Pranatheswar** · [LinkedIn](https://www.linkedin.com/in/devasai-pranatheswar)
