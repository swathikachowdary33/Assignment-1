def calculate_ticket_price(seats, timing, is_weekend):
    
    # Base prices
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }
    
    # Timing multipliers
    timing_multiplier = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }
    
    # Filter valid seats
    valid_seats = [seat for seat in seats if seat in prices]
    
    if len(valid_seats) == 0:
        return "No valid booking"
    
    #Base total
    base_total = sum(prices[seat] for seat in valid_seats)
    
    #Timing adjustment
    multiplier = timing_multiplier.get(timing, 1)
    timing_total = base_total * multiplier
    
    #Weekend surcharge
    if is_weekend:
        timing_total += timing_total * 0.10
    
    #Discount
    discount = 0
    if len(valid_seats) >= 5:
        discount = timing_total * 0.15
        timing_total -= discount
    
    #Booking fee
    booking_fee = 50 * len(valid_seats)
    subtotal = timing_total + booking_fee
    
    #GST
    tax = subtotal * 0.12
    
    #Final amount
    final_amount = subtotal + tax
    
    return {
        "base_total": round(base_total),
        "timing_adjustment": round(timing_total),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": round(final_amount)
    }


#Example run
seats = ["VIP", "REGULAR", "VIP"]
timing = "evening"
is_weekend = True

result = calculate_ticket_price(seats, timing, is_weekend)
print(result)