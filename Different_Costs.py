import streamlit as st
import pandas as pd

def calculate_costs(fixed_costs, variable_costs):
    """
    Calculate the total fixed and variable costs and return the sum.
    """
    total_fixed_costs = sum(fixed_costs.values())
    total_variable_costs = sum(variable_costs.values())
    total_costs = total_fixed_costs + total_variable_costs

    return {
        "Total Fixed Costs": total_fixed_costs,
        "Total Variable Costs": total_variable_costs,
        "Total Costs": total_costs
    }

# Streamlit App
st.title("Mining Cost Calculator")
st.write("Enter costs for fixed and variable expenses to calculate total cost.")

# Fixed cost categories
fixed_cost_categories = [
    "Equipment Costs", "Infrastructure Costs", "Land Acquisition Costs", "Administrative Salaries",
    "Insurance Premiums", "Office Expenses", "Permits and Licensing Costs", "Mine Closure Bonds",
    "Depreciation Costs", "Amortization Costs", "Base Energy Costs", "Scheduled Maintenance Costs"
]

# Variable cost categories
variable_cost_categories = [
    "Drilling Costs", "Blasting Costs", "Loading and Hauling Costs", "Processing Costs",
    "Hourly Labor Costs", "Contractor Fees", "Explosives Costs", "Lubricants Costs",
    "Spare Parts Costs", "Waste Management Costs", "Water Treatment Costs", "Emission Control Costs",
    "Variable Energy Costs", "Water Usage Costs", "Ore Transportation Costs", "Product Shipment Costs"
]

# Semi-variable & other costs
other_cost_categories = [
    "Equipment Repair Costs", "Maintenance Costs (Routine and Repairs)", "Supervisor Salaries (Base + Overtime)",
    "Fuel Costs (Standby + Operational)", "Exploration Costs", "Feasibility Study Costs",
    "Research and Development Costs", "Contingency Costs", "Community Engagement Costs",
    "Rehabilitation and Reclamation Costs"
]

# Collect fixed costs
st.subheader("Fixed Costs")
fixed_costs = {}
for category in fixed_cost_categories:
    fixed_costs[category] = st.number_input(f"Enter {category}", min_value=0.0, step=0.1)

# Collect variable costs
st.subheader("Variable Costs")
variable_costs = {}
for category in variable_cost_categories:
    variable_costs[category] = st.number_input(f"Enter {category}", min_value=0.0, step=0.1)

# Collect other costs
st.subheader("Other Costs")
for category in other_cost_categories:
    fixed_costs[category] = st.number_input(f"Enter {category}", min_value=0.0, step=0.1)

# Calculate total costs
if st.button("Calculate Total Costs"):
    cost_summary = calculate_costs(fixed_costs, variable_costs)
   
    # Display cost breakdown
    st.subheader("Cost Breakdown Table")
    cost_data = {
        "Category": list(fixed_costs.keys()) + list(variable_costs.keys()) + ["Total Fixed Costs", "Total Variable Costs", "Total Costs"],
        "Amount": list(fixed_costs.values()) + list(variable_costs.values()) + [
            cost_summary["Total Fixed Costs"],
            cost_summary["Total Variable Costs"],
            cost_summary["Total Costs"]
        ]
    }
    cost_table = pd.DataFrame(cost_data)
    st.dataframe(cost_table)

st.write("Thank you for using the Cost Calculator!")
