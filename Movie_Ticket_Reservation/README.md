# Cinema Ticket Booking System

A feature-rich console-based C++ application that simulates a movie ticket reservation system with separate interfaces for regular users and administrators. Features persistent data storage and comprehensive seat management.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [System Architecture](#system-architecture)

## Features

### User Mode
- **View Movies** – Browse available movies with genres and base prices
- **Book Tickets** – Reserve seats with visual cinema layout representation
  - VIP Seats (Rows 1-2) with 40% price markup
  - Regular Seats (Rows 3-10) at base price
  - Official receipt generation upon successful booking
- **Cancel Booking** – Free up previously reserved seats

### Admin Mode (Password Protected)
- **Default Password:** `1234`
- **Add Movies** – Create new movie listings with title, genre, and pricing (up to 10 movies)
- **Remove Movies** – Delete movies and automatically remove associated seat files
- **Update Pricing** – Modify base ticket prices for existing movies

## Project Structure

| Class | Purpose |
|-------|---------|
| `Movie` | Manages individual movie details (title, genre, base price) |
| `Seat` | Abstract base class for seat coordinates and booking status |
| `Regular_Seat` | Inherits from Seat; calculates regular pricing |
| `VIP_Seat` | Inherits from Seat; applies 40% markup to base price |
| `AdminManager` | Handles movie catalog, file I/O, and authentication |
| `CinemaHall` | Manages 10×10 seat matrix and persistent storage |
| `Ticket` | Generates billing receipts |

### Data Persistence
- `movies.txt` – Stores movie catalog with details
- `<Movie_Title>_seats.txt` – Tracks seat availability across sessions

## Getting Started

### Prerequisites
- C++17 compatible compiler (GCC/MinGW recommended)
- Terminal or command prompt

### Compilation & Execution

```bash
g++ -std=c++17 Movie_Ticket_Reservation.cpp -o CinemaSystem
./CinemaSystem
```

**Note:** C++17 is required for the `<filesystem>` library.

## Usage Guide

> **Important:** On first run, the cinema has no movies. Log in as admin to add movies before users can book tickets.

### Admin Setup (First-Time Run)

1. Select **Option 4: Admin Panel** from the main menu
2. Enter password: `1234`
3. Select **Option 1: Add Movies**
4. Enter movie details (Title, Genre, Ticket Price)
5. Repeat for up to 10 movies
6. Return to main menu

### Booking a Ticket

1. Select **Option 2: Book Ticket** from the main menu
2. Choose a movie from the displayed list
3. Review the cinema layout:
   - `[ ]` = Available seat
   - `[X]` = Booked seat
4. Enter your desired Row (1-10) and Column (1-10)
5. Confirm booking and receive official receipt

**Pricing Note:** VIP seats in Rows 1-2 automatically include the 40% markup.

### Canceling a Seat

1. Select **Option 3: Remove Seat** from the main menu
2. Choose the movie for which you booked a ticket
3. Enter the Row and Column of your booked seat
4. Seat availability updates automatically

### Admin Panel Operations

- **Remove Movies** – Deletes movie from catalog and removes associated seat file
- **Change Price** – Updates base price; VIP markup adjusts automatically

## System Architecture

### Core Design Principles
- **Object-Oriented Programming** – Leverages classes, inheritance, and polymorphism
- **Input Validation** – Comprehensive error handling prevents crashes
- **Data Persistence** – File-based storage maintains state across sessions
- **Modular Design** – Separate user and admin interfaces with distinct responsibilities