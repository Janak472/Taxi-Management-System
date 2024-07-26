

#student Id S3975459
# Problems In code = in services.txt packages format is not working while services is working fine


class Service:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Service ID: {self.ID}")
        print(f"Service Name: {self.name}")
        print(f"Price: {self.price} (AUD)")

    def set_price(self, new_price):
        self.price = new_price

# This code defines a class called Service. It has an initialization method __init__ which takes three parameters: ID, name, and price. These parameters are used to initialize attributes
# of the Service object. The ID, name, and price attributes represent the unique identifier, name, and price (in AUD) of the service, respectively.
# The class has a method display_info which prints out information about the service including its ID, name, and price. Another method set_price allows for updating the price of the service.
# Overall, this class is designed to represent a basic service with attributes for identification, name, and price, along with methods to display information and modify the price.


class ExtraService:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Service Name: {self.name}")
        print(f"Price: {self.price} (AUD)")
        # The ExtraService class is designed to represent additional services that can be added to a customer's taxi ride. It contains two attributes: name for storing the service's name
# and price for its cost in AUD. The class also includes a method called display_info() which prints out the name and price of the extra service.
# This class provides a blueprint for creating and managing various additional services that customers can choose from during their ride.


class Customer:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def get_discount(self):
        pass

    def display_info(self):
        pass

#Default Discounts
DEFAULT_BASIC_DISCOUNT = 0.10
DEFAULT_ENTERPRISE_FIRST_RATE = 0.15
DEFAULT_ENTERPRISE_THRESHOLD = 100

class BasicCustomer(Customer):


    def __init__(self, ID, name, discount_rate=DEFAULT_BASIC_DISCOUNT):
        super().__init__(ID, name)
        self.discount_rate = discount_rate

    def get_discount(self, distance_fee):
        return self.discount_rate * distance_fee

    def display_info(self):
        print(f"Customer ID: {self.ID}")
        print(f"Customer Name: {self.name}")
        print(f"Discount Rate: {self.discount_rate}")

    def set_discount_rate(self, new_rate):
        self.discount_rate = new_rate



class EnterpriseCustomer(Customer):

    def __init__(self, ID, name, first_rate=DEFAULT_ENTERPRISE_FIRST_RATE, threshold=DEFAULT_ENTERPRISE_THRESHOLD):
        super().__init__(ID, name)
        self.first_rate = first_rate
        self.second_rate = first_rate + 0.05
        self.threshold = threshold

    def get_discount(self, distance_fee):
        if distance_fee < self.threshold:
            return self.first_rate * distance_fee
        else:
            return self.second_rate * distance_fee

    def display_info(self):
        print(f"Customer ID: {self.ID}")
        print(f"Customer Name: {self.name}")
        print(f"First Rate: {self.first_rate}")
        print(f"Second Rate: {self.second_rate}")
        print(f"Threshold: {self.threshold}")

    def set_discount_rates(self, first_rate, second_rate):
        self.first_rate = first_rate
        self.second_rate = second_rate

    def set_threshold(self, threshold):
        self.threshold = threshold

# This code defines two classes, Customer and two subclasses BasicCustomer and EnterpriseCustomer.
# The Customer class is a base class that initializes with an ID and a name. It has two methods, get_discount (which is not implemented and acts as a placeholder for subclasses to override)
# and display_info (also not implemented, serving as a placeholder for displaying customer information).
# The BasicCustomer class is a subclass of Customer. It inherits the ID and name attributes from its parent class. Additionally, it introduces a discount_rate attribute which is set to a
# default value of 0.10 (or 10%). The get_discount method is overridden to calculate the discount based on the distance_fee and the discount_rate. The display_info method is also overridden
# to display the customer's ID, name, and discount rate. It includes a set_discount_rate method to allow for updating the discount rate.
# The EnterpriseCustomer class is another subclass of Customer. Like BasicCustomer, it inherits the ID and name attributes. It introduces additional attributes like first_rate, second_rate,
# and threshold with default values based on constants defined at the top of the code. The get_discount method is overridden to calculate the discount based on distance_fee, taking into
# account the threshold. The display_info method is overridden to display the customer's ID, name, first rate, second rate, and threshold. It includes methods set_discount_rates and
# set_threshold to allow for updating these values.Overall, these classes provide a basic structure for representing different types of customers, each with their own way of calculating discounts and displaying information.



