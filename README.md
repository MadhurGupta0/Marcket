
# E-Commerce Web Application with Product Recommendation System

This is a Django-based e-commerce web application featuring a product recommendation system powered by a machine learning model. The application uses Cython to optimize performance for computation-heavy tasks related to the recommendation engine. The app provides a user-friendly interface for product browsing, adding items to a cart, and checking out, along with viewing personalized product recommendations.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Cython Optimization](#How-to-Compile-Cython-Code)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- **Product Display**: Browse products with details such as name, description, price, and category.
- **User Cart and Checkout**: Add products to a shopping cart and proceed to checkout.
- **Product Recommendation System**: A machine learning model that recommends products to users based on behavior, product attributes, or collaborative filtering.
- **Cython Optimization**: Performance-critical parts of the recommendation system are optimized using Cython.
- **User Interaction**: Users can interact with the recommendation system by viewing recommended products, providing feedback, and seeing updated recommendations based on their actions.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **Machine Learning**: Scikit-Learn, Pandas, NumPy
- **Optimization**: Cython
- **Database**: SQLite (for development purposes)
- **Version Control**: Git, GitHub

## Requirements

- Python 3.8+
- Django 3.2+
- Cython
- NumPy, Pandas, Scikit-Learn
- Virtualenv (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>

cd ecommerce-app

```
### 2. Create a Virtual Environment
```bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
```
### 3. Install Dependencies

```
pip install -r requirements.txt
```
### 4. Run Migrations and Create a Superuser

```

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create a superuser for accessing the admin panel
```
### 5. Compile Cython Code
Ensure that Cython is installed and then compile the Cython modules:


```

cd ecommerce-app
python setup.py build_ext --inplace
```
### 6. Run the Development Server

```
python manage.py runserver
```
### 7. Access the Application
Open your web browser and go to http://localhost:8000/ to access the application.

## Usage
- **Browse Products:** View the list of available products on the home page.
- **Add to Cart:** Click on a product to view its details and add it to your shopping cart.
- **Checkout:** Go to the cart page and proceed to checkout to place an order.
- **View Recommendations:** The application provides personalized product recommendations based on user interactions and past behavior.
- **Provide Feedback:** Users can rate products and leave reviews, which are then used to improve the recommendation engine.
- **Cython Optimization:**
 The recommendation system involves computation-heavy tasks that have been optimized using Cython. This includes parts of the recommendation algorithm, such as data preprocessing, similarity calculations, and matrix operations.

## How to Compile Cython Code
To compile the Cython code, run the following command from the root directory:

bash
```
python setup.py build_ext --inplace
This will build the Cython extensions and integrate them with the Django application.
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
