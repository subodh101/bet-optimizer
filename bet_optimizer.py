def kelly_criterion_bet(probability: float, odds: float, bankroll: float = 100) -> float:
    """
    Calculate the Kelly Criterion bet size.

    Args:
        probability: The probability of winning the bet (0 to 1).
        odds: The odds received on the bet (in decimal form, e.g., 1.0 for even money).
        bankroll: The current size of the bankroll.

    Returns:
        The optimal fraction of the bankroll to bet.
    """
    if not 0 <= probability <= 1:
        print("Probability must be between 0 and 1")
        return 0
    if odds <= 0:
        print("Odds must be greater than 0")
        return 0
    if bankroll <= 0:
        print("Bankroll must be greater than 0")
        return 0

    complement = 1 - probability
    bet_size = (probability * odds - complement) / odds

    return bet_size * bankroll


def get_positive_odds(probability: float):
    """
    Calculate the minimum positive odds required for a bet to have a positive expected value.

    Args:
        probability (float): The probability of winning the bet (0 to 1).

    Returns:
        float: The minimum positive odds required for a bet to have a positive expected value.
               Returns infinity if the probability is 0, and None if the probability is outside the valid range.
    # ev = p * odds - (1-p) * 1
    # p * odds -1 + p > 0  # make ev positive
    # p(odds + 1) > 1
    # odds > (1/p) - 1
    """
    if probability == 0:
        return float("inf")
    if not 0 <= probability <= 1:
        return None

    return (1 - probability) / probability
