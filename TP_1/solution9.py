def electricity_bill(kwh):
  if kwh<0:
    return None
  tier1_kwh=min(kwh,50)
  tier2_kwh=min(max(kwh-50,0),150)
  tier3_kwh=max(kwh-200,0)

  energy_cost=(tier1_kwh*480)+(tier2_kwh*610)+(tier3_kwh*730)

  subtotal=energy_cost + 2000

  total_bill=round(subtotal*1.10)

  return total_bill

  #(b)
test_values=[0,35,50,120,200,350]

for kwh in test_values:
    bill_riel=electricity_bill(kwh)
    bill_usd=bill_riel/4100
    print(f"{kwh:3d} kWh -> {bill_riel:7,} riel  (≈ {bill_usd:6.2f} USD)")

