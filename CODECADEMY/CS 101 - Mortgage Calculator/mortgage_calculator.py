# Lvl 1. Monthly Interest & Number of Payments Calculation

def calculate_mortgage(loan_amount, annual_interest_rate, loan_term):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term * 12

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / number_of_payments
    else:
        growth_factor = (1 + monthly_interest_rate) ** number_of_payments
        monthly_payment = (
            loan_amount
            * monthly_interest_rate
            * growth_factor
            / (growth_factor - 1)
        )

    total_paid = monthly_payment * number_of_payments
    total_interest = total_paid - loan_amount

    return monthly_payment, total_paid, total_interest

# Lvl 2. Setup Main() & Getting Started

def main():

    print("------------------------ Computer Science - 101 --------------------------")
    print("-------- MORTGAGE CALCULATOR - Codecademy's Portfolio Project 01 ---------")

    # Lvl 3. Implementation of Exception – Handling

    while True:
        try:
            loan_amount = int(input("Please Enter your Loan Amount: $"))
            if loan_amount <= 0:
                print("Loan amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Enter a whole-dollar amount, without a dollar sign or commas.")

    while True:
        try:
            annual_interest_rate = float(
                input("Please Enter your Annual Interest Rate in (%): ")
            )
            if annual_interest_rate < 0:
                print("Interest rate cannot be negative.")
                continue
            break
        except ValueError:
            print("Enter a number, such as 5 or 6.5.")

    while True:
        try:
            loan_term = int(input("Please Enter the Loan Term in Whole Years: "))
            if loan_term <= 0:
                print("Loan term must be greater than zero.")
                continue
            break
        except ValueError:
            print("Enter a whole number of years, such as 10 or 30.")

    # Lvl 4. Monthly Payment Calculation, Total Repayment & Interest Calculation – Function Call

    monthly_payment, total_paid, total_interest = calculate_mortgage(loan_amount, annual_interest_rate, loan_term)

    # Lvl 5. Print Statements

    print(f"Loan amount: ${loan_amount:,.2f}")
    print(f"Annual interest rate: {annual_interest_rate:.2f}%")
    print(f"Loan term: {loan_term} years")

    print(f"Estimated Monthly Principal & Interest Payment: ${monthly_payment:,.2f}")
    print(f"Total paid over {loan_term} years: ${total_paid:,.2f}")
    print(f"Total interest paid: ${total_interest:,.2f}")

# Lvl 6. Finalizing the Program

if __name__ == "__main__":
    main()
