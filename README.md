# Taxi-Management-System
Customer Trip Booking and Discount Management System in Python


---

# Customer Trip Booking and Discount Management System in Python

## Overview

This project is a Python-based application designed to manage customer trip bookings and discount rates. It includes features for booking trips with multiple destinations, adding new locations, and adjusting discount rates for both Basic and Enterprise customers. The system also handles various input validations and exceptions to ensure a smooth user experience.

## Features

1. **Book a Trip with Multiple Destinations:**
    - Customers can book trips to multiple destinations in a single booking.
    - The system calculates the total distance, applicable discounts, and the final cost of the trip.

2. **Add New Locations:**
    - Users can add new locations to the system.
    - The system ensures that the location name is a valid string.

3. **Adjust Discount Rate for Basic Customers:**
    - Administrators can adjust the discount rate for all Basic customers.
    - The system validates the input to ensure it is a positive number.

4. **Adjust Discount Rate for Enterprise Customers:**
    - Administrators can adjust the discount rate for individual Enterprise customers.
    - The system validates the customer ID or name and ensures the input rates are positive numbers.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/customer-trip-booking-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd customer-trip-booking-system
    ```

3. Install any necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to book trips, add locations, and adjust discount rates.

## Code Structure

- `main.py`: The main entry point of the application.
- `booking.py`: Contains the `Booking` class for handling trip bookings.
- `customer.py`: Contains the `Customer`, `BasicCustomer`, and `EnterpriseCustomer` classes.
- `location.py`: Contains the `Location` class for handling location data.
- `records.py`: Contains the `Records` class for managing customers and locations.
- `exceptions.py`: Contains custom exception classes for input validation.

## Sample Input and Output

### Book a Trip

1. **Input:**
    ```text
    Enter customer name: John Doe
    Enter departure location name: New York
    Enter destination location name: Los Angeles
    ```

2. **Output:**
    ```text
    Booking receipt:
    - Customer: John Doe
    - Departure: New York
    - Destinations: Los Angeles
    - Total Distance: 3940 miles
    - Discount: $200
    - Total Cost: $3600
    ```

### Add a New Location

1. **Input:**
    ```text
    Enter location ID: L10
    Enter location name: Chicago
    ```

2. **Output:**
    ```text
    Location Chicago added successfully.
    ```

### Adjust Discount Rate

1. **Input:**
    ```text
    Enter the new discount rate for Basic customers: 0.15
    ```

2. **Output:**
    ```text
    Discount rate updated successfully.
    ```



## Contact

For any inquiries or feedback, please contact Janak Nagwani at janak472@gmail.com.

---
