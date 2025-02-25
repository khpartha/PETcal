import math

# Constants from the original C++ code
PI = math.pi
DENSITY_PET = 0.050  # lb/in³
LB_TO_GRAMS = 453.592  # Conversion factor

def calculate_volume_walls(outer_radius, inner_radius, height):
    return PI * height * (outer_radius**2 - inner_radius**2)

def calculate_volume_bottom(outer_radius, thickness):
    return PI * outer_radius**2 * thickness

def calculate_volume_handle(radius, length):
    return PI * radius**2 * length

def calculate_pet_grams(diameter, height):
    """
    Calculate the PET required for one cup.
    """
    outer_radius = diameter / 2.0
    thickness = 0.0197  # 0.5 mm in inches
    inner_radius = outer_radius - thickness

    # Handle dimensions (can be adjusted as needed)
    handle_radius = 0.25  # inches
    handle_length = 2.0   # inches

    # Calculate volumes
    volume_walls = calculate_volume_walls(outer_radius, inner_radius, height)
    volume_bottom = calculate_volume_bottom(outer_radius, thickness)
    volume_handle = calculate_volume_handle(handle_radius, handle_length)

    total_volume = volume_walls + volume_bottom + volume_handle

    # Convert volume to weight in pounds, then to grams
    weight_in_pounds = total_volume * DENSITY_PET
    weight_in_grams = weight_in_pounds * LB_TO_GRAMS

    return weight_in_grams

def calculate_monthly_pet_and_cost(num_items, diameter, height, price_per_gram=20):
    """
    Calculate the total PET required for monthly production and its cost.
    """
    pet_per_item = calculate_pet_grams(diameter, height)
    total_pet = num_items * pet_per_item
    total_cost = total_pet * price_per_gram
    return total_pet, total_cost

# Example usage:
if __name__ == '__main__':
    # Input: monthly production numbers and cup dimensions
    num_items = int(input("Enter the number of cups produced in a month: "))
    diameter = float(input("Enter the diameter of the cup (in inches): "))
    height = float(input("Enter the height of the cup (in inches): "))

    total_pet, total_cost = calculate_monthly_pet_and_cost(num_items, diameter, height)

    print(f"\nMonthly PET required: {total_pet:.2f} grams")
    print(f"Monthly cost: {total_cost:.2f} rupees")
