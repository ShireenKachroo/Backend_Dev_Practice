# BACKEND DEVELOPMENT

---

## 1. CLIENT-SERVER ARCHITECTURE

**CLIENT:** Requests a service from the server.

**SERVER:** A program running on a machine/infra that receives requests, processes them, and sends responses.

**DATABASE:** Persistent storage for application data.

```text
CLIENT
   |
   | HTTP REQUEST
   ↓
SERVER / BACKEND
   |
   +-------> DATABASE
   |
   ↓
HTTP RESPONSE
   |
CLIENT
```

### BACKEND

Backend is the server-side part of an application responsible for:

* Processing client requests
* Applying business logic
* Validating data
* Authentication and authorization
* Communicating with databases
* Communicating with external services/APIs
* Returning responses to clients

---

## 2. API — APPLICATION PROGRAMMING INTERFACE

**API:** An interface/contract through which one software component interacts with another.

Typical application flow:

```text
FRONTEND
   ↓
  API
   ↓
BACKEND
   ↓
DATABASE / OTHER SERVICES
```

An API defines:

* What can be requested
* How it should be requested
* What response will be returned

### API vs BACKEND

**API ≠ Backend**

The API is the **interface exposed by the backend**.

The backend contains the actual:

* Business logic
* Data processing
* Authentication
* Database interaction
* Services

---

## 3. HTTP — HYPERTEXT TRANSFER PROTOCOL

HTTP is a standardized protocol that defines how clients and servers communicate through **requests and responses**.

### HTTP REQUEST

**METHOD + URL/PATH + HEADERS + BODY**

### HTTP RESPONSE

**STATUS CODE + HEADERS + BODY**

### COMMON HTTP METHODS

| Method | Purpose                       |
| ------ | ----------------------------- |
| GET    | Retrieve data                 |
| POST   | Create/submit data            |
| PUT    | Completely replace a resource |
| PATCH  | Partially update a resource   |
| DELETE | Delete a resource             |

---

## 4. HTTP REQUEST COMPONENTS

### PATH / URL

Identifies the resource or endpoint being accessed.

Path parameters can identify a specific resource.

Example concept:

`/students/101`

Here, `101` identifies a particular student.

### QUERY PARAMETERS

Used to:

* Filter
* Search
* Sort
* Paginate
* Refine

Example concept:

`/students?department=CSE`

**Path → identifies the resource**

**Query → filters/refines the resource**

### HEADERS

Carry metadata or instructions about the request.

Common uses:

* Authentication information
* Content type
* Caching information
* Client information

### BODY

Contains data sent to the server.

Commonly used with:

* POST
* PUT
* PATCH

---

## 5. HTTP STATUS CODES

Status codes communicate the result of an HTTP request.

### 2xx — SUCCESS

**200 OK**
Request succeeded.

**201 CREATED**
A new resource was successfully created.

**204 NO CONTENT**
Request succeeded but there is no response body.

### 4xx — CLIENT ERROR

**400 BAD REQUEST**
The request is invalid.

**401 UNAUTHORIZED**
The client has not been successfully authenticated.

**403 FORBIDDEN**
The client is authenticated but does not have permission.

**404 NOT FOUND**
The requested resource does not exist.

### 5xx — SERVER ERROR

**500 INTERNAL SERVER ERROR**
An unexpected error occurred on the server.

---

## 6. IDEMPOTENCY

An operation is **idempotent** when making the same request multiple times produces the same intended final state.

### Generally

**GET → Idempotent**

Repeatedly reading data does not change the data.

**PUT → Idempotent**

Repeatedly replacing a resource with the same representation results in the same final state.

**DELETE → Generally Idempotent**

Repeated deletion does not change the final state after the resource has already been deleted.

**POST → Generally NOT Idempotent**

Repeated POST requests can create multiple resources.

---

## 7. REST — REPRESENTATIONAL STATE TRANSFER

REST is an **architectural style** for designing web APIs.

### RESOURCE-ORIENTED DESIGN

REST APIs are generally designed around resources rather than actions.

Examples of resources:

* Students
* Products
* Orders
* Users

HTTP methods express the operation performed on the resource.

### REST API PATTERN

| Operation        | Endpoint         | Method |
| ---------------- | ---------------- | ------ |
| Get all students | `/students`      | GET    |
| Create student   | `/students`      | POST   |
| Get one student  | `/students/{id}` | GET    |
| Update student   | `/students/{id}` | PATCH  |
| Delete student   | `/students/{id}` | DELETE |

### STATELESSNESS

Each request should contain the information necessary for the server to process it.

Statelessness does **not** mean that the application cannot have state.

