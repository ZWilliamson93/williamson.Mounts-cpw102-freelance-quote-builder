# def calculate_estimated_work(work_hours):
#     estimated_hours = work_hours * 40 








def main():
    input_name = input("Client name:")
    work_hours = float(input("Enter the number of hours worked:"))
    hourly_rate = int(input("Input hourly rate:"))
    direct_expenses = float(input("Input direct expenses:"))

    cleaned_name = input_name.strip().title()
    labor_cost = work_hours * hourly_rate 
    total_estimate = labor_cost + direct_expenses 
    print("Client:", cleaned_name)
    print(f"Labor cost: ${labor_cost:.2f}")
    print(f"Direct expenses: ${direct_expenses:.2f}")
    print(f"Total estimate: ${total_estimate:.2f}")

main()