class Trip:
    def __init__(self, customer, rate_type, destinations):
        self.customer = customer
        self.rate_type = rate_type
        self.destinations = destinations

# The Trip class encapsulates information about a specific journey made by a customer. It comprises three essential attributes. Firstly, there's customer, ' \
# which holds details about the individual undertaking the trip, and it's expected to be an instance of the Customer class. Secondly, rate_type denotes the specific pricing scheme ' \
# 'applied to this trip, and it's anticipated to be an instance of the Rate class. Lastly, destinations refers to a collection of locations or destinations relevant to this trip.
# Although the exact structure of this attribute isn't outlined in this code snippet, it likely contains information about the various places involved in the journey. In summary,
# the Trip class acts as a container, consolidating details about a customer, their associated pricing rate, and the specific destinations associated with a single trip record.
class Package:
    def __init__(self, ID, name, services):
        self.ID = ID
        self.name = name
        self.services = services

    def compute_price(self, service_dict):
        total_price = sum(service_dict[service].price for service in self.services)
        return 0.8 * total_price

    def display_info(self, service_dict):
        print(f"Package ID: {self.ID}")
        print(f"Package Name: {self.name}")
        print("Services:")
        for service_id in self.services:
            service = service_dict.get(service_id)
            if service:
                print(f"  - {service.name}")
            else:
                print(f"  - Service with ID {service_id} not found")

# The provided code defines a Python class called Package. This class represents a bundled set of services and has three main attributes: ID, name, and services. The ID and name store unique identifiers and names for the package, respectively. Meanwhile, the services attribute is a list that contains the IDs of the individual services included in the package.
#The class incorporates two essential methods. Firstly, the compute_price(self, service_dict) method calculates the total price of all the services within the package. It requires a dictionary named service_dict to look up the prices of individual services. The total price is determined as 80% of the sum of the prices of all services in the package.
# Secondly, the display_info(self, service_dict) method is responsible for presenting information about the package. This includes its ID, name, and the list of services it encompasses. It also relies on the service_dict to look up the names of the individual services. The method prints out the package's ID and name, and subsequently iterates through the list of services, displaying their names. In the event that a service with a specific ID cannot be located in the service_dict, the user is notified.
# Overall, this class offers functionality to represent, calculate the price, and display information pertaining to a package of services.

class Location:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def display_info(self):
        print(f"Location ID: {self.ID}")
        print(f"Location Name: {self.name}")

# The Location class is responsible for representing specific locations. It contains two main attributes: ID for uniquely identifying the location and name to provide a descriptive label.
# The class also features a display_info method, which prints out details about the location, including its ID and name. This allows for easy retrieval and presentation of information about
# a particular location within the program.

class Rate:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Rate ID: {self.ID}")
        print(f"Rate Name: {self.name}")
        print(f"Price per km: {self.price} (AUD)")

# The Rate class is designed to represent different rate types used in the program. It contains three attributes: ID for uniquely identifying the rate, name to provide a descriptive label, and
# price to specify the cost per kilometer in Australian Dollars (AUD). The class also features a display_info method, which prints out details about the rate, including its ID, name, and price
# per kilometer. This method allows for easy retrieval and presentation of information about a specific rate within the program.

