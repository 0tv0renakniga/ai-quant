import numpy as np

# Example inputs
risk_free_rate = 0.03
expected_market_return = 0.08
beta_asset = 1.2

# CAPM expected return calculation
expected_return_asset = risk_free_rate + beta_asset * (expected_market_return - risk_free_rate)

print(f"Expected return (CAPM): {expected_return_asset:.2%}")

