## **Ecommerce Backend**

**Description:**

This repository contains the backend code for a robust and scalable ecommerce platform. It handles core functionalities such as product management, order processing, user authentication, payment integration, and inventory control.
Built by Rokari-19

**Features:**

* **Product Management:**
  * Create, edit, and delete products
  * Manage product categories and attributes
  * Set product pricing and availability
* **Order Processing:**
  * Accept and process customer orders
  * Calculate shipping costs and taxes
  * Handle order status updates and notifications via email
* **User Authentication:**
  * Allow users to create accounts and log in
  * Implement secure password hashing and storage
* **Payment Integration:**
  * Stripe integrated payment gateway
  * Handle secure payment processing and transaction management
  * custom logic for converting local currencies to dollar (e.g naira to dollar)
* **Inventory Control:**
  * Track product stock levels and manage inventory adjustments
  * Implement low-stock alerts and automatic reorder processes

**Technologies:**

* **Backend Framework:** Django Rest Framework
* **Database:** SQLite3 database (a postgres db can also be configured for this project, see railway.com for details on django and railway)
* **API:** RESTapi
* **Other Technologies:** Stripe payment gateway for secure purchases on the site

**Installation:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rokari-19/Ecommerce-Back-end.git
   ```
   
2. **Configure virtual environment:**
   ```bash
   python3 -m venv 'path/to/venv
   
4. **Install dependencies:**
   ```bash
   cd Ecommerce-Back-end
   pip3 install -r requirements.txt
   ```
5. **Start the server:**
   ```bash
   python3 manage.py runserver
   ```
**Contributing:**

* **Fork the repository.**
* **Create a new branch.**
* **Make your changes.**
* **Submit a pull request.**