class Booking:
    def __init__(self, customer, departure, destination, distance, rate):
        self.customer = customer
        self.departure = departure
        self.destination = destination
        self.distance = distance
        self.rate = rate

    def compute_cost(self):
        # Retrieve the customer's discount
        discount = self.customer.get_discount(self.distance)

        # Calculate the basic fee (distance * rate price)
        basic_fee = self.distance * self.rate.price

        # Calculate the distance fee (if any)
        distance_fee = max(basic_fee - discount, 0)

        return distance_fee, basic_fee, discount

    def display_receipt(self):
        distance_fee, basic_fee, discount = self.compute_cost()
        total_cost = basic_fee + distance_fee - discount

        print("---------------------------------------------------------")
        print("Taxi Receipt")
        print("---------------------------------------------------------")
        print(f"Name: {self.customer.name}")
        print(f"Departure: {self.departure.name}")
        print(f"Destination: {self.destination.name}")
        print(f"Rate: {self.rate.name} (AUD per km)")
        print(f"Distance: {self.distance} (km)")
        print("---------------------------------------------------------")
        print(f"Basic fee: {basic_fee} (AUD)")
        print(f"Distance fee: {distance_fee} (AUD)")
        print(f"Discount: {discount} (AUD)")






        print("---------------------------------------------------------")

        # Initialize service_cost to 0
        service_cost = 0

        # Check if an extra service is ordered
        extra_service = input("Do you want to order an extra service/package? (y/n): ").lower()
        while extra_service not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
            extra_service = input("Do you want to order an extra service/package? (y/n): ").lower()
        if extra_service == 'y':
            while True:
                print("Available services/packages:")
                for index, service in enumerate(program.services, start=1):
                    print(f"{index}. {service.name} - ${service.price}")

                try:
                    service_choice = int(
                        input("Enter the number of the service/package you want to order (or 0 to skip): "))
                    if service_choice == 0:
                        break
                    elif 1 <= service_choice <= len(program.services):
                        service = program.services[service_choice - 1]
                        print(f"You ordered {service.name} for ${service.price}.")
                        service_cost = service.price  # Update service_cost with the selected service price
                        program.service = service  # Store the selected service
                        break
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        total_cost += service_cost
        print(f"Total cost: {total_cost} (AUD)")




