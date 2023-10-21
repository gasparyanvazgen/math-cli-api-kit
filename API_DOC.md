# Math CLI API Kit - API Documentation

This documentation provides detailed information on the endpoints and their usage for the Math CLI API Kit.

**API Version**: 0.1.0-beta

## Endpoints

### Algebraic Operations

#### Addition
- **URL**: `/api/math/api/algebra/sum`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the first number.
  - `y`: Represents the second number.
- **Response**: Provides the sum of `x` and `y`.

#### Subtraction
- **URL**: `/api/math/api/algebra/sub`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the minuend.
  - `y`: Represents the subtrahend.
- **Response**: Provides the result of subtracting `y` from `x`.

#### Multiplication
- **URL**: `/api/math/api/algebra/mul`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the first factor.
  - `y`: Represents the second factor.
- **Response**: Provides the product of `x` and `y`.

#### Division
- **URL**: `/api/math/api/algebra/div`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the dividend.
  - `y`: Represents the divisor.
- **Response**: Provides the result of dividing `x` by `y`.

#### Powers
- **URL**: `/api/math/api/algebra/pow`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the base.
  - `y`: Represents the exponent.
- **Response**: Provides the result of raising `x` to the power of `y`.

#### Square Root
- **URL**: `/api/math/api/algebra/square_root`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the number for which the square root is to be found.
- **Response**: Provides the square root of `x`.

#### Factorial
- **URL**: `/api/math/api/algebra/factorial`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the number for which the factorial is to be found.
- **Response**: Provides the factorial of `x`.

#### Exponential Function
- **URL**: `/api/math/api/algebra/exp`
- **Method**: `POST`
- **Request Body**:
  - `x`: Represents the exponent.
- **Response**: Provides the exponential function of `x`.

### Geometric Operations

#### Surface Area of a Square
- **URL**: `/api/math/api/geometry/surface_of_square`
- **Method**: `POST`
- **Request Body**:
  - `a`: Represents the length of a side of the square.
- **Response**: Provides the surface area of the square.

#### Surface Area of a Circle
- **URL**: `/api/math/api/geometry/surface_of_circle`
- **Method**: `POST`
- **Request Body**:
  - `r`: Represents the radius of the circle.
- **Response**: Provides the surface area of the circle.

#### Surface Area of a Triangle
- **URL**: `/api/math/api/geometry/surface_of_triangle`
- **Method**: `POST`
- **Request Body**:
  - `b`: Represents the length of the base of the triangle.
  - `h`: Represents the height of the triangle.
- **Response**: Provides the surface area of the triangle.

#### Surface Area of a Trapezoid
- **URL**: `/api/math/api/geometry/surface_of_trapezoid`
- **Method**: `POST`
- **Request Body**:
  - `a`: Represents the length of one of the parallel sides of the trapezoid.
  - `b`: Represents the length of the other parallel side of the trapezoid.
  - `h`: Represents the height of the trapezoid.
- **Response**: Provides the surface area of the trapezoid.

#### Length of the Hypotenuse
- **URL**: `/api/math/api/geometry/hypotenuse`
- **Method**: `POST`
- **Request Body**:
  - `a`: Represents the length of one of the triangle's legs.
  - `b`: Represents the length of the other triangle's leg.
- **Response**: Provides the length of the hypotenuse.

## Example Usage

### Using Python

The Python `requests` library can be used to make POST requests to these endpoints. Here's an example of using Python to calculate the sum of two numbers:

```python
import requests

url = 'http://localhost:8000/api/math/api/algebra/sum'

data = {
    'x': 5,
    'y': 3
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    if response.status_code is 200:
        result = response.json()['results']
        print(f'Sum of two numbers: {result}')
    else:
        print('Error:', response.json()['message'])

except requests.exceptions.RequestException as e:
    print('Network error:', e)
```

### Using JavaScript

In JavaScript, you can use the `fetch` API to make POST requests to these endpoints. Here's an example of using JavaScript to calculate the surface area of a square:

```javascript
const url = 'http://localhost:8000/api/math/api/geometry/surface_of_square';

const data = {
    'a': 4
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
    .then(response => {
        if (!response.ok) {
            throw an Error(`Error: ${response.status} - ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        const result = data.result;
        console.log(`Surface area of the square: ${result}`);
    })
    .catch(error => {
        console.error('Network error:', error);
    });
}
```
