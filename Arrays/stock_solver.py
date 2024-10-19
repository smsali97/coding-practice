# Define the prices variable
prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9]

# Define other variables
inventory = 800
cost_per_unit = 4
period_1_days = 15
period_2_days = 15

# Update variables for SKU 2002
disposal_cost_per_unit = 4

# Demand forecast (same for both periods)
demand_period_1 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
demand_period_2 = demand_period_1

# Initialize variables to store the best prices and maximum profit
best_price_period_1 = 0
best_price_period_2 = 0
max_profit = 0

# Iterate through all possible price combinations
for price_1 in prices:
  for price_2 in prices:
    # Calculate sales in each period
    sales_period_1 = min(inventory, demand_period_1[prices.index(price_1)] * period_1_days)
    remaining_inventory = inventory - sales_period_1
    sales_period_2 = min(remaining_inventory, demand_period_2[prices.index(price_2)] * period_2_days)

    # Calculate unsold inventory
    unsold_inventory = inventory - sales_period_1 - sales_period_2

    # Calculate total revenue
    total_revenue = (sales_period_1 * price_1) + (sales_period_2 * price_2)

    # Calculate total profit
    total_profit = total_revenue - (inventory * cost_per_unit) - (unsold_inventory * disposal_cost_per_unit)

    print(price_1,price_2,total_revenue,- (inventory * cost_per_unit) - (unsold_inventory * disposal_cost_per_unit),total_profit)
    # Update best prices and maximum profit if current combination is better
    if total_profit > max_profit:
      max_profit = total_profit
      best_price_period_1 = price_1
      best_price_period_2 = price_2

# Print the results
print(f"Best price for Period 1: ${best_price_period_1}")
print(f"Best price for Period 2: ${best_price_period_2}")
print(f"Maximum Profit: ${max_profit}")