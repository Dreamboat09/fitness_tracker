# Fitness Tracker API Documentation

A RESTful API for tracking workouts, exercises, and user profiles built with Django REST Framework.

---

## Table of Contents
- [Authentication](#authentication)
- [User Endpoints](#user-endpoints)
- [Profile Endpoints](#profile-endpoints)
- [Workout Endpoints](#workout-endpoints)
- [Exercise Endpoints](#exercise-endpoints)

---

## Authentication

All endpoints (except register and login) require authentication using Token-based authentication.

---

## User Endpoints

### 1. Register User
**POST** `/api/register/`

Create a new user account.

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}
```

---

### 2. Login
**POST** `/api/login/`

Login and receive authentication token.

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "securepass123"
}
```

---

### 3. Logout
**POST** `/api/logout/`

Logout and invalidate token.

---

## Profile Endpoints

### 4. List All Profiles
**GET** `/api/profile/`

Get list of all user profiles (admin only or filtered by permissions).


---

### 5. Get Profile Details
**GET** `/api/profile/<id>/`

Get details of a specific profile.

---

### 6. Update Profile
**PUT/PATCH** `/api/profile/update/<id>/`

Update user profile information.

**Request Body (PATCH - partial update):**
```json
{
  "bio": "Marathon runner and fitness coach",
  "weight": 74.0
}
```

---

### 7. Delete Profile
**DELETE** `/api/profile/delete/<id>/`

Delete a user profile.


---

## Workout Endpoints

### 8. List All Workouts
**GET** `/api/workout/`

Get list of all workouts for the authenticated user.


**Query Parameters (optional):**
- `workout_type` - Filter by type (cardio, strength, flexibility, sports)
- `date` - Filter by specific date (YYYY-MM-DD)
- `date_from` - Start date for range
- `date_to` - End date for range
- `intensity` - Filter by intensity (low, medium, high)
- `min_duration` - Minimum duration in minutes
- `max_duration` - Maximum duration in minutes
- `search` - Search in notes
- `ordering` - Order by field (e.g., -date, duration)

---

### 9. Get Workout Details
**GET** `/api/workout/<id>/`

Get details of a specific workout.


---

### 10. Create Workout
**POST** `/api/work/create/`

Create a new workout entry.


**Request Body:**
```json
{
  "workout_type": "strength",
  "duration": 60,
  "date": "2025-10-24",
  "intensity": "medium",
  "calories_burned": 300,
  "notes": "Upper body workout"
}
```

---

### 11. Update Workout
**PUT/PATCH** `/api/workout/update/<id>/`

Update an existing workout.


**Request Body (PATCH - partial update):**
```json
{
  "duration": 50,
  "calories_burned": 350
}
```

---

### 12. Delete Workout
**DELETE** `/api/workout/delete/<id>/`

Delete a workout entry.


---

## Exercise Endpoints

### 13. List All Exercises
**GET** `/api/exercise/`

Get list of all exercises in workouts.


---

### 14. Get Exercise Details
**GET** `/api/exercise/<id>/`

Get details of a specific exercise.


---

### 15. Create Exercise
**POST** `/api/exercise/create/`

Add a new exercise to a workout.


**Request Body:**
```json
{
  "workout": 1,
  "name": "Bench Press",
  "sets": 4,
  "reps": 10,
  "weight": 80,
  "notes": "Warmup sets included"
}
```

---

### 16. Update Exercise
**PUT/PATCH** `/api/exercise/update/<id>/`

Update an existing exercise.


**Request Body (PATCH):**
```json
{
  "sets": 5,
  "reps": 12
}
```

---

### 17. Delete Exercise
**DELETE** `/api/exercise/delete/<id>/`

Delete an exercise from a workout.

---