The database can still maintain persistent application state.

It means that the server should not depend on hidden conversational state from previous requests to understand the current request.

---

# FASTAPI

---

## 8. FASTAPI

**FastAPI:** A Python web framework used for building APIs and backend applications.

FastAPI provides:

* Routing
* Request handling
* Data validation
* Automatic API documentation
* Dependency Injection
* HTTP exception handling
* Async support
* Security utilities

### ROUTES / ENDPOINTS

A route connects an HTTP method and URL path to a Python function.

General flow:

```text
HTTP REQUEST
     ↓
METHOD + PATH
     ↓
MATCHING ROUTE
     ↓
PYTHON FUNCTION
     ↓
RESPONSE
```

---

## 9. UVICORN

**Uvicorn:** An ASGI server used to run FastAPI applications.

```text
FASTAPI APPLICATION
        ↓
     UVICORN
        ↓
      SERVER
        ↓
HTTP REQUESTS
```

FastAPI defines the application's behavior.

Uvicorn provides the server/runtime layer that runs the application and handles incoming connections.

### DEVELOPMENT MODE

Auto-reload can restart the development server when code changes.

---

## 10. SWAGGER / OPENAPI

FastAPI automatically generates API documentation using **OpenAPI**.

Swagger UI provides an interactive interface to:

* View endpoints
* View request parameters
* View request/response schemas
* Send requests
* Test APIs

FastAPI's default Swagger UI is available at:

`/docs`

---

# PYDANTIC & DATA VALIDATION

---

## 11. PYDANTIC

**Pydantic:** A Python library used for data validation and structured data models.

In FastAPI, Pydantic models are commonly used for:

* Request bodies
* Response structures
* Data types
* Validation rules

### REQUEST VALIDATION FLOW

```text
CLIENT JSON
    ↓
PYDANTIC MODEL
    ↓
VALIDATION
    ↓
VALID DATA
    ↓
ENDPOINT FUNCTION
```

If incoming data does not satisfy the model, FastAPI rejects it before normal endpoint logic runs.

### IMPORTANT

**Pydantic ≠ JSON**

**JSON** is a data format.

**Pydantic** is a Python validation/modeling tool that can parse and validate structured data.

---

## 12. REQUEST BODY

The request body contains structured data sent by the client to the server.

It is commonly used with:

* POST
* PUT
* PATCH

General flow:

```text
CLIENT
   ↓
JSON BODY
   ↓
PYDANTIC MODEL
   ↓
VALIDATION
   ↓
BACKEND LOGIC
```

---

## 13. RESPONSE MODELS

A response model defines the structure of data that an API should return.

Benefits:

* Consistent API responses
* Response validation
* Prevention of accidental extra fields
* Clear API documentation
* Separation between internal data and API output

General flow:

```text
BACKEND LOGIC
      ↓
RESPONSE MODEL
      ↓
VALIDATED RESPONSE
      ↓
CLIENT
```

---

# CRUD & API OPERATIONS

---

## 14. CRUD

CRUD represents the four basic operations performed on data.

| Operation | HTTP Method | Meaning             |
| --------- | ----------- | ------------------- |
| CREATE    | POST        | Create a resource   |
| READ      | GET         | Retrieve a resource |
| UPDATE    | PATCH / PUT | Modify a resource   |
| DELETE    | DELETE      | Remove a resource   |

CRUD is a **data operation concept**, not something exclusive to FastAPI or REST.

---

## 15. PATH PARAMETERS VS QUERY PARAMETERS

### PATH PARAMETERS

Used when the value identifies **which resource** we are referring to.

Example:

`/students/101`

→ Refers to student `101`.

### QUERY PARAMETERS

Used when the value **filters or refines** a collection.

Example:

`/students?department=CSE`

→ Returns students belonging to CSE.

### MENTAL MODEL

**PATH = IDENTITY**

**QUERY = FILTERING / REFINEMENT**

---

## 16. ERROR HANDLING

Successful operations generally **return** a response.

Errors are explicitly raised using an HTTP exception mechanism.

### SUCCESS

```text
REQUEST
   ↓
SUCCESS
   ↓
RETURN RESPONSE
```

### ERROR

```text
REQUEST
   ↓
ERROR CONDITION
   ↓
RAISE HTTP EXCEPTION
   ↓
ERROR RESPONSE
```

Raising an exception stops normal execution of the endpoint and produces an error response.

### COMMON EXAMPLES

**Resource exists → Return the resource**

**Resource does not exist → Raise 404**

---

## 17. PATCH — PARTIAL UPDATE

