# CS 101 — Mortgage Calculator

A Python command-line mortgage estimator built as a Codecademy CS 101 portfolio project. Given a loan amount, annual interest rate, and loan term, it estimates the monthly principal-and-interest payment, total repayment, and total interest.

**Author:** [PS-Chakradhar](https://github.com/PS-Chakradhar)  
**Repository:** [CODECADEMY-Portfolio-Projects-](https://github.com/PS-Chakradhar/CODECADEMY-Portfolio-Projects-)

## Features

- Collects loan details interactively in the terminal
- Validates numeric inputs and re-prompts for invalid values
- Calculates a fixed-rate mortgage payment
- Handles 0% interest separately
- Displays estimated monthly payment, total repayment, and total interest
- Formats monetary results to two decimal places

## Requirements

- Python 3
- No third-party packages

## Run the program

From the repository root, run:

```bash
cd "CODECADEMY/CS 101 - Mortgage Calculator"
python3 mortgage_calculator.py
```

Enter the loan amount in whole dollars, the annual interest rate as a percentage, and the term in whole years. For example, enter `350000`, `5`, and `10`—without currency symbols, commas, or a percent sign.

## Calculation

The program assumes a fixed annual interest rate and monthly payments. Let:

- `P` be the principal (amount borrowed)
- `i` be the annual interest rate entered as a percentage
- `r` be the monthly interest rate as a decimal: `(i / 100) / 12`
- `n` be the total number of monthly payments: `loan term in years × 12`

For a positive rate, the monthly payment is estimated with the standard amortizing-loan formula:

```text
M = P × [r(1 + r)^n] / [(1 + r)^n − 1]
```

At 0% interest, the monthly payment is `P / n`. Total repayment is estimated as the monthly payment multiplied by the number of payments; total interest is total repayment minus the original principal.

## Example

For a `$350,000` loan at `5%` annual interest over `10` years, the estimates are:

| Result | Estimate |
|---|---:|
| Monthly principal-and-interest payment | `$3,712.29` |
| Total repayment | `$445,475.16` |
| Total interest | `$95,475.16` |

These are estimates. A lender’s schedule may differ slightly due to rounding and loan-specific terms.

## Assumptions and limitations

- The interest rate remains fixed throughout the term.
- Payments are made monthly using a standard amortization schedule.
- The estimate covers **principal and interest only**. It excludes property taxes, homeowners insurance, mortgage insurance, HOA fees, closing costs, and other charges.
- The calculator does not model adjustable-rate loans, refinancing, extra payments, or early payoff.
- The program uses the rate entered by the user; it does not retrieve current rates or connect to a lender.
- Loan amounts are entered in whole dollars and terms in whole years.

This is an educational estimate, not a lender quote or financial advice.

## Manual test scenarios

- `$350,000`, `5%`, `10 years`: monthly payment should be about `$3,712.29`.
- `$350,000`, `0%`, `10 years`: monthly payment should be about `$2,916.67`, with `$0.00` total interest.
- Non-numeric, zero, or negative values where invalid should cause the program to prompt again.

## License

This project is covered by the repository’s [MIT License](../../LICENSE).