# The Booking class manages the details of a taxi booking. This class represents a taxi booking and contains several attributes: customer, departure, destination, distance, and rate.
# These attributes store information about the customer making the booking, the departure location, the destination location, the distance to be traveled, and the rate charged per kilometer,
# respectively.The class has two important methods. Firstly, the compute_cost(self) method calculates the cost of the taxi ride. It begins by retrieving the customer's discount based on the
# provided distance. Next, it computes the basic fee, which is the product of the distance and the rate price. Then, it determines the distance fee, taking into account the discount. Finally,
# it returns the distance fee, basic fee, and discount.Secondly, the display_receipt(self) method is responsible for generating a receipt for the taxi ride. It utilizes the information
# gathered earlier to display various details such as the customer's name, departure and destination locations, the chosen rate, distance traveled, and associated fees. The receipt is
# formatted to provide clear information about the charges and discounts. Additionally, it offers the option to order extra services or packages, listing available options and their respective
# prices. The total cost is then updated to include the cost of any selected services.Overall, this class encapsulates the booking information, enables the computation of costs, and generates a detailed receipt for taxi rides.
class Records:
    def __init__(self):
        self.customers = []
        self.locations = []
        self.rate_types = []
        self.services = []
    def read_customers(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.strip().split(',')]
                customer_id = int(data[0])
                customer_name = data[1]
                customer_type = data[2]
                discount_rate = float(data[3])
                threshold = float(data[4]) if len(data) == 5 else None
                if customer_type == 'B':
                    customer = BasicCustomer(customer_id, customer_name, discount_rate)
                elif customer_type == 'E':
                    customer = EnterpriseCustomer(customer_id, customer_name, discount_rate, threshold)
                self.customers.append(customer)
    def add_customer(self, customer):
        try:
            with open('customers.txt', 'a') as file:
                if isinstance(customer, BasicCustomer):
                    customer_type = 'B'
                    discount_rate = customer.discount_rate
                    file.seek(2)
                    file.write(f"{customer.ID}, {customer.name}, {customer_type}, {discount_rate}\n")
                elif isinstance(customer, EnterpriseCustomer):
                    customer_type = 'E'
                    discount_rate = customer.first_rate
                    threshold = customer.threshold
                    file.seek(2)
                    file.write(f"{customer.ID}, {customer.name}, {customer_type}, {discount_rate}, {threshold}\n")
                # Write customer information to file
            self.customers.append(customer)  # Add customer to the list
            print(f"Customer {customer.name} added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def read_locations(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                location_id, location_name = [x.strip() for x in line.strip().split(',')]
                location = Location(location_id, location_name)
                self.locations.append(location)

    def read_rates(self, filename):
        with open(filename,'r') as file:
            for line in file:
                rate_id, rate_name, price_per_km = [x.strip() for x in line.strip().split(',')]
                rate = Rate(rate_id, rate_name, float(price_per_km))
                self.rate_types.append(rate)

    def read_services(self, filename):
        with open(filename, 'r') as file:
            reading_packages = False
            for line in file:
                data = [x.strip() for x in line.strip().split(',')]
                service_id = data[0]
                service_name = data[1]
                service_price = float(data[2])

                if service_id[0] == 'S':
                    service = Service(service_id, service_name, service_price)
                elif service_id[0] == 'P':
                    components = [self.find_service(service_id) for service_id in data[2:]]
                    service = Package(service_id, service_name, components)

                self.services[service_id] = service

    def display_existing_services(self):
        print("{:<10} {:<15} {}".format("ID", "Name", "Price"))
        for service_id, service in self.services.items():
            print("{:<10} {:<15} {}".format(service.ID, service.name, service.price))



        self.services[service.ID] = service
    def find_service(self, search_value):
        for service in self.services:
            if str(search_value) in (str(service.ID), service.name):
                return service
        return None
    def find_customer(self, search_value):
        for customer in self.customers:
            if str(search_value) in (str(customer.ID), customer.name):
                return customer
        return None

    def find_location(self, search_value):
        for location in self.locations:
            if (search_value) == location.ID or (search_value) == location.name:
                return location
        return None

    def find_rate(self, search_value):
        for rate_type in self.rate_types:
            if str(search_value) in [rate_type.ID, rate_type.name]:
                return rate_type
        return None

    def list_customers(self):
        print("{:<10} {:<15} {:<10} {:<20} {}".format("ID", "Name", "Type", "Discount Rate", "Threshold"))
        for customer in self.customers:
            if isinstance(customer, BasicCustomer):
                print(
                    "{:<10} {:<15} {:<10} {:<20} {}".format(customer.ID, customer.name, "Basic", customer.discount_rate,
                                                            ""))
            elif isinstance(customer, EnterpriseCustomer):
                print("{:<10} {:<15} {:<10} {:<20} {:<10}".format(customer.ID, customer.name, "Enterprise",
                                                                  customer.first_rate,
                                                                  customer.threshold if hasattr(customer,
                                                                                                'first_rate') else ""))

    def add_location(self, location):
        try:
            if not location.name.isalpha():
                raise ValueError("Location name must contain only alphabetic characters.")

            with open('locations.txt', 'a') as file:
                # Write location information to file
                file.write(f"\n{location.ID}, {location.name}")

            self.locations.append(location)  # Add location to the list
            print(f"Location {location.name} added successfully.")
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid location name.")

    def list_services(self):
        print("{:<10} {:<15} {}".format("ID", "Name", "Price"))
        for service in self.services:
            print("{:<10} {:<15} {}".format(service.ID, service.name, service.price))
    def list_locations(self):
        print("{:<10} {}".format("ID", "Name"))
        for location in self.locations:
            print("{:<10} {}".format(location.ID, location.name))

    def list_rates(self):
        print("{:<10} {:<15} {}".format("ID", "Name", "Price per km"))
        for rate_type in self.rate_types:
            print("{:<10} {:<15} {}".format(rate_type.ID, rate_type.name, rate_type.price))

    def add_service(self, value):
        try:
            if isinstance(value, Service):
                service_id = value.ID
            elif isinstance(value, Package):
                service_id = value.ID
            else:
                raise ValueError("Invalid value type. Must be Service or Package.")

            # Check if the service already exists
            if service_id in self.services:
                raise ValueError(f"Service with ID {service_id} already exists.")

            self.services[service_id] = value

            with open('services.txt', 'a') as file:
                # Write service information to file
                file.write(f"\n{service_id}, {value.name}, {value.price}")

            print(f"Service {value.name} added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def adjust_discount_for_basic(self):
        try:
            new_rate = float(input("Enter the new discount rate for Basic customers: "))
            if new_rate <= 0:
                raise ValueError("Invalid rate")
            for customer in self.customers:
                if isinstance(customer, BasicCustomer):
                    customer.discount_rate = new_rate
            print("Discount rate updated successfully.")
        except ValueError as e:
            print(e)
            self.adjust_discount_for_basic()

    def adjust_discount_for_enterprise(self):
        try:
            customer_id_or_name = input("Enter the ID or name of the Enterprise customer: ")
            new_rate = float(input("Enter the new first discount rate: "))
            if new_rate <= 0:
                raise ValueError("Invalid rate")

            found = False
            for customer in self.customers:
                if (str(customer_id_or_name) == str(
                        customer.ID) or customer_id_or_name == customer.name) and isinstance(customer,
                                                                                             EnterpriseCustomer):
                    customer.first_rate = new_rate
                    found = True
                    break

            if not found:
                raise ValueError("Invalid customer")

            print("First discount rate updated successfully.")
        except ValueError as e:
            print(e)
            self.adjust_discount_for_enterprise()

# The `Records` class functions as a comprehensive container for managing customer data, locations, rate types, and services/packages. It encompasses methods to read and write data to files and
# conduct various operations on these records. To begin, the `read_customers` method extracts customer data from a file, interprets it, and creates instances of either `BasicCustomer` or
# `EnterpriseCustomer` based on customer type. These instances are subsequently added to the list of customers. The `add_customer` method facilitates the addition of a customer to the list and
# appends their details to a file, appropriately handling customer type-specific information. Meanwhile, `read_locations` reads location data from a file, generating `Location` instances that
# are incorporated into the list of locations. Similarly, `read_rates` processes rate type data from a file, creating `Rate` instances that join the list of rate types. The `read_services`
# method parses service/package data from a file. Depending on the ID prefix, it generates a `Service` or a `Package` instance, including any components if
# it's a package. `display_existing_services` provides a formatted list of existing services, presenting their ID, name, and price. Methods such as `find_service`, `find_customer`,
# `find_location`, and `find_rate` facilitate targeted searches for specific records based on provided search values, returning the respective record or `None` if not found.
# Additionally, `list_customers`, `list_locations`, `list_services`, and `list_rates` deliver formatted lists of customers, locations, services, and rate types, respectively. `add_location`
# manages the addition of a location to the list and appends its information to a file. Finally, `add_service` enables the addition of a service or package to the list, appending its details
# to a file. The `adjust_discount_for_basic` and `adjust_discount_for_enterprise` methods allow for the modification of discount rates for basic and enterprise customers, respectively.
# Overall, the `Records` class serves as a centralized hub for various types of records, offering methods for reading, writing, and manipulating the data effectively.

class InvalidNameError(Exception):
    pass

class InvalidLocationError(Exception):
    pass

class InvalidRateTypeError(Exception):
    pass

class InvalidDistanceError(Exception):
    pass
class Operations:
    def __init__(self):
        self.records = Records()
        self.services = []
        self.bookings = []

    def load_data(self):
        try:
            self.records.read_customers('customers.txt')
            self.records.read_locations('locations.txt')
            self.records.read_rates('rates.txt')
            self.load_services('services.txt')  # Load services/packages
        except FileNotFoundError as e:
            print(f"Error: {e.filename} not found. Please make sure the file exists.")
            exit(1)

    def load_services(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                service_id, service_name, service_price = line.strip().split(', ')
                service_id = f"S{len(self.services) + 1}"  # Generating a unique ID
                self.services.append(Service(service_id, service_name, float(service_price)))

    def book_trip(self):
        while True:
            try:
                customer_name = input("Enter customer name: ")
                if not customer_name.isalpha():
                    raise InvalidNameError("Invalid name. Names should only contain alphabet characters.")

                departure = None
                destination = None

                while departure is None or destination is None or departure == destination:
                    while True:
                        departure_name = input("Enter departure location name: ")

                        if not departure_name.isalpha():
                            print("Invalid location name. Please enter a name with alphabetic characters.")
                        else:
                            break

                    if not self.records.find_location(departure_name):
                        add_new_location = input(
                            "Location not found. Do you want to add a new location? (y/n): ").lower()
                        if add_new_location == 'y':
                            new_location_id = f"L{len(self.records.locations) + 1}"
                            new_location_name = departure_name  # Use the entered location name

                            # Create a new Location object
                            new_location = Location(new_location_id, new_location_name)
                            self.records.locations.append(new_location)

                            # Save the new location to the file
                            with open('locations.txt', 'a') as file:
                                file.write(f"{new_location_id}, {new_location_name}\n")

                            departure = new_location
                        else:
                            return
                    else:
                        departure = self.records.find_location(departure_name)
                    while True:
                        destination_name = input("Enter destination location name: ")

                        if not destination_name.isalpha():
                            print("Invalid location name. Please enter a name with alphabetic characters.")
                        else:
                            break
                    if not self.records.find_location(destination_name):
                        add_new_location = input(
                            "Location not found. Do you want to add a new location? (y/n): ").lower()
                        if add_new_location == 'y':
                            new_location_id = f"L{len(self.records.locations) + 1}"
                            new_location_name = destination_name  # Use the entered location name

                            # Create a new Location object
                            new_location = Location(new_location_id, new_location_name)
                            self.records.locations.append(new_location)

                            # Save the new location to the file
                            with open('locations.txt', 'a') as file:
                                file.write(f"{new_location_id}, {new_location_name}\n")

                            destination = new_location
                        else:
                            return
                    else:
                        destination = self.records.find_location(destination_name)

                    if departure is None or destination is None or departure == destination:
                        print("Invalid locations. Please enter valid departure and destination locations.")

                if departure is None:
                    raise InvalidLocationError(f"Invalid departure location: {departure_name}")

                if destination is None:
                    raise InvalidLocationError(f"Invalid destination location: {destination_name}")

                if departure == destination:
                    raise InvalidLocationError("Departure and destination cannot be the same.")

                while True:
                    try:
                        distance = float(input("Enter distance (in km): "))
                        if distance <= 0:
                            raise ValueError("Distance must be a positive number.")
                        break
                    except ValueError:
                        print("Invalid input. Distance must be a number greater than 0.")

                customer = self.records.find_customer(customer_name)
                rate_name = input("Enter rate type name: ")
                rate = self.records.find_rate(rate_name)

                if customer is None:
                    add_new_customer = input("Customer not found. Do you want to add a new customer? (y/n): ").lower()
                    if add_new_customer == 'y':
                        new_customer_id = int(input("Enter customer ID: "))
                        new_customer_name = input("Enter customer name: ")
                        while True:
                            new_customer_type = input("Enter customer type (B for Basic, E for Enterprise): ").upper()
                            if new_customer_type not in ['B', 'E']:
                                print("Invalid customer type. Please enter B for Basic or E for Enterprise.")
                            else:
                                break
                        if new_customer_type == 'B':
                            new_discount_rate = float(input(f"Enter discount rate (press Enter for default: {DEFAULT_BASIC_DISCOUNT}): ") or DEFAULT_BASIC_DISCOUNT)
                            new_customer = BasicCustomer(new_customer_id, new_customer_name, new_discount_rate)
                        elif new_customer_type == 'E':
                            new_first_rate = float(input(f"Enter first rate (press Enter for default: {DEFAULT_ENTERPRISE_FIRST_RATE}): ") or DEFAULT_ENTERPRISE_FIRST_RATE)
                            new_threshold = float(input(f"Enter threshold (press Enter for default: {DEFAULT_ENTERPRISE_THRESHOLD}): ") or DEFAULT_ENTERPRISE_THRESHOLD)
                            new_customer = EnterpriseCustomer(new_customer_id, new_customer_name, new_first_rate,
                                                              new_threshold)
                        else:
                            print("Invalid customer type. Please enter B for Basic or E for Enterprise.")
                            return

                        self.records.add_customer(new_customer)
                        customer = new_customer

                    else:
                        return

                if rate is None:
                    add_new_rate = input("Rate type not found. Do you want to add a new rate type? (y/n): ").lower()
                    if add_new_rate == 'y':
                        new_rate_id = f"R{len(self.records.rate_types) + 1}"
                        new_rate_name = input("Enter rate type name: ")
                        new_rate_price = float(input("Enter price per km: "))

                        # Create a new Rate object
                        new_rate = Rate(new_rate_id, new_rate_name, new_rate_price)
                        self.records.rate_types.append(new_rate)
                        # Add the new rate to the list and save it to the file
                        self.records.rate_types.append(new_rate)
                        with open('rates.txt', 'a') as file:
                            file.write(f"{new_rate_id}, {new_rate_name}, {new_rate_price}\n")

                        rate = new_rate  # Set rate to the new rate

                booking = Booking(customer, departure, destination, distance, rate)
                booking.display_receipt()


                if isinstance(customer, BasicCustomer) and customer not in self.records.customers:
                    self.records.customers.append(customer)

                break  # Exit the loop if the entire booking process is successful

            except (
                    ValueError, InvalidNameError, InvalidLocationError, InvalidRateTypeError,
                    InvalidDistanceError) as e:
                print(f"Error: {e}")

    def order_extra_service(self):
        while True:  # Add a loop here
            print("Available services/packages:")
            for index, service in enumerate(self.services, start=1):
                print(f"{index}. {service.name} - ${service.price}")

            try:
                service_choice = int(input("Enter the number of the service/package you want to order: "))
                if 1 <= service_choice <= len(self.services):
                    service = self.services[service_choice - 1]
                    print(f"You ordered {service.name} for ${service.price}.")
                    self.service = service  # Store the selected service
                    break  # Exit the loop after a valid choice
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_customers(self):
        self.records.list_customers()

    def display_locations(self):
        self.records.list_locations()

    def display_rates(self):
        self.records.list_rates()

    def display_services(self):
        print("{:<10} {:<20} {}".format("ID", "Name", "Price (AUD)"))
        for service in self.services:
            print("{:<10} {:<20} {}".format(service.ID, service.name, service.price))

    def start(self):
        self.load_data()

        while True:
            print("\nMenu:")
            print("1. Book a trip")
            print("2. Display existing customers")
            print("3. Display existing locations")
            print("4. Display existing rate types")
            print("5. Display existing services")
            print("6. Exit the program")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.book_trip()
            elif choice == '2':
                self.display_customers()
            elif choice == '3':
                self.display_locations()
            elif choice == '4':
                self.display_rates()
            elif choice == '5':
                self.display_services()
            elif choice == '6':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
# The `Operations` class orchestrates various operations within the program. It encompasses functionalities for loading data, booking trips, ordering extra services, displaying information
# about customers, locations, rates, and services, as well as handling the program's main menu. The `load_data` method initiates the loading of customer, location, and
# rate data from their respective files, as well as services/packages through the `load_services` method. This operation is safeguarded against a `FileNotFoundError`. The `load_services`
# method processes service/package data, generating unique IDs and appending instances to the list of services. The `book_trip` function enables the user to book a trip by inputting customer
# information, departure and destination locations, distance, and rate type. It guides the user through possible scenarios and validates user inputs, ensuring accurate and meaningful data.
# The `order_extra_service` method allows the user to select additional services or packages to include in the booking. It displays available options and handles user input to finalize the
# selection. Functions like `display_customers`, `display_locations`, `display_rates`, and `display_services` provide formatted lists of existing customers, locations, rates, and services
# respectively. Lastly, the `start` method serves as the main menu, offering options for booking a trip, viewing existing data, or exiting the program. It continuously prompts the user for
# input until the exit option is chosen. Overall, the `Operations` class serves as the control center, overseeing the execution of key functionalities within the program.

# Instantiate and run the program
program = Operations()
program.start()


#References

# Classes and Objects:
#
# Python Classes and Objects = https://docs.python.org/3/tutorial/classes.html

# Inheritance:
#
# Inheritance in Python = https://docs.python.org/3/tutorial/classes.html#inheritance
# GeeksforGeeks - Inheritance in Python = https://www.geeksforgeeks.org/inheritance-in-python/
# Polymorphism:
#
# GeeksforGeeks - Polymorphism in Python = https://www.geeksforgeeks.org/polymorphism-in-python/
# File Handling:
#
# Python File Handling = https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# W3Schools - Python File Handling = https://www.w3schools.com/python/python_file_handling.asp
# Error Handling (try...except): https://docs.python.org/3/tutorial/errors.html
#
# Python Errors and Exceptions
# Python Exception Handling :https://docs.python.org/3/tutorial/errors.html
# String Formatting:
#
# Python String Formatting
# Lists and Dictionaries:https://docs.python.org/3/tutorial/datastructures.htmls
#
# Python Data Structures
# File I/O:https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#
# Python File I/O
# Lambda Functions:https://www.w3schools.com/python/python_lambda.asp
#
# Python Lambda Functions
# String Methods:https://www.w3schools.com/python/ref_string.asp
#
# Python String Methods
# Flow Control (if...else, for loops):https://docs.python.org/3/tutorial/controlflow.html
#
# Python Control Flow :https://docs.python.org/3/tutorial/controlflow.html