PATCH is used when only some fields of a resource need to be modified.

Example:

```text
Existing Student:
Name = Shireen
Department = CSE

PATCH:
Department = AI/ML

Result:
Name = Shireen
Department = AI/ML
```

Only the supplied fields should be changed.

### IMPORTANT CONCEPT

A PATCH request must distinguish between:

**Field not provided**

and

**Field explicitly provided**

This allows the backend to update only the fields the client actually wants to change.

---

# DEPENDENCY INJECTION

---

## 18. DEPENDENCY INJECTION

**Dependency Injection (DI):**

Instead of an endpoint creating or obtaining a required component itself, the framework provides or **injects** that dependency.

### CONCEPT

```text
ENDPOINT
   ↓
"I NEED X"
   ↓
DEPENDENCY SYSTEM
   ↓
PROVIDES X
   ↓
ENDPOINT USES X
```

FastAPI uses `Depends()` for Dependency Injection.

### WHY DI?

DI allows common functionality to be:

* Reused
* Centralized
* Maintained easily
* Shared across endpoints
* Tested more easily

### COMMON REAL-WORLD DEPENDENCIES

* Current user
* Database session
* Authentication checks
* Authorization checks
* Common validation
* Permissions

### MENTAL MODEL

**Dependency = Something an endpoint needs**

**Injection = Framework provides it to the endpoint**

---

# MIDDLEWARE

---

## 19. MIDDLEWARE

Middleware is a layer that runs around the **request/response lifecycle**.

```text
CLIENT
   ↓
REQUEST
   ↓
MIDDLEWARE
   ↓
ENDPOINT
   ↓
MIDDLEWARE
   ↓
RESPONSE
   ↓
CLIENT
```

Middleware is useful for logic that should apply broadly across requests.

### COMMON USE CASES

* Logging
* Request timing
* CORS
* Monitoring
* Request/response processing
* Some authentication-related processing

### MIDDLEWARE VS DEPENDENCY

**Dependency:**

Usually attached to a particular endpoint/router and provides something the endpoint needs.

**Middleware:**

Sits in the request/response pipeline and can operate across many or all requests.

---

# ASYNCHRONOUS PROGRAMMING

---

## 20. SYNCHRONOUS VS ASYNCHRONOUS

### SYNCHRONOUS

Execution waits for the current operation to finish before continuing.

```text
TASK A
  ↓
WAIT
  ↓
TASK A FINISHES
  ↓
TASK B
```

### ASYNCHRONOUS

While an I/O operation is waiting, the system can work on other tasks.

```text
TASK A → WAITING FOR I/O
              ↓
           TASK B
              ↓
           TASK C
              ↓
       TASK A COMPLETES
```

### ASYNC IS MOST USEFUL FOR I/O-BOUND WORK

Examples:

* Database calls
* Network requests
* External APIs
* File I/O

### CPU-BOUND WORK

Async alone is generally not the solution for heavy CPU computation.

Examples:

* Large ML computations
* Complex numerical computations
* Video encoding

### `async def` AND `await`

**`async def`** defines an asynchronous function.

**`await`** waits for an asynchronous operation without blocking the event loop in the usual async model.

For our current backend level, understanding the mental model is more important than learning the internals of event loops and coroutines.

---

# AUTHENTICATION & AUTHORIZATION

---

## 21. AUTHENTICATION VS AUTHORIZATION

### AUTHENTICATION

> **Who are you?**

Authentication verifies the identity of a user.

```text
USERNAME + PASSWORD
        ↓
AUTHENTICATION
        ↓
"USER IS SHIREEN"
```

### AUTHORIZATION

> **What are you allowed to do?**

Authorization determines what an authenticated user is allowed to access or perform.

```text
USER = SHIREEN
      ↓
AUTHORIZATION
      ↓
ALLOWED / NOT ALLOWED
```

### EASY DISTINCTION

**Authentication → Identity**

**Authorization → Permissions**

---

## 22. BASIC AUTHENTICATION

HTTP Basic Authentication is a standard HTTP authentication mechanism that sends username and password credentials with a request.

General flow:

```text
CLIENT
   ↓
USERNAME + PASSWORD
   ↓
AUTHENTICATION
   ↓
VERIFY CREDENTIALS
   ↓
VALID → ACCESS
INVALID → 401 UNAUTHORIZED
```

FastAPI provides security utilities for extracting Basic Authentication credentials.

### IMPORTANT

Basic Authentication is useful for understanding the authentication mechanism, but production systems require proper security practices such as:

* Password hashing
* HTTPS
* Secure credential storage
* Token/session management
* Access control
* Proper authentication architecture
