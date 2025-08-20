# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Can the new quantitative trading strategies of hedge funds still work next week?

## Stakeholder & User
<Who decides? Who uses the output? Timing & workflow context>
Stakeholder/Decision owner: Fund manager, High-net-worth individuals or institutional investors
Users/Tool operator: Fund manager

## Useful Answer & Decision
Predictive: 
Metric: weekly return, maximum drawdown, volatility, slippage cost, contribution ratio of core factors
Artifact to deliver: forecast report

## Assumptions & Constraints
Data availability: Sufficient, timely, and accurate market/data feeds next week.
Capacity: Strategy operates within its scalable capital range.
Latency: Trading infrastructure maintains expected low-latency execution (no unexpected delays).
Compliance: No new rules restricting strategy mechanics.

## Known Unknowns / Risks
What’s uncertain: sudden market liquidity changes, unforeseen volatility spikes (e.g., geopolitical/macro events), unexpected data quality issues (delays, corruption), temporary infrastructure latency jumps, hidden overfitting to recent market patterns
How you’ll test or monitor: real-time tracking of key metrics vs. thresholds, cross-checks across data sources for integrity, stress tests for extreme market conditions, rolling window analysis (in-sample vs. out-of-sample), alert systems for market regime deviations

## Lifecycle Mapping
- Assess the new quantitative trading strategy’s effectiveness next week → Problem Framing & Scoping (Stage 01) → Defined scope document
- ...

## Repo Plan
/data/: Raw/processed market data, validation datasets
/src/: Strategy code, utils, infrastructure scripts, tests
/notebooks/: Validation, daily monitoring, post-week evaluation notebooks
/docs/: Strategy specs, risk checklist, execution log
cadence for updates: Raw data, monitoring notebook, execution log