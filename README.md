
# bet-optimizer

`bet-optimizer` is a Python package designed for those interested in applying mathematical strategies to betting. It leverages the Kelly Criterion and the concept of positive expected value (EV) in betting, helping users calculate the optimal bet size and the minimum positive odds required for a bet to have a positive expected value.

## Features

- **Kelly Criterion Bet Calculation**: Calculate the optimal fraction of your bankroll to bet based on your probability of winning and the odds offered.
- **Positive Odds Calculation**: Determine the minimum positive odds required for a bet to have a positive expected value, based on the probability of winning.

## Installation

The package can be easily installed via pip. Just run the following command in your terminal:

```bash
pip install bet-optimizer
```

## Usage

### Kelly Criterion Bet Size Calculation

To calculate the optimal bet size using the Kelly Criterion:

```python
from bet_optimizer import kelly_criterion_bet

probability = 0.5  # Probability of winning the bet
odds = 2.0  # Decimal odds of the bet
bankroll = 100  # Size of your current bankroll

bet_size = kelly_criterion_bet(probability, odds, bankroll)
print(f"Optimal Bet Size: {bet_size}")
```

### Positive Odds Calculation

To calculate the minimum positive odds required for a bet:

```python
from bet_optimizer import get_positive_odds

probability = 0.5  # Probability of winning the bet

positive_odds = get_positive_odds(probability)
print(f"Minimum Positive Odds: {positive_odds}")
```

## Requirements

- Python 3.6 or later.

## License

This project is licensed under the Apache License - see the [LICENSE](https://github.com/subodh101/bet-optimizer/blob/main/LICENSE) file for details.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Support

If you encounter any problems or have any questions, please open an issue on the project's [GitHub page](https://github.com/subodh101/bet-optimizer).

## More Information

For more information and to download the package, visit [bet-optimizer on PyPI](https://pypi.org/project/bet-optimizer/).
